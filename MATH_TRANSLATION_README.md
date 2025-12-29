# Math Translation Layer - User Guide

## Overview

The Math Translation Layer automatically processes markdown documents containing LaTeX equations, applies human-readable translations, and prepares content for Text-to-Speech (TTS) audio generation.

## Features

- **Automatic Equation Detection**: Scans markdown files for both display (`$$...$$`) and inline (`$...$`) LaTeX equations
- **Translation Application**: Matches equations against a comprehensive translation table (588+ entries)
- **Visual Callout Boxes**: Wraps equations in styled callout boxes showing both visual and spoken forms
- **Folder Processing**: Maintains folder structure when processing multiple documents
- **TTS Integration**: Generates clean text files ready for the TTS pipeline
- **Statistics Tracking**: Reports on equations found, translated, and untranslated

## How to Use

### 1. Access the Math Translation Tab

Launch the Theophysics Manager and navigate to the **Math Translation** tab in the sidebar.

### 2. Check Translation Table Status

The top section shows:

- **Translation Table**: Whether the Excel file is loaded
- **Entries**: Number of equation translations available
- **Excel**: Whether the source file exists

If the table isn't loaded, click **Reload Translation Table**.

### 3. Process Documents

**Document Scanner Section:**

1. **Input Folder**: Browse to select a folder containing your markdown documents
2. **Output Folder**: Browse to select where processed documents should be saved
3. Click **Process Documents**

The system will:

- Scan all `.md` files in the input folder (including subfolders)
- Detect LaTeX equations
- Apply translations from the table
- Create formatted documents with callout boxes
- Maintain the same folder structure in the output

**Results** show:

- Total files processed
- Equations found and translated
- Any errors encountered

### 4. Generate TTS Audio

**TTS Audio Generation Section:**

1. Browse to select a **processed document** (from your output folder)
2. Click **Preview TTS Text** to see what will be spoken
3. Click **Generate Audio** to create a TTS-ready text file

The TTS text file is saved to:

```
O:\Theophysics_Backend\TTS_Pipeline\INBOX\
```

You can then run the TTS pipeline to generate the actual audio file.

## Example Workflow

### Input Document (`example.md`):

```markdown
# Theophysics Equation

The fundamental equation is:

$$\Delta E_{\text{required}} = T \cdot \Delta S$$

This shows the relationship between energy and entropy.
```

### Processed Output:

```markdown
# Theophysics Equation

The fundamental equation is:

> [!math] Mathematical Equation
> **Visual:** > $$\Delta E_{\text{required}} = T \cdot \Delta S$$
>
> **Spoken:**
> Delta E required equals T times Delta S

This shows the relationship between energy and entropy.
```

### TTS Text Output:

```
Theophysics Equation

The fundamental equation is:

Delta E required equals T times Delta S

This shows the relationship between energy and entropy.
```

## Callout Box Styling

The processed documents use Obsidian-compatible callout syntax:

- `> [!math]` creates a special math callout
- Visual equation is preserved for reading
- Spoken translation is provided for TTS

To apply custom styling in Obsidian, copy the CSS from:

```
O:\Theophysics_Backend\TTS_Pipeline\math_callout_styles.css
```

To your Obsidian vault's CSS snippets folder.

## Translation Table

The translation table is located at:

```
O:\Theophysics_Backend\TTS_Pipeline\MATH_TRANSLATION_TABLE_UPDATED (1).xlsx
```

**Format:**

- Column 1: LaTeX equation (with or without `$` delimiters)
- Last Column: Spoken translation

**Example entries:**
| LaTeX | Spoken |
|-------|--------|
| `$\chi = \chi_{\text{potential}} + \chi_{\text{actualized}}$` | "chi equals chi potential plus chi actualized" |
| `$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$` | "Delta x times Delta p is greater than or equal to h-bar over two" |

## Tips

1. **Batch Processing**: Process entire folders at once to maintain consistency
2. **Preview First**: Always preview TTS text before generating audio
3. **Folder Structure**: Output maintains input structure, making organization easy
4. **Untranslated Equations**: Check the results for untranslated equations and add them to the table
5. **Inline vs Display**: Display math (`$$`) gets full callouts, inline math (`$`) gets simpler formatting

## Troubleshooting

**Translation table not loading:**

- Verify the Excel file exists at the expected path
- Check file permissions
- Click "Reload Translation Table"

**No equations detected:**

- Ensure equations use proper LaTeX delimiters (`$` or `$$`)
- Check that files are valid markdown (`.md`)

**TTS audio not generating:**

- Verify the TTS pipeline is set up correctly
- Check that the INBOX folder exists
- Ensure the TTS text file was created successfully

## Integration with TTS Pipeline

After generating TTS text files, use the existing TTS pipeline:

```bash
cd O:\Theophysics_Backend\TTS_Pipeline
python tts_pipeline.py
```

Or use the batch file:

```bash
LAUNCH_TTS.bat
```

The pipeline will:

1. Read files from INBOX
2. Apply the Theophysics normalizer
3. Generate audio using your configured TTS engine
4. Save audio to OUTBOX
5. Move processed files to PROCESSED

## Future Enhancements

- Direct audio generation from the UI
- Real-time equation preview
- Batch TTS generation
- Custom translation editing
- Equation search and filtering
