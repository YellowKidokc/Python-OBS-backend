# DASHBOARD PNG AUTO-ORGANIZATION SYSTEM

## 📁 FOLDER STRUCTURE (Auto-Created)

```
O:\00_MEDIA\Dashboards\
├── 2024-12-26\                    ← Auto-created daily folders
│   ├── Primary_Framework_metrics.png
│   ├── Primary_Framework_radar.png
│   ├── Theory_Comparison_full.png
│   └── CDCM_Analysis_14-30.png
│
├── 2024-12-27\                    ← Tomorrow's folder (auto-created when needed)
│   ├── Updated_Analysis_metrics.png
│   └── Framework_Comparison.png
│
└── 2024-12-28\                    ← And so on...
    └── Weekly_Report.png
```

**NO MANUAL SETUP NEEDED** - Folders create automatically!

---

## 🎯 HOW IT WORKS

### **When you export a dashboard:**

1. **System checks date** → December 26, 2024
2. **Creates folder if needed** → `O:\00_MEDIA\Dashboards\2024-12-26\`
3. **Generates smart filename** → `Primary_Framework_metrics.png`
4. **Saves TWO copies:**
   - **Local:** `O:\Theophysics_Backend\dashboards\images\Primary_Framework_metrics.png`
   - **Media:** `O:\00_MEDIA\Dashboards\2024-12-26\Primary_Framework_metrics.png`

### **Naming Convention:**

```
[Framework_Name]_[Chart_Type]_[Optional_Time].png

Examples:
✓ Primary_Framework_metrics.png
✓ Primary_Framework_radar.png
✓ Theory_Comparison_full.png
✓ CDCM_Analysis_14-30.png (with timestamp)
✓ String_Theory_coherence.png
✓ Quantum_Loop_violations.png
```

---

## 🔄 INTEGRATION WITH YOUR EXISTING MEDIA SYSTEM

I noticed you already have organization scripts:

```
O:\00_MEDIA\
├── ORGANIZE-MEDIA.bat         ← Your existing organizer
├── Organize-Media.ps1          ← PowerShell version
├── Sync-To-R2.ps1              ← Cloudflare R2 sync
├── Publish-Gallery.ps1         ← Gallery publisher
└── Dashboards\                 ← NEW (integrates with your system)
    └── 2024-12-26\
```

**The Dashboards folder follows your existing structure:**
- Date-based organization (like your other folders)
- Clean naming (underscores, no spaces)
- PNG format (compatible with gallery system)
- Ready for R2 sync (via your Sync-To-R2.ps1)

---

## 📊 EXAMPLE WORKFLOW

### **Scenario: Generate CDCM Dashboard**

```python
from core.coherence.screenshot_exporter import export_dashboard_png

# Export dashboard
png = export_dashboard_png(
    html_path="Primary_Framework_dashboard.html",
    output_dir="./dashboards/images",
    filename_prefix="Primary_Framework",
    chart_type="metrics"
)

# Result:
# ✓ Local: O:\Theophysics_Backend\dashboards\images\Primary_Framework_metrics.png
# ✓ Media: O:\00_MEDIA\Dashboards\2024-12-26\Primary_Framework_metrics.png
```

### **Next Day (December 27):**

```python
# Same code, but system automatically:
# 1. Creates O:\00_MEDIA\Dashboards\2024-12-27\
# 2. Saves there instead

png = export_dashboard_png(...)
# ✓ Media: O:\00_MEDIA\Dashboards\2024-12-27\Primary_Framework_metrics.png
```

---

## 🎨 CHART TYPES (Auto-Named)

When you export different chart types, they get descriptive names:

| Chart Type | Filename Example |
|------------|------------------|
| **Metrics Card** | `Primary_Framework_metrics.png` |
| **Radar Chart** | `Primary_Framework_radar.png` |
| **Bar Chart** | `Primary_Framework_bars.png` |
| **Comparison** | `Theory_Comparison_full.png` |
| **Full Dashboard** | `CDCM_Analysis_complete.png` |

---

## 🔍 FINDING YOUR DASHBOARDS

### **List Recent Exports:**

```python
from core.coherence.screenshot_exporter import list_recent_dashboards

# Show last 7 days
list_recent_dashboards(days=7)

# Output:
# 📁 Recent dashboard PNGs (last 7 days):
#   • 2024-12-26/Primary_Framework_metrics.png (2.3 MB) - 2024-12-26 14:30
#   • 2024-12-26/Theory_Comparison_full.png (3.1 MB) - 2024-12-26 14:32
#   • 2024-12-25/CDCM_Analysis_complete.png (4.5 MB) - 2024-12-25 22:15
```

### **View in File Explorer:**

```
📂 O:\00_MEDIA\Dashboards\
    📂 2024-12-26\
        🖼️ Primary_Framework_metrics.png (2.3 MB)
        🖼️ Primary_Framework_radar.png (1.8 MB)
        🖼️ Theory_Comparison_full.png (3.1 MB)
