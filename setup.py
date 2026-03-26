from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This fucntion returns list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]##when we go to next line \n is also read so we remove that

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Sanskar',
    author_email='sanskarpetkar76@gmail.com',
    packages=find_packages(),##it sees __init__ file in folder if its there it tries to build it as package
    install_requires=get_requirements('requirements.txt')
)

##-e. in requiremnts.txt file is used to trugger setup.py