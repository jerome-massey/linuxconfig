#!/usr/bin/python3

import subprocess
import argparse
import yaml

def apt_up(option):
    if option == 'update':
        subprocess.run('sudo apt update', shell=True)
    elif option == 'upgrade':
        subprocess.run('sudo apt update && sudo apt upgrade -y', shell=True)
    else:
        subprocess.run('sudo apt update', shell=True)



def add_repo_cli(conf):
    for key, cmd in conf['addrepocli'].items():
        if 'app' in key:
           subprocess.run(f'sudo apt --assume-yes install {cmd}', shell=True) 
        else:
            subprocess.run(cmd, shell=True)
    apt_up('update')

    
    
def add_repo_gui(conf):
    for key, cmd in conf['addrepogui'].items():
        if 'app' in key:
           subprocess.run(f'sudo apt --assume-yes install {cmd}', shell=True) 
        else:
            subprocess.run(cmd, shell=True)
    apt_up('update')



def install_cli(conf):
    for key, cmd in conf['addappscli'].items():
        subprocess.run(f'sudo apt --assume-yes install {cmd}', shell=True)
        


def install_gui(conf):
    for key, cmd in conf['addappsgui'].items():
        subprocess.run(f'sudo apt --assume-yes install {cmd}', shell=True)
        
        

def commands_cli(conf):
    for key, cmd in conf['commandscli'].items():
        subprocess.run(cmd, shell=True)
        


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gui', default='no' ,help='Do you have a GUI? [yes or no]?')
    args = parser.parse_args()
    with open('./test.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.Loader)
    apt_up('upgrade')
    if args.gui == 'no':
        add_repo_cli(config)
        install_cli(config)
        commands_cli(config)
    elif args.gui == 'yes':
        add_repo_cli(config)
        add_repo_gui(config)
        install_cli(config)
        install_gui(config)
        commands_cli(config)
    else:
        add_repo_cli(config)
        install_cli(config)
        commands_cli(config)



if __name__ == '__main__':
    main()