```

---

## 🚀 SYNC TO CLOUDFLARE R2

Your existing `Sync-To-R2.ps1` script can include dashboards:

```powershell
# Add to your Sync-To-R2.ps1:
$dashboards = "O:\00_MEDIA\Dashboards"
rclone sync $dashboards r2:theophysics-media/Dashboards --progress
```

This syncs all dashboard PNGs to your R2 bucket, maintaining the date folder structure.

---

## 📸 ADVANCED NAMING OPTIONS

### **With Timestamp (for versioning):**

```python
exporter = ScreenshotExporter()
png = exporter.export_dashboard(
    html_path="dashboard.html",
    output_dir="./output",
    filename_prefix="Analysis",
    chart_type="metrics",
    sync_to_media=True
)

# Result: Analysis_metrics_2024-12-26_14-30.png
```

### **Without Date Folders (flat structure):**

```python
exporter = ScreenshotExporter(use_date_folders=False)
png = exporter.export_dashboard(...)

# Result: O:\00_MEDIA\Dashboards\Analysis_metrics_2024-12-26.png
```

---

## 🎯 CONFIGURATION

### **Default Settings (in screenshot_exporter.py):**

```python
DEFAULT_WIDTH = 2560          # High-res 1440p
DEFAULT_HEIGHT = 1440         # Perfect for 4K monitors
MEDIA_FOLDER = "O:/00_MEDIA/Dashboards"
use_date_folders = True       # Auto-create YYYY-MM-DD subfolders
```

### **Customize:**

```python
from core.coherence.screenshot_exporter import ScreenshotExporter

exporter = ScreenshotExporter(
    width=3840,              # 4K ultra-wide
    height=2160,             # Ultra HD
    media_folder=Path("D:/My/Custom/Path"),
    use_date_folders=False   # Flat structure
)
```

---

## 🔧 INTEGRATION WITH QT APP

The Coherence Analysis Tab will automatically:

1. Generate HTML dashboard
2. Take PNG screenshot
3. Save to both locations:
   - Local: `O:\Theophysics_Backend\dashboards\images\`
   - Media: `O:\00_MEDIA\Dashboards\YYYY-MM-DD\`
4. Show success message with paths

**You don't need to do anything manually!**

---

## 📦 COMPLETE FILE LOCATIONS

### **When you click "Generate Dashboard" in the app:**

```
CDCM.xlsx (input)
    ↓
[Load & Analyze]
    ↓
HTML Dashboard
    ↓ (screenshot)
    ↓
TWO COPIES:
    ├─→ LOCAL: O:\Theophysics_Backend\dashboards\images\[name].png
    └─→ MEDIA: O:\00_MEDIA\Dashboards\YYYY-MM-DD\[name].png
```

### **File Sizes:**

- **Metrics card**: ~2-3 MB
- **Radar chart**: ~1-2 MB
- **Full dashboard**: ~4-6 MB
- **Comparison**: ~3-4 MB

---

## ✅ SUMMARY

### **What You Get:**

✓ **Auto-organization** by date (YYYY-MM-DD folders)  
✓ **Smart naming** (Framework_ChartType.png)  
✓ **Dual storage** (local + media)  
✓ **High-res PNGs** (2560x1440)  
✓ **No manual setup** required  
✓ **Integration** with existing media system  
✓ **R2 sync ready** (via your scripts)  

### **What You Do:**

1. Click "Generate Dashboard" in app
2. Done! (everything else is automatic)

### **Where Files Go:**

- **Work in progress**: `O:\Theophysics_Backend\dashboards\`
- **Permanent archive**: `O:\00_MEDIA\Dashboards\YYYY-MM-DD\`
- **Cloud backup**: Via your Sync-To-R2.ps1

---

## 🎯 NEXT STEPS

**1. Test the system:**
```bash
cd "O:\Theophysics_Backend\Backend Python"
python core\coherence\screenshot_exporter.py
```

**2. Generate your first dashboard:**
```python
python test_coherence.py  # Creates dashboard + PNG
```

**3. Check media folder:**
```
📂 O:\00_MEDIA\Dashboards\2024-12-26\
    🖼️ [Your new PNG here]
```

**4. Optional - Add to R2 sync:**
```powershell
# Edit Sync-To-R2.ps1, add:
rclone sync "O:\00_MEDIA\Dashboards" r2:theophysics-media/Dashboards
```

---

**NO MANUAL FOLDER CREATION NEEDED!**  
System creates everything automatically based on today's date.
