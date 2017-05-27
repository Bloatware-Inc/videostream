# video_stream

# Client Dependencies
1. docker
2. xauth (needed for outputting stream to host)

## Set up on Raspberry Pi
```bash
sudo apt-get install motion
sudo modprobe bcm2835-v4l2
```

## Set up on Client
Modify IP address and port from client.py (line 8)

## How to Run Application
```bash
## LINUX CLIENT
./run.sh

## RASPBERRY PI SERVER
sudo motion -c motion.conf -n
```
