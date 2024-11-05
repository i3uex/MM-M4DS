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
RUN pip install sqlalchemy
RUN pip install boto3

COPY dataProcessing_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/
COPY contracts_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/
COPY transformations_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_validation_python/workflows/

COPY fileFormatting.py ./wf_validation_python/workflows/

COPY workflow_scripts.sh ./wf_validation_python/workflow_scripts.sh

RUN chmod +x ./wf_validation_python/workflow_scripts.sh

CMD ["/bin/bash", "./wf_validation_python/workflow_scripts.sh"]
