#!/bin/bash

g++ -c Panda3DGame.cxx -o Panda3DGame.o -std=gnu++11 -O2 -I/usr/include/panda3d/

g++ Panda3DGame.o -o main -L/usr/lib/python3/dist-packages/panda3d -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3direct