# Definition 2.0 - Complete Guide

**Version:** 2.0  
**Last Updated:** 2025-12-12

---

## Overview

Definition 2.0 is a research-grade definition management system that:

- ✅ **Indexes** your entire vault to track term usage
- ✅ **Detects drift** when terms are used inconsistently
- ✅ **Maps equations** to show where each variable appears
- ✅ **Fetches external sources** (SEP > arXiv > Wikipedia)
- ✅ **Tracks provenance** so you know what's auto-generated vs human-written
- ✅ **Processes at scale** (700+ definitions with multi-threading)
- ✅ **Ensures correctness** (only includes high-certainty data ≥ 90%)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Obsidian Vault                          │
│                  (Source of Truth)                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              VaultIndexer (Python)                          │
│  • Scans all .md files                                      │
│  • Extracts definitions (type: definition)                  │
│  • Tracks term usages                                       │
│  • Indexes equations (with % id: and % uses:)               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         External Source Fetcher                             │
│  Priority: SEP > arXiv > IEP > PhilPapers > Wikipedia       │
│  • Checks high-value sources first                          │
│  • Downloads verified content                               │
│  • Adds provenance banners                                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           DriftDetector (AI-powered)                        │
│  • Compares canonical definition vs actual usage            │
│  • Detects contradictions                                   │
│  • Generates drift log entries                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│        DefinitionProcessorV2 (Orchestrator)                 │
│  • Coordinates all engines                                  │
│  • Multi-threaded processing                                │
│  • Generates reports & provenance logs                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Output Files                                   │
│  • Definitions_v2/def-*.md (generated notes)                │
│  • processing_summary.md                                    │
│  • provenance_log.json                                      │
│  • drift_log.json                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## The 10-Section Definition Standard

Every definition note has these sections:

1. **Canonical Definition** - One-sentence precise statement
2. **Axioms** - Ontological, mathematical, conservation laws
3. **Mathematical Structure** - Equations, dynamics, thresholds
4. **Domain Interpretations** - Physics, info theory, psych, sociology, theology
5. **Operationalization** - How to measure it
6. **Failure Modes** - What "broken" looks like
7. **Integration Map** - Where it appears in papers & equations
8. **Usage Drift Log** - Auto-populated deviations
9. **External Comparison** - How it matches/differs from literature
10. **Notes & Examples** - Analogies, diagrams, open questions

---

## Quick Start

### 1. Using the GUI

1. Open the Theophysics Manager
2. Go to **Definitions V2** tab
3. Configure:
   - CPU cores (default: 8)
   - Force reprocess (if needed)
   - Download external sources ✓
   - Detect drift ✓
4. Click **🚀 Start Processing**
5. Wait for completion (progress bar shows status)
6. Click **📊 View Report** to see results

### 2. Using Python CLI

```bash
cd theophysics_manager
python -m engine.definition_processor_v2 "path/to/vault" --workers 8
```

Options:
- `--workers N` - Number of CPU cores to use
- `--output DIR` - Custom output directory
- `--force` - Force reprocess all definitions

### 3. Using the AI Copilot (Obsidian Plugin)

1. Install an AI plugin (e.g., Copilot, Smart Connections)
2. Load the prompt from: `prompts/definition_copilot_prompt.md`
3. Open any definition note
4. Run the copilot to check:
   - Consistency
   - Mathematical correctness
   - Cross-domain alignment
   - External comparison
   - Drift detection

---

## Provenance Tracking

Every auto-generated block is marked with a banner:

```markdown
> [AUTOGENERATED — SOURCE: EXTERNAL]  
> Source: Stanford Encyclopedia of Philosophy  
> Confidence: 0.95  
> Retrieved: 2025-12-12  
> Do not treat as canonical until reviewed by human author.

[Content here...]
```

**Source Types:**
- `EXTERNAL` - From web sources (SEP, arXiv, Wikipedia)
- `PYTHON` - Generated by Python scripts
- `AI` - Generated by AI models
- `WEB` - General web scraping
- `USER` - Human-written (no banner)

**Confidence Levels:**
- `≥ 0.90` - Included in output (high certainty)
- `< 0.90` - Excluded (too uncertain)

---

## Equation Mapping

To track where variables appear in equations, add comments:

```markdown
$$
% id: eq-coherence-dynamic-01
% uses: C, G, Γ
\frac{dC}{dt} = G(C) - \Gamma(C)\, C
$$
```

The indexer will:
1. Extract the equation ID
2. Parse the variables used
3. Link to definition notes
4. Generate the Integration Map table

---

## Drift Detection

Drift is detected when a term is used differently than its canonical definition.

**Types of Drift:**
- `compatible_expansion` - Extends the definition in a compatible way
- `minor_drift` - Slightly different usage, not contradictory
- `contradiction` - Direct contradiction with canonical definition

**Example Drift Log Entry:**

