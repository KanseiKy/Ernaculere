#!/usr/bin/env bash

source color.sh

function error() {
    echo -e "[${BLUE}Ernaculere${RESET}]: (${RED}Error${RESET}: ${YELLOW}${1}${RESET}): ${2}"
}

function info() {
    echo -e "[${BLUE}Ernaculere${RESET}]: (${GREEN}Info${RESET}: ${YELLOW}${1}${RESET}): ${2}"
}