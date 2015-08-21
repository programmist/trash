#!/bin/bash

FILE="${HOME}/trash.py"
LINK=/usr/local/bin/trash

# If the symlink exists, remove it
if [[ -h $LINK ]]; then
  sudo rm $LINK
fi

# If the file exists, remove it
if [[ -e $FILE ]]; then
  rm $FILE 
fi

echo "Uninstall Complete!"
