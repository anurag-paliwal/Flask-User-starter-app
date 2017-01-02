#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate
cd /application
# Download requirements to build cache
pip download -d /build -r requirements.txt --no-input
pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements
pip install --no-index -f /build -r requirements.txt
pip install --no-index -f /build -r requirements_test.txt

# Run test.sh arguments
exec $@
