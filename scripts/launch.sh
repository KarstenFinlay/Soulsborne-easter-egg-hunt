#!/bin/bash

# run from project root

if [ ! -f "./Dockerfile" ]; then
    echo "Could not locate Dockerfile. Run launch script from project root."
    exit 1
fi

# check if build is enforced

BUILD=false

if [[ $* == *--build* ]]; then
    echo "--build flag passed; building image."
    BUILD=true
fi

SAVE=false

if [[ $* == *--save* ]]; then
    echo "--save flag passed; will save results to ./Results."
    SAVE=true
fi

# check whether image exists. If not; always build

if docker inspect --type image easter_souls_app >/dev/null 2>&1; then
    if [ "$BUILD" = true ]; then
        echo "Easter Souls image already exists. Deleting..."
        docker rmi easter_souls_app
    fi
else
    BUILD=true
fi

# build image when necessary

if [ "$BUILD" = true ]; then
    echo "Creating image..."
    docker build -t easter_souls_app:latest .
fi

# run image

docker run -it --name easter_souls easter_souls_app:latest

# check run was successful

if $?; then
    echo "Unexpected failure while running container."
    docker rm easter_souls >/dev/null 2>&1
    exit 1
else
    if [ "$SAVE" = false ]; then
        docker rm easter_souls >/dev/null 2>&1
        exit 0
    else
        echo "Run was successful. Getting results..."
    fi
fi

# check results directory exists

if [ ! -f "./Results" ]; then
    echo "No Results directory found. Creating..."
    mkdir Results
fi

# copy result file from docker container to local results

docker container cp easter_souls:/usr/src/Results/. ./Results/

# remove container

docker rm easter_souls >/dev/null 2>&1
