#! /bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: web-server($0) TAG (eg: latest, v0.1)"
	exit 1
fi

DIR="$(dirname "${BASH_SOURCE[0]}")"
docker build -t web-server:${1} -f ${DIR}/../Dockerfile ${DIR}/..

