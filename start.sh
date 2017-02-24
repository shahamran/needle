#!/bin/bash

source activate $1
jupyter-notebook --NotebookApp.file_to_run=$2
source deactivate
