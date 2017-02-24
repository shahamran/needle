#!/bin/bash
#
# Do everything in your power to start the notebook

env_name=needle
req_file=requirements.txt
nb_file=Aliens.ipynb

function errorExit {
  echo $1
  exit 1
}

function init {
  # exit an activated environment
  source deactivate
}

function checkConda {
  printf "Checking conda version... "
  if ! conda --version 2> /dev/null; then
    errorExit "conda must be installed for this to work"
  else
    printf " ..done!\n"
  fi
}

function createEnv {
  if conda env list | grep "^$env_name\s" > /dev/null; then
    echo "Found environment: '$env_name'! Let's use it."
    source activate $env_name || errorExit "could not activate environment"
  else
    echo "Creating python environment..."
    conda create --name $env_name --file $req_file || \
      errorExit "could not create environment"
    source activate $env_name
  fi
}

function runNotebook {
  echo "Running notebook"
  echo
  jupyter-notebook --NotebookApp.file_to_run=$nb_file
}

init
checkConda
createEnv
runNotebook
