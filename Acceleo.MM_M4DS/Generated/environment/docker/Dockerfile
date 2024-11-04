FROM python:3.11-slim

WORKDIR ./wf_validation_python
ENV PYTHONPATH=./wf_validation_python

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*


RUN git clone --depth 1 --branch develop https://github.com/franjmelchor/MD4DSP-m2python.git .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install h5py
RUN pip install pyarrow
RUN pip install pymongo
RUN pip install sqlalchemy
RUN pip3 install pyodbc
RUN apt-get update && \
    apt-get install -y curl gnupg apt-transport-https unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    rm -rf /var/lib/apt/lists/*

COPY dataProcessing_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/
COPY contracts_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/
COPY transformations_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/

COPY fileFormatting.py ./wf_validation_python/workflows/

COPY workflow_scripts.sh ./wf_validation_python/workflow_scripts.sh

RUN chmod +x ./wf_validation_python/workflow_scripts.sh

CMD ["/bin/bash", "./wf_validation_python/workflow_scripts.sh"]
