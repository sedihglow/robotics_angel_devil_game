import argparse
import socket
import time
import yaml


from hexapod import Hexapod_12DOF
 
my_hexapod = None
    
# open config file
f= open('config_12DOF.yaml')
my_config = yaml.load(f)
my_hexapod = Hexapod_12DOF(my_config)

# Drop then raise
my_hexapod.reset()

my_hexapod.rotate(5)
"""
my_hexapod.reset()

my_hexapod.rotate(5,Left=true)

my_hexapod.reset()

my_hexapod.step(5)

my_hexapod.reset()
"""







