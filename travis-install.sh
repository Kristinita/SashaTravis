#!/bin/bash
parallel ::: "gem install travis" \
	"sudo apt update && sudo apt install fd-find && sudo ln --symbolic $(which fdfind) /usr/local/bin/fd"
