# base image
FROM nvcr.io/nvidia/l4t-tensorflow:r32.4.4-tf2.3-py3
LABEL maintainer="syakuta[softwing.co.jp"
# update and install
RUN apt-get update && \
    apt-get install -y \
	git \
	zip \
	cmake \
	vim \
	libopencv-dev \
	python3-opencv

# install lib
RUN pip3 install keras pillow
