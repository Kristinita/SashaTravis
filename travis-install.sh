#!/bin/bash
parallel ::: "gem install travis" \
	"sudo apt update && sudo apt install $(grep --extended-regexp --invert-match '^(#|$)' aptpackages) && sudo ln --symbolic $(which fdfind) /usr/local/bin/fd"
