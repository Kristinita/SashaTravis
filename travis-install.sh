#!/bin/bash
parallel ::: "gem install travis" \
	"sudo apt update && sudo apt install $(egrep --invert-match '^(#|$)' aptpackages) && sudo ln --symbolic $(which fdfind) /usr/local/bin/fd"
