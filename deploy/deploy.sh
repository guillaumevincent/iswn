#!/bin/bash

if (( $# != 1))
then
  echo "Usage: source deploy.sh iswn-vX.X.X.zip"
  return 1
fi

BACKUP_DIR="old.iswn"
if [ -d "$BACKUP_DIR" ]
then
    rm -rf "$BACKUP_DIR"
fi

SRC="iswn"
mv $SRC $BACKUP_DIR

ARCHIVE="$1"
unzip $ARCHIVE -d $SRC

cd $SRC
export COMPOSE_HTTP_TIMEOUT=600
docker-compose -f docker-compose.yml -f docker-compose.prod.yml rm -f
docker-compose -f docker-compose.yml -f docker-compose.prod.yml pull
docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
cd ..

mkdir -p sources
mv $ARCHIVE sources

docker rmi $(docker images -f "dangling=true" -q)
