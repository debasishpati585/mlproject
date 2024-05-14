from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_reuirements(file_path:str)->List[str]:
    '''
    This function will return the list of reuirements
    '''
    reuirements=[]
    with open(file_path) as file_obj:
        reuirements=file_obj.readlines()
        reuirements=[req.replace("\n","") for req in reuirements]

        if HYPEN_E_DOT in reuirements:
            reuirements.remove(HYPEN_E_DOT)

    return reuirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Debasish',
    author_email='debasishpati585@gmail.com',
    packages=find_packages(),
    install_reuires=get_reuirements('reuirements.txt')
)