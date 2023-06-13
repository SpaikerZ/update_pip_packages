import os
import re

#make requiremants in pip.txt
os.system('pip freeze > pip.txt')

#open pip.txt and install every requirement
with open('pip.txt', 'r') as pip_list:
    while True:
        line = pip_list.readline()
        if not line:
            break
        line = line.strip()
        r = r'[a-zA-z0-9]{1,}(?=\=\=)'
        regex_string = re.findall(r, line)

        if len(regex_string) < 1:
            print('String is Wrong')
            print(f'Cant update {line}')
            continue
        print(regex_string[0])
        os.system(f'pip3 install --upgrade {regex_string[0]}')



