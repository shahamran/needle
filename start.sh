#!/bin/bash

env_name="$1"
file_name="$2"

source activate $env_name
jupyter-notebook --NotebookApp.file_to_run=$file_name
source deactivate
