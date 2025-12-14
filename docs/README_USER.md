# Theophysics Research Manager

A comprehensive Python-based knowledge management system for Obsidian vaults with AI-powered semantic processing, definition tracking, research link management, and database synchronization.

## Features

### 🗂️ Vault System
- **Full & Incremental Scanning**: Scan your entire Obsidian vault or just detect changes
- **Hash-based Change Detection**: Efficiently tracks file modifications using SHA256 hashing
- **Metadata Extraction**: Automatically parses YAML frontmatter, tags, and wiki-links
- **Real-time Metrics**: Track notes, tags, links, definitions, and errors

### 📚 Definition Management
- **Auto-detection**: Automatically finds undefined terms from wiki-links
- **Stub Generation**: Creates definition placeholders for missing terms
- **Definition Editor**: Built-in GUI for creating and editing term definitions
- **Classification System**: Organize definitions by type and status
- **Alias Support**: Define multiple names for the same concept

### 🔗 Research Link System
- **Custom Link Registry**: Store external research links for terms
- **Text Link Processor**: Automatically convert terms to markdown links
- **Source Tracking**: Organize links by source (Wikipedia, arXiv, etc.)

### 🏗️ Structure Builder
- **Template Injection**: Add consistent structure to notes
- **Footnote Sections**: Automatically add footnote sections
- **Heading Management**: Ensure proper H1 titles

### 💾 Database Architecture
- **SQLite Primary Store**: Fast, portable, file-based database
- **PostgreSQL Sync**: Optional sync to central Postgres database
- **Schema Management**: Automatic table creation and maintenance
- **VACUUM Support**: Database optimization tools

### 🤖 AI Engine (Full Implementation)
- **OpenAI Integration**: GPT-4 for text generation, embeddings for semantic search
- **Anthropic Claude**: Alternative AI provider support
- **Semantic Search**: Vector-based similarity search across all notes
- **AI Definition Generation**: Automatic definition creation with context
- **Classification Inference**: AI-powered concept categorization
- **Concept Extraction**: Automatic related concept identification
- **Ontology Building**: AI-assisted relationship inference

### 🕸️ Ontology System
- **Concept Graph Building**: Automatic ontology from definitions
- **Relationship Tracking**: Parent/child/related concept connections
- **Path Finding**: Discover relationships between concepts
- **Cycle Detection**: Identify circular relationships
- **Graph Export**: JSON, GraphViz formats for visualization
- **Completeness Scoring**: Measure definition quality

### 🔬 Entity Extraction
- **People Detection**: Automatic extraction of person names
- **Place Identification**: Geographical location recognition
- **Scientific Terms**: Technical vocabulary extraction
- **Citation Tracking**: Academic reference detection
- **Auto-linking**: Automatic research link generation

## System Architecture

```
Obsidian Vault (Source of Truth)
    ↓
Python Scanner (vault_engine)
    ↓
SQLite Database (Local Index)
    ├─ Notes table
    ├─ Definitions table
    └─ Research Links table
    ↓
PostgreSQL (Optional Mirror)
```

## Installation

### Prerequisites
- Python 3.10 or higher
- An Obsidian vault to manage

### Setup

1. **Clone or extract the project**:
```bash
cd theophysics_manager
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Application

```bash
python main.py
```

### First-Time Setup

1. **Select Your Vault**:
   - Go to the "Vault System" tab
   - Click "Browse Vault…"
   - Select your Obsidian vault directory

2. **Run Initial Scan**:
   - Click "Full Scan" to index your entire vault
   - View metrics: notes, tags, links, definitions

3. **Configure Database** (optional):
   - Go to the "Database" tab
   - Set custom SQLite path if desired
   - Configure PostgreSQL connection string if using remote sync

### Working with Definitions

1. **Scan for Missing Definitions**:
   - Go to "Definitions" tab
   - Click "Scan Vault for Missing Definitions"
   - View all terms that need definitions

2. **Create/Edit Definitions**:
   - Enter term name
   - Add comma-separated aliases
   - Select classification
   - Write definition body
   - Click "Save / Update Definition"

### Managing Research Links

1. **Add Custom Links**:
   - Go to "Research Links" tab
   - Enter term, source label, and URL
   - Click "Add Link"

2. **Process Text with Links**:
   - Paste text in input area
   - List terms to link (comma-separated)
   - Click "Process / Add Markdown Links"
   - Copy output with auto-generated links

### Structure Builder

1. **Inject Structure**:
   - Go to "Structure" tab
   - Browse to select a note file
   - Click "Inject Structure / Footnote Section"
   - Adds H1 title and Footnotes section if missing

### Database Operations

1. **Export to PostgreSQL**:
   - Go to "Database" tab
   - Enter Postgres connection string:
     ```
     postgresql://user:password@host:port/database
     ```
   - Click "Export to PostgreSQL"

2. **Optimize SQLite**:
   - Click "Export to SQLite (already primary)"
   - Runs VACUUM to optimize database

## File Structure

```
theophysics_manager/
├── main.py                          # Main GUI application
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── engine/                          # Backend modules
    ├── __init__.py
    ├── settings.py                  # Configuration management
    ├── utils.py                     # Parsing utilities
    ├── database_engine.py           # SQLite & Postgres
    ├── vault_engine.py              # Vault scanning
    ├── definition_engine.py         # Definition management
    ├── research_engine.py           # Research links
    ├── structure_engine.py          # Note structure templates
    └── ai_engine.py                 # AI interface (placeholder)
