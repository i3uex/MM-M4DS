#!/bin/bash
set -e

if [ ! -d "data" ]; then
    mkdir data
fi

if [ ! -d "data/sqlserver" ]; then
    mkdir data/sqlserver
fi
if [ ! -d "data/datasets" ]; then
    mkdir data/datasets
fi
if [ ! -d "data/datasetsTest" ]; then
    mkdir data/datasetsTest
fi
if [ ! -d "data/mongo" ]; then
    mkdir data/mongo
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

docker build -t ubuntu-22.04:latest -f Dockerfile .

clear

cp /home/carlos/Escritorio/datasets/rowFilter_output_dataDictionary.csv "$(pwd)/data/"datasets
cp /home/carlos/Escritorio/datasets/rowFilter_output_dataDictionary.csv "$(pwd)/data/"datasets
cp /home/carlos/Escritorio/datasetsTest/columnFilter_output_dataDictionary.csv "$(pwd)/data/"datasetsTest
cp /home/carlos/Escritorio/datasetsTest/columnFilter_output_dataDictionary.csv "$(pwd)/data/"datasetsTest
cp /home/carlos/Escritorio/datasetsTest/ruleEngine_territory_output_dataDictionary.csv "$(pwd)/data/"datasetsTest
cp /home/carlos/Escritorio/datasetsTest/ruleEngine_territory_output_dataDictionary.csv "$(pwd)/data/"datasetsTest

docker run -it --rm --name wf_validation_python --network host --mount type=bind,source="$(pwd)/data",target=/wf_validation_python/data ubuntu-22.04:latest

docker rmi ubuntu-22.04:latest

clear

echo -e "Exiting the application...\n"
