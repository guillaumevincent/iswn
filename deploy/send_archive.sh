#!/bin/bash

if (( $# != 1 ))
then
  echo "Usage: source send_archive.sh iswn-vX.X.X.zip"
  return 1
fi

FILENAME="$1"
echo "send archive on the server"
scp $FILENAME admin@iswn:/home/admin
scp deploy.sh admin@iswn:/home/admin
rm $FILENAME
