#!/bin/sh

sort -n | tail -n 1 | cut -d' ' -f 2 | rev | cut -d'/' -f 1 | rev
