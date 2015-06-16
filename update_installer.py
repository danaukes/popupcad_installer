# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:18:42 2015

@author: danaukes
"""

import glob
import os
import putfiles

local_directory = 'dist'

html_template = \
'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML+RDFa 1.1//EN">
<html>
<head>
<meta http-equiv="refresh" content="0; url={address}" />
</head>
<body lang=EN-US link=blue vlink=purple>
<div >
<p>Please visit <a href="{address}">{address}</a></p>
</div>
</body>
</html>'''

def build_download_redirect(address,local_path):
    redirect_filename = os.path.join(local_path,'download_link.html')
    with open(redirect_filename,'w') as f:
        f.writelines(html_template.format(address=address))
    return redirect_filename

def run():
    files = glob.glob(local_directory+'\\*.msi')
    basenames = sorted([os.path.basename(file) for file in files])
    print(basenames)
    
    installer_basename = basenames[-1]
    installer_filename = os.path.normpath(os.path.join(local_directory,installer_basename))
    current_filename = os.path.normpath(os.path.join(local_directory,'current'))
    with open(current_filename,'w') as f:
        f.write(installer_basename)
    
    redirect_filename = build_download_redirect('http://www.popupcad.org/downloads/'+installer_basename,local_directory)
    
    files = [installer_filename,current_filename,redirect_filename]
    import yaml
    try:
        with open('putinfo.yaml','r') as f:
            putinfo = yaml.load(f)  
    except FileNotFoundError:
        putinfo = putfiles.PutInfo('','','','')

    putinfo = putfiles.putfiles(putinfo,files)

    with open('putinfo.yaml','w') as f:
        putinfo = yaml.dump(putinfo,f)  
    
#    return putinfo


if __name__=='__main__':
    newputinfo = run()