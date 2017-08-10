#!/bin/bash
find ./ -type f -name "*.pyc" -print0 | xargs -0 /bin/rm -f;
find ./ -type f -name ".DS*" -print0 | xargs -0 /bin/rm -f;
