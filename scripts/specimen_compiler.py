#!/usr/bin/env python3
"""
Specimen Compiler - Typography System Generator
Extracts and generates structured typography systems from font files or design references.
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Type scale ratios
SCALE_RATIOS = {
    'minor_second': 1.067,
    'major_second': 1.125,
    'minor_third': 1.200,
    'major_third': 1.250,
    'perfect_fourth': 1.333,
    'augmented_fourth': 1.414,
    'perfect_fifth': 1.500,
    'golden_ratio': 1.618,
}

def generate_type_scale(
    base_size: float = 16.0,
    ratio: str = 'minor_third',
    steps_up: int = 5,
    steps_down: int = 2
) -> Dict[str, Dict[str, Any]]:
    """
    Generate a modular type scale.
    
    Args:
        base_size: Base font size in pixels (typically 16px)
        ratio: Scale ratio name from SCALE_RATIOS
        steps_up: Number of steps larger than base
        steps_down: Number of steps smaller than base
    
    Returns:
        Dictionary of type scale steps with sizes and metadata
    """
    if ratio not in SCALE_RATIOS:
        ratio = 'minor_third'
    
    scale_ratio = SCALE_RATIOS[ratio]
    scale = {}
    
    # Generate smaller sizes (going down)
    for i in range(steps_down, 0, -1):
        size = base_size / (scale_ratio ** i)
        scale[f'xs{i}' if i > 1 else 'xs'] = {
            'px': round(size, 2),
            'rem': round(size / 16, 3),
            'step': -i
        }
    
    # Base size
    scale['base'] = {
        'px': base_size,
        'rem': base_size / 16,
        'step': 0
    }
    
    # Generate larger sizes (going up)
    size_labels = ['sm', 'md', 'lg', 'xl', '2xl', '3xl', '4xl', '5xl', '6xl']
    for i in range(1, steps_up + 1):
        size = base_size * (scale_ratio ** i)
        label = size_labels[i - 1] if i <= len(size_labels) else f'{i}xl'
        scale[label] = {
            'px': round(size, 2),
            'rem': round(size / 16, 3),
            'step': i
        }
    
    return scale


def generate_font_weights() -> Dict[str, int]:
    """Generate standard font weight scale."""
    return {
        'thin': 100,
        'extra_light': 200,
        'light': 300,
        'regular': 400,
        'medium': 500,
        'semi_bold': 600,
        'bold': 700,
        'extra_bold': 800,
        'black': 900
    }


def generate_line_heights(scale: Dict[str, Dict[str, Any]]) -> Dict[str, float]:
    """
    Generate proportional line heights for each type scale step.
    Smaller text gets taller line-height, larger text gets shorter.
    """
    line_heights = {}
    
    for key, value in scale.items():
        size_px = value['px']
        
        # Proportional line height calculation
        # Smaller sizes: 1.6-1.7
        # Medium sizes: 1.4-1.5
        # Large sizes: 1.1-1.3
        if size_px <= 14:
            lh = 1.65
        elif size_px <= 18:
            lh = 1.5
        elif size_px <= 24:
            lh = 1.4
        elif size_px <= 36:
            lh = 1.3
        else:
            lh = 1.2
        
        line_heights[key] = round(lh, 2)
    
    return line_heights


def generate_letter_spacing(scale: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    """
    Generate letter spacing (tracking) for each type scale step.
    Larger text benefits from tighter tracking.
    """
    letter_spacing = {}
    
    for key, value in scale.items():
        size_px = value['px']
        
        # Letter spacing in em units
        if size_px <= 12:
            ls = '0.02em'  # Slightly loose for small text
        elif size_px <= 18:
            ls = '0em'     # Normal
        elif size_px <= 36:
            ls = '-0.01em' # Slightly tight
        else:
            ls = '-0.02em' # Tighter for display sizes
        
        letter_spacing[key] = ls
    
    return letter_spacing


def create_semantic_mappings(scale: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    """
    Map semantic use cases to type scale steps.
    """
    return {
        'display': 'xl',      # Hero text
        'h1': 'lg',           # Main heading
        'h2': 'md',           # Section heading
        'h3': 'sm',           # Subsection heading
        'h4': 'base',         # Small heading
        'body': 'base',       # Body text
        'small': 'xs',        # Small text
        'caption': 'xs',      # Captions, labels
        'overline': 'xs'      # All caps labels
    }


def compile_typography_system(
    base_size: float = 16.0,
    ratio: str = 'minor_third',
    font_family_primary: str = 'system-ui, -apple-system, sans-serif',
    font_family_secondary: Optional[str] = None,
    font_family_mono: str = 'ui-monospace, monospace',
    mode: str = 'balanced'
) -> Dict[str, Any]:
    """
    Compile a complete typography system.
    
    Args:
        base_size: Base font size in pixels
        ratio: Type scale ratio
        font_family_primary: Primary font stack
        font_family_secondary: Optional secondary/display font stack
        font_family_mono: Monospace font stack
        mode: 'tight', 'balanced', or 'loose' spacing
    
    Returns:
        Complete typography system dictionary
    """
    
    # Adjust steps based on mode
    if mode == 'tight':
        steps_up, steps_down = 4, 1
    elif mode == 'loose':
        steps_up, steps_down = 6, 2
    else:  # balanced
        steps_up, steps_down = 5, 2
    
    # Generate core scale
    scale = generate_type_scale(base_size, ratio, steps_up, steps_down)
    
    # Generate supporting properties
    weights = generate_font_weights()
    line_heights = generate_line_heights(scale)
    letter_spacing = generate_letter_spacing(scale)
    semantic = create_semantic_mappings(scale)
    
    # Font families
    font_families = {
        'primary': font_family_primary,
        'mono': font_family_mono
    }
    
    if font_family_secondary:
        font_families['secondary'] = font_family_secondary
    
    # Compile system
    system = {
        'version': '1.0',
        'meta': {
            'id': 'ts_generated',
            'mode': mode,
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'engine': {
                'name': 'specimen',
                'engine_version': '0.1.0'
            }
        },
        'config': {
            'base_size': base_size,
            'ratio': ratio,
            'ratio_value': SCALE_RATIOS.get(ratio, 1.200)
        },
        'fonts': {
            'families': font_families,
            'weights': weights
        },
        'scale': scale,
        'line_heights': line_heights,
        'letter_spacing': letter_spacing,
        'semantic': semantic
    }
    
    return system


def compile_from_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compile typography system from a configuration dictionary.
    
    Expected config keys:
        - base_size (optional, default: 16.0)
        - ratio (optional, default: 'minor_third')
        - font_family_primary (optional)
        - font_family_secondary (optional)
        - font_family_mono (optional)
        - mode (optional, default: 'balanced')
    
    Returns:
        Result dictionary with 'ok', 'typography_system', and 'message' keys
    """
    try:
        base_size = config.get('base_size', 16.0)
        ratio = config.get('ratio', 'minor_third')
        font_primary = config.get('font_family_primary', 'system-ui, -apple-system, sans-serif')
        font_secondary = config.get('font_family_secondary')
        font_mono = config.get('font_family_mono', 'ui-monospace, monospace')
        mode = config.get('mode', 'balanced')
        
        system = compile_typography_system(
            base_size=base_size,
            ratio=ratio,
            font_family_primary=font_primary,
            font_family_secondary=font_secondary,
            font_family_mono=font_mono,
            mode=mode
        )
        
        return {
            'ok': True,
            'typography_system': system,
            'message': 'Typography system compiled successfully'
        }
        
    except Exception as e:
        return {
            'ok': False,
            'typography_system': None,
            'message': f'Compilation failed: {str(e)}'
        }


if __name__ == '__main__':
    # Test compilation
    result = compile_from_config({
        'base_size': 16,
        'ratio': 'minor_third',
        'mode': 'balanced'
    })
    
    if result['ok']:
        print(json.dumps(result['typography_system'], indent=2))
    else:
        print(f"Error: {result['message']}")
