# Contributing to Offline AI Agent | المساهمة في وكيل الذكاء الاصطناعي المحلي

Thank you for your interest in contributing to the Offline AI Agent project! This document provides guidelines and information for contributors.

شكراً لاهتمامك بالمساهمة في مشروع وكيل الذكاء الاصطناعي المحلي! هذا المستند يوفر الإرشادات والمعلومات للمساهمين.

## Table of Contents | جدول المحتويات

- [Code of Conduct | قواعد السلوك](#code-of-conduct--قواعد-السلوك)
- [Getting Started | البدء](#getting-started--البدء)
- [Development Setup | إعداد التطوير](#development-setup--إعداد-التطوير)
- [Contributing Guidelines | إرشادات المساهمة](#contributing-guidelines--إرشادات-المساهمة)
- [Pull Request Process | عملية طلب السحب](#pull-request-process--عملية-طلب-السحب)
- [Coding Standards | معايير البرمجة](#coding-standards--معايير-البرمجة)
- [Testing Guidelines | إرشادات الاختبار](#testing-guidelines--إرشادات-الاختبار)
- [Documentation | التوثيق](#documentation--التوثيق)
- [Community | المجتمع](#community--المجتمع)

---

## Code of Conduct | قواعد السلوك

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

هذا المشروع وكل من يشارك فيه محكوم بقواعد السلوك الخاصة بنا. من خلال المشاركة، من المتوقع أن تلتزم بهذا الكود.

### Our Pledge | تعهدنا

We pledge to make participation in our project a harassment-free experience for everyone, regardless of:
- Age | العمر
- Body size | حجم الجسم
- Disability | الإعاقة
- Ethnicity | العرق
- Gender identity and expression | الهوية والتعبير الجنسي
- Level of experience | مستوى الخبرة
- Nationality | الجنسية
- Personal appearance | المظهر الشخصي
- Race | العرق
- Religion | الدين
- Sexual identity and orientation | الهوية والميول الجنسية

---

## Getting Started | البدء

### Prerequisites | المتطلبات المسبقة

Before contributing, ensure you have:
قبل المساهمة، تأكد من أن لديك:

- Python 3.8 or higher
- Git knowledge
- Basic understanding of AI/ML concepts
- معرفة أساسية بمفاهيم الذكاء الاصطناعي/التعلم الآلي

### Areas for Contribution | مجالات المساهمة

We welcome contributions in the following areas:
نرحب بالمساهمات في المجالات التالية:

- 🐛 **Bug Fixes** | إصلاح الأخطاء
- ✨ **New Features** | الميزات الجديدة
- 📚 **Documentation** | التوثيق
- 🧪 **Testing** | الاختبار
- 🌍 **Translations** | الترجمات
- 🎨 **UI/UX Improvements** | تحسينات واجهة المستخدم
- ⚡ **Performance Optimizations** | تحسينات الأداء

---

## Development Setup | إعداد التطوير

### 1. Fork and Clone | الفرق والاستنساخ

```bash
# Fork the repository on GitHub
# انسخ المستودع على GitHub

# Clone your fork
git clone https://github.com/YOUR-USERNAME/offline-ai-agent.git
cd offline-ai-agent

# Add upstream remote
git remote add upstream https://github.com/ayamohamedai/offline-ai-agent.git
```

### 2. Create Virtual Environment | إنشاء البيئة الافتراضية

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies | تثبيت التبعيات

```bash
# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Or install in development mode
pip install -e .[dev]
```

### 4. Install Pre-commit Hooks | تثبيت خطافات ما قبل الالتزام

```bash
pre-commit install
```

### 5. Set Up Configuration | إعداد التكوين

```bash
# Copy example environment file
cp .env.example .env

# Edit configuration as needed
# عدل التكوين حسب الحاجة
```

---

## Contributing Guidelines | إرشادات المساهمة

### Issue Reporting | الإبلاغ عن المشاكل

When reporting issues, please include:
عند الإبلاغ عن المشاكل، يرجى تضمين:

- Clear description of the problem
- وصف واضح للمشكلة
- Steps to reproduce
- خطوات إعادة الإنتاج
- Expected vs actual behavior
- السلوك المتوقع مقابل السلوك الفعلي
- Environment details (OS, Python version, etc.)
- تفاصيل البيئة (نظام التشغيل، إصدار Python، إلخ)
- Error messages or logs
- رسائل الخطأ أو السجلات

### Feature Requests | طلبات الميزات

For new features, please:
للميزات الجديدة، يرجى:

1. Check existing issues and discussions
2. فحص المشاكل والمناقشات الموجودة
3. Clearly describe the feature and its benefits
4. وصف الميزة وفوائدها بوضوح
5. Provide use cases and examples
6. تقديم حالات الاستخدام والأمثلة

### Types of Contributions | أنواع المساهمات

#### 🐛 Bug Fixes
- Fix existing functionality
- إصلاح الوظائف الموجودة
- Include tests for the fix
- تضمين اختبارات للإصلاح
- Update documentation if needed
- تحديث التوثيق إذا لزم الأمر

#### ✨ New Features
- Add new functionality
- إضافة وظائف جديدة
- Include comprehensive tests
- تضمين اختبارات شاملة
- Update documentation and examples
- تحديث التوثيق والأمثلة
- Consider performance implications
- مراعاة تأثيرات الأداء

#### 📚 Documentation
- Improve existing documentation
- تحسين التوثيق الموجود
- Add new tutorials or guides
- إضافة دروس أو أدلة جديدة
- Fix typos and grammatical errors
- إصلاح الأخطاء الإملائية والنحوية
- Add code examples and use cases
- إضافة أمثلة الكود وحالات الاستخدام

---

## Pull Request Process | عملية طلب السحب

### Before Submitting | قبل التقديم

1. **Sync with upstream** | المزامنة مع المستودع الأصلي
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch** | إنشاء فرع الميزة
   ```bash
   git checkout -b feature/your-feature-name
   # or for bug fixes:
   git checkout -b bugfix/issue-number-description
   ```

3. **Make your changes** | قم بالتغييرات
   - Follow coding standards
   - اتبع معايير البرمجة
   - Write tests
   - اكتب الاختبارات
   - Update documentation
   - حدث التوثيق

4. **Test your changes** | اختبر التغييرات
   ```bash
   # Run tests
   pytest
   
   # Run linting
   flake8 src/
   
   # Format code
   black src/
   
   # Type checking
   mypy src/
   ```

### Submitting the PR | تقديم طلب السحب

1. **Push your changes** | ادفع التغييرات
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Use clear, descriptive title
   - استخدم عنوان واضح ووصفي
   - Fill out the PR template
   - املأ نموذج طلب السحب
   - Link related issues
   - اربط المشاكل ذات الصلة
   - Add screenshots if UI changes
   - أضف لقطات شاشة إذا كانت تغييرات واجهة المستخدم

### PR Template | نموذج طلب السحب

```markdown
## Description | الوصف
Brief description of changes made.
وصف مختصر للتغييرات المجراة.

## Type of Change | نوع التغيير
- [ ] Bug fix | إصلاح خطأ
- [ ] New feature | ميزة جديدة  
- [ ] Documentation update | تحديث التوثيق
- [ ] Performance improvement | تحسين الأداء
- [ ] Other | أخرى

## Testing | الاختبار
- [ ] Tests pass locally
- [ ] Added new tests for changes
- [ ] Updated existing tests

## Checklist | قائمة المراجعة
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

---

## Coding Standards | معايير البرمجة

### Python Style Guide | دليل أسلوب Python

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:
نتبع PEP 8 مع بعض التعديلات:

- Line length: 88 characters (Black default)
- طول السطر: 88 حرف
- Use double quotes for strings
- استخدم علامات الاقتباس المزدوجة للنصوص
- Type hints for all function signatures
- تلميحات النوع لجميع توقيعات الوظائف

### Code Organization | تنظيم الكود

```
src/offline_ai_agent/
├── api/           # API-related code
├── core/          # Core business logic  
├── models/        # Data models
├── services/      # External services
├── utils/         # Utility functions
└── tests/         # Test files
```

### Naming Conventions | اتفاقيات التسمية

- **Classes**: PascalCase (`AIAgent`, `DocumentProcessor`)
- **Functions/Variables**: snake_case (`process_document`, `model_config`)
- **Constants**: UPPER_SNAKE_CASE (`DEFAULT_MODEL`, `MAX_FILE_SIZE`)
- **Private methods**: Leading underscore (`_internal_method`)

### Documentation Standards | معايير التوثيق

#### Docstring Format

```python
def process_document(file_path: str, chunk_size: int = 1000) -> List[str]:
    """
    Process a document and split it into chunks.
    
    معالجة مستند وتقسيمه إلى أجزاء.
    
    Args:
        file_path: Path to the document file
        chunk_size: Size of each text chunk
        
    Returns:
        List of text chunks
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If chunk_size is invalid
        
    Example:
        >>> chunks = process_document("document.pdf", 500)
        >>> print(len(chunks))
        10
    """
```

---

## Testing Guidelines | إرشادات الاختبار

### Test Structure | هيكل الاختبار

```
tests/
├── unit/          # Unit tests
├── integration/   # Integration tests
├── fixtures/      # Test data and fixtures
└── conftest.py    # Pytest configuration
```

### Writing Tests | كتابة الاختبارات

```python
import pytest
from offline_ai_agent.core.agent import OfflineAIAgent

class TestOfflineAIAgent:
    """Test cases for OfflineAIAgent class."""
    
    @pytest.fixture
    def agent(self):
        """Create agent instance for testing."""
        return OfflineAIAgent(test_mode=True)
    
    def test_agent_initialization(self, agent):
        """Test agent initializes correctly."""
        assert agent is not None
        assert agent.test_mode is True
    
    @pytest.mark.asyncio
    async def test_process_query(self, agent):
        """Test query processing functionality."""
        response = await agent.process_query("What is AI?")
        assert isinstance(response, str)
        assert len(response) > 0
```

### Test Commands | أوامر الاختبار

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/offline_ai_agent

# Run specific test file
pytest tests/unit/test_agent.py

# Run tests matching pattern
pytest -k "test_agent"

# Run tests with verbose output
pytest -v

# Run integration tests
pytest tests/integration/
```

---

## Documentation | التوثيق

### Types of Documentation | أنواع التوثيق

1. **API Documentation** | توثيق API
   - Generated from docstrings
   - مُولد من docstrings
   
2. **User Guides** | أدلة المستخدم
   - Installation instructions
   - تعليمات التثبيت
   - Configuration guides
   - أدلة التكوين
   - Usage examples
   - أمثلة الاستخدام

3. **Developer Documentation** | توثيق المطور
   - Architecture overview
   - نظرة عامة على البنية
   - Contributing guidelines
   - إرشادات المساهمة
   - API reference
   - مرجع API

### Documentation Tools | أدوات التوثيق

- **Sphinx** for comprehensive documentation
- **MkDocs** for user-friendly guides  
- **Docstrings** for inline documentation
- **README** files for quick reference

---

## Community | المجتمع

### Communication Channels | قنوات التواصل

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and discussions
- **Email**: Direct contact for sensitive matters
- **Wiki**: Community-maintained documentation

### Getting Help | الحصول على المساعدة

- Check existing documentation
- فحص التوثيق الموجود
- Search existing issues
- البحث في المشاكل الموجودة
- Ask in discussions
- اسأل في المناقشات
- Contact maintainers if needed
- اتصل بالمشرفين إذا لزم الأمر

### Recognition | التقدير

Contributors will be recognized in:
سيتم التعرف على المساهمين في:

- AUTHORS.md file
- Release notes
- ملاحظات الإصدار
- Project documentation
- توثيق المشروع
- Social media acknowledgments
- الإقرارات على وسائل التواصل الاجتماعي

---

## Questions? | أسئلة؟

If you have any questions about contributing, feel free to:
إذا كان لديك أي أسئلة حول المساهمة، لا تتردد في:

- Open an issue with the "question" label
- فتح مشكلة بتصنيف "سؤال"
- Start a discussion in GitHub Discussions
- بدء مناقشة في مناقشات GitHub
- Contact the maintainers directly
- الاتصال بالمشرفين مباشرة

Thank you for contributing to making AI more accessible and powerful for everyone!

شكراً لك على المساهمة في جعل الذكاء الاصطناعي أكثر إتاحة وقوة للجميع!
