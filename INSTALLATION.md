# Installing Specimen

Specimen is available as a Claude Skill for use in conversations with Claude.

## For Users

### Install from Claude Skills Marketplace

1. Go to [claude.ai](https://claude.ai)
2. Navigate to **Settings** → **Skills**
3. Search for **"Specimen"**
4. Click **"Add Skill"**
5. Start a new conversation

### Usage

Once installed, simply:
1. Ask Claude to create a typography system: *"Generate a type system with a 1.2 ratio"*
2. Customize if needed: *"Use Inter as the primary font"*
3. Request your preferred export format: *"Give me CSS variables"*

## For Developers

### Running Locally

If you want to use Specimen outside of Claude:

```bash
# Clone the repository
git clone https://github.com/yourusername/specimen-skill.git
cd specimen-skill

# No additional dependencies needed (uses Python stdlib)

# Test the compiler
python -c "from scripts.specimen_compiler import compile_from_config; print(compile_from_config({'base_size': 16, 'ratio': 'minor_third'}))"
```

### Integration

```python
from specimen_compiler import compile_from_config
from specimen_exports import export_css_variables

# Configure typography system
config = {
    'base_size': 16,
    'ratio': 'minor_third',
    'font_family_primary': 'Inter, system-ui, sans-serif',
    'mode': 'balanced'
}

# Compile system
result = compile_from_config(config)

if result['ok']:
    typography_system = result['typography_system']
    
    # Export to CSS
    css = export_css_variables(typography_system)
    print(css)
```

## Requirements

- Python 3.8+

All dependencies are included in Claude's environment and Python's standard library.

## Support

- **Issues**: [GitHub Issues] TBA
- **Documentation**: See [README.md](README.md)
- **Author**: [@heathenft](https://x.com/heathenft)
