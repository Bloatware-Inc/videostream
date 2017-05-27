import cv2
import requests
import numpy as np

# reenable after authenication is in place
# r = requests.get('http://192.168.1.xx/mjpeg.cgi', auth=('user', 'password'), stream=True)
r = requests.get('http://192.168.1.xx/mjpeg.cgi', stream=True)
if(r.status_code == 200):
    bytes = bytes()
    for chunk in r.iter_content(chunk_size=1024):
        bytes += chunk
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('i', i)
            if cv2.waitKey(1) == 27:
                exit(0)
else:
    print("Received unexpected status code {}".format(r.status_code))