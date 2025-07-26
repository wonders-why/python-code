# pip is a package contianing all the files for your module "thats wht i heard i guess"
# apperently we can use pip module in commandline to download all the modulles offered by python as libraries

#i just downaloded the camelcase using it

# step one: move to the directly of your pip file in python directory
# step two: in that pip directory wriet the command install filename
# step three: enjoy

import camelcase

x = camelcase.CamelCase()
txt = 'hello world!'
print(x.hump(txt)) # this funtion coverts all the first alphabets to capital letters