#!/bin/sh
docker rm -f postgres
docker run --name postgres  -e POSTGRES_PASSWORD=postgres -d pwf-postgres:0.0.1
docker rm -f pwf-agenda-backend
docker run --name=pwf-agenda-backend  --link postgres:postgres -p 9191:80 -d pwf-agenda-backend:0.0.1

docker ps