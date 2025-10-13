# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a dual-component project:
1. **scicolor** - A Python package providing curated color maps for scientific visualizations with emphasis on perceptual uniformity and color-blind friendliness
2. **Scicolor Color Picker** - A Vue.js 3 web application for browsing and selecting colors from the scicolor collection

## Repository Structure

```
scicolor/                       # Python package
  __init__.py                   # Main package with get_cmap(), list_cmaps(), plot_cmaps()
  scientific_colors/            # Scientific colour maps (perceptually uniform)
  cet_colors/                   # CET color maps
  ocean_colors/                 # CMOcean color maps
colorpicker/                    # Vue.js web application
  src/
    components/                 # Vue components
    router/                     # Vue Router configuration
exps/                          # Jupyter notebooks for experimentation
```

## Python Package Development

This project uses **uv** for dependency management and packaging.

### Installation and Testing
```bash
# Install dependencies and sync virtual environment
uv sync

# Test the package
uv run python -c "import scicolor; print(scicolor.list_cmaps())"

# Or activate the virtual environment
source .venv/bin/activate  # On Unix/macOS
python -c "import scicolor; print(scicolor.list_cmaps())"

# Run Jupyter notebooks with uv
uv run jupyter notebook exps/
```

### Adding Dependencies
```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name
```

### Key Architecture - scicolor Package

The package uses a registry-based system defined in `scicolor/__init__.py`:

- **color_info_list**: Central registry of all color maps with metadata (class, type, perceptually_uniform, color_blind_friendly)
- **color_info_df**: Pandas DataFrame built from color_info_list for filtering operations
- Color maps are loaded lazily via source-specific functions:
  - `_get_matplotlib_cmap()` - Matplotlib native maps
  - `_get_scientific_colors()` - Scientific colour maps (txt files)
  - `_get_wesanderson_cmap()` - Wes Anderson palettes (hardcoded hex values)
  - `_get_cet_cmap()` - CET maps (CSV format)
  - `_get_ocean_cmap()` - Ocean maps (txt files)
  - `_get_metbrewer_cmap()` - MetBrewer palettes (hardcoded hex values)

### Adding New Color Maps

To add a new color map to scicolor:
1. Place color data files in the appropriate directory (e.g., `scicolor/scientific_colors/`)
2. Add entry to `color_info_list` in `scicolor/__init__.py` with format:
   ```python
   ["name", "source", "cm_class", "cm_type", perceptually_uniform, color_blind_friendly]
   ```
3. Ensure the source-specific loader function handles the file format correctly
4. For hardcoded palettes (wesanderson, metbrewer), add hex values to the mapping dictionary

### Color Map Classification

- **cm_class**: categorical, sequential, diverging, multi_sequential, misc
- **cm_type**: categorical, discrete, continuous
- **perceptually_uniform**: True/False/None - indicates if color transitions are perceptually linear
- **color_blind_friendly**: True/False/None - indicates accessibility for color vision deficiency

## Web Application Development

### Commands
```bash
cd colorpicker

# Install dependencies
npm install

# Start dev server (http://localhost:5173)
npm run dev

# Build for production (outputs to dist/)
npm run build

# Preview production build
npm run preview
```

### Key Architecture - Web Application

- **Vue 3 Composition API** with `<script setup>` syntax throughout
- **Data Source**: `colorpicker/public/colors/colors.json` - must be kept in sync with Python package's color_info_list
- **State Management**: Custom reactive stores using Vue 3's Composition API (no Vuex/Pinia)
  - `ColorSwatchStore.js` manages user's personal color collection with localStorage persistence
- **Routing**: Vue Router 4 with routes defined in `src/router/`
- **Styling**: Tailwind CSS + daisyUI theme "corporate"
- **Icons**: Font Awesome via `@fortawesome/vue-fontawesome`

### Core Components
- `HomePage.vue` - Main layout with drawer navigation
- `ColorPicker.vue` - Filter controls and color scheme grid
- `ColorScheme.vue` - Individual palette display with copy functionality
- `ColorSwatch.vue` - Personal color collection management

### Deployment Configuration
- Base path: `/scicolor/` (configured in vite.config.js)
- Builds to `colorpicker/dist/`
- Includes Google Analytics and social meta tags

## Package Distribution

### Python Package (PyPI)
```bash
# Build distribution packages (wheel and sdist)
uv build

# Upload to PyPI (requires credentials)
uv publish

# Or manually with twine
twine upload dist/*
```

### Web Application (GitHub Pages)
The web app is deployed to GitHub Pages at https://yang3kc.github.io/scicolor/

## Data Synchronization

**CRITICAL**: When adding/modifying color maps:
1. Update `scicolor/__init__.py` color_info_list
2. Regenerate `colorpicker/public/colors/colors.json` to match
3. The JSON must contain the same metadata structure for the web app to display correctly

## Dependencies

### Python Package
- matplotlib (for colormap objects)
- numpy (for color data processing)
- pandas (for filtering/querying color maps)

### Web Application
- Vue 3.4+
- Vue Router 4
- Vite 5 (build tool)
- Tailwind CSS 3 + daisyUI
- Font Awesome

## Testing

No formal test suite is currently configured. Testing is done via:
- Python: Jupyter notebooks in `exps/` directory
- Web app: Manual testing in development mode
