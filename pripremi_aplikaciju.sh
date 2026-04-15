#!/bin/bash
echo "Priprema mreža i volumena..."
docker volume create beauty_data
docker network create beauty_network || true

echo "Buildanje imageova..."
docker compose build
echo "Priprema završena uspješno."