```

## Configuration File

Settings are stored in `theophysics_config.json` in the same directory as `main.py`:

```json
{
  "vault_path": "D:/path/to/your/vault",
  "sqlite_path": "D:/path/to/your/vault/theophysics.db",
  "postgres_conn_str": "postgresql://user:pass@host/db",
  "model_name": "gpt-4o"
}
```

## Database Schema

### Notes Table
- `path`: File path (unique)
- `title`: Note title (from filename)
- `yaml`: YAML frontmatter (JSON)
- `tags`: Extracted tags (JSON array)
- `links`: Wiki-links (JSON array)
- `hash`: SHA256 content hash
- `updated_at`: Unix timestamp

### Definitions Table
- `term`: Term name (unique)
- `aliases`: Alternative names (JSON array)
- `classification`: Type/category
- `body`: Definition text
- `status`: "missing", "draft", or "complete"
- `file_path`: Source note path
- `updated_at`: Unix timestamp

### Research Links Table
- `term`: Term name
- `source`: Source label (e.g., "Wikipedia")
- `url`: Full URL

## Extending the System

### Adding AI Features

The `ai_engine.py` module is a placeholder ready for integration:

```python
from engine.ai_engine import AIEngine

ai_engine = AIEngine(settings_mgr)

# Future: Real embeddings
embeddings = ai_engine.embed_texts(["some text"])

# Future: AI-generated definitions
definition = ai_engine.generate_definition("quantum entanglement", context)
```

### Obsidian Plugin Integration

The Python backend is designed to work alongside the Obsidian TypeScript plugin:

1. **Plugin writes semantic tags** → Python scanner reads them
2. **Python builds definitions** → Plugin queries them via JSON export
3. **UUID registry** → Maintained in both systems for consistency

### Custom Processors

You can extend any engine module:

```python
# Example: Custom research link source
class ArxivLinkEngine(ResearchLinkEngine):
    def fetch_arxiv_links(self, term):
        # Query arXiv API
        # Add links automatically
        pass
```

## ✅ What's New in v2.0 - Full AI Edition

- [x] **Full OpenAI Integration**: GPT-4 + embeddings
- [x] **Anthropic Claude Support**: Alternative AI provider
- [x] **Semantic Search**: Vector-based note similarity
- [x] **AI Definition Generator**: Context-aware definitions
- [x] **Ontology Engine**: Complete concept graph system
- [x] **Entity Extraction**: People, places, scientific terms
- [x] **Completeness Scoring**: Definition quality metrics
- [x] **Advanced Research Links**: Entity-based auto-linking
- [x] **Graph Export**: JSON & GraphViz formats

## Roadmap

- [ ] Real-time vault watching (file system events)
- [ ] ChromaDB integration for persistent vectors
- [ ] Evidence bundle system with AI citation
- [ ] Interactive ontology visualization (web UI)
- [ ] Note similarity clustering & recommendations
- [ ] REST API for plugin integration
- [ ] Web dashboard (Flask/FastAPI)
- [ ] Batch AI processing for large vaults
- [ ] Custom LLM model support (LLaMA, Mistral)

## Troubleshooting

### "No module named 'PySide6'"
```bash
pip install PySide6
```

### "Vault path not set" error
- Go to Vault System tab and browse to select your vault

### PostgreSQL connection fails
- Verify connection string format
- Check that PostgreSQL server is running
- Ensure `psycopg[binary]` is installed

### SQLite database locked
- Close any other applications accessing the database
- Restart the application

## Contributing

This is a research system designed for Theophysics vault management. Feel free to adapt it for your own knowledge base needs.

## License

Proprietary - Theophysics Research Project

## Credits

Built as part of the Theophysics Research initiative, integrating:
- Obsidian knowledge management
- Python backend processing
- AI semantic classification
- Multi-database architecture

---

**Version**: 1.0.0  
**Last Updated**: December 2025

