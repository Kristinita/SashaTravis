#!/bin/bash
# @Author: SashaChernykh
# @Date: 2025-03-15 15:13:47
# @Last Modified by: SashaChernykh
# @Last Modified time: 2025-03-16 20:20:15


pipenv run gh-release-install Kristinita/tidy-html5 tidy /usr/local/bin --verbose &

wait
