#!/bin/sh

for f in "$@"
do
   test -f "$f" && cat "$f"
done
