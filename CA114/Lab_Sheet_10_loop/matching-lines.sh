#!/bin/sh

for arg in "$@"
do
   if test -f "$arg"
   then
      grep bingo -w "$arg"
   fi
done
