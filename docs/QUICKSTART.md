# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Install (Windows)

Double-click `setup.bat` or run in PowerShell:
```bash
.\setup.bat
```

This will:
- Create a Python virtual environment
- Install all dependencies (PySide6, PyYAML, psycopg)

### Step 2: Run the Application

Double-click `run.bat` or:
```bash
venv\Scripts\activate
python main.py
```

### Step 3: Configure Your Vault

1. **Select Vault**:
   - Click "Vault System" tab
   - Click "Browse Vault…"
   - Navigate to your Obsidian vault folder
   - Select it

2. **Run First Scan**:
   - Click "Full Scan"
   - Watch metrics update: Notes, Tags, Links, Definitions

### Step 4: Try Key Features

#### A. Find Missing Definitions
```
1. Go to "Definitions" tab
2. Click "Scan Vault for Missing Definitions"
3. See all [[wiki-links]] that need definitions
4. Fill in definitions in the right panel
5. Click "Save / Update Definition"
```

#### B. Add Research Links
```
1. Go to "Research Links" tab
2. Left panel: Add custom links
   - Term: "quantum mechanics"
   - Source: "Wikipedia"
   - URL: https://en.wikipedia.org/wiki/Quantum_mechanics
3. Right panel: Process text with auto-links
   - Paste your text
   - List terms to link
   - Get markdown output
```

#### C. Structure Your Notes
```
1. Go to "Structure" tab
2. Browse to a note file
3. Click "Inject Structure / Footnote Section"
4. Opens the note in your default editor
5. Check that H1 title and Footnotes section were added
```

#### D. Export to Database
```
1. Go to "Database" tab
2. (Optional) Set custom SQLite path
3. (Optional) Configure PostgreSQL:
   postgresql://user:password@localhost:5432/theophysics
4. Click "Export to PostgreSQL"
5. Your data is now synced!
```

## 🎯 Common Workflows

### Daily Research Workflow
1. Write notes in Obsidian
2. Run "Quick Scan (incremental)" to detect changes
3. Scan for missing definitions
4. Fill in 2-3 key definitions
5. Export to database (auto-backup)

### Knowledge Base Building
1. Run "Full Scan" weekly
2. Review all missing definitions
3. Prioritize by frequency (most-linked terms first)
4. Add research links for key concepts
5. Structure important theorem/proof notes

### Multi-Device Sync
1. Set up PostgreSQL on server
2. Each device: Configure same Postgres connection
3. Export from Device A
4. Device B automatically has latest definitions
5. SQLite remains local, Postgres is the sync layer

## ⚙️ Configuration

### Settings File Location
`theophysics_config.json` (in same folder as main.py)

### Example Configuration
```json
{
  "vault_path": "D:/Obsidian/MyVault",
  "sqlite_path": "D:/Obsidian/MyVault/theophysics.db",
  "postgres_conn_str": "postgresql://user:pass@localhost:5432/research",
  "model_name": "gpt-4o"
}
```

## 🔧 Troubleshooting

### Application won't start
- Verify Python 3.10+ is installed: `python --version`
- Re-run `setup.bat`
- Check console for error messages

### "Vault path not set"
- First time? Go to Vault System → Browse Vault
- Already set? Check `theophysics_config.json` exists

### Scan finds 0 notes
- Confirm vault path is correct
- Check vault contains `.md` files
- Try "Full Scan" instead of incremental

### Definitions not showing
- Run vault scan first
- Then scan for definitions
- Check SQLite database was created

### PostgreSQL export fails
- Verify PostgreSQL is running
- Test connection string with psql
- Install psycopg: `pip install psycopg[binary]`

## 📊 Understanding Metrics

**Notes**: Total `.md` files scanned  
**Tags**: Sum of all tag lengths (rough measure of tag usage)  
**Links**: Sum of all link lengths (rough measure of connectivity)  
**Definitions**: Terms in the definitions table  
**Errors**: Parse errors encountered (should be 0)

## 🎓 Advanced Tips

### Automatic Scanning
- Use Windows Task Scheduler to run periodic scans
- Command: `venv\Scripts\python.exe main.py --scan-and-exit` (requires script modification)

### Custom SQLite Queries
```sql
-- Find most-linked terms
SELECT json_extract(links, '$') as link_count, title, path
FROM notes
ORDER BY length(links) DESC
LIMIT 20;

-- Find notes without tags
SELECT title, path FROM notes WHERE tags = '[]';

-- List all missing definitions
SELECT term, status FROM definitions WHERE status = 'missing';
```

### Backup Strategy
1. SQLite database is in your vault (syncs with Obsidian)
2. PostgreSQL is your cloud backup
3. Git-track the SQLite file for version history
4. Export to Postgres weekly for disaster recovery

## 🔮 Next Steps

1. **Integrate with Obsidian Plugin**: The TypeScript plugin reads from SQLite
2. **Add AI Features**: Uncomment OpenAI in requirements, wire to ai_engine.py
3. **Build Ontology**: Use definition classifications to map concept relationships
4. **Evidence Bundles**: Extend structure_engine to create citation networks
5. **Semantic Search**: Add embeddings via ai_engine, store in SQLite

## 📞 Need Help?

Check the full README.md for detailed documentation on:
- System architecture
- Database schemas
- Extending the engines
- API integration
- Obsidian plugin coordination

---

**Happy researching! 🚀**

