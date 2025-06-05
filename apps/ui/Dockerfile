FROM node:20-slim

WORKDIR /app

# Install pnpm package manager
RUN npm install -g pnpm@10.11.1

# Install dependencies
COPY package.json ./
RUN pnpm install

# Copy source
COPY . .

EXPOSE 5173
CMD ["sh", "-c", "pnpm dev --host --port ${UI_PORT:-5173}"]
