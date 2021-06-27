#!/usr/bin/env python3

import subprocess
import colorama
import shutil
import time
import sys
import os

deno_modules = [
    'https://deno.land/std@0.99.0/node/module.ts'
]

wasm = [
    ''
]

exe = [
    'deno',
    'npm',
    'node',
    'npx',
    'rustc'
]

colorama.init()

RED = colorama.Fore.RED
BLUE = colorama.Fore.LIGHTBLUE_EX
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RESET = colorama.Fore.RESET

def error(msg: str):
    print(f'[{BLUE}Ernaculere{RESET}]: ({RED}Error{RESET}: {YELLOW}build.py{RESET}): {msg}')

def info(msg: str):
    print(f'[{BLUE}Ernaculere{RESET}]: ({GREEN}Info{RESET}: {YELLOW}build.py{RESET}): {msg}')

def check():
    info('Checkong executables...')
    time.sleep(0.7)
    for i in exe:
        info(f'Checking {i}...')
        exec = shutil.which(i)

        if exec == None:
            error(f'Couldn\'t find \'{i}\'')
            error(f'Please install \'{i}\' and set the PATH correctly')
            error('Aborting...')
            sys.exit(1)

    info('Done!')
    time.sleep(0.7)

    

def install_deno_modules():
    info('Installing Deno modules...')
    time.sleep(0.7)
    for i in deno_modules:
        cmd = f'deno install -qf --unstable --no-check {i} &> /dev/null' if os.name == 'posix' else f'deno install -qf --unstable --no-check {i} > NUL'
        os.system(cmd)

    info('Done!')
    time.sleep(0.7)

def install_node_modules():
    info('Installing NPM modules...')
    time.sleep(0.7)

    cmd = f'npm --silent install &> /dev/null' if os.name == 'posix' else 'npm --silent --quiet install > NUL'
    os.system(cmd)

    info('Done!')
    time.sleep(0.7)

def build_wasm():
    info('Compiling WASM files...')
    time.sleep(0.7)

    for i in wasm:
        os.system(f'npx asc {i}.ts -b {i}.wasm --t {i}.wat')

    info('Done!')
    time.sleep(0.7)

def build_rust():
    info('Compiling Rust files...')
    time.sleep(0.7)
    
    info('Done!')
    time.sleep(0.7)

def main():
    check()
    install_deno_modules()
    install_node_modules()

if __name__ == '__main__':
    main()