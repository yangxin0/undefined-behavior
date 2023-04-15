#! /bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: build_all($0) TAG (eg: latest, v0.1)"
	exit 1
fi

nginx/build.sh $1
server/scripts/build.sh $1
web/scripts/build.sh $1

