# Project Structure

Clean, organized structure for the Theophysics Manager system.

## 📁 Directory Layout

```
theophysics_manager/
├── 📄 main.py                          # Main GUI application entry point
├── 📄 requirements.txt                  # Python dependencies
├── 📄 README.md                         # Main project documentation
├── 📄 LICENSE                           # MIT License
├── 📄 CONTRIBUTING.md                   # Contribution guidelines
├── 📄 .gitignore                        # Git ignore rules
├── 📄 PROJECT_STRUCTURE.md              # This file
│
├── 📂 engine/                           # Backend processing modules
│   ├── __init__.py                      # Package initialization
│   ├── settings.py                      # Configuration management (40 lines)
│   ├── utils.py                         # Parsing utilities (30 lines)
│   ├── database_engine.py               # SQLite + PostgreSQL (280 lines)
│   ├── vault_engine.py                  # Vault scanning (50 lines)
│   ├── definition_engine.py             # Definition management (300+ lines)
│   ├── research_engine.py               # Entity extraction + links (350+ lines)
│   ├── structure_engine.py              # Note templates (40 lines)
│   ├── ai_engine.py                     # OpenAI/Claude integration (450+ lines)
│   └── ontology_engine.py               # Concept graphs (450+ lines)
│
├── 📂 scripts/                          # Installation & utilities
│   ├── install.py                       # Universal Python installer
│   ├── install.bat                      # Windows installation
│   ├── install.sh                       # Linux/Mac installation
│   ├── run.bat                          # Windows run script
│   └── run.sh                           # Linux/Mac run script
│
├── 📂 docs/                             # Documentation
│   ├── README.md                        # Documentation index
│   ├── README_USER.md                   # Complete user guide
│   ├── QUICKSTART.md                    # 5-minute tutorial
│   ├── FULL_FEATURES.md                 # Feature documentation
│   ├── INSTALLATION.md                  # Detailed setup guide
│   └── API.md                           # API documentation (future)
│
└── 📂 .github/                          # GitHub configuration
    └── ISSUE_TEMPLATE/
        ├── bug_report.md                # Bug report template
        └── feature_request.md           # Feature request template
```

## 📊 File Counts & Stats

| Category | Count | Lines |
|----------|-------|-------|
| **Python Modules** | 10 | 2,000+ |
| **Scripts** | 5 | 500+ |
| **Documentation** | 7 | 2,500+ |
| **Configuration** | 3 | 100+ |
| **Total Files** | 25+ | 5,100+ |

## 🎯 Key Files

### Entry Points
- **`main.py`** - Launch the GUI application
- **`scripts/install.py`** - Universal installation
- **`scripts/run.bat/sh`** - Quick launch scripts

### Core Engines
- **`engine/vault_engine.py`** - Obsidian vault scanning
- **`engine/definition_engine.py`** - Semantic definition management
- **`engine/research_engine.py`** - Entity extraction system
- **`engine/ai_engine.py`** - OpenAI/Claude integration
- **`engine/ontology_engine.py`** - Concept graph building
- **`engine/database_engine.py`** - SQLite + PostgreSQL

### Documentation
- **`README.md`** - Main project overview
- **`docs/QUICKSTART.md`** - Get started in 5 minutes
- **`docs/INSTALLATION.md`** - Detailed setup
- **`docs/FULL_FEATURES.md`** - Complete feature list

## 🏗️ Data Flow

```
User Interface (main.py)
    ↓
Engine Layer (engine/*.py)
    ↓
Database Layer (SQLite)
    ↓
Cloud Layer (PostgreSQL)
```

## 📦 What Gets Committed to Git

### ✅ Include
- Source code (`*.py`)
- Documentation (`*.md`)
- Configuration templates
- Scripts
- LICENSE
- README
- .gitignore

### ❌ Exclude (.gitignore)
- Virtual environments (`venv/`)
- Compiled Python (`__pycache__/`, `*.pyc`)
- Database files (`*.db`)
- Configuration with secrets (`theophysics_config.json`)
- API keys (`.env`, `*_key.*`)
- IDE settings (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Logs (`*.log`)

## 🔒 Security Notes

**NEVER commit:**
- API keys (OpenAI, Anthropic)
- Database credentials
- Personal vault data
- Configuration with sensitive info

**Always:**
- Use environment variables for secrets
- Keep `.env` in `.gitignore`
- Use example config files
- Document what needs to be configured

## 📝 Naming Conventions

### Files
- Python modules: `lowercase_with_underscores.py`
- Scripts: `lowercase.sh`, `lowercase.bat`
- Documentation: `UPPERCASE.md` or `TitleCase.md`

### Directories
- All lowercase
- No spaces
- Descriptive names

### Code
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

## 🎨 Organization Principles

1. **Separation of Concerns**
   - GUI in `main.py`
   - Logic in `engine/`
   - Utilities in `scripts/`
   - Docs in `docs/`

2. **Modularity**
   - Each engine is independent
   - Clear interfaces
   - Easy to extend

3. **Documentation**
   - README at root
   - Detailed docs in `docs/`
   - Docstrings in code
   - Examples inline

4. **Portability**
   - Cross-platform scripts
   - Relative paths
   - Virtual environments
   - No hard-coded paths

## 🚀 Future Additions

Planned structure additions:
- `tests/` - Unit and integration tests
- `examples/` - Example vaults and configurations
- `plugins/` - Extensible plugin system
- `api/` - REST API server
- `web/` - Web dashboard
- `docker/` - Docker containerization

---

**Last Updated**: December 2025  
**Version**: 2.0.0

