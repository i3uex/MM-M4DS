#!/bin/bash
set -e

if [ ! -d "data" ]; then
    mkdir data
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

cp /home/carlos/Escritorio/datasets/missing_input_dataDictionary.csv "$(pwd)/data/"
cp /home/carlos/Escritorio/datasetsTest/missing_output_dataDictionary.csv "$(pwd)/data/"

docker run -it --rm --name wf_validation_python --mount type=bind,source="$(pwd)/data",target=/wf_validation_python/data ubuntu-22.04:latest

docker rmi ubuntu-22.04:latest

clear

echo -e "Exiting the application...\n"
