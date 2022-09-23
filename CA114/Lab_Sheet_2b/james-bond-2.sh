#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/james-bond.txt" > schedule.txt
grep Moore < schedule.txt | wc -l
