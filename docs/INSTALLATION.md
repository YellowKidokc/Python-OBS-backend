# Installation Guide

Complete installation instructions for Theophysics Manager.

## 📋 Prerequisites

### Required
- **Python 3.10 or higher** - [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **10 GB free disk space** (for vault mirroring)

### Optional
- **OpenAI API Key** - For AI features ([Get one](https://platform.openai.com/))
- **Anthropic API Key** - For Claude AI ([Get one](https://www.anthropic.com/))
- **PostgreSQL** - For cloud sync ([Download](https://www.postgresql.org/download/))
- **Git** - For version control ([Download](https://git-scm.com/))

---

## 🚀 Installation Methods

### Method 1: Automated (Recommended)

#### Windows
```cmd
cd scripts
install.bat
```

#### Linux/Mac
```bash
cd scripts
chmod +x install.sh
./install.sh
```

The automated installer will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Find available port
- ✅ Create configuration
- ✅ Run tests

---

### Method 2: Manual Installation

#### 1. Clone or Download
```bash
git clone https://github.com/yourusername/theophysics-manager.git
cd theophysics-manager
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Core dependencies (required)
pip install PySide6 pyyaml numpy

# AI features (optional but recommended)
pip install openai anthropic

# Database sync (optional)
pip install psycopg[binary]

# Or install everything at once:
pip install -r requirements.txt
```

#### 4. Create Configuration
Create `theophysics_config.json`:
```json
{
  "vault_path": null,
  "sqlite_path": null,
  "postgres_conn_str": null,
  "model_name": "gpt-4o",
  "server_port": 8000,
  "server_host": "localhost"
}
```

---

## 🔧 Configuration

### Setting Up Your Vault

1. Launch the application:
   ```bash
   python main.py
   ```

2. Go to **"Vault System"** tab
3. Click **"Browse Vault…"**
4. Select your Obsidian vault folder
5. Click **"Full Scan"**

### Setting Up AI (Optional)

#### OpenAI
```bash
# Windows
set OPENAI_API_KEY=sk-your-key-here

# Linux/Mac
export OPENAI_API_KEY=sk-your-key-here
```

#### Anthropic Claude
```bash
# Windows
set ANTHROPIC_API_KEY=sk-ant-your-key-here

# Linux/Mac
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Setting Up PostgreSQL (Optional)

1. Install PostgreSQL
2. Create a database:
   ```sql
   CREATE DATABASE theophysics;
   ```
3. In the application:
   - Go to **"Database"** tab
   - Enter connection string:
     ```
     postgresql://user:password@localhost:5432/theophysics
     ```
   - Click **"Export to PostgreSQL"**

---

## 🐳 Docker Installation (Advanced)

Coming soon! Docker support is planned for v2.1.

---

## ☁️ Replit Installation

1. Fork the Replit: [Link to be added]
2. Run the application:
   ```bash
   python scripts/install.py
   python main.py
   ```
3. The GUI will be available in the Replit webview

---

## 🧪 Verify Installation

### Test Imports
```python
python -c "import PySide6; import yaml; import numpy; print('✓ All core modules OK')"
```

### Test AI (if installed)
```python
python -c "import openai; import anthropic; print('✓ AI modules OK')"
```

### Run Test Suite
```bash
pytest tests/
```

---

## 🔍 Troubleshooting

### Python Version Too Old
**Error**: "Python 3.10+ required"

**Solution**:
1. Download Python 3.10+ from https://www.python.org/
2. During installation, check "Add Python to PATH"
3. Restart your terminal

### Port Already in Use
**Error**: "Port 8000 already in use"

**Solution**:
The installer automatically finds an available port. If you need a specific port, edit `theophysics_config.json`:
```json
{
  "server_port": 8080
}
```

### Missing Dependencies
**Error**: "ModuleNotFoundError: No module named 'PySide6'"

**Solution**:
```bash
# Activate venv first
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Then install
pip install PySide6
```

### Virtual Environment Issues
**Error**: "venv not activating"

**Solution**: Try alternative method:
```bash
# Install virtualenv
pip install virtualenv

# Create venv with virtualenv
virtualenv venv

# Activate
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### OpenAI API Errors
**Error**: "OpenAI API key not set"

**Solution**:
1. Get API key from https://platform.openai.com/
2. Set environment variable before running:
   ```bash
   set OPENAI_API_KEY=your-key  # Windows
   export OPENAI_API_KEY=your-key  # Linux/Mac
   ```

### PostgreSQL Connection Failed
**Error**: "Postgres connection failed"

**Solution**:
1. Verify PostgreSQL is running:
   ```bash
   pg_ctl status  # Check status
   ```
2. Test connection string:
   ```bash
   psql postgresql://user:password@localhost:5432/dbname
   ```
3. Check firewall allows port 5432

---

## 📚 Next Steps

After successful installation:

1. **Quick Start**: Read [QUICKSTART.md](QUICKSTART.md)
2. **Features**: See [FULL_FEATURES.md](FULL_FEATURES.md)
3. **Documentation**: Browse [README_USER.md](README_USER.md)

---

## 💡 Platform-Specific Notes

### Windows
- Use PowerShell or Command Prompt
- Paths use backslashes: `\`
- May need to allow Python in Windows Defender

### Linux
- May need `sudo` for system packages
- Use `python3` instead of `python`
- Install system dependencies:
  ```bash
  sudo apt-get install python3-venv python3-dev
  ```

### macOS
- Use `python3` instead of `python`
- May need Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```

### Replit
- No virtual environment needed
- All dependencies install automatically
- GUI runs in webview

---

## 🆘 Still Having Issues?

1. Check [GitHub Issues](https://github.com/yourusername/theophysics-manager/issues)
2. Open a new issue with:
   - Your OS and Python version
   - Full error message
   - Steps to reproduce
3. Join our Discord: [Link]

---

**Last Updated**: December 2025  
**Version**: 2.0.0

