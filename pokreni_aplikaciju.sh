#!/bin/bash
echo "Pokretanje aplikacije..."
docker compose up -d
echo "-------------------------------------------------"
echo "Aplikacija je dostupna na: http://localhost:8080"
echo "-------------------------------------------------"