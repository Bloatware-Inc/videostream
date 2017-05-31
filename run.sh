#!/bin/bash

# thanks to Jurgen:
# https://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container/25280523#25280523

docker build -t bloatwareinc/videostream .
docker run -ti -v $PWD:/videostream:rw -p 8081:8081 bloatwareinc/videostream

