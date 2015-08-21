#!/bin/bash

SRC_FILE=./trash.py
DEST_FILE="${HOME}/trash.py"
LINK=/usr/local/bin/trash

if [[ -e $DEST_FILE && -h $LINK ]]; then
  echo "The trash command is already installed"
  exit 0
fi

if [[ ! -e $FILE ]]; then
  chmod +x $SRC_FILE
  cp $SRC_FILE $HOME
  echo "$SRC_FILE copied to $DEST_FILE"
fi

if [[ ! -h $LINK ]]; then
  sudo ln -s $DEST_FILE $LINK 
  echo "$LINK created"
fi

echo "Installation complete!"
