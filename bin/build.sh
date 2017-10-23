#!/usr/bin/env bash
set -eu

DIR="$(cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")" && pwd)"
cd "${DIR}/.."

if [[ -d dist ]] ; then
    rm -r ./dist
fi

python setup.py sdist