| Date | File | Context | Deviation |
|------|------|---------|-----------|
| 2025-12-10 | [[Paper-03]] | "G_total represents societal grace pool" | Minor drift - aggregate vs rate |

---

## External Source Priority

Sources are checked in this order:

1. **Stanford Encyclopedia of Philosophy** (SEP) - Priority 1
   - Most authoritative for philosophy/theory
   - Peer-reviewed, expert-written
   
2. **arXiv** - Priority 2
   - Best for cutting-edge physics/math
   - Pre-prints, rapid dissemination
   
3. **Internet Encyclopedia of Philosophy** (IEP) - Priority 3
   - Good alternative to SEP
   
4. **PhilPapers** - Priority 4
   - Comprehensive philosophy database
   
5. **Scholarpedia** - Priority 5
   - Peer-reviewed encyclopedia
   
6. **Wikipedia** - Priority 7
   - Fallback only
   - Good for general concepts

---

## File Structure

After processing, you'll have:

```
vault/
├── Definitions/                    # Your original definitions
├── Definitions_v2/                 # Generated output
│   ├── def-coherence.md
│   ├── def-grace.md
│   ├── def-logos-field.md
│   ├── ...
│   ├── processing_summary.md       # Human-readable report
│   ├── provenance_log.json         # Complete provenance data
│   └── external_sources/           # Downloaded content
│       ├── sep/
│       ├── arxiv/
│       └── wikipedia/
└── .theophysics/                   # Cache & indexes
    ├── definition_index.json
    └── drift_log.json
```

---

## Best Practices

### 1. Start Small
Process 10-20 definitions first to verify everything works.

### 2. Review Provenance
Always review auto-generated content before treating it as canonical.

### 3. Update Regularly
Run processing after major vault changes to detect new drift.

### 4. Use the AI Copilot
For critical definitions (C, χ, Φ, G), use the AI copilot for deep verification.

### 5. Manual Integration
Don't auto-merge external content. Review and integrate manually.

### 6. Track Changes
Keep the drift log and provenance log in version control.

---

## Troubleshooting

### "No definitions found"
- Ensure your definition notes have `type: definition` in frontmatter
- Check vault path is correct

### "External sources failing"
- Check internet connection
- Some sources may be rate-limited (wait 1-2 minutes)
- Wikipedia is always available as fallback

### "Processing is slow"
- Reduce number of workers if system is overloaded
- Disable external downloads for faster processing
- Use incremental mode (don't force reprocess)

### "High memory usage"
- Normal for 700+ definitions
- Reduce workers if memory is constrained
- Process in batches (filter by domain)

---

## Advanced Usage

### Custom Templates

Create your own template:

```python
from engine.structure_engine import StructureEngine

engine = StructureEngine(settings, db)
path = engine.build_definition_structure(
    term="Quantum Coherence",
    symbol="Q_c",
    template_path=Path("my_template.md")
)
```

### Programmatic Access

```python
from engine.definition_processor_v2 import DefinitionProcessorV2

processor = DefinitionProcessorV2(
    vault_path=Path("vault"),
    max_workers=16
)

# Process all
stats = processor.process_all_definitions()

# Generate specific note
path = processor.generate_definition_note("def-coherence")
```

### Integration with AI

```python
from engine.enhanced_definition_engine import EnhancedDefinitionEngine

engine = EnhancedDefinitionEngine(
    vault_path=Path("vault"),
    ai_engine=my_ai_engine  # Your AI wrapper
)

# AI-powered drift detection
report = engine.check_drift("def-coherence")
```

---

## Performance

**Benchmarks** (700 definitions, 8 workers):
- Indexing: ~30 seconds
- External fetching: ~10-15 minutes (with rate limiting)
- Drift detection: ~2 minutes
- Report generation: ~10 seconds
- **Total: ~15-20 minutes**

**Memory Usage:**
- Indexing: ~500 MB
- Processing: ~1-2 GB
- Peak: ~2.5 GB

**Disk Space:**
- Index files: ~10 MB
- External sources: ~50-100 MB (if downloaded)
- Generated notes: ~5-10 MB

---

## FAQ

**Q: Will this overwrite my existing definitions?**  
A: No. Generated files go to `Definitions_v2/`. Your originals are untouched.

**Q: Can I use this without internet?**  
A: Yes, but external source fetching will be skipped.

**Q: How accurate is drift detection?**  
A: With AI: ~85-90%. Without AI: ~60-70% (heuristic-based).

**Q: Can I customize the 10 sections?**  
A: Yes, edit `templates/definition_template.md`.

**Q: What if I have 10,000 definitions?**  
A: System scales well. Use 16-32 workers and expect ~1-2 hours.

---

## Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/theophysics-manager/issues)
- **Docs:** `docs/` directory
- **Examples:** `examples/` directory

---

**Built for the Theophysics Research Initiative**  
**Version 2.0 - December 2025**
