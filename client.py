import cv2
import requests
import numpy as np


def stream_video():
    print('Getting stream ready...')
    try:
        # reenable after authentication is in place
        # r = requests.get('http://192.168.1.xx/mjpeg.cgi', auth=('user', 'password'), stream=True)
        response = requests.get('http://192.168.0.11:8081/mjpeg.cgi', stream=True)
        print('Sent request to stream server')

        if (response.status_code == 200):  # status is OK
            bytes = bytes()
            for chunk in response.iter_content(chunk_size=1024):
                bytes += chunk
                start_marker = bytes.find(b'\xff\xd8')
                end_marker = bytes.find(b'\xff\xd9')
                if start_marker != -1 and end_marker != -1:
                    jpg = bytes[start_marker:end_marker + 2]
                    bytes = bytes[end_marker + 2:]  # reset bytes
                    image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)  # read jpg image
                    cv2.imshow('i', image)
                    if cv2.waitKey(1) == 27:  # escape key
                        exit(0)
        else:
            print("Received unexpected status code {}".format(response.status_code))
    except OSError as error:
        print('An OS error has occurred!')
        print(error)


if __name__ == '__main__':
    stream_video()
