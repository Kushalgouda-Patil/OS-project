#!/bin/bash

function update() {
  echo "Updating software..."
}

function run() {
  python pyfile.py
}

if [ "$1" == "-i" ]; then
  update
elif [ "$1" == "-r" ]; then
  run
else
  echo "Usage: xyz [options]"
  echo "Options:"
  echo "  -i, --initialize: Initialize usn and dob"
  echo "  -r, --run: Fetch the attendence"
fi
