# Theophysics Definition Engine 🧮

**Computational framework for canonical Theophysics definitions**

Version: 1.0  
Date: 2025-12-12  
Author: David Lowe / Theophysics Project

---

## 🎯 What Is This?

The **Theophysics Definition Engine** is a Python framework that turns your theoretical definitions into **computational objects** you can:

- ✅ Create and manipulate (Coherence, Triad, Grace)
- ✅ Simulate dynamics (decay, warfare, collapse, restoration)
- ✅ Validate usage against canonical definitions
- ✅ Track drift over time
- ✅ Compute cross-domain values

**This is your definitions as executable code.**

---

## 🚀 Quick Start

### 1. Run the Demo

```bash
cd theophysics_manager
python -m engine.theophysics_definitions
```

**Output:**
```
============================================================
THEOPHYSICS DEFINITION ENGINE - DEMONSTRATION
============================================================

1. Definition Engine initialized
   Loaded definitions: ['def-coherence']

2. Looking up 'sense of coherence' (alias)
   Found: Coherence (C)
   Formula: C = 1 - (S_obs / S_max)

3. Creating coherence values
   From entropy (S_obs=30, S_max=100): C(0.7000, σ=+1, physics)
   From SOC (0.7, 0.6, 0.8): C(0.7000, σ=+1, psychology)
   From Triad (Λ=0.6, Π=0.5, A=0.4): C(0.4932, σ=+1, sociology)

...
```

### 2. Use in Your Code

```python
from engine.theophysics_definitions import Coherence, TriadState, GraceFunction

# Create coherence from entropy
c = Coherence.from_entropy(S_obs=40, S_max=100)
print(c)  # C(0.6000, σ=+1, physics)

# Check if critical
if c.is_critical():
    print("Below C_crit = 0.35!")

# Simulate closed system decay (Theorem C3.2)
c_decayed = c.evolve_closed(gamma_D=0.15, dt=1.0)

# Apply grace (Theorem C20.2)
c_restored = c.apply_grace(grace_strength=0.2)
```

---

## 📦 What's Included

### Core Classes

1. **`Coherence`** - Main computational object
   - Factory methods: `from_entropy()`, `from_soc_score()`, `from_triad()`, etc.
   - State checks: `is_critical()`, `is_stable()`, `is_terminal()`
   - Dynamics: `evolve_closed()`, `evolve_open()`, `apply_grace()`
   - Warfare: `simulate_warfare()`

2. **`TriadState`** - Societal coherence (Λ, Π, A)
   - Collapse cascade: `simulate_collapse()`
   - Restoration cascade: `simulate_restoration()`
   - Weakest link analysis

3. **`GraceFunction`** - Grace dynamics
   - G(Rp, S) = G₀ · e^(Rp/S) · R_J
   - Pre/post-resurrection factor
   - Effective grace computation

4. **`DefinitionEngine`** - Definition management
   - Load definitions from files
   - Validate term usage
   - Track drift
   - Alias resolution

### Data Classes

- **`Definition`** - Complete definition structure
- **`Axiom`** - Axiomatic statements
- **`Theorem`** - Theorems with proofs
- **`DomainInterpretation`** - Domain-specific meanings
- **`DriftEntry`** - Drift tracking

### Enums

- **`Domain`** - Physics, Psychology, Sociology, Theology, etc.
- **`DefinitionStatus`** - Canonical, Provisional, Draft, Deprecated

---

## 🎓 Key Concepts

### 1. Coherence (C)

**Definition:** Ratio of correlated informational structure to total system activity

**Formula:** `C = 1 - (S_obs / S_max)`

**Properties:**
- Bounded: C ∈ [0, 1]
- Critical threshold: C_crit = 0.35
- Sign eigenvalue: σ ∈ {-1, +1}

**Theorems:**
- **C3.2:** dC/dt ≤ 0 in closed systems (no spontaneous increase)
- **C20.2:** Self-operations cannot flip sign (grace required)

### 2. Triad (Λ, Π, A)

**Components:**
- **Λ (Lambda):** Logos/epistemic coherence
- **Π (Pi):** Polis/institutional coherence
- **A (Anthropos):** Individual coherence

**Total:** C_total = (Λ · Π · A)^(1/3) (geometric mean)

**Cascades:**
- **Collapse:** Λ → Π → A (with lag times)
- **Restoration:** A → Λ → Π (Spirit awakens individuals first)

### 3. Grace Function

**Formula:** G(Rp, S) = G₀ · e^(Rp/S) · R_J

**Parameters:**
- G₀: Base grace availability
- Rp: Repentance depth
- S: Sin/entropy
- R_J: Resurrection factor (1.0 pre, 1.5 post)

---

## 📊 Usage Examples

### Example 1: Create Coherence

