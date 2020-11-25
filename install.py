import sys
import subprocess

# add more packages to this list to download
listOfPackages = ['PyPI', 'PySimpleGUI', 'matplotlib', 'faker', 'psycopg2', 'psycopg2-binary']
for i in listOfPackages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
    reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    print(installed_packages)
