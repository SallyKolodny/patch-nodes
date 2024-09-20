#!/usr/bin/python3

import urwid
from urwid import LineBox, Text, Pile, Columns, CheckBox, Button, AttrMap, Divider
import sys

class PatchNodesUI():

  def __init__(self):
    """
    Constructor.
    """
    self._SALLY = 'sally.osoyalce.com'
    self._KERMIT = 'kermit.osoyalce.com'
    self._PHOEBE = 'phoebe.osoyalce.com'
    self._MAIA = 'maia.osoyalce.com'
    self._BRAT = 'brat.osoyalce.com'

    self._patch_candidates = {
      self._SALLY: True,
      self._KERMIT: True,
      self._PHOEBE: True,
      self._MAIA: True,
      self._BRAT: True
    }

    # Define a palette where 
    #  - The first element of the tuple is a lable for the entry
    #  - The second element is the foreground
    #  - The third element is the background
    self._palette = [
      ('header', 'light green', 'black'),
      ('default', 'light green', 'black'),
    ]

  def cancel_callback(self, button):
    """
    Callback function for the cancel button. When this button is clicked the 
    application will exit.
    """
    raise urwid.ExitMainLoop()

  def checkbox_callback(self, host_widget, new_state):
    """
    Callback function for the checkbox widgets. Used to register whether a host
    has been selected for patching or not.
    """
    host = host_widget.get_label()
    patch_candidates = self.patch_candidates()
    if new_state:
      patch_candidates[host] = True
    else:
      patch_candidates[host] = False
    self.patch_candidates(patch_candidates)

  def okay_callback(self, button):
    """
    Callback function for the okay button. When this button is clicked the application
    will SSH to each of the hosts that have been selected and execute the 'apt' commands
    used to patch the system.
    """
    patch_candidates = self.patch_candidates()
    for host in patch_candidates.keys():
      if patch_candidates[host]:
        print(f"Patching {host}")
      else:
        print(f"Skipping {host}")

  def launch_ui(self):
    """
    Actually render the UI.
    """
    # Title text
    title_widget = LineBox(Text(' PATCH NODES '))
    title_map = AttrMap(title_widget, 'header')

    # Selection help text
    select_help_widget = Text('Select which hosts you want to patch:\n')
    select_help_map = AttrMap(select_help_widget, 'default')

    # Host selection checkboxes
    sally_widget = CheckBox(self._SALLY, state=True)
    urwid.connect_signal(sally_widget, 'change', self.checkbox_callback)
    sally_map = AttrMap(sally_widget, 'default')
    kermit_widget = CheckBox(self._KERMIT, state=True)
    urwid.connect_signal(kermit_widget, 'change', self.checkbox_callback)
    kermit_map = AttrMap(kermit_widget, 'default')
    phoebe_widget = CheckBox(self._PHOEBE, state=True)
    urwid.connect_signal(phoebe_widget, 'change', self.checkbox_callback)
    phoebe_map = AttrMap(phoebe_widget, 'default')
    maia_widget = CheckBox(self._MAIA, state=True)
    urwid.connect_signal(maia_widget, 'change', self.checkbox_callback)
    maia_map = AttrMap(maia_widget, 'default')
    brat_widget = CheckBox(self._BRAT, state=True)
    urwid.connect_signal(brat_widget, 'change', self.checkbox_callback)
    brat_map = AttrMap(brat_widget, 'default')

    host_map_list = [
      select_help_map,
      sally_map,
      kermit_map,
      phoebe_map,
      maia_map,
      brat_map
    ]

    # Add 15 lines after the host selection checkboxes with this widget
    padding_15 = Divider(' ', 15)
    host_map_list.append(padding_15)

    hosts_map = AttrMap(LineBox(Pile(host_map_list)), 'default')

    # Okay button
    okay_widget = Button("OK")
    urwid.connect_signal(okay_widget, 'click', self.okay_callback)
    okay_map = AttrMap(okay_widget, 'header')

    # Cancel button
    cancel_widget = Button("Cancel")
    urwid.connect_signal(cancel_widget, 'click', self.cancel_callback)
    cancel_map = AttrMap(cancel_widget, 'header')
    buttons_list = Columns([(6, okay_map), (10, cancel_map)], dividechars = 2)
    buttons_map = AttrMap(LineBox(AttrMap(buttons_list, 'header')), 'header')

    widget_list = [
      title_map,
      hosts_map,
      buttons_map
    ]

    # Assemble the widgets
    screen = Pile(widget_list)

    # Fill the screen
    #  - Align the widget at the top of the screen
    fill = urwid.Filler(screen, 'top')

    # Setup the loop
    palette = self.palette()
    loop = urwid.MainLoop(fill, palette, unhandled_input=self.parse_input)

    # Run the loop
    loop.run()

  def palette(self):
    """
    Get method.
    """
    return self._palette

  def patch_candidates(self, patch_candidates=None):
    """
    Get and set method.
    """
    if patch_candidates:
      self._patch_candidates = patch_candidates
    return self._patch_candidates

  def parse_input(self, key: str) -> None:
    """
    Catchall function to handle user input.
    """
    if key in ['q', 'Q']:
      # If user enters a "Q" exit the main loop
      raise urwid.ExitMainLoop()

if __name__ == '__main__':
  patch_app = PatchNodesUI()
  patch_app.launch_ui()