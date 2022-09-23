#!/bin/sh

wget -q -O - "https://activepeers.com/files/james-bond.txt" > schedule.txt
grep Pierce < schedule.txt
