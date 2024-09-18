#CAMBIAR LAS RUTAS DE LOS COPY DE LOS ARCHIVOS GENERADOS

CONTRACTS_SCRIPT="generated_code.contracts_Job_Model_data_set_with_metanode_PYTHON_"
TRANSFORMATIONS_SCRIPT="generated_code.transformations_Job_Model_data_set_with_metanode_PYTHON_"
WORKFLOW_SCRIPT="generated_code.dataProcessing_Job_Model_data_set_with_metanode_PYTHON_"

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
        if ! python3 -m $CONTRACTS_SCRIPT; then
            echo "An error occurred while executing the Workflow validation contracts."
        fi
    elif [ "$option" -eq 2 ]; then
        echo -e "Executing the Workflow data transformations...\n"
        if ! python3 -m $TRANSFORMATIONS_SCRIPT; then
            echo "An error occurred while executing the Workflow data transformations."
        fi
    elif [ "$option" -eq 3 ]; then
        echo -e "Executing the complete Pipeline...\n"
        if ! python3 -m $WORKFLOW_SCRIPT; then
            echo "An error occurred while executing the complete Pipeline."
        fi
    elif [ "$option" -eq 4 ]; then
        echo -e "Exiting the application...\n"
        break
    else
        echo -e "Invalid option. Please select a valid option.\n"
    fi
done
