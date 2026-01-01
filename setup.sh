#!/bin/bash

TOOL_NAME="dorktool"
SOURCE_FILE="dorktool.py"
INSTALL_PATH="/usr/local/bin"

echo "[+] Installing $TOOL_NAME ..."

if [ ! -f "$SOURCE_FILE" ]; then
    echo "[-] $SOURCE_FILE not found"
    exit 1
fi

chmod +x "$SOURCE_FILE"
sudo cp "$SOURCE_FILE" "$INSTALL_PATH/$TOOL_NAME"

if [ -f "$INSTALL_PATH/$TOOL_NAME" ]; then
    echo "[✓] Installed successfully"
    echo "[✓] Run with: $TOOL_NAME"
else
    echo "[-] Installation failed"
fi
