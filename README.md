# sa_popgrid
Code and process for conducting sensitivity analysis for the gridded population gravity model on a cluster

## Getting Started using `sa_popgrid` on a cluster

### Note
The following code was tested on THECUBE cluster courtesy of the Reed Research Group at Cornell University.  This cluster has 32 compute nodes with dual 8-core Intel E52680 CPUs @ 2.7 GHz with 128 GB of RAM running OpenHPC v1.3.8 with CentOS 7.6.

### STEP 1:  Installing GDAL
This code has a GDAL 2.2.3 dependency.  This was installed using the following using the default compiler `gcc 8.3.0`:

```shell script
# change directories into your libs dir; make on if it does not exist
cd ~/libs

# download GDAL
wget http://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.gz

# untar
tar xzf gdal-2.2.3.tar.gz
cd gdal-2.2.3

# compile from source
./configure --with-libkml
make

# install to a local path...I chose my home dir and the following commands assume that
export DESTDIR="$HOME" && make -j4 install

# add bin to path; if you do not have a bash_profile setup run...
vim ~/.bash_profile

# and add in the following or append to an existing PATH variable and libs variable
PATH=$PATH:$HOME/usr/local/bin
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/usr/local/lib

# save and exit vim and source your changes using
source ~/.bash_profile
```

Running `make` will take a while.  Once you have finished the process you can test the GDAL install by executing `gdalinfo` which should return:
```
Usage: gdalinfo [--help-general] [-json] [-mm] [-stats] [-hist] [-nogcp] [-nomd]
                [-norat] [-noct] [-nofl] [-checksum] [-proj4]
                [-listmdd] [-mdd domain|`all`]*
                [-sd subdataset] [-oo NAME=VALUE]* datasetname
FAILURE: No datasource specified.
```

### STEP 2:  Create a Python Virtual Environment
We want to use Python 3.6 so execute in your home directory:

```shell script
python3 -m venv pyenv
```

In this case `pyenv` is simply the name I have chosen for my virutal environemnt.

### STEP 3:  Install the `sa_popgrid` package and the Required Python Modules
First activate your Python virtual environment by running:
```shell script
source pyenv/bin/activate
```

Then install the `sa_popgrid` package from GitHub:
```shell script
pip install git+https://github.com/IMMM-SFA/sa_popgrid.git
```

Confirm that the package installed correctly by first entering a Python prompt:
```shell script
python
```
and then executing:
```python
import sa_popgrid
```
If no errors return then all is well.  Exit the Python prompt by excuting:
```python
exit()
```

### STEP 4:  Build the Latin Hypercube Sample and Problem Dictionary

```python
# This script generates a sample set of 1000 using LHS 
#
# To run:  
# 1.  Activate your Python virtual environment containing the `sa_popgrid` package
# 2.  Execute this script by running:  `python generate_lhs_sample_1000.py`

import sa_popgrid

# where to write the job script
output_job_script = '/home/fs02/pmr82_0001/spec994/projects/population/code/lhs_delta'

# run only one sample
sample_list = 1000

# directory to store the output files in
output_dir = '/home/fs02/pmr82_0001/spec994/projects/population/outputs/lhs'

# my Python virtual environemnt
venv_dir = '/home/fs02/pmr82_0001/spec994/pyenv'

# submit the SLURM job
sa_popgrid.run_lhs(output_job_script,
                    sample_list,
                    output_dir,
                    venv_dir,
                    alpha_urban_upper=2.0,
                    alpha_urban_lower=-2.0,
                    alpha_rural_upper=2.0,
                    alpha_rural_lower=-2.0,
                    beta_urban_upper=2.0,
                    beta_urban_lower=-0.5,
                    beta_rural_upper=2.0,
                    beta_rural_lower=-0.5,
                    kernel_density_lower=50000,
                    kernel_density_upper=100000,
                    walltime='00:10:00')
```

### STEP 5:  Run model batch runs for each sample

```python


```




