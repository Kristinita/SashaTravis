#!/bin/bash
parallel ::: 'gem install travis' \
	'sudo apt update && sudo apt-get install $(egrep -v "^(#|$)" aptpackages) && sudo ln -s $(which fdfind) /usr/local/bin/fd'