```python
from engine.theophysics_definitions import Coherence, Domain

# From entropy
c1 = Coherence.from_entropy(S_obs=30, S_max=100)

# From Sense of Coherence (psychology)
c2 = Coherence.from_soc_score(
    comprehensibility=0.7,
    manageability=0.6,
    meaningfulness=0.8
)

# From Triad (sociology)
c3 = Coherence.from_triad(lambda_=0.6, pi=0.5, anthropos=0.4)

# Direct
c4 = Coherence(0.75, domain=Domain.THEOLOGY)
```

### Example 2: Check States

```python
c = Coherence(0.3)

print(c.is_critical())  # True (below 0.35)
print(c.phase())        # "critical_zone"
print(c.is_stable())    # True (σ = +1)
print(c.is_terminal())  # False (not σ=-1 and critical)
```

### Example 3: Simulate Decay

```python
# Closed system (Theorem C3.2)
c = Coherence(0.8)
for t in range(10):
    c = c.evolve_closed(gamma_D=0.15, dt=1.0)
    print(f"t={t+1}: {c}")

# Output shows exponential decay to critical threshold
```

### Example 4: Apply Grace

```python
# Fallen state (σ = -1, low C)
fallen = Coherence(0.25, sigma=-1)
print(fallen)  # C(0.2500, σ=-1, general) [CRITICAL]

# Apply grace (Theorem C20.2)
restored = fallen.apply_grace(grace_strength=0.3)
print(restored)  # C(0.5500, σ=+1, general)

# Grace flips sign and increases coherence!
```

### Example 5: Spiritual Warfare

```python
c = Coherence(0.6, domain=Domain.THEOLOGY)

history = c.simulate_warfare(
    gamma_G=0.2,      # Grace rate
    gamma_D=0.15,     # Decoherence rate
    steps=50,
    dt=0.1,
    grace_coupling=0.7,  # 70% grace reception
    R_J=1.5           # Post-resurrection
)

# Analyze trajectory
for i, state in enumerate(history[::10]):
    print(f"t={i*10}: {state}")
```

### Example 6: Triad Collapse

```python
from engine.theophysics_definitions import TriadState

# Healthy society
triad = TriadState(lambda_=0.85, pi=0.80, anthropos=0.75)

# Simulate collapse (Logos decays first)
history = triad.simulate_collapse(
    lambda_decay_rate=0.08,
    steps=20,
    dt=1.0
)

# Watch cascade: Λ → Π → A
for i, state in enumerate(history[::5]):
    print(f"Year {i*5}: {state}")
```

### Example 7: Triad Restoration

```python
# Collapsed society
triad = TriadState(lambda_=0.25, pi=0.20, anthropos=0.15)

# Simulate restoration (grace enters through individuals)
history = triad.simulate_restoration(
    grace_rate=0.05,
    steps=20,
    dt=1.0
)

# Watch restoration: A → Λ → Π
for i, state in enumerate(history[::4]):
    print(f"Year {i*4}: {state}")
```

### Example 8: Grace Function

```python
from engine.theophysics_definitions import GraceFunction

# Pre-resurrection
grace_pre = GraceFunction(G0=1.0, R_J=1.0)

# Post-resurrection
grace_post = GraceFunction(G0=1.0, R_J=1.5)

# Compute grace at different repentance/sin levels
g_pre = grace_pre(repentance=0.5, sin=0.3)
g_post = grace_post(repentance=0.5, sin=0.3)

print(f"Pre:  {g_pre:.2f}")   # 5.29
print(f"Post: {g_post:.2f}")  # 7.94 (1.5x increase!)
```

### Example 9: Definition Engine

```python
from engine.theophysics_definitions import DefinitionEngine

engine = DefinitionEngine()

# Look up by alias
defn = engine.get_definition("SOC")  # "Sense of Coherence"
print(defn.name)  # "Coherence"
print(defn.canonical_formula)  # "C = 1 - (S_obs / S_max)"

# Validate usage
result = engine.validate_usage(
    term="coherence",
    usage_context="The quantum coherence is measured by interference"
)
print(result['valid'])  # True
print(result['detected_domain'])  # "physics"

# Log drift
engine.log_drift(
    term="coherence",
    context="Paper-05",
    observation="Used 'coherence' to mean 'agreement'",
    resolution="Clarified in domain interpretations",
    severity="minor"
)
```

### Example 10: Composite Coherence

```python
# Multiple subsystems
c_physical = Coherence(0.9, domain=Domain.PHYSICS)
c_mental = Coherence(0.7, domain=Domain.PSYCHOLOGY)
c_social = Coherence(0.5, domain=Domain.SOCIOLOGY)
c_spiritual = Coherence(0.6, domain=Domain.THEOLOGY)

# Composite (geometric mean)
c_total = Coherence.composite([c_physical, c_mental, c_social, c_spiritual])
print(c_total)  # C(0.6593, σ=+1, general)

# Note: Lower than any individual component!
# This is multiplicative vulnerability.
```

