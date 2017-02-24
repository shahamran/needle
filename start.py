#!/usr/bin/env python3

# imports
import subprocess
import argparse

# constants
ENV_NAME = 'needle'
REQ_FILE = 'requirements.txt'
NB_FILE = 'Aliens.ipynb'


def errorExit(msg):
    """Print a message and exit with an error code"""
    print(msg)
    exit(1)


def init():
    """Start with this"""
    pass


def checkConda():
    """Checks if conda is installed"""
    print('Checking conda version...', end=' ')
    version = subprocess.getoutput('conda --version')
    if version:
        print(version, '..done!')
    else:
        errorExit('conda must be installed for this to work')


def createEnv():
    """Creates the required conda environment if it doesn't exist"""
    envs = subprocess.getoutput('conda env list').split('\n')
    envs = [env.split()[0] for env in envs 
            if not env.startswith('#') and len(env) > 0]
    if ENV_NAME in envs:
        print('Found environment: "' + ENV_NAME + '"! Lets use it.')
    else:
        print('Creating python environment...')
        subprocess.call('conda create --name ' + ENV_NAME +
                        ' --file ' + REQ_FILE)


def runNotebook(windows=True):
    """Runs the jupyter notebook"""
    print('Running notebook...\n')
    if windows:
        try:
            subprocess.run(['start.bat', ENV_NAME, NB_FILE])
        except:
            runNotebook(windows=False)
    else:
        try:
            subprocess.run(['start.sh', ENV_NAME, NB_FILE])
        except:
            errorExit('error! could not run notebook')


def main():
    init()
    checkConda()
    createEnv()
    runNotebook()


if __name__ == '__main__':
    main()
