#!/bin/bash

# Check if fzf is installed
if ! command -v fzf &>/dev/null; then
  echo 'Error: fzf is not installed.' >&2
  exit 1
fi

# Check if python is installed
if ! command -v python &>/dev/null; then
  # If python is not found, check for python3
  if command -v python3 &>/dev/null; then
    echo "Error: 'python' command is not found, but 'python3' is available." >&2
    echo "Please consider linking 'python' to 'python3'. For example:" >&2
    echo "  sudo ln -s \"$(command -v python3)\" /usr/local/bin/python" >&2
    exit 1
  else
    echo "Error: Python is not installed." >&2
    exit 1
  fi
fi

# Check if the Python library 'libvoikko' (imported as 'voikko') is installed
if ! python -c "import libvoikko" &>/dev/null; then
  echo "Error: Python library 'libvoikko' (module 'voikko') is not installed." >&2
  echo "On Debian, you might install it using:" >&2
  echo "  sudo apt-get install python3-libvoikko" >&2
  echo "Then, if necessary, link 'python' to 'python3' with:" >&2
  echo "  sudo ln -s \"$(command -v python3)\" /usr/local/bin/python" >&2
  exit 1
fi

# Proceed with fzf using python
echo '' | fzf --print-query \
  --preview-window='bottom:50%' \
  --preview "echo {q} | tr ' ' '\n' | xargs -I _ python finstem.py _" \
  --bind "enter:execute(echo {q} | tr ' ' '\n' | xargs -I _ python finstem.py _)+abort"
