#!/bin/bash
set -e

if [ ! -d "data" ]; then
    mkdir -p data
fi

if [ ! -d "data/d1/test" ]; then
    mkdir -p data/d1/test
fi
if [ ! -d "data/d2" ]; then
    mkdir -p data/d2
fi
if [ ! -d "data/d2" ]; then
    mkdir -p data/d2
fi
if [ ! -d "data/d3" ]; then
    mkdir -p data/d3
fi
if [ ! -d "data/d3" ]; then
    mkdir -p data/d3
fi
if [ ! -d "data/d4" ]; then
    mkdir -p data/d4
fi
if [ ! -d "data/d4" ]; then
    mkdir -p data/d4
fi
if [ ! -d "data/d5" ]; then
    mkdir -p data/d5
fi
if [ ! -d "data/d5" ]; then
    mkdir -p data/d5
fi
if [ ! -d "data/d6" ]; then
    mkdir -p data/d6
fi
if [ ! -d "data/d6" ]; then
    mkdir -p data/d6
fi
if [ ! -d "data/d7" ]; then
    mkdir -p data/d7
fi
if [ ! -d "data/d7" ]; then
    mkdir -p data/d7
fi
if [ ! -d "data/d8" ]; then
    mkdir -p data/d8
fi
if [ ! -d "data/d8" ]; then
    mkdir -p data/d8
fi
if [ ! -d "data/d9" ]; then
    mkdir -p data/d9
fi
if [ ! -d "data/d9" ]; then
    mkdir -p data/d9
fi
if [ ! -d "data/d10" ]; then
    mkdir -p data/d10
fi
if [ ! -d "data/d10" ]; then
    mkdir -p data/d10
fi
if [ ! -d "data/d11" ]; then
    mkdir -p data/d11
fi
if [ ! -d "data/d11" ]; then
    mkdir -p data/d11
fi
if [ ! -d "data/d12" ]; then
    mkdir -p data/d12
fi
if [ ! -d "data/d12" ]; then
    mkdir -p data/d12
fi
if [ ! -d "data/d13" ]; then
    mkdir -p data/d13
fi
if [ ! -d "data/d13" ]; then
    mkdir -p data/d13
fi
if [ ! -d "data/d14" ]; then
    mkdir -p data/d14
fi
if [ ! -d "data/d14" ]; then
    mkdir -p data/d14
fi
if [ ! -d "data/d15" ]; then
    mkdir -p data/d15
fi
if [ ! -d "data/d15" ]; then
    mkdir -p data/d15
fi
if [ ! -d "data/d16" ]; then
    mkdir -p data/d16
fi
sudo apt-get update --yes
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update --yes

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin --yes

docker build --no-cache -t ubuntu-knime:latest -f Dockerfile .

clear

cp /home/carlos/Escritorio/datasets/missing_input_dataDictionary.csv "$(pwd)/data/"d1/test


cp /home/carlos/Descargas/PMMLModel/PMMLModel/students_decisionTree_PMML.pmml "$(pwd)/data"


docker run -it --rm --name docker-knime --network host --mount type=bind,source="$(pwd)/data",target=/wf_validation_knime/data ubuntu-knime:latest

docker rmi ubuntu-knime:latest

clear

echo -e "Exiting the application...\n"
