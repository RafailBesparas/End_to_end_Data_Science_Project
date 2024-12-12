import os
from pathlib import Path
import logging

# Setting up basic logging configuration to capture events at INFO level and format them with timestamp.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name which will be used as a base directory for creating the project structure.
project_name = "datascience"

# Defining a set of file paths for the project structure.
# This includes directories and files commonly found in a data science project, such as config, pipeline, and utils.
list_of_files ={
    ".github/workflows/.gitkeep",  # Placeholder to ensure empty directories are pushed to version control.
    f"src/{project_name}/__init__.py",  # Initialization file for the base source directory.
    f"src/{project_name}/components/__init__.py",  # Initialization file for components module.
    f"src/{project_name}/utils/__init__.py",  # Initialization file for utilities module.
    f"src/{project_name}/utils/common.py",  # Common utility functions file.
    f"src/{project_name}/config/__init__.py",  # Initialization file for configuration module.
    f"src/{project_name}/config/configuration.py",  # File for handling configuration settings.
    f"src/{project_name}/pipeline/__init__.py",  # Initialization file for pipeline module.
    f"src/{project_name}/entity/__init__.py",  # Initialization file for entity module.
    f"src/{project_name}/entity/config_entity.py",  # File for defining configuration-related entities.
    f"src/{project_name}/constants/__init__.py",  # Initialization file for constants module.
    "config/config.yaml",  # YAML configuration file.
    "params.yaml",  # YAML file for parameter settings.
    "schema.yaml",  # YAML file for schema definitions.
    "main.py",  # Entry point of the application.
    "Dockerfile",  # Docker configuration file.
    "setup.py",  # Setup script for the Python package.
    "research/research.ipynb",  # Jupyter notebook for research and experimentation.
    "templates/index.html",  # HTML template for a web application.
    "app.py"  # Main application file.
}

# Iterating through each file path in the list to create the project structure.
for filepath in list_of_files:
    filepath = Path(filepath)  # Using Pathlib for cross-platform path handling.
    filedir, filename = os.path.split(filepath)  # Separating directory and filename.

    # Create directories if they don't already exist.
    if filedir!="":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory {filedir} for the file:  {filename}")

    # Create an empty file if it doesn't exist or if the existing file is empty.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:  # Opening file in write mode to ensure it's empty.
            pass  # File created and immediately closed.
        logging.info(f"Creating empty file: {filepath}")

    # Log a message if the file already exists and is not empty.
    else:
        logging.info(f"{filename} already exists")
