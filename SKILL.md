---
name: specimen
description: Typography system compiler that generates structured type scales, font stacks, and typographic tokens. Use when users request type systems, font scales, typography tokens, design system typography, or ask to create/export typographic styles. Pairs with hexed for complete design systems.
license: MIT
---

# Specimen

**Specimen** is a typography system compiler that generates structured, production-ready type scales and typographic design tokens.

## Overview

Typeset generates complete typography systems including:
- Modular type scales (multiple ratio options)
- Font family stacks (primary, secondary, monospace)
- Font weight scales
- Proportional line heights
- Letter spacing (tracking)
- Semantic mappings (h1, h2, body, etc.)

Output is deterministic, structured, and ready for CSS, Tailwind, SCSS, or Figma.

---

## What Specimen Produces

A complete typography system including:

1. **Type scale**: Modular scale from base size (e.g., 16px) using mathematical ratios
2. **Font families**: Primary, secondary (optional), and monospace stacks
3. **Font weights**: Standard 100-900 weight scale with semantic names
4. **Line heights**: Proportional to each type scale step
5. **Letter spacing**: Optimized tracking for each size
6. **Semantic mappings**: h1-h4, body, caption, etc. → scale steps

---

## Usage Instructions

### Step 1: Define System Parameters

Determine the configuration:

```python
config = {
    'base_size': 16,  # Base font size in pixels
    'ratio': 'minor_third',  # Scale ratio (see available ratios below)
    'font_family_primary': 'Inter, system-ui, sans-serif',
    'font_family_secondary': 'Playfair Display, serif',  # Optional
    'font_family_mono': 'JetBrains Mono, monospace',
    'mode': 'balanced'  # 'tight', 'balanced', or 'loose'
}
```

**Available ratios:**
- `minor_second` (1.067) - Very subtle
- `major_second` (1.125) - Subtle
- `minor_third` (1.200) - Balanced (recommended)
- `major_third` (1.250) - Moderate
- `perfect_fourth` (1.333) - Clear distinction
- `augmented_fourth` (1.414) - Strong
- `perfect_fifth` (1.500) - Very strong
- `golden_ratio` (1.618) - Maximum contrast

**Modes:**
- `tight`: 4 steps up, 1 step down (compact scale)
- `balanced`: 5 steps up, 2 steps down (default)
- `loose`: 6 steps up, 2 steps down (extended scale)

### Step 2: Compile the System

```python
import sys
sys.path.append('/home/claude/specimen/scripts')

from specimen_compiler import compile_from_config

result = compile_from_config(config)

if result['ok']:
    typography_system = result['typography_system']
    # System is ready for export
else:
    print(f"Error: {result['message']}")
```

### Step 3: Export to Desired Formats

```python
from specimen_exports import (
    export_css_variables,
    export_tailwind_config,
    export_scss_variables,
    export_figma_tokens,
    export_json
)

# CSS Variables
css = export_css_variables(typography_system)

# Tailwind Config
tailwind = export_tailwind_config(typography_system)

# SCSS Variables
scss = export_scss_variables(typography_system)

# Figma Tokens (Tokens Studio format)
figma_result = export_figma_tokens(typography_system)
figma_tokens = figma_result['tokens']

# Raw JSON
json_output = export_json(typography_system)
```

### Step 4: Save and Present Outputs

Save exports to `/mnt/user-data/outputs/`:

```python
import json

# Save JSON system
with open('/mnt/user-data/outputs/typography-system.json', 'w') as f:
    json.dump(typography_system, f, indent=2)

# Save CSS variables
with open('/mnt/user-data/outputs/typography.css', 'w') as f:
    f.write(css)

# Save Tailwind config
with open('/mnt/user-data/outputs/tailwind-typography.config.js', 'w') as f:
    f.write(tailwind)

# Save SCSS variables
with open('/mnt/user-data/outputs/typography.scss', 'w') as f:
    f.write(scss)

# Save Figma tokens
with open('/mnt/user-data/outputs/figma-typography-tokens.json', 'w') as f:
    json.dump(figma_tokens, f, indent=2)
```

Then use `present_files` to share them with the user.

---

## Integration with Hexed

Specimen pairs perfectly with the Hexed color system compiler:

**Combined workflow:**
1. Use Hexed to extract color system from images
2. Use Typeset to generate typography system
3. Combine both into complete design system tokens

**Example:**
```python
# Step 1: Generate colors with Hexed
color_result = compile_from_images(image_paths)
color_system = color_result['color_system']

# Step 2: Generate typography with Specimen
type_result = compile_from_config(typography_config)
type_system = type_result['typography_system']

# Step 3: Create unified design system
design_system = {
    'version': '1.0',
    'colors': color_system,
    'typography': type_system,
    'generated_at': datetime.utcnow().isoformat()
}
```

---

## Best Practices

1. **Start with standard ratios** - Use `minor_third` (1.2) or `major_third` (1.25) for most projects
2. **Match to use case**:
   - Marketing/editorial: `golden_ratio` or `perfect_fifth`
   - UI/product: `minor_third` or `major_third`
   - Compact interfaces: `major_second`
3. **Choose appropriate mode**:
   - Tight: Mobile apps, compact UIs
   - Balanced: Most websites and apps
   - Loose: Marketing sites, content-heavy sites
4. **Font stacks matter** - Include fallbacks for web fonts
5. **Ask which formats they need** - Don't generate all unless requested

---

## Recommended Type Scale Ratios by Use Case

**Web Applications:** minor_third (1.2)
- Balanced hierarchy
- Not too dramatic
- Works well for dashboards and tools

**Marketing Sites:** perfect_fourth (1.333) or golden_ratio (1.618)
- Strong visual hierarchy
- Eye-catching headings
- Editorial feel

**Mobile Apps:** major_second (1.125) or minor_third (1.2)
- Compact but clear
- Efficient use of screen space
- Good readability

**Content/Editorial:** major_third (1.25) or perfect_fourth (1.333)
- Clear hierarchy for long-form content
- Comfortable reading experience
- Traditional typographic feel

---

## Common Configurations

### Modern SaaS App
```python
{
    'base_size': 16,
    'ratio': 'minor_third',
    'font_family_primary': 'Inter, system-ui, sans-serif',
    'font_family_mono': 'JetBrains Mono, monospace',
    'mode': 'balanced'
}
```

### Marketing Site
```python
{
    'base_size': 18,
    'ratio': 'perfect_fourth',
    'font_family_primary': 'Inter, system-ui, sans-serif',
    'font_family_secondary': 'Playfair Display, serif',
    'mode': 'loose'
}
```

### Mobile App
```python
{
    'base_size': 16,
    'ratio': 'major_second',
    'font_family_primary': 'system-ui, -apple-system, sans-serif',
    'mode': 'tight'
}
```

---

## Author

Created by Heathen ([@heathenft](https://x.com/heathenft))

## License

MIT License - See LICENSE file for details
