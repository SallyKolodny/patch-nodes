"""
mvc/PatchNodesController.py

The MVC "Controller" class.
"""

import os,sys

# Get the directory name where this program is installed
patch_nodes_mvc_dir = os.path.dirname(os.path.abspath(__file__))
# Add the "mvc" directory to the search path when trying to import modules
sys.path.append(patch_nodes_mvc_dir)
# Import the MVC classes
from mvc import PatchNodesModel as Model
from mvc import PatchNodesView as View

class PatchNodesController():

  def __init__(self):
    pass