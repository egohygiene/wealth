module.exports = {
  extends: ['eslint:recommended', 'plugin:react/recommended'],
  plugins: ['react'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
}
