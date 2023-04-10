#! /bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: chatgpt-server($0) TAG (eg: latest, v0.1)"
	exit 1
fi

DIR="$(dirname "${BASH_SOURCE[0]}")"
docker build -t chatgpt-server:${1} -f ${DIR}/../Dockerfile ${DIR}/..

