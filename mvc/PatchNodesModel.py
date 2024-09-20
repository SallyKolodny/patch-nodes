"""
mvc/PatchNodesModel.py

The MVC "Model" class.
"""

import os

class PatchNodesModel():

  def __init__(self):
    """
    Constructor. Sets the per-user filename of the file used to store the list of managed hosts.
    """
    # hosts_dir is the directory where patch-nodes.py stores the list of managed hosts
    hosts_dir = os.path.expanduser('~') + "/.config"
    if not os.path.exists(hosts_dir):
      os.mkdir(hosts_dir)
    # self._hosts_file is the file where patch-nodes.py stores the list of managed hosts
    self._hosts_file = hosts_dir + "/patch-nodes-hosts.txt"
    # Get a list of managed hosts
    self._hosts = self.read_hosts_file()

  def add_host(self, host):
    """
    Add a new host to the list of managed hosts and write the new list to the managed hosts file.
    If the host already exists in the managed host list, then do nothing. 
    """
    pass

  def hosts(self):
    """
    Get method. Return the list of managed hosts.
    """
    return self._hosts

  def hosts_file(self):
    """
    Get method. Return the fully qualified filename that holds the list of managed hosts.
    """
    return self._hosts_file

  def read_hosts_file(self):
    """
    Get method. Read the list of managed hosts from the file that stores this list.
    """
    hosts_file = self.hosts_file()
    hosts_list = []
    # Check that the hosts_file exists
    if os.path.isfile(hosts_file):
      # Open the file
      with open(hosts_file) as file:
        # Step through the file contents, line by line
        for line in file:
          hosts_list.append(line.rstrip())
    return hosts_list

