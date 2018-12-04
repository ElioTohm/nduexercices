# advance OS
please feel free to check my assignments the following demostrates the use of multiprocess using python
the following code is a word occurences using multi processing

## Installation
using docker
```bash
curl -sSL https://get.docker.com | sh
usermod pi -aG docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
local
```bash
sudo apt install python2.7
```

please make sure to read and run setup.sh
```bash
sh setup.sh
```

## Usage
using docker
```bash
docker-compose up 
```
countPool.py will load multiple files without memory constraints each file on a process
countPoolMemRest.py will chunk multiple files and use pool to execute
countProcess.py first attempt to create multi processing word occurences