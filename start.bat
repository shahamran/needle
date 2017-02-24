@echo off

call deactivate
call activate %~1
call jupyter-notebook --NotebookApp.file_to_run=%~2
call deactivate