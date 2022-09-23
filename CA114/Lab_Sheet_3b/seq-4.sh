#!/bin/sh

seq "$1" | sort -n -r | head -n "$2"
