# A Needle in a Data Haystack - Final Project
## By: Matan Cohen, Nir Schipper and Ran Shaham
We chose to write our project as a [Jupyter Notebook](https://jupyter.org). 
This allows us to write nicely presented code and use interactive widgets to explore the data.

### Running Interactively
1. Fetch the project's code using one of the following methods:
  - Clone it:  
    `git clone https://github.com/shahamran/needle.git`
  - Download it using [this link](https://github.com/shahamran/needle/archive/master.zip)

2. Download and install [Miniconda](https://conda.io/miniconda.html) or [Anaconda](https://www.continuum.io/downloads)

3. Now, run the notebook:

#### Automatically
1. Open a terminal (command prompt in Windows), and `cd` to the project's root directory. E.g. `cd C:\Users\John\Documents\needle`
2. Run `python start.py <os>` where `<os>` is `windows` or `linux`, depending on your OS.

#### Manually

1. Open a terminal (command prompt in Windows), and `cd` to the project's root directory. E.g. `cd C:\Users\John\Documents\needle`
2. Create the python environment needed to run this project:  
   `conda create --name needle --file requirements.txt`  
   This may take some time
3. Linux: `source activate needle` -- Windows: `activate needle`
4. Run `jupyter notebook`, and click the `Aliends.ipynb` file in the opened browser window
5. When finished, run `deactivate` (or `source deactivate` on linux)

##### FAQ
- __`conda` commands exit with an error__: Try re-installing conda locally - i.e. select 'Just for me' in the installation wizrd. This may solve permission errors.

### Static version
Visit the [Github rendering of the notebook](/Aliens.ipynb).
