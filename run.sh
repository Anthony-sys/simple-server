#!/bin/bash


installer() {
pkg install python3
}


run() {
python3 server.py
}


installer
run
