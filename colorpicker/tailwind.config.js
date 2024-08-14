/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  theme: {
    extend: {
      typography: (theme) => ({
        DEFAULT: {
          css: {
            maxWidth: "none"
          }
        }
      })
    }
  },
  daisyui: {
    themes: [
      {
        kevin: {
          ...require("daisyui/src/theming/themes")["autumn"],
          "primary": "#ac4142",
          "background-color": "white"
        }
      }
    ],
    styled: true,
    base: true
  }
}
