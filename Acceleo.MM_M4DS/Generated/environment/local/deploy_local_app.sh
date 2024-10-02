#!/bin/bash
set -e

sudo apt update --yes
sudo apt install python3-pip python3-venv git --yes
sudo pip3 install virtualenv

REPO_URL="https://github.com/franjmelchor/MD4DSP-m2python.git"
PROJECT_DIR="./wf_validation_python"
PYTHON_INTERPRETER="3.11"

CONTRACTS_SCRIPT="contracts_Job_Model_data_set_with_metanode_PYTHON_"
TRANSFORMATIONS_SCRIPT="transformations_Job_Model_data_set_with_metanode_PYTHON_"
WORKFLOW_SCRIPT="dataProcessing_Job_Model_data_set_with_metanode_PYTHON_"

VENV_DIR="$PROJECT_DIR/venv"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Cloning the project repository..."
    git clone --depth 1 --branch develop $REPO_URL $PROJECT_DIR
else
    echo "Project directory already exists. Skipping clone."
fi

if [ ! -d "./wf_validation_python/data" ]; then
    mkdir ./wf_validation_python/data/
fi

cp -R /home/carlos/Escritorio/datasets/* ./wf_validation_python/data/
cp -R /home/carlos/Escritorio/datasetsTest/* ./wf_validation_python/data/


cp $CONTRACTS_SCRIPT.py ./wf_validation_python/generated_code/
cp $TRANSFORMATIONS_SCRIPT.py ./wf_validation_python/generated_code/
cp $WORKFLOW_SCRIPT.py ./wf_validation_python/generated_code/


if [ ! -d "$VENV_DIR" ]; then
    echo "Creating a Python virtual environment..."
    virtualenv -p "$PYTHON_INTERPRETER" $VENV_DIR
fi

source "$VENV_DIR/bin/activate"

cd "$PROJECT_DIR"


if [ -f "requirements.txt" ]; then
    echo "Installing project requirements..."
    python3 -m pip install --no-cache-dir -r requirements.txt
else
    echo "requirements.txt not found. Skipping installation of requirements."
fi

clear

while true; do
    echo -e "\nWhat would you like to do?"
    echo "    1. Execute the Workflow validation contracts"
    echo "    2. Execute the Workflow data transformations"
    echo "    3. Execute the complete Pipeline (transformations and contracts)"
    echo -e "    4. Exit\n"

    read -r -p "Select an option: " option
    clear

    if [ "$option" -eq 1 ]; then
        echo -e "Executing the Workflow validation contracts...\n"
        if ! python3 -m generated_code.$CONTRACTS_SCRIPT; then
            echo "An error occurred while executing the Workflow validation contracts."
        fi
    elif [ "$option" -eq 2 ]; then
        echo -e "Executing the Workflow data transformations...\n"
        if ! python3 -m generated_code.$TRANSFORMATIONS_SCRIPT; then
            echo "An error occurred while executing the Workflow data transformations."
        fi
    elif [ "$option" -eq 3 ]; then
        echo -e "Executing the complete Pipeline...\n"
        if ! python3 -m generated_code.$WORKFLOW_SCRIPT; then
            echo "An error occurred while executing the complete Pipeline."
        fi
    elif [ "$option" -eq 4 ]; then
        echo -e "Exiting the application...\n"
        break
    else
        echo -e "Invalid option. Please select a valid option.\n"
    fi
done

