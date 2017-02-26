#!/usr/bin/env python3
"""
A script to start the jupyter notebook with the correct environment.

If the required python (conda) environment does not exist, this script
creates it - and in this case the user should explicitly review and accept
the download and installation of the python packages (the user is prompted
to agree).
"""

# imports
import subprocess
import argparse
import os.path as path

# constants
ENV_NAME = 'needle'
REQ_FILE = 'requirements.txt'
NB_FILE = 'Aliens.ipynb'
SOURCE_DIR = '.'
START_CMD = 'start'

WIN = 'windows'
WIN_EXT = '.bat'
LIN = 'linux'
LIN_EXT = '.sh'


def error_exit(msg):
    """
    Print a message and exit with an error code (1).
    ``msg`` can be a string or an Error class instance (everything that
    implements the __str__ is ok though).
    This function does not return.
    """
    print(str(msg))
    exit(1)


def init(platform, env=None, source_dir=SOURCE_DIR):
    """Start with this"""
    global START_CMD
    global ENV_NAME
    global REQ_FILE
    global NB_FILE
    # check the platform and change the start command accordingly
    if platform == WIN:
        START_CMD += WIN_EXT
    elif platform == LIN:
        START_CMD += LIN_EXT
    else:
        error_exit('unsupported platform name: "' + platform + '"')
    # change the environment name if needed
    if env:
        ENV_NAME = env
    # get the correct file names (with the given source dir)
    START_CMD = path.join(source_dir, START_CMD)
    REQ_FILE = path.join(source_dir, REQ_FILE)
    NB_FILE = path.join(source_dir, NB_FILE)


def check_conda():
    """Checks if conda is installed"""
    print('Checking conda version...', end=' ')
    status, version = subprocess.getstatusoutput('conda --version')
    if status == 0:
        print(version, '..done!')
    else:
        error_exit(version + '\nconda must be installed for this to work')


def create_env():
    """Creates the required conda environment if it doesn't exist"""
    envs = subprocess.getoutput('conda env list').split('\n')
    envs = [env.split()[0] for env in envs
            if not env.startswith('#') and len(env) > 0]
    if ENV_NAME in envs:
        print('Found environment: "' + ENV_NAME + '"! Lets use it.')
    else:
        print('Creating python environment...')
        try:
            subprocess.run('conda create --name ' + ENV_NAME +
                           ' --file ' + REQ_FILE).check_returncode()
        except subprocess.CalledProcessError as e:
            error_exit(e)


def run_notebook():
    """Runs the jupyter notebook"""
    print('Running notebook...')
    try:
        subprocess.run([START_CMD, ENV_NAME, NB_FILE]).check_returncode()
    except subprocess.CalledProcessError as e:
        error_exit(e)
    except:
        error_exit('could not run notebook')


def parseArgs():
    """Parses program's arguments and return the platform (windows/linux)"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('platform', type=str, choices=[WIN, LIN],
                        help='the platform on which the script runs')
    parser.add_argument('-e', '--env', type=str, default=ENV_NAME,
                        help='relevant conda environment name')
    parser.add_argument('-d', '--directory', type=str, default=SOURCE_DIR,
                        metavar='root_dir',
                        help="project's root directory")
    return parser.parse_args()


def main():
    args = parseArgs()
    init(platform=args.platform, env=args.env, source_dir=args.directory)
    check_conda()
    create_env()
    run_notebook()


if __name__ == '__main__':
    main()
