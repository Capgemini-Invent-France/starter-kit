# How to create a virtual environement 

Python virtual environment is basically a separate folder that creates an independent set of installed packages, Python binaries in its own directory, that isolates any other installation of Python on your computer.
Python virtual environment is used to prevent interfering with the behavior of other applications. Therefore it will prevent packages or Python version conflicts when working with different projects that are running on the same system. It will avoid conflicts.

## venv 

Creating a venv is done by executing the following command : 
```
python -m venv /path/to/new/virtual/environment
```

To launch the venv with Windows and PowerShell run the following command : 
```
<venv>\Scripts\Activate.ps1
```

## conda

With conda, you can create, export, list, remove, and update environments that have different versions of Python and/or packages installed in them. You can also share an environment file.

Firtly you need to install conda. 
Then you can use the terminal to create an environement with the following steps : 

1. To create an environement :
```
conda create --name name_of_your_env

2. When conda asks you to proceed, type y:
```
proceed ([y]/n)?
```
This creates the myenv environment in /envs/. No packages will be installed in this environment.

3. To create an environment with a specific version of Python:
```
conda create -n myenv python=3.9
```

4. You can then install all the package you want with this classic command line : 
```
conda install -n name_of_your_env pandas
conda install -n name_of_your_env torch=11.1.3
```

5. To create an environment with a specific version of Python and multiple packages: 
```
conda create -n name_of_your_env python=3.9 scipy=0.17.3 
```

## poetry
Poetry makes project environment isolation one of its core features. What this means is that it will always work isolated from your global Python installation. 
By default, Poetry will try to use the Python version used during Poetry’s installation to create the virtual environment for the current project.

Once you install poetry with pip, you can create a poetry virtual environement following those steps in your terminal : 

1. Create or initilaize poetry inside your current project/package directory : 
```
poetry init
```
The init command will ‘initialize’ an existing directory and create a pyproject.toml which will manage your project and its dependencies.

2. You can add dependencies to your project/project : 
```
poetry add pandas==1.8.5
```
The add command adds dependencies to pyproject.toml and poetry.lock, and installs them.

3. You can also create a poetry environement from an existing requirement.txt using :
```
poetry add $( cat requirements.txt )
```

4. You can also install a poetry env from existing project/package dependencies. If you're using an already created project that has either poetry.lock or pyproject.toml files, you can install those dependencies to the virtual environment: 
``` 
poetry install
```
The install command read pyproject.toml or poetry.lock file and installs all listed dependencies.

5. You can now enter in your poetry environement using this command :
```
poetry shell
```
and exit it with this command : 
```
exit
```


