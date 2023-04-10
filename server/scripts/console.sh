#! /bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: chatgpt-console($0) TAG (eg: latest, v0.1)"
	exit 1
fi

# Must remove entrypoint
docker run -it --entrypoint "" chatgpt-server:${1} /bin/bash

