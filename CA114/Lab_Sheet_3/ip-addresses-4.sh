#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/weblogs2.txt" | cut -d ',' -f 1 | sort | uniq -c
