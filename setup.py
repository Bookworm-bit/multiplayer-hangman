import os
import main

with open('requirements.txt', 'r') as rqfile:
    installed_packages = str(os.system('pip freeze'))
    requirements = rqfile.readlines()
    for item in requirements:
        if item not in installed_packages:
            os.system('pip install ' + item)
        else:
            pass
os.system("cls" if os.name == "nt" else "clear")

exec(open('main.py').read())