# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Vue.js 3 web application called "Scicolor Color Picker" - a tool for browsing and selecting color palettes specifically curated for scientific visualizations. The app allows users to view color schemes, copy individual colors or entire palettes, and manage a personal swatch collection.

## Development Commands

```bash
# Install dependencies
npm install

# Start development server (runs on http://localhost:5173)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Tech Stack & Architecture

- **Vue.js 3** with Composition API (`<script setup>`)
- **Vue Router 4** for routing
- **Vite** for build tooling and development server
- **Tailwind CSS** + **daisyUI** for styling
- **Font Awesome** for icons

## Key Architecture Points

### Component Structure
- `App.vue`: Root component with router-view
- `HomePage.vue`: Main layout with drawer navigation
- `ColorPicker.vue`: Core component managing color scheme display and filtering
- `ColorScheme.vue`: Individual color palette display with interaction handlers
- `ColorSwatch.vue`: User's personal color collection management
- `ColorSwatchStore.js`: Reactive store for swatch state management

### Data Flow
- Color palettes are loaded from `/public/colors/colors.json`
- State management uses Vue 3's Composition API with reactive stores
- No external state management library (Vuex/Pinia) - uses composables pattern

### Key Features
- Dynamic filtering (min colors, color-blind friendly)
- Color copying with toast notifications
- Personal swatch collection with localStorage persistence
- Responsive design with mobile drawer navigation

## File Structure Notes

- Color palette data: `/public/colors/colors.json`
- Components: `/src/components/`
- Utilities: `/src/components/utils.js`
- Main entry: `/src/main.js`
- Configuration: `vite.config.js`, `tailwind.config.js`

## Deployment Configuration

- Base path configured for `/scicolor/` deployment
- Includes Google Analytics integration
- Social media meta tags configured
- Builds to `/dist` directory

## Development Notes

- No testing framework currently configured
- Uses Font Awesome icons via Vue component integration
- Tailwind configured with daisyUI theme "corporate"
- PostCSS with Autoprefixer for CSS processing