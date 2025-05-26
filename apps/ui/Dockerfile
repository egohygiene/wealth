FROM node:20-slim

WORKDIR /app

# Install pnpm package manager
RUN npm install -g pnpm

# Install dependencies
COPY package.json ./
RUN pnpm install

# Copy source
COPY . .

EXPOSE 5173
CMD ["pnpm", "dev", "--host"]
