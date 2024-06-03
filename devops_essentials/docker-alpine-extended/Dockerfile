# Use the official Alpine image from the Docker Hub
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Copy the configuration file to the container
COPY config.txt /app/config.txt

# Default command
CMD ["echo", "Hello, World!"]
