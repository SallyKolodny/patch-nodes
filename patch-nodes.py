#!/usr/bin/python3
"""
The "main" Patch Nodes program.

This application is used to patch multiple systems from a single application. 
It is an implementation of the "Model, View, Controller" (MVC) software design pattern.
"""
import os, sys

# Get the directory name where this program is installed
patch_nodes_dir = os.path.dirname(os.path.abspath(__file__))
# Add the "mvc" directory to the search path when trying to import modules
sys.path.append(patch_nodes_dir + "/mvc")
# Import the MVC classes
from mvc import PatchNodesModel as Model
from mvc import PatchNodesView as View
from mvc import PatchNodesController as Controller


