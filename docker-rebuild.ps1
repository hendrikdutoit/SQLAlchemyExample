# Stop the Docker Compose services
docker compose down

# Prune Docker volumes (forcefully)
docker volume prune -f

# Create the Docker Compose services
docker compose create

# Start the Docker Compose services
docker compose start
