#!/bin/bash
echo "Brisanje cijelog projekta..."
docker compose down -v --rmi all
echo "Sve je obrisano (kontejneri, mreže, volumeni i imageovi)."