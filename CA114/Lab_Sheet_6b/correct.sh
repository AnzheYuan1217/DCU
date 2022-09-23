#!/bin/sh

if cmp -s "expected-stdout.txt" "actual-stdout.txt"
then
   echo "correct"
else
   echo "incorrect"
   false
fi
