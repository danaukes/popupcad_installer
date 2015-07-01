# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:18:42 2015

@author: danaukes
"""

import glob
import os
import putfiles

local_directory = 'dist'

def run():
    files = glob.glob(os.path.normpath(os.path.join(local_directory,'*.msi')))
    basenames = sorted([os.path.basename(file) for file in files])
    
    installer_basename = basenames[-1]
    installer_filename = os.path.normpath(os.path.join(local_directory,installer_basename))

    files = [installer_filename]

    import yaml
    try:
        with open('putinfo.yaml','r') as f:
            putinfo = yaml.load(f)  
    except FileNotFoundError:
        putinfo = putfiles.PutInfo('','','','')

    putinfo = putfiles.putfiles(putinfo,files)

    with open('putinfo.yaml','w') as f:
        putinfo = yaml.dump(putinfo,f)  
    
if __name__=='__main__':
    run()