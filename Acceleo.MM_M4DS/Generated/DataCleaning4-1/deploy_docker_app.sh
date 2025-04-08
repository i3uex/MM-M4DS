#!/bin/bash
set -e

if [ ! -d "data" ]; then
    mkdir -p data
fi

#sudo apt-get update --yes
#sudo apt-get install ca-certificates curl
#sudo install -m 0755 -d /etc/apt/keyrings
#sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
#sudo chmod a+r /etc/apt/keyrings/docker.asc

#echo \
#  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
#  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
#  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#sudo apt-get update --yes

#sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin --yes

docker build --no-cache -t ubuntu_22_04:latest -f Dockerfile .

clear

cp /home/carlos/mathOperation_input_dataDictionary.csv "$(pwd)/data/"




docker run -it --rm --name docker41 --network host --mount type=bind,source="$(pwd)/data",target=/wf_val/data ubuntu_22_04:latest

docker rmi ubuntu_22_04:latest

clear

echo -e "Exiting the application...\n"
