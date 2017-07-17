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
#import glob
import shutil

# Remove the existing folders folder
shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)

import idealab_tools.setup_tools as st
    
popupcad_parent_directory = st.fix(popupcad.localpath,'../')

packages = []
packages.append('popupcad')
packages.append('dev_tools')
packages.append('popupcad_manufacturing_plugins')
packages.append('popupcad_deprecated')
packages.append('pypoly2tri')
packages.append('qt')
packages.append('tkinter')
packages.append("matplotlib.backends.backend_qt4agg")
packages.append("matplotlib.backends.backend_tkagg")

#if sys.platform=='win32':
packages.append("scipy.integrate.vode")
packages.append("scipy.integrate.lsoda")
#if sys.platform=='darwin':
#    packages.append('scipy.special._ufuncs_cxx')
packages.append("scipy.sparse.csgraph._validation")
if sys.platform=='win32':
    packages.append("OpenGL.platform.win32")
elif sys.platform =='darwin':
    packages.append("OpenGL.platform.darwin")
    
packages.append("sympy.assumptions.handlers")
packages.append("numpy")
packages.append("scipy")
packages.append("lxml")
packages.append("lxml._elementpath")

zip_includes = []
include_files = []

include_files.extend(st.include_entire_directory(popupcad.supportfiledir,'supportfiles'))
#include_files.extend(include_entire_directory(popupcad.documentation_directory ,'docs'))
include_files.extend(st.include_entire_directory('licenses','licenses'))

if sys.platform=='darwin':
    pass
elif sys.platform=='linux':
    pass
elif sys.platform=='win32':
    include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/shapely/DLLs/geos_c.dll'),'geos_c.dll'))
    include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
    include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
    include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libmmd.dll'),'libmmd.dll'))
    include_files.append((st.fix(popupcad_parent_directory,'LICENSE'),'LICENSE'))

    zip_includes.extend(st.include_entire_directory(st.fix(st.python_installed_directory,"Lib/site-packages/OpenGL"),"OpenGL"))

includes = []
excludes = ['popupcad_gazebo']

build_exe_options = {}
build_exe_options['include_msvcr']=True
build_exe_options["include_files"]=include_files
build_exe_options["zip_includes"]=zip_includes
build_exe_options['packages']=packages
build_exe_options['includes']=includes
build_exe_options['excludes']=excludes
build_exe_options['icon']=popupcad.iconfile

bdist_mac_options = {}
bdist_mac_options['iconfile'] = popupcad.iconfile 
#bdist_mac_options['qt_menu_nib'] = 
bdist_mac_options['bundle_name'] = 'popupcad_bundle'
#bdist_mac_options['include_frameworks'] = []
#bdist_mac_options['codesign_identity'] = 
#bdist_mac_options['codesign_entitlements'] = 
#bdist_mac_options['codesign_deep'] = 
#bdist_mac_options['codesign_resource_rules'] = 

bdist_msi_options = {'upgrade_code': popupcad.windows_uuid}

bdist_dmg_options = {}
bdist_dmg_options['volume_label']='popupcad_volume'
#bdist_dmg_options['applications-shortcut']=True
#bdist_dmg_options['']=

setup_options = {}
setup_options['build_exe']=build_exe_options
setup_options['bdist_msi']=bdist_msi_options
setup_options['bdist_mac']=bdist_mac_options
setup_options['bdist_dmg']=bdist_dmg_options

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
setup_arguments['executables'].append(Executable(st.fix(popupcad_parent_directory,"popupcad.py"), base=base,shortcutName=popupcad.program_name,shortcutDir="ProgramMenuFolder"))
setup_arguments['options'] = setup_options

setup(**setup_arguments)        
