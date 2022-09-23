#!/bin/sh

wget -q -O - "https://activepeers.com/files/bbc1.txt" > schedule.txt
grep News < schedule.txt | grep -v 'Have I Got News for You'
