#!/usr/bin/env python3
"""
Offline AI Agent - Main Application Entry Point

This module serves as the primary entry point for the Offline AI Agent application.
It initializes the AI agent, loads configuration, and starts the application.

Author: Aya Mohamed
License: MIT
"""

import asyncio
import logging
import signal
import sys
from pathlib import Path
from typing import Optional

import uvicorn
import yaml
from loguru import logger

# Import core modules
from src.offline_ai_agent.core.agent import OfflineAIAgent
from src.offline_ai_agent.core.config import Config
from src.offline_ai_agent.api.server import create_app
from src.offline_ai_agent.utils.logging import setup_logging


class ApplicationManager:
    """Manages the lifecycle of the Offline AI Agent application."""
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialize the application manager.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config_path = config_path
        self.config: Optional[Config] = None
        self.agent: Optional[OfflineAIAgent] = None
        self.app = None
        
    async def initialize(self) -> None:
        """Initialize the application components."""
        try:
            # Load configuration
            logger.info(f"Loading configuration from {self.config_path}")
            self.config = await self.load_config()
            
            # Setup logging
            setup_logging(self.config)
            
            # Initialize AI agent
            logger.info("Initializing AI Agent...")
            self.agent = OfflineAIAgent(self.config)
            await self.agent.initialize()
            
            # Create FastAPI app if API is enabled
            if self.config.api.enabled:
                logger.info("Creating API server...")
                self.app = create_app(self.agent, self.config)
                
            logger.success("Application initialized successfully!")
            
        except Exception as e:
            logger.error(f"Failed to initialize application: {str(e)}")
            raise
    
    async def load_config(self) -> Config:
        """Load configuration from YAML file."""
        config_path = Path(self.config_path)
        
        if not config_path.exists():
            logger.warning(f"Config file {self.config_path} not found, using defaults")
            return Config()
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)
            return Config.from_dict(config_data)
        except Exception as e:
            logger.error(f"Failed to load config: {str(e)}")
            raise
    
    async def start_server(self) -> None:
        """Start the API server."""
        if not self.app or not self.config:
            raise RuntimeError("Application not initialized")
        
        logger.info(f"Starting server on {self.config.api.host}:{self.config.api.port}")
        
        config = uvicorn.Config(
            app=self.app,
            host=self.config.api.host,
            port=self.config.api.port,
            log_level=self.config.app.log_level.lower(),
            reload=self.config.development.reload if hasattr(self.config, 'development') else False
        )
        
        server = uvicorn.Server(config)
        await server.serve()
    
    async def start_cli(self) -> None:
        """Start the command-line interface."""
        if not self.agent:
            raise RuntimeError("AI Agent not initialized")
        
        logger.info("Starting CLI mode...")
        print("\n" + "="*50)
        print("🤖 Offline AI Agent - Interactive Mode")
        print("="*50)
        print("Type 'help' for commands, 'exit' to quit")
        print("-"*50 + "\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("👋 Goodbye!")
                    break
                    
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                
                # Process user query
                response = await self.agent.process_query(user_input)
                print(f"\n🤖 AI Agent: {response}\n")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error processing query: {str(e)}")
                print(f"❌ Error: {str(e)}\n")
    
    def show_help(self) -> None:
        """Show CLI help information."""
        help_text = """
📚 Available Commands:
  help          - Show this help message
  exit/quit/q   - Exit the application
  
💡 Usage Examples:
  - Ask questions about your documents
  - "What is the main topic of document X?"
  - "Summarize the key points from the uploaded files"
  - "Find information about [topic]"
  
🔧 Features:
  - Offline document processing
  - Vector-based search
  - Multi-language support
  - Context-aware responses
        """
        print(help_text)
    
    async def shutdown(self) -> None:
        """Gracefully shutdown the application."""
        logger.info("Shutting down application...")
        
        if self.agent:
            await self.agent.shutdown()
        
        logger.info("Application shutdown complete")


def setup_signal_handlers(app_manager: ApplicationManager) -> None:
    """Setup signal handlers for graceful shutdown."""
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, shutting down...")
        asyncio.create_task(app_manager.shutdown())
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


async def main():
    """Main application entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Offline AI Agent")
    parser.add_argument(
        "--config", 
        default="config.yaml", 
        help="Path to configuration file"
    )
    parser.add_argument(
        "--mode", 
        choices=["server", "cli", "both"], 
        default="both",
        help="Application mode"
    )
    parser.add_argument(
        "--host",
        default=None,
        help="Override server host"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Override server port"
    )
    
    args = parser.parse_args()
    
    # Create and initialize application manager
    app_manager = ApplicationManager(args.config)
    setup_signal_handlers(app_manager)
    
    try:
        await app_manager.initialize()
        
        # Override config if command line args provided
        if args.host and app_manager.config:
            app_manager.config.api.host = args.host
        if args.port and app_manager.config:
            app_manager.config.api.port = args.port
        
        # Start application based on mode
        if args.mode == "server":
            await app_manager.start_server()
        elif args.mode == "cli":
            await app_manager.start_cli()
        else:  # both
            # Start server in background and CLI in foreground
            server_task = asyncio.create_task(app_manager.start_server())
            cli_task = asyncio.create_task(app_manager.start_cli())
            
            # Wait for either to complete
            done, pending = await asyncio.wait(
                [server_task, cli_task], 
                return_when=asyncio.FIRST_COMPLETED
            )
            
            # Cancel remaining tasks
            for task in pending:
                task.cancel()
    
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        sys.exit(1)
    finally:
        await app_manager.shutdown()


if __name__ == "__main__":
    # Run the main application
    asyncio.run(main())
