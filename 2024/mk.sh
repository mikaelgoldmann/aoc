#!/bin/bash
x=$1/dec$1
mkdir $1 && cp template.py $x.py && touch $x.sample && touch $x.in
