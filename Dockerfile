FROM brandonsoto/opencv-python

MAINTAINER Brandon Soto <brandon.soto09@gmail.com> 

ADD . /videostream
EXPOSE 8081
ENV DISPLAY :0
CMD ["python3", "/videostream/client.py"]
