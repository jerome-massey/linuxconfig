#!/usr/bin/python3

import yaml
import pprint

with open('./test.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.Loader)
    pprint.pprint(config)
    #pprint.pprint(config['addrepo'].items())
    
    

    
