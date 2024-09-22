"""
mvc/PatchNodesModel.py

The MVC "Model" class.
"""

import os
import sqlite3

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
    self._db_file = hosts_dir + "/patch-nodes-hosts.db"
    self._con = None
    self._cur = None
    self.init_db()

  def __del__(self):
    """
    Destructor. Closes the sqlite3 database 
    """
    if self._con is not None:
      con = self.con()
      con.close()

  def con(self):
    """
    Get method. Return a sqlite3 database connection object.
    """
    if not self._con:
      db_file = self.db_file()
      self._con = sqlite3.connect(db_file)
    return self._con
  
  def cur(self):
    """
    Get method. Return a sqlite3 database cursor object.
    """
    if not self._cur:
      con = self.con()
      self._cur = con.cursor()
    return self._cur
    
  def add_host(self, host, category, description):
    """
    Add a new host to the db. If the host exists already, return an error string otherwise return
    True. It is the responsibility of the MVC Controller to check and deal with these two cases.
    """
    cur = self.cur()
    new_row = [(host, category, description)]
    if self.host_exists(host):
      return "ERROR: Duplicate hostname"
    with self.con() as con:
      cur.execute("INSERT INTO host VALUES(?, ?, ?)", new_row)
      con.commit()
    return True

  def get_hosts(self):
    """
    Get method. Return the list of managed hosts.
    """
    pass
  
  def db_file(self):
    """
    Get method. Return the fully qualified file path to the file containing the sqlite3 database.
    """
    return self._db_file
  
  def host_exists(self, host):
    """
    Check if a host exists in the hosts table.
    """
    cur = self.cur()
    res = cur.execute("SELECT host FROM host WHERE host=?", (host))
    if res.fetchone() is None:
      return True
    else:
      return False

  def init_db(self):
    """
    Initialize the sqlite3 database. Create the "hosts" table if it doesn't exist.
    """
    cur = self.cur()
    res = cur.execute("SELECT name from sqlite_master WHERE name='host'")
    if not res:
      with self.con() as con:
        cur.execute("CREATE TABLE host(host TEXT, category TEXT , description TEXT, patch INTEGER)")
        cur.execute("CREATE TABLE category(category TEXT)")
        categories = [('Dev'), ('QA'), ('Prod')]
        cur.executemany("INSERT INTO category VALUES(?)", categories)
        con.commit()
