#### Building our application as a setup.py


from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


#Metadata information for the project
setup(
    name="mlproject",
    version="0.0.1",
    author="manthan",
    author_email = 'jmanthan6598@gmail.com',
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt')

)