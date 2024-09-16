# Use the official Python 3.11 slim image as the base as it's the python version used for the MD4DSP project
FROM python:3.11

# Set the working directory inside the container to /app.
# All subsequent commands, such as copying files or running commands, will use this directory as the default path.
# organizing the container’s filesystem structure and making it easier to manage and locate files.
WORKDIR /app

# installs Git and cleans up unnecessary files
# - apt-get update: updates the package list to ensure the latest versions of packages are installed.
# - apt-get install -y --no-install-recommends git: installs Git without extra recommended packages to keep the image
# small.
# - rm -rf /var/lib/apt/lists/*: removes the cached package lists to reduce the image size further.
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# Clone the project repository from GitHub
# - depth 1: clones only the latest commit, reducing the amount of data pulled and speeding up the build process
# - branch develop: clones the develop branch of the repository
RUN git clone --depth 1 --branch develop https://github.com/franjmelchor/MD4DSP-m2python.git .

# Install the project requirements without using or storing package cache, which reduces the final image size.
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory to PYTHONPATH
# Setting the PYTHONPATH allows Python to locate the modules within the /app directory, ensuring that the application \
# can be run without module import errors.
ENV PYTHONPATH=/app

# Copy the desired files into the generated_code directory
COPY generated_code/contracts_Job_Model_data_set_with_metanode_KNIME_.py generated_code/
COPY generated_code/contracts_Job_Model_data_set_with_metanode_PYTHON_.py generated_code/

# Copy the shell script into the container
COPY script_calls.sh /app/script_calls.sh

# Make the shell script executable
RUN chmod +x /app/script_calls.sh

# Use the JSON format for CMD to execute the shell script
CMD ["/bin/bash", "/app/script_calls.sh"]


