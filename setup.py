from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    from requirements.txt file
    '''

    # Initializing blank requirements list
    requirements = []

    # Opening the file.
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        # Remove e_dot if present in requirements.txt
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'ml-project-gem_price_prediction-regression',
    version = '0.0.1',
    author = 'Ajwar CK',
    author_email= 'ajwar.trn@outlook.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)