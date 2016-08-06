#!/bin/bash

SRC="iswn"
rm -rf $SRC
BACKUP_DIR="old.iswn"
mv $BACKUP_DIR $SRC
cd $SRC
docker-compose -f docker-compose.yml -f docker-compose.prod.yml rm -f
docker-compose -f docker-compose.yml -f docker-compose.prod.yml pull
docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

