set "env_name = needle"
set "req_file = requirements.txt"
set "nb_file = Aliens.ipynb"


:errorExit
echo %~1
exit 1
goto:eof


:init
Rem exit an activated environment
source deactivate
goto:eof


:checkConda
echo "Checking conda version... "
if not conda --version 2> /dev/null; then
  errorExit "conda must be installed for this to work"
else
  printf " ..done!\n"
fi
goto:eof


:createEnv
if conda env list | grep "^$env_name\s" > /dev/null; then
  echo "Found environment: '$env_name'! Let's use it."
  source activate $env_name || errorExit "could not activate environment"
else
  echo "Creating python environment..."
  conda create --name $env_name --file $req_file || \
    errorExit "could not create environment"
  source activate $env_name
fi
goto:eof


:runNotebook
echo "Running notebook"
echo
jupyter-notebook --NotebookApp.file_to_run=$nb_file
goto:eof


call:init
call:checkConda
call:createEnv
call:runNotebook
