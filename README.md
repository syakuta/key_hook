# Key hook check program

## Purpose
    Created as a practice of image classification.

## Features
    If the key is on the hook, it determines that you are at home, otherwise it determines that you are out.

## Video link

https://youtu.be/oPS3WQ1q_A4

## Execution environment

NVIDIA Jetson Nano 2GB Development Kit
logicool C505 HD Web Camera

## Installation
1. Clone gituhub and build docker container
```
    $ git clone https://github.com/syakuta/key_hook.git
```
2. Create docker image
```
    $ cd key_hook
      
    $ sudo docker build -t swg/key_hook:1.0 .
```
3. Display permission setting
```
    $ xhost local:
```
4. Start docker container
```
    $ sudo docker run -it --rm --network host --runtime nvidia --privileged --device /dev/video0 -e DISPLAY=$DISPLAY -v ~/key_hook/src/:/root/src -v /tmp/.X11-unix/:/tmp/.X11-unix swg/key_hook:1.0
```
5. start program
```
    $ cd /root/src
      
    $ python3 key_hook.py
```
6. End program

    Press the [q] key in the frame or ctrl + [c] to exit.
```
    $ exit
```
7. Revocation of Display permission
```
    $ xhost -local:
```
