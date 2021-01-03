# Virtual Env(ironment)

"""
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating
isolated python virtual environments for them.
"""

# Creation of a Virtual env :-
"""
Desktop screen or any background -> Press Ctrl+Shift+N to make a new folder or simply right click, choose "New Folder" 
option and New Folder will be created -> enter the new folder -> Hold shift and right click -> select 'Open with terminal'
to open a command prompt redirected from the new folder -> Type command "pip install virtualenv" if the package of 
virtualenv is not installed otherwise it is not needed -> after installation completes, type "Virtualenv" and after giving
a space provide any name for the environment -> your environment will be created.     
"""

# Unknown things to be known about Virtual Environment :-
"""
If you get an error about folder deny , you must log into and by the option "run as administrator". Type "set-execution 
policy remote-signed. Type 'Y' for yes then to get rid off the error.
"""

"""
The newly created environment can be called as a "baby of python interpreter" or "small command prompt". This environment
will be completely different than the actual base python interpreter. It will have different modules, packages, package 
versions, etc. than the base interpreter. It is because you are in virtualenv and the interpreter in which packages are
installed are outside the environment.
"""

# commands to be used :-
"""
pip install package -> download new modules.
pip uninstall package -> uninstall packages.
import package -> imports the package for usage of functions if the specified package is already downloaded.
"""

# commands for activating Virtualenv :-
"""
.\ "name of new folder" \ Scripts \ activate.
"""

# Deactivating VirtualEnv :-
"""
After you enter into the virtualEnv, type Deactivate to deactivate the Virtualenv and return to the main command prompt.
"""

# requirement.txt :-
"""
You can create a "requirements.txt" which will keep an update of modules and it's versions installed in the new VirtualEnv
in a text file below the folder of created VirtualEnv. This type of text files are useful for a person who wants to download 
exact packages like yours. 
"""

# Creation of requirement.txt :-
"""
This type of text files do not exist but should be created manually. You need to type "pip freeze > requirement.txt". After 
you execute this command, a text file named requirements will be created automatically in the new folder which will have
details about modules installed in the Env along with their versions.  
"""

# Installing accurate versioned modules :-
"""
You can install a module by specifying their versions.
Use command "pip install scipy == 1.4.4 (Example)"
"""

# Installing all packages at once :-
"""
Use requirement.txt to download all modules at once. You can either delete all packages and then use requirement.txt or 
download them again. 
Use "pip install -r .\ requirement.txt" to download all packages at once.
"""

# copying VirtualEnv to base interpreter :-
"""
As said, VirtualEnv is different than base interpreter. Being a new environment, VirtualEnv does not have modules and all 
functions as same as Base Interpreter. But You can copy the all content of the base to VirtualEnv by using a simple command 
Use "VirtualEnv --system-site-package "VirtualEnv name" "  
"""

"""
Now you can further, Use VirtualEnv with better ways. 
"""