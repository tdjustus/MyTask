#!/bin/bash

PYTHONPATH=$(which python3)
if [ -z "$PYTHONPATH" ]; then
    PYTHONPATH=$(which python)
    if [ -z "$PYTHONPATH" ]; then
        echo "Python not found. Please install Python."
        exit 1
    fi
fi

$PYTHONPATH $(dirname $0)/mytask.py "$@"