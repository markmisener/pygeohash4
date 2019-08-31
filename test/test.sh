#!/bin/bash
set -e

docker build -t pygeohash4 .
docker run \
    -v $(pwd)/.:/usr/local/src/pygeohash4/ \
    pygeohash4 \
    bash -c "export PYTHONPATH=/usr/local/src/pygeohash4 && pytest -vv"
