#!/bin/bash

set -e


venv="venv"

echo "making $venv"

virtualenv $venv
source $venv/bin/activate

echo "installing perfect"
pip install -e .
