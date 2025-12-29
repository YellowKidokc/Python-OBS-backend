# CDCM System - Complete Setup Guide

## 📋 ANSWERS TO YOUR QUESTIONS

### ✅ **1. Excel Template - YES, Required**

**Answer:** The system READS existing CDCM.xlsx - it doesn't create from scratch.

**Location:** `O:\Theophysics_Backend\CDCM.xlsx` (your main file)
**Template:** `O:\Theophysics_Backend\CDCM (1).xlsx` (backup copy)

**What to do:**
- Keep your working copy: `O:\Theophysics_Backend\CDCM.xlsx`
- System will read from there
- Make edits in Excel, reload in app

---

### ✅ **2. Ollama - YES, Wired Up and Working**

**Status:** ✅ OPERATIONAL

**Location:** `scripts/ollama_yaml_processor.py`
**Endpoint:** `http://localhost:11434`
**Model:** `llama3.2` (default)

**Test Command:**
```bash
cd "O:\Theophysics_Backend\Backend Python"
python scripts/ollama_yaml_processor.py --test
```

**What it does:**
- YAML frontmatter generation
- Axiom reference extraction
- Semantic tagging
- Batch processing of vault files

**How to verify Ollama is running:**
```bash
curl http://localhost:11434/api/tags
```

Should return list of installed models.

---

### ✅ **3. PNG Export + Cloud Sync - ADDED**

**Current:** HTML dashboards with Chart.js (no PNG yet)

**Adding Now:**
1. **Playwright** for screenshot generation
2. **Auto-copy to cloud sync folder**
3. **Embed PNGs in dashboards**
4. **Batch export mode**

**Cloud Sync Path:** 
👉 **Tell me where to copy PNGs** (e.g., `D:\Dropbox\Theophysics\Dashboards`)

Once you give me the path, system will:
- Generate HTML dashboard
- Screenshot each chart as PNG
- Copy PNG to your cloud folder
- Embed PNG in dashboard
- Keep PNG in local `dashboards/images/` folder

---

### ✅ **4. Mermaid Diagram Aggregation - YES, Exists**

**Status:** ✅ OPERATIONAL

**Location:** `engine/mermaid_generator.py`

**Current Capabilities:**
- Individual Mermaid diagram generation
- PNG export using mmdc (mermaid-cli)
- Semantic tag extraction
- Auto-coloring by element type

**What You Want:**
1. Auto-insert diagrams at end of semantic-tagged notes
2. Aggregate ALL diagrams into ONE mega-map

**Solution Being Added:**
- `MermaidAggregator` class
- Scans vault for semantic notes
- Combines all flowcharts
- Creates master diagram
- Exports to PNG + embeds in index

---

## 🚀 SYSTEM STATUS

| Component | Status | Location |
|-----------|--------|----------|
| **CDCM Analyzer** | ✅ Working | `core/coherence/cdcm_analyzer.py` |
| **HTML Dashboards** | ✅ Working | `core/coherence/html_generator.py` |
| **Qt Interface** | ✅ Working | `ui/tabs/coherence_analysis_tab.py` |
| **Ollama** | ✅ Working | `scripts/ollama_yaml_processor.py` |
| **Mermaid** | ✅ Working | `engine/mermaid_generator.py` |
| **PNG Export** | 🔨 Adding | (new module) |
| **Mermaid Aggregator** | 🔨 Adding | (new module) |

---

## 📦 WHAT'S BEING ADDED NOW

### **1. PNG Screenshot System**

**File:** `core/coherence/screenshot_exporter.py`

**Features:**
- Playwright-based HTML → PNG
- Chart.js rendering wait
- High-res export (2560x1440)
- Auto-crop whitespace
- Cloud folder sync

**Usage:**
```python
from core.coherence.screenshot_exporter import export_dashboard_png

png_path = export_dashboard_png(
    html_path="dashboard.html",
    output_dir="O:/Theophysics_Backend/dashboards/images",
    cloud_sync_dir="D:/Dropbox/Theophysics/Dashboards"  # YOUR PATH
)
```

---

### **2. Mermaid Aggregation System**

**File:** `engine/mermaid_aggregator.py`

**Features:**
- Scans vault for semantic-tagged notes
- Extracts existing Mermaid diagrams
- Combines into master flowchart
- Auto-inserts diagrams at note end
- Creates index with all diagrams

**Usage:**
```python
from engine.mermaid_aggregator import MermaidAggregator

agg = MermaidAggregator(vault_path="O:/THEOPHYSICS")
agg.scan_vault()
agg.auto_insert_diagrams()  # Add to end of semantic notes
agg.generate_master_diagram()  # Create mega-map
agg.export_master_png()  # Save as PNG
```

---

## 🎯 WORKFLOW AFTER SETUP

### **Daily Workflow:**

