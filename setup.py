## this file is used to create our application as a package
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    # this function will return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        print(requirements)
        requirements = [req.replace("\n","") for req in requirements]

        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
            print(requirements)
        
        

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'shubhangi jain',
    packages = find_packages(), ## this will find __init__.py file in all the folders and it will consider the folder as a package, and build it so we can import it as a package
    install_requires = get_requirements('requirements.txt')
)