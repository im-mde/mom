#!/bin/bash

# author: Matthew E. (im-mde)
# date: October 19, 2021
# summary: execute mqsc commands from input file passed as argument


if [ $# -ne 2 -a $# -ne 3 ]; then
    echo "Error: Expected 2 or 3 Arguments"
    echo "Syntax:"
    echo "./mqscfile [Queue Manager] [Input File]"
    echo "./mqscfile [Queue Manager] [Input File] [Output File]"
    exit 1
fi

if [ $# -eq 2 ]; then
    runmqsc $1 < $2
elif [ $# -eq 3 ]; then
    runmqsc $1 < $2 > $3
fi

if [ $? -ne 0 -a $# -eq 3 ]; then
   rm $3
fi