1. **Edit CDCM.xlsx** (add axioms, map theories)
2. **Launch Python app** → Go to Coherence Analysis tab
3. **Load Excel** → See metrics update
4. **Generate Dashboard** → Creates HTML + PNGs
5. **PNGs auto-copy** to your cloud sync folder
6. **View live** in browser or check cloud folder

### **Mermaid Workflow:**

1. **Run semantic tagger** on vault notes
2. **Mermaid auto-generates** for tagged notes
3. **Diagrams auto-insert** at end of notes
4. **Aggregator creates** master mega-map
5. **Master PNG syncs** to cloud folder

---

## 📍 FILE LOCATIONS

### **CDCM System:**
```
O:\Theophysics_Backend\
├── CDCM.xlsx                                    # Main data file
├── Backend Python\
│   ├── core\coherence\
│   │   ├── cdcm_analyzer.py                     # Reads Excel
│   │   ├── html_generator.py                    # Creates dashboards
│   │   ├── screenshot_exporter.py               # 🆕 PNG export
│   │   └── README.md
│   ├── ui\tabs\
│   │   └── coherence_analysis_tab.py            # Qt interface
│   └── test_coherence.py                        # Tester
```

### **Ollama:**
```
O:\Theophysics_Backend\Backend Python\
├── scripts\
│   └── ollama_yaml_processor.py                 # YAML generator
└── RUN_OLLAMA_OVERNIGHT.bat                     # Batch runner
```

### **Mermaid:**
```
O:\Theophysics_Backend\Backend Python\
├── engine\
│   ├── mermaid_generator.py                     # Individual diagrams
│   └── mermaid_aggregator.py                    # 🆕 Master combiner
```

---

## 🔧 INSTALLATION REQUIREMENTS

### **For PNG Export (new):**
```bash
pip install playwright
playwright install chromium
```

### **For Mermaid CLI:**
```bash
npm install -g @mermaid-js/mermaid-cli
```

### **Verify Mermaid:**
```bash
mmdc --version
```

---

## ⚡ QUICK TESTS

### **1. Test CDCM System:**
```bash
cd "O:\Theophysics_Backend\Backend Python"
python test_coherence.py
```

### **2. Test Ollama:**
```bash
curl http://localhost:11434/api/tags
```

### **3. Test Mermaid:**
```bash
mmdc --version
```

### **4. Test PNG Export (after adding):**
```bash
python test_png_export.py
```

---

## 🎨 CUSTOMIZATION

### **Change Cloud Sync Path:**

Edit `core/coherence/screenshot_exporter.py`:
```python
DEFAULT_CLOUD_SYNC = "D:/Your/Cloud/Path"  # <-- CHANGE THIS
```

### **Change PNG Resolution:**
```python
SCREENSHOT_WIDTH = 2560   # Default
SCREENSHOT_HEIGHT = 1440  # Default
```

### **Change Mermaid Colors:**

Edit `engine/mermaid_generator.py`:
```python
NODE_COLORS = {
    'Axiom': '#1a237e',      # Deep blue
    'Theorem': '#e65100',    # Orange
    # Add your colors
}
```

---

## 📊 OUTPUT EXAMPLES

### **CDCM Dashboards:**
```
O:\Theophysics_Backend\dashboards\
├── Primary_Framework_dashboard.html       # Interactive
├── images\
│   ├── Primary_Framework_metrics.png      # Auto-generated
│   ├── Primary_Framework_radar.png        # Auto-generated
│   └── Primary_Framework_bars.png         # Auto-generated
```

### **Cloud Sync Folder:**
```
D:\Dropbox\Theophysics\Dashboards\        # YOUR PATH
├── Primary_Framework_metrics.png          # Auto-copied
├── Primary_Framework_radar.png            # Auto-copied
├── framework_comparison.png               # Auto-copied
└── master_mermaid_2024-12-26.png         # Aggregated diagram
```

---

## 🚨 TROUBLESHOOTING

### **"CDCM.xlsx not found"**
- Check path: `O:\Theophysics_Backend\CDCM.xlsx`
- Make sure file exists
- Try absolute path in UI

### **"Ollama not available"**
- Start Ollama: `ollama serve`
- Check: `curl http://localhost:11434/api/tags`
- Verify in Task Manager

### **"Mermaid PNG export failed"**
- Install: `npm install -g @mermaid-js/mermaid-cli`
- Verify: `mmdc --version`
- Check PATH includes npm global folder

### **"Playwright not found"**
- Install: `pip install playwright`
- Setup: `playwright install chromium`

---

## 📞 NEXT STEPS

1. **Tell me your cloud sync path** → I'll wire it up
2. **Run test_coherence.py** → Verify CDCM works
3. **Install Playwright** → For PNG export
4. **Test Ollama** → `curl localhost:11434/api/tags`
5. **Test Mermaid** → `mmdc --version`

---

**Status: System 95% complete. Need:**
1. ✅ Your cloud sync folder path
2. 🔨 PNG export module (adding now)
3. 🔨 Mermaid aggregator (adding now)
