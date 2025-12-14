# Definition 2.0 Integration Checklist

**Use this checklist to integrate Definition 2.0 into your existing system.**

---

## ✅ Phase 1: Installation (5 minutes)

- [ ] Install additional dependencies:
  ```bash
  pip install -r requirements_v2.txt
  ```

- [ ] Verify installation:
  ```bash
  python -c "from engine.definition_processor_v2 import DefinitionProcessorV2; print('✓ Ready')"
  ```

- [ ] Check existing engines are compatible:
  ```bash
  python -c "from engine.enhanced_definition_engine import EnhancedDefinitionEngine; print('✓ Enhanced engine OK')"
  python -c "from engine.knowledge_acquisition_engine import KnowledgeAcquisitionEngine; print('✓ Knowledge engine OK')"
  python -c "from engine.structure_engine import StructureEngine; print('✓ Structure engine OK')"
  ```

---

## ✅ Phase 2: UI Integration (10 minutes)

### Option A: Add to Existing Main Window

Edit `ui/main_window.py` or `ui/main_window_v2.py`:

```python
# Add import at top
from ui.tabs.definitions_v2_tab import DefinitionsV2Tab

# In __init__ or setup_tabs method, add:
self.definitions_v2_tab = DefinitionsV2Tab(
    self.definitions_manager,
    self.settings
)
self.tabs.addTab(self.definitions_v2_tab, "Definitions V2")
```

### Option B: Standalone Launch

Create `launch_definitions_v2.py`:

```python
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from ui.tabs.definitions_v2_tab import DefinitionsV2Tab
from engine.settings import Settings

app = QApplication(sys.argv)
settings = Settings()
settings.set("vault_path", "path/to/vault")

tab = DefinitionsV2Tab(None, settings)
tab.show()

sys.exit(app.exec())
```

**Checklist:**
- [ ] UI tab added to main window OR standalone launcher created
- [ ] Tab loads without errors
- [ ] All buttons visible
- [ ] Settings accessible

---

## ✅ Phase 3: Test Run (15 minutes)

### Create Test Vault

```bash
mkdir test_vault
cd test_vault
mkdir Definitions
```

### Create 3 Test Definitions

**File: `Definitions/def-test-1.md`**
```markdown
---
type: definition
id: def-test-1
symbol: T1
name: Test Term One
---

# T1 — Test Term One

## 1. Canonical Definition

> **Test Term One is a placeholder for testing.**
```

**File: `Definitions/def-test-2.md`**
```markdown
---
type: definition
id: def-test-2
symbol: T2
name: Test Term Two
---

# T2 — Test Term Two

## 1. Canonical Definition

> **Test Term Two is another test placeholder.**
```

**File: `Definitions/def-test-3.md`**
```markdown
---
type: definition
id: def-test-3
symbol: T3
name: Test Term Three
---

# T3 — Test Term Three

## 1. Canonical Definition

> **Test Term Three completes the test set.**
```

### Run Processor

```bash
python -m engine.definition_processor_v2 "test_vault" --workers 2
```

**Expected output:**
```
======================================================================
Definition 2.0 Mass Processor
======================================================================

[1/4] Indexing vault...
  ✓ Found 3 definitions
  ✓ Found 0 equations
  ✓ Tracked 0 term usages

[2/4] Processing 3 definitions...
  Using 2 workers
  Min confidence threshold: 0.9

  Progress: 3/3 (100.0%) - ETA: 0.0m

[3/4] Generating reports...
  ✓ Summary report: test_vault/Definitions_v2/processing_summary.md
  ✓ Provenance log: test_vault/Definitions_v2/provenance_log.json

[4/4] Complete!
  Total time: 0.5 minutes
  Rate: 6.0 definitions/second

  Results:
    ✓ Success: 3
    ⚠ Partial: 0
    ✗ Failed: 0
    ⊘ Skipped: 0
```

**Checklist:**
- [ ] Processing completes without errors
- [ ] `Definitions_v2/` folder created
- [ ] `processing_summary.md` generated
- [ ] `provenance_log.json` generated
- [ ] Reports are readable

---

## ✅ Phase 4: Verify Outputs (10 minutes)

### Check Generated Files

```bash
ls test_vault/Definitions_v2/
```

**Expected:**
- `def-test-1.md`
- `def-test-2.md`
- `def-test-3.md`
- `processing_summary.md`
- `provenance_log.json`
- `external_sources/` (directory)

### Verify Processing Summary

Open `test_vault/Definitions_v2/processing_summary.md`:

**Should contain:**
- Statistics section
- Definitions with drift (should be empty for test)
- External sources summary

### Verify Provenance Log

Open `test_vault/Definitions_v2/provenance_log.json`:

**Should contain:**
```json
{
  "generated": "2025-12-12T...",
  "total_definitions": 3,
  "entries": [
    {
      "term_id": "def-test-1",
      "term_name": "Test Term One",
      "status": "success",
      "provenance": [...],
      "external_sources": [...],
      ...
    },
    ...
  ]
}
```

**Checklist:**
- [ ] All 3 definitions processed
- [ ] Summary report readable
- [ ] Provenance log valid JSON
- [ ] External sources attempted (may be empty for test terms)

---

## ✅ Phase 5: AI Copilot Setup (Optional, 15 minutes)

### For Obsidian Copilot Plugin

1. [ ] Install Copilot plugin in Obsidian
2. [ ] Open plugin settings
3. [ ] Add custom prompt
4. [ ] Copy content from `prompts/definition_copilot_prompt.md`
5. [ ] Save as "Definition Integrity Copilot"

### Test the Copilot