---

## 🔬 Mathematical Foundations

### Coherence Dynamics

**Closed System (Theorem C3.2):**
```
dC/dt = -Γ_D · C  (always ≤ 0)
```

**Open System:**
```
dC/dt = Γ_G · Ĝ - Γ_D · D̂
```

Where:
- Γ_G: Grace rate
- Γ_D: Decoherence rate
- Ĝ: Grace operator (external)
- D̂: Decoherence operator

### Sign Eigenvalue (Theorem C20.2)

```
[σ̂, Û_self] = 0
```

Self-operations commute with sign → **cannot flip sign**.

Only external grace can flip: Ĝ|Ψ_{σ=-1}⟩ → |Ψ_{σ=+1}⟩

### Triad Total

```
C_total = (Λ · Π · A)^(1/3)
```

Geometric mean → multiplicative vulnerability.

If any component → 0, total → 0.

### Grace Function

```
G(Rp, S) = G₀ · e^(Rp/S) · R_J
```

Exponential dependence on repentance/sin ratio.

Post-resurrection: R_J = 1.5 (50% increase).

---

## 📁 File Structure

```
theophysics_manager/
├── engine/
│   └── theophysics_definitions.py    # Main module (1000+ lines)
├── examples/
│   └── theophysics_definitions_example.py  # 10 examples
└── THEOPHYSICS_DEFINITIONS_README.md  # This file
```

---

## 🧪 Run All Examples

```bash
python examples/theophysics_definitions_example.py
```

**Includes:**
1. Basic coherence operations
2. Closed system decay
3. Grace application
4. Spiritual warfare simulation
5. Triad collapse cascade
6. Triad restoration
7. Grace function dynamics
8. Definition engine usage
9. Composite coherence
10. Critical threshold analysis

---

## 🔧 Integration with Definition 2.0

This module **complements** the Definition 2.0 system:

### Definition 2.0 (External Processing)
- Indexes vault
- Fetches external sources
- Tracks provenance
- Detects drift
- Generates reports

### Theophysics Definitions (Computational)
- Computes coherence values
- Simulates dynamics
- Validates usage
- Tracks drift programmatically
- Provides canonical implementations

**Together:** External data + computational verification = complete system.

---

## 📊 Constants

```python
C_MIN = 0.0                  # Minimum coherence
C_MAX = 1.0                  # Maximum coherence
C_CRIT = 0.35                # Critical threshold
R_J_POST_RESURRECTION = 1.5  # Resurrection factor
```

---

## 🎯 Use Cases

### 1. Research
- Compute coherence from experimental data
- Validate theoretical predictions
- Simulate collapse/restoration scenarios

### 2. Paper Writing
- Generate figures (coherence trajectories)
- Verify mathematical consistency
- Compute cross-domain values

### 3. Definition Validation
- Check if usage matches canonical definition
- Track drift over time
- Ensure cross-domain consistency

### 4. Education
- Interactive demonstrations
- Visualize dynamics
- Explore parameter space

---

## 🐛 Troubleshooting

### Import Error

```bash
ModuleNotFoundError: No module named 'yaml'
```

**Fix:**
```bash
pip install pyyaml
```

### Validation Fails

If `validate_usage()` returns `valid=False`:
- Check term spelling
- Ensure definition is loaded
- Use `get_definition()` to verify

### Coherence Out of Bounds

If you see warnings like:
```
Warning: Coherence 1.2 > 1, clamping to 1
```

This is expected - coherence is automatically clamped to [0, 1].

---

## 📚 Further Reading

- **Theophysics Papers:** See `Papers/` directory
- **Definition 2.0 Guide:** `docs/DEFINITION_V2_GUIDE.md`
- **Master Equation:** `Papers/Master-Equation.md`
- **Coherence Definition:** `Definitions/def-coherence.md`

---

## 🤝 Contributing

To add new definitions:

1. Create definition in `Definitions/` folder
2. Use `DefinitionParser.parse_file()` to load
3. Register with `DefinitionEngine`
4. Add computational methods if needed

Example:
```python
# Load custom definition
engine = DefinitionEngine()
grace_def = engine.load_definition("Definitions/def-grace.md")

# Now available by ID or alias
defn = engine.get_definition("grace")
```

---

## 📄 License

MIT License - See main LICENSE file

---

## 🙏 Credits

**Author:** David Lowe  
**Project:** Theophysics Research Initiative  
**Version:** 1.0  
**Date:** 2025-12-12

---

**Built for rigorous, computational Theophysics research. 🧮**
