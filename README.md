# lambda-function-for-oracle-db
> Lambda function to connect and query oracle RDS database

This article will explain how to create a AWS Lambda function to connect to Oracle (RDS) database and query data. 

Since lambda is based on linux environment its recommended to create this function on linux host. If you are using windows machine make use to WSL or VM or Docker.

**Pre-requiest**

1. Python 3.8
2. [cx_Oracle python module](https://pypi.org/project/cx-Oracle/#files)
3. [Oracle instant client](https://www.oracle.com/in/database/technologies/instant-client/linux-x86-64-downloads.html)
4. [libiao package](https://pkgs.org/download/libaio)

👆 Download and keep it ready

#### Step 1
Check the python version installed, AWS Lambda supports Python version 3.6/3.7/3.8 at the time of this article written.

```sh
$ python --version
Python 3.8.11
```

Step 2
Install pip

```sh
$ sudo apt install python3-pip

$ pip3 --version
pip 21.1.3 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

Step 3
Install Virtual Python Environment builder

```sh
$ pip3 install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.6.0-py2.py3-none-any.whl (5.3 MB)
     |████████████████████████████████| 5.3 MB 2.5 MB/s
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.2-py2.py3-none-any.whl (338 kB)
     |████████████████████████████████| 338 kB 4.4 MB/s
Collecting backports.entry-points-selectable>=1.0.4
  Downloading backports.entry_points_selectable-1.1.0-py2.py3-none-any.whl (6.2 kB)
Collecting filelock<4,>=3.0.0
  Downloading filelock-3.0.12-py3-none-any.whl (7.6 kB)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.0.2-py2.py3-none-any.whl (10 kB)
Collecting six<2,>=1.9.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, platformdirs, filelock, distlib, backports.entry-points-selectable, virtualenv
Successfully installed backports.entry-points-selectable-1.1.0 distlib-0.3.2 filelock-3.0.12 platformdirs-2.0.2 six-1.16.0 virtualenv-20.6.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv      
/ # 
```
Step 4
Create virtual environment `oralmdfn`
```sh
$ virtualenv oralmdfn
created virtual environment CPython3.8.11.final.0-64 in 688ms
  creator CPython3Posix(dest=/oralmdfn, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: pip==21.1.3, setuptools==57.1.0, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```
Step 5
Activate virtual environment
```sh
$ source oralmdfn/bin/activate
(oralmdfn) $ 

# you will see the virtual environment name in () if activated 
```
Step 6
Install cx_Oracle module vai pip
Make sure you have downloaded the right version of cx_Oracle module. In this artical I use python 3.8 so i have downloaded `cx_Oracle-8.2.1-cp38-cp38-manylinux1_x86_64.whl` (👈cp38 is for python 3.8)

```

```