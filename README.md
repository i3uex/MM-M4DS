
# MM-M4DSP - Metamodels, Validation library, Models and Code Generation

This repository includes an Eclipse Modeling Framework (EMF) project with the metamodels ContractDef, Library, Environment, Workflow and Contract designs, the validation library specification with different transformations available and its associated contracts. It also includes some models that comply with the Workflow metamodel, which includes the perspective or conceptual model (Workflow), as well as the operational model (Environment).

Additionally, the project contains an Acceleo project, embedded in the root directory, to generate code from the current Eclipse Modeling Framework project.


## Eclipse EMF Configuration

To use this project properly, you must follow the next steps:

1. Clone this project to your Eclipse Modeling Framework (EMF) IDE. If you are not able to clone it with Eclipse, you can just download the project from [MM-M4DS](https://github.com/i3uex/MM-M4DS) and import it with Eclipse IDE with "File" → "Import..." → "Existing projects into workspace" → "Select archive file" and select the corresponding zip file with the downloaded project.

2. In this step, you can explore/modify the different metamodels designed in the project stored in `metamodel` directory (.aird files), the different models created and stored in `model` directory and the validation library `library_validation.xmi` stored in model directory.

## Acceleo Project Configuration

To use the code generation capabilities of Acceleo with this project, follow these steps to properly set up and execute the code generation process:

1. Create the Acceleo Project in Eclipse

    Open Eclipse and go to File → New → Project....

    Choose Acceleo Project and click Next.

    Set the Project name to Acceleo.MM_M4DS.

    Click Next.

    In the Metamodel URIs field, browse and select the URIs from the .ecore metamodels (Workflow, Library, ContractDef, Contract and Environment).

    In Type, select Library.
    
    In template section check the options: "Generate documentation", "Generate file" and "Main template".

    Leave the default values for other fields and click Finish.

    This will create a working Acceleo project structure with a src directory containing a sample .mtl file.

2. Replace Template Code with the Project Templates

    Copy all .mtl files and any necessary helper Java files from the existing Acceleo.MM_M4DS/src directory of the repository into the src folder of the created Acceleo project.

    Ensure that the directory structure (i.e., the package structure) is preserved.

    If prompted by Eclipse, refresh the project (right-click on the project and select Refresh or press F5).

3. Generate Code from a Model

    Once the templates are in place and the project is configured:

    Right-click on the main .mtl file (e.g., GenerateAll.mtl) in the src folder.

    Select Run As → Launch Acceleo Application.

    In the Model field, click Browse Workspace and select the desired .xmi model file from the model/ directory (e.g., wf_validation_KNIME_contracts.xmi).

    In the Target field, choose or create a destination folder (e.g., Acceleo.MM_M4DS/Generated/) where the generated code will be placed.

    Click Run to execute the code generation.

4. Output Files

The generated code will appear in the directory specified in the Target field. 



## Project Structure
```bash
prueba_M4DS/
│
├── Acceleo.MM_M4DS/
│  ├── Generated/
│  ├── src/
│  └── ...
│
├── metamodel/
│  ├── images/
│  │  ├── /prueba_M4DS/metamodel/images/ContractDefinitionMM.png
│  │  ├── /prueba_M4DS/metamodel/images/ContractMM.png
│  │  ├── /prueba_M4DS/metamodel/images/Environment class diagram.png
│  │  ├── /prueba_M4DS/metamodel/images/LibraryMM.png
│  │  └── /prueba_M4DS/metamodel/images/WorkflowMM.png
│  │
│  ├── Contract.aird
│  ├── Contract.ecore
│  ├── ContractDef.aird
│  ├── ContractDef.ecore
│  ├── Environment.aird
│  ├── Environment.ecore
│  ├── Library.aird
│  ├── Library.ecore
│  ├── Workflow.aird
│  └── Workflow.ecore
│
├── model/
│  ├── knime_dataDictionaries/
│  │  └── ...
│  ├── python_dataDictionaries/
│  │  └── ...
│  ├── wf_validation_KNIME_contracts.xmi
│  ├── library_validation.xmi
│  ├── library_validation_job.xmi
│  └── ...
│
└── README.md
```

- **`Acceleo.MM_M4DS/`**: contains the Acceleo project to get generated code from models.
- **`Acceleo.MM_M4DS/Generated`**: folder from Acceleo project to store generated code files.
- **`Acceleo.MM_M4DS/src`**: source code files with Acceleo templates for code generation from models.


- **`metamodel/`**: contains the designed metamodels, stored in .ecore and .aird format. Open .aird files to see the metamodel as a class diagram (for a better visualization).
- **`metamodel/images`**: contains the designed metamodels but exported in png format.


- **`model/`**: contains the models created that comply with the Workflow metamodel. A model of this kind is `wf_validation_KNIME_contracts.xmi`. In addition, in this directory is stored the validation contract library (`wf_validation_library.xmi`).
- **`model/knime_dataDictionaries`**: contains the data exported from KNIME platform for the `wf_validation_KNIME_contracts` Workflow model.
- **`model/python_dataDictionaries`**: contains the data exported from Python platform for the `wf_validation_KNIME_contracts` Workflow model.
- 

- **`README.md`**: file that contains the documentation of the project.
  

## Authors

- [Francisco Javier Melchor González](https://www.github.com/franjmelchor)
- [Carlos Breuer Carrasco](https://www.github.com/carlosbc24)
- [Carlos Cambero Rojas](https://www.github.com/CCamberoR)


## Questions
If you have any questions, please contact any of the authors.
