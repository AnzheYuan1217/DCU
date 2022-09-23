#!/bin/sh

rev | cut -d' ' -f1,2 | rev | sort | uniq
