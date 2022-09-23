#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/weblogs2.txt" | cut -d ',' -f 3 | sort | uniq | wc -l