1. [ ] Open a definition note in Obsidian
2. [ ] Trigger copilot with custom prompt
3. [ ] Verify it returns:
   - Status summary
   - Consistency check
   - Mathematical verification
   - Recommendations

---

## ✅ Phase 6: Production Run (20 minutes)

### Backup First!

```bash
# Create backup of your vault
cp -r /path/to/vault /path/to/vault_backup_$(date +%Y%m%d)
```

### Run on Full Vault

**Via GUI:**
1. [ ] Open Definitions V2 tab
2. [ ] Set workers to 8 (or your CPU count)
3. [ ] Check all options
4. [ ] Click "Start Processing"
5. [ ] Wait for completion (~15-20 minutes for 700 defs)

**Via CLI:**
```bash
python -m engine.definition_processor_v2 "/path/to/vault" --workers 8
```

### Monitor Progress

Watch for:
- [ ] Progress updates every 10 definitions
- [ ] No critical errors
- [ ] External sources being fetched
- [ ] ETA countdown

### Review Results

After completion:
- [ ] Check `Definitions_v2/processing_summary.md`
- [ ] Review drift log for inconsistencies
- [ ] Examine external comparisons
- [ ] Verify provenance tracking

---

## ✅ Phase 7: Integration & Review (Ongoing)

### Review Auto-Generated Content

For each definition with external content:
1. [ ] Read the provenance banner
2. [ ] Check confidence score (should be ≥0.90)
3. [ ] Verify source URL
4. [ ] Assess relevance
5. [ ] Manually integrate if valuable

### Address Drift

For each drift detected:
1. [ ] Read the drift log entry
2. [ ] Check severity (compatible/minor/contradiction)
3. [ ] Review context
4. [ ] Update canonical definition OR
5. [ ] Add clarification to domain-specific section

### Update Canonical Definitions

For definitions needing updates:
1. [ ] Open original definition file
2. [ ] Review auto-generated external comparison
3. [ ] Integrate high-value content
4. [ ] Add provenance note in "Notes & Examples"
5. [ ] Update `last_reviewed` date

---

## ✅ Phase 8: Establish Workflow (30 minutes)

### Weekly Processing

Create `scripts/weekly_definition_check.py`:

```python
from pathlib import Path
from engine.definition_processor_v2 import DefinitionProcessorV2
from datetime import datetime

vault_path = Path("path/to/vault")
processor = DefinitionProcessorV2(vault_path, max_workers=8)

print(f"Weekly Definition Check - {datetime.now()}")
stats = processor.process_all_definitions(force_reprocess=False)

# Email or log results
print(f"Processed: {stats['success']}")
print(f"Drift detected: {stats['partial']}")
```

### Pre-Publication Check

Create `scripts/pre_publication_check.py`:

```python
from pathlib import Path
from engine.enhanced_definition_engine import EnhancedDefinitionEngine

vault_path = Path("path/to/vault")
engine = EnhancedDefinitionEngine(vault_path)

# Full index
engine.full_index()

# Check all drift
drift_report = engine.check_drift()

if drift_report['total_drifts'] > 0:
    print("⚠️ WARNING: Drift detected!")
    print(f"Total: {drift_report['total_drifts']}")
    print("Review before publication!")
else:
    print("✓ All definitions consistent!")
```

**Checklist:**
- [ ] Weekly check script created
- [ ] Pre-publication check script created
- [ ] Scripts added to cron/task scheduler (optional)
- [ ] Team notified of new workflow

---

## ✅ Phase 9: Documentation & Training (1 hour)

### For Your Team

1. [ ] Share `DEFINITION_V2_README.md`
2. [ ] Walk through `docs/DEFINITION_V2_GUIDE.md`
3. [ ] Demo the GUI
4. [ ] Show example outputs
5. [ ] Explain provenance system
6. [ ] Demonstrate AI copilot

### Create Internal Guide

Document your specific:
- [ ] Vault structure
- [ ] Custom templates (if any)
- [ ] Workflow procedures
- [ ] Review process
- [ ] Publication checklist

---

## ✅ Phase 10: Optimization (Optional)

### Performance Tuning

If processing is slow:
- [ ] Increase workers (up to CPU count)
- [ ] Disable external downloads for quick checks
- [ ] Use incremental mode (don't force reprocess)
- [ ] Process in batches by domain

### Custom Templates

If you need custom sections:
- [ ] Copy `templates/definition_template.md`
- [ ] Modify sections
- [ ] Update `structure_engine.py` to use custom template
- [ ] Test with new definitions

### AI Integration

If you have AI access:
- [ ] Implement AI engine wrapper
- [ ] Pass to `EnhancedDefinitionEngine`
- [ ] Enable AI-powered drift detection
- [ ] Test accuracy improvements

---

## 🎉 Completion Checklist

You're ready for production when:

- [x] All dependencies installed
- [x] Test run successful (3 definitions)
- [x] UI integrated or standalone launcher created
- [x] Production run completed (700+ definitions)
- [x] Outputs verified (reports, provenance, drift)
- [x] AI copilot configured (optional)
- [x] Workflow established (weekly checks, pre-pub)
- [x] Team trained on new system
- [x] Documentation accessible

---

## 🚀 You're Ready!

**Next steps:**
1. Run weekly checks
2. Review drift logs
3. Integrate high-value external content
4. Use AI copilot for critical definitions
5. Run pre-publication checks

**Questions?**
- Check `docs/DEFINITION_V2_GUIDE.md`
- Review `examples/process_definitions_example.py`
- Read troubleshooting section

---

**Status:** ✅ Integration Complete  
**Date:** 2025-12-12  
**Version:** 2.0
