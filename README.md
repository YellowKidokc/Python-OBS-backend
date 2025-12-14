# Theophysics Research Manager

> **AI-Powered Knowledge Management for Obsidian** 🚀

A comprehensive Python-based system for managing large Obsidian vaults with semantic AI, entity extraction, ontology building, and cloud synchronization.

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yourusername/theophysics-manager)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

## ✨ Features

- 🗂️ **Vault System** - Full & incremental scanning with hash-based change detection
- 📚 **Definition Management** - Auto-detect terms, semantic parsing, completeness scoring
- 🔬 **Entity Extraction** - People, places, scientific terms, citations
- 🕸️ **Ontology Engine** - Complete concept graph system with relationship tracking
- 🤖 **AI Integration** - OpenAI GPT-4 & Anthropic Claude for semantic search & generation
- 💾 **Dual Database** - SQLite (local mirror) + PostgreSQL (cloud sync)
- 🔗 **Research Links** - Auto-generate links to Wikipedia, arXiv, SEP, Scholar
- 🏗️ **Structure Builder** - Note templates and validation

## 🚀 Quick Start

### Windows
```cmd
cd scripts
install.bat
```

### Linux/Mac
```bash
cd scripts
chmod +x install.sh
./install.sh
```

### Universal (Python)
```bash
python scripts/install.py
```

Then run:
```bash
python main.py
```

## 📖 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[Quick Start](docs/QUICKSTART.md)** - 5-minute tutorial
- **[Full Features](docs/FULL_FEATURES.md)** - Complete feature list
- **[API Documentation](docs/API.md)** - For developers
- **[Contributing](CONTRIBUTING.md)** - How to contribute

## 🎯 Use Cases

- **Academic Research** - Track concepts, build ontologies, extract citations
- **Knowledge Management** - Semantic search, concept relationships, quality metrics  
- **Writing & Documentation** - Auto-link terms, generate glossaries, ensure consistency
- **AI-Assisted Learning** - Semantic similarity, AI definitions, concept discovery

## 🏗️ Architecture

```
Obsidian Vault (Source of Truth)
    ↓
Python Scanner (vault_engine)
    ↓
SQLite Database (Local Mirror)
    ├→ definition_engine (terms)
    ├→ research_engine (entities)
    ├→ ontology_engine (graphs)
    └→ ai_engine (embeddings)
    ↓
PostgreSQL (Cloud Sync)
```

## 🔧 Requirements

- Python 3.10+
- Optional: OpenAI API key for AI features
- Optional: PostgreSQL for cloud sync

## 📦 What's Included

```
theophysics_manager/
├── main.py                # GUI application
├── engine/                # Backend modules (10 files)
├── scripts/               # Installation & utilities
├── docs/                  # Documentation
└── requirements.txt       # Dependencies
```

## 🌟 Key Technologies

- **GUI**: PySide6 (Qt)
- **AI**: OpenAI GPT-4, Anthropic Claude
- **Database**: SQLite, PostgreSQL
- **Data**: NumPy, PyYAML

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Links

- [GitHub Repository](https://github.com/yourusername/theophysics-manager)
- [Issue Tracker](https://github.com/yourusername/theophysics-manager/issues)
- [Documentation](docs/)

## 💡 Credits

Built for the Theophysics Research initiative. Integrates:
- Obsidian knowledge management
- Python AI processing
- Multi-database architecture
- Semantic classification systems

---

**Version**: 2.0.0 - Full AI Edition  
**Last Updated**: December 2025
