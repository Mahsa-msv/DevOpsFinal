# Use the official Node.js image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package files to the working directory
COPY package.json package-lock.json /app/

# Install dependencies
RUN npm install

# Copy all source files
COPY . /app

# Build the project for production
RUN npm run build

# Serve the app
EXPOSE 3000
CMD ["npx", "serve", "-s", "build"]