#!/usr/bin/env bash

source color.sh
source log.sh

if command -v deno &> /dev/null; then
    error "bundle.sh" "Couldn't find 'deno'"
    error "bundle.sh" "Please install 'deno' and try again and set the PATH correctly"
    error "bundle.sh" "Aborting..."
    exit 1
fi

deno test -qA test