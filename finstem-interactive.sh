#!/bin/bash

if ! [ -x "$(command -v fzf)" ]; then
	echo 'Error: fzf is not installed.' >&2
	exit 1
fi

echo '' | fzf --print-query \
	--preview-window='bottom:50%' \
	--preview 'python finstem.py {q}'