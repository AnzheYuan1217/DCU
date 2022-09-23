#!/bin/sh

cut -d',' -f 1 | sort | uniq -c | sort -n | tail -n 1 | rev | cut -d ' ' -f 1 | rev
