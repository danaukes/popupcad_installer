# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes.
Email: danaukes<at>seas.harvard.edu.
Please see LICENSE.txt for full license.
"""
import popupcad
import sys
from cx_Freeze import setup, Executable
import os
from os.path import join,normpath,dirname
import update_installer

def fix(*args,**kwargs):
    return normpath(join(*args,**kwargs))
    
def include_entire_directory(source_dir,dest_dir):
    m = len(source_dir)
    include = [(source_dir, dest_dir)]
    for root, subfolders, files in os.walk(source_dir):
        for filename in files:
            source = fix(root, filename)
            dest = fix(dest_dir, root[m+1:], filename)
            include.append((source,dest))
    return include
    
popupcad_parent_directory = fix(popupcad.localpath,'../')

packages = []
packages.append('popupcad')
packages.append('dev_tools')
packages.append('popupcad_manufacturing_plugins')
packages.append('popupcad_deprecated')
packages.append('pypoly2tri')

packages.append("scipy.integrate.vode")
packages.append("scipy.integrate.lsoda")
packages.append("scipy.sparse.csgraph._validation")
packages.append("OpenGL.platform.win32")
packages.append("sympy.assumptions.handlers")
packages.append("numpy")
packages.append("scipy")
     
python_installed_directory = dirname(sys.executable)

include_files = []
include_files.append((fix(python_installed_directory,'Lib/site-packages/shapely/geos_c.dll'),'geos_c.dll'))
include_files.append((fix(python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
include_files.append((fix(python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
include_files.append((fix(python_installed_directory,'Lib/site-packages/numpy/core/libmmd.dll'),'libmmd.dll'))
include_files.append((fix(popupcad_parent_directory,'LICENSE'),'LICENSE'))
include_files.extend(include_entire_directory(popupcad.supportfiledir,'supportfiles'))
include_files.extend(include_entire_directory(popupcad.documentation_directory ,'docs'))
include_files.extend(include_entire_directory('licenses','licenses'))

zip_includes = include_entire_directory(fix(python_installed_directory,"Lib\\site-packages\\OpenGL"),"OpenGL")

includes = []
excludes = []

build_exe_options = {"include_msvcr":True,"include_files":include_files,"zip_includes": zip_includes,'packages':packages,'includes':includes,'excludes':excludes,'icon':popupcad.iconfile }
bdist_msi_options = {'upgrade_code': popupcad.windows_uuid}

setup_options = {}
setup_options['build_exe']=build_exe_options
setup_options['bdist_msi']=bdist_msi_options

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup_arguments = {}
setup_arguments['name'] = popupcad.program_name
setup_arguments['author'] = popupcad.author
setup_arguments['author_email'] = popupcad.author_email
setup_arguments['version'] = popupcad.version
setup_arguments['description'] = popupcad.description
setup_arguments['executables'] = []
setup_arguments['executables'].append(Executable(fix(popupcad_parent_directory,"popupcad.py"), base=base,shortcutName=popupcad.program_name,shortcutDir="ProgramMenuFolder"))
setup_arguments['options'] = setup_options

setup(**setup_arguments)        
update_installer.run()