#!/bin/bash

cd code
$1 $2 $3 $4 -L/usr/X11R6/lib -lm -lpthread -lX11 && $5