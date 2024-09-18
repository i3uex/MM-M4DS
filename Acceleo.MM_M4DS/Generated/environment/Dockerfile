FROM python:3.11-slim


WORKDIR ./wf_model_dataset_python


RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*


RUN git clone --depth 1 --branch develop https://github.com/franjmelchor/MD4DSP-m2python.git .

RUN pip install --no-cache-dir -r requirements.txt


ENV PYTHONPATH=./wf_model_dataset_python


COPY ./dataProcessing_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_model_dataset_python/generated_code/
COPY ./contracts_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_model_dataset_python/generated_code/
COPY ./transformations_Job_Model_data_set_with_metanode_PYTHON_.py ./wf_model_dataset_python/generated_code/

COPY workflow_scripts.sh ./wf_model_dataset_python/workflow_scripts.sh

RUN chmod +x ./wf_model_dataset_python/workflow_scripts.sh

CMD ["/bin/bash", "./wf_model_dataset_python/workflow_scripts.sh"]
