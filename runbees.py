import setup
import bees
import json


bees.up(1,'default','us-east-1d','ami-ff17fb96','t1.micro','ubuntu','MyFirstKeyPair','subnet-0ca46926')
bees.attack('http://www.dublintrading.com/',1,1)
bees.down()
