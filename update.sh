#!/bin/bash


script() {
rm -rf simple-server
}


installer() {
git clone https://github.com/Anthony-sys/simple-server
} 


cache() {
cd simple-server
}

pem() {
chmod +x run.sh
chmod +x update.sh
}


run() {
python server.py
}



script
installer
cache
pem
run
