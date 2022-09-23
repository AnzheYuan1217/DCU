#!/bin/sh

smallest_num="$1"
for i in "$@"
do
 if [ $i -lt $smallest_num ]
 then
  smallest_num=$i
 fi
done
echo $smallest_num
