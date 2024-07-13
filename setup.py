# responsible in creating my machine learning application as a package and can be able to deploy in Pypi

from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Gurram Yogit',
    author_email = 'yogit.gurram@gmail.com',
    packages = find_packages(), ## find packages sees in how many folders we have __init__.py , it will directly consider this src as package itself
    install_requires = get_requirements('requirements.txt'),


)
# meta data information about the entire project
# -e . is used to specify an "editable" installation of a package. This is particularly relevant when you are developing a package or managing dependencies in a development environment.