#!/bin/bash
# Builds the Interop Server Docker image.

SERVER=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
docker build -t uavaustin/armhf-interop-server ${SERVER}
