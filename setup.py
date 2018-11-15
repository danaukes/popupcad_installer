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

import importlib

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
packages.append('idealab_tools')
packages.append('foldable_robotics')
packages.append('ezdxf')
packages.append('qt')
packages.append('tkinter')
packages.append("matplotlib.backends.backend_qt4agg")
packages.append("matplotlib.backends.backend_tkagg")

packages.append("scipy.integrate.vode")
packages.append("scipy.integrate.lsoda")
packages.append("scipy.sparse.csgraph._validation")
packages.append("OpenGL.platform.win32")
    
packages.append("sympy.assumptions.handlers")
packages.append("numpy")
packages.append("scipy")
packages.append("lxml")
packages.append("lxml._elementpath")

packages.append('pyqtgraph')
packages.append('OpenGL')
packages.append('meshio')

zip_includes = []
include_files = []

include_files.extend(st.include_entire_directory(popupcad.supportfiledir,'supportfiles'))
#include_files.extend(include_entire_directory(popupcad.documentation_directory ,'docs'))
include_files.extend(st.include_entire_directory('licenses','licenses'))

#include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/shapely/DLLs/geos_c.dll'),'geos_c.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/geos_c.dll'),'Library/bin/geos_c.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/geos.dll'),'Library/bin/geos.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/lib/geos_c.lib'),'Library/lib/geos_c.lib'))
include_files.append((st.fix(st.python_installed_directory,'Library/lib/geos.lib'),'Library/lib/geos.lib'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/geos_c.dll'),'Library/lib/geos_c.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/geos.dll'),'Library/lib/geos.dll'))
#include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
#include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libifcoremd.dll'),'libifcoremd.dll'))
#include_files.append((st.fix(st.python_installed_directory,'Lib/site-packages/numpy/core/libmmd.dll'),'libmmd.dll'))
include_files.append((st.fix(popupcad_parent_directory,'LICENSE'),'LICENSE'))

include_files.extend(st.include_entire_directory(st.fix(st.python_installed_directory,'Library/plugins/platforms'),''))
include_files.extend(st.include_entire_directory(st.fix(st.python_installed_directory,'Library/bin'),''))

zip_includes.extend(st.include_entire_directory(st.fix(st.python_installed_directory,"Lib/site-packages/OpenGL"),"OpenGL"))



includes = []
includes.append('pyqtgraph')
includes.append('pyqtgraph.debug')
includes.append('numpy.core._methods')
includes.append("scipy.sparse.csgraph._validation")

excludes = []
excludes.append('popupcad_gazebo')

excludes.append('gtk')
excludes.append('_gtkagg')
excludes.append('_tkagg')
excludes.append('bsddb')
excludes.append('curses')
excludes.append('pywin.debugger')
excludes.append('pywin.debugger.dbgcon')
excludes.append('pywin.dialogs')
excludes.append('tcl')
excludes.append('tk')
excludes.append('Tkconstants')
excludes.append('Tkinter')
excludes.append('babel')
excludes.append('notebook')
excludes.append('spyder')
excludes.append('ipython')
excludes.append('jupyter_client')
excludes.append('jupyter_core')


build_exe_options = {}
build_exe_options['packages']=packages
build_exe_options['includes']=includes
build_exe_options['excludes']=excludes
build_exe_options["include_files"]=include_files
build_exe_options["zip_includes"]=zip_includes
build_exe_options['include_msvcr']=True

bdist_msi_options = {'upgrade_code': popupcad.windows_uuid}


setup_options = {}
setup_options['build_exe']=build_exe_options
setup_options['bdist_msi']=bdist_msi_options

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


module = importlib.import_module('tcl')
p = list(module.__path__)[0]
os.environ['TCL_LIBRARY'] = p
os.environ['TK_LIBRARY'] = p

setup(**setup_arguments)        
