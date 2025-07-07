# SciColor - Scientific Color Picker

A Vue.js 3 web application for browsing and selecting color palettes specifically curated for scientific visualizations and data analysis.

## Features

- **Curated Color Palettes**: Browse color schemes from Tableau, scientific publications, and other trusted sources
- **Interactive Color Selection**: Click colors to copy hex codes, with visual feedback
- **Personal Swatch Collection**: Save and manage your favorite colors across sessions
- **Smart Filtering**: Filter by minimum color count and color-blind friendly palettes
- **Palette Operations**: Shuffle, restore, and copy entire color schemes
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Technology Stack

- **Vue.js 3** with Composition API
- **Vue Router 4** for navigation
- **Vite** for development and build tooling
- **Tailwind CSS** + **daisyUI** for styling
- **Font Awesome** for icons

## Development

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd colorpicker

# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at `http://localhost:5173`

### Build for Production

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## Usage

1. **Browse Palettes**: Scroll through the available color schemes
2. **Filter Options**: Use the controls to filter by color count or color-blind friendly options
3. **Copy Colors**: Click individual colors to copy their hex codes
4. **Manage Swatches**: Add colors to your personal collection for comparison
5. **Export Palettes**: Copy entire color schemes for use in your projects

## Project Structure

```
src/
├── components/
│   ├── HomePage.vue          # Main layout component
│   ├── ColorPicker.vue       # Core color picker functionality
│   ├── ColorScheme.vue       # Individual palette display
│   ├── ColorSwatch.vue       # Personal swatch management
│   ├── ColorSwatchStore.js   # State management
│   ├── Toast.vue            # Notification system
│   └── utils.js             # Utility functions
├── router/
│   └── index.js             # Vue Router configuration
├── main.js                  # Application entry point
├── main.css                 # Global styles
└── App.vue                  # Root component
```

## Color Data

Color palettes are stored in `/public/colors/colors.json` and include:
- Collection metadata (name, source, description)
- Individual color schemes with hex codes
- Labels for categorization (categorical, sequential, etc.)
- Color-blind friendly indicators

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).