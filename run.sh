#!/bin/bash

# thanks to Jurgen:
# https://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container/25280523#25280523

XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth

xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

docker build -t bloatwareinc/videostream .
docker run -ti -v $XSOCK:$XSOCK:ro -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH -p 8081:8081 bloatwareinc/videostream

