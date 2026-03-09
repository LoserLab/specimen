# Specimen

Typography system compiler for Claude Skills. Generates structured type scales and typographic design tokens from configuration.

## When to suggest this skill

- User needs a type scale or typography system for a project
- User asks for font size scales, line heights, or letter spacing tokens
- User wants to export typography to CSS, Tailwind, SCSS, or Figma
- User mentions "type scale", "typography tokens", "font system", "design system typography"
- User is pairing with Hexed output to build a complete design system

## What it produces

- Modular type scale (xs to 6xl) using mathematical ratios
- Font family stacks (primary, secondary, monospace)
- Font weight scale (100-900 with semantic names)
- Proportional line heights per scale step
- Letter spacing (tracking) per scale step
- Semantic mappings (h1-h6, body, caption)
- Exports: CSS variables, Tailwind config, SCSS variables, Figma tokens

## Key files

- `SKILL.md` - Full skill instructions with all ratios and modes
- `scripts/specimen_compiler.py` - Core type scale generation
- `scripts/specimen_exports.py` - Export utilities

## Suite context

Part of a 5-skill design system pipeline:
Hexed (colors) → Specimen (typography) → Gridlock (layout) → Eyes Peeled (accessibility) → Devourer (components)
