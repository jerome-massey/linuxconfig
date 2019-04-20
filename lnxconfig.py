#!/usr/bin/python3

import subprocess
import yaml

def apt_up():
    pass



def add_repo(conf):
    for key, cmd in conf:
        subprocess.run(cmd, shell=True)



def install_app():
    pass



def main():
    with open('./test.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.Loader)
    add_repo(config)

    

if __name__ == '__main__':
    main()
