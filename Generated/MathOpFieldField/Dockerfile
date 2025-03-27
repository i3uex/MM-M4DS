FROM python:3.11-slim

WORKDIR ruta
ENV PYTHONPATH=ruta

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 --branch develop https://github.com/i3uex/MD4DSP-m2python.git .

RUN wget https://download.java.net/java/ga/jdk11/openjdk-11_linux-x64_bin.tar.gz && \
    tar -xvf openjdk-11_linux-x64_bin.tar.gz -C /usr/local && \
    ln -s /usr/local/jdk-11/bin/java /usr/bin/java

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install h5py
RUN pip install pyarrow

COPY dataProcessing_Job_02_Data_Cleaning_Workflow4-1.py ruta/workflows/
COPY contracts_Job_02_Data_Cleaning_Workflow4-1.py ruta/workflows/
COPY transformations_Job_02_Data_Cleaning_Workflow4-1.py ruta/workflows/

COPY fileFormatting.py ruta/workflows/

COPY workflow_scripts.sh ruta/workflow_scripts.sh

RUN chmod +x ruta/workflow_scripts.sh

CMD ["/bin/bash", "ruta/workflow_scripts.sh"]
