#!/bin/bash

for i in $(seq -f "%02g" 1 25)
do
    PYFILE="./day_$i/main.py"
    if test -f "$PYFILE";
    then
        echo "#### Day $i ####"
        python3.9 $PYFILE
    fi
    printf "\n"
done
