#!/bin/bash
# @Author: SashaChernykh
# @Date: 2025-03-15 15:13:47
# @Last Modified by: SashaChernykh
# @Last Modified time: 2025-03-15 17:58:35

# Kira Goddess!
pipenv run gh-release-install Kristinita/tidy-html5 tidy .venv/bin --verbose &

# Kira Goddess!
pipenv run gh-release-install sharkdp/fd "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz" --extract "fd-{tag}-x86_64-unknown-linux-gnu/fd" .venv/bin/fd --verbose &

# Kira Goddess!
wait
