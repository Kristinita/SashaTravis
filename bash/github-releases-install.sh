#!/bin/bash
# @Author: SashaChernykh
# @Date: 2025-03-15 15:13:47
# @Last Modified by: SashaChernykh
# @Last Modified time: 2025-03-15 18:17:58


pipenv run gh-release-install Kristinita/tidy-html5 tidy .venv/bin --verbose &

pipenv run gh-release-install sharkdp/fd "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz" --extract "fd-{tag}-x86_64-unknown-linux-gnu/fd" .venv/bin/fd --verbose &

wait
