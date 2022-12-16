#!/bin/bash

docker pull github/super-linter:latest
docker run -e IGNORE_GITIGNORED_FILES=true -e IGNORE_GENERATED_FILES=true -e RUN_LOCAL=true -e USE_FIND_ALGORITHM=true -v "$(pwd)":/tmp/lint github/super-linter
