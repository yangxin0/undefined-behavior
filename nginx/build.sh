#! /bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: nginx-server($0) TAG (eg: latest, v0.1)"
	exit 1
fi

DIR="$(dirname "${BASH_SOURCE[0]}")"
docker build -t nginx-server:${1} -f ${DIR}/Dockerfile ${DIR}/../server

