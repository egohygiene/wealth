import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tsconfigPaths from 'vite-tsconfig-paths'
import checker from 'vite-plugin-checker'
import svgr from 'vite-plugin-svgr'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    tsconfigPaths(),
    checker({ typescript: true, eslint: { files: ['./src'] } }),
    svgr(),
    VitePWA(),
  ],
  server: {
    port: Number(process.env.UI_PORT) || 5173,
    proxy: {
      '/api': {
        target: `http://localhost:${process.env.API_PORT || 8000}`,
        changeOrigin: true,
      },
    },
  },
})
