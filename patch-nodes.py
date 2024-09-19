#!/usr/bin/python3

import urwid
from urwid import LineBox, Text, Pile, Columns, CheckBox, Button, AttrMap

SALLY = 'sally.osoyalce.com'
KERMIT = 'kermit.osoyalce.com'
PHOEBE = 'phoebe.osoyalce.com'
MAIA = 'maia.osoyalce.com'
BRAT = 'brat.osoyalce.com'

# Catchall function to handle user input
def parse_input(key: str) -> None:

  if key in ['q', 'Q']:
    # If user enters a "Q" exit the main loop
    raise urwid.ExitMainLoop()

# Callback function for the checkbox widgets. Used to register whether a host
# has been selected for patching or not.
patch_candidates = {
  SALLY: True,
  KERMIT: True,
  PHOEBE: True,
  MAIA: True,
  BRAT: True
}
def checkbox_callback(checkbox, new_state):
  if new_state:
    patch_candidates[checkbox.label] = True
  else:
    patch_candidates[checkbox.label] = False

# Callback function for the cancel button. When this button is clicked the application
# will exit.
def cancel_callback(button):
  raise urwid.ExitMainLoop()

# Callback function for the okay button. When this button is clicked the application
# will SSH to each of the hosts that have been selected and execute the 'apt' commands
# used to patch the system.
def okay_callback(button):
  for host in patch_candidates.keys():
    if patch_candidates[host]:
      print(f"Patching {host}")
    else:
      print(f"Skipping {host}")


# Define a palette where 
#  - The first element of the tuple is a lable for the entry
#  - The second element is the foreground
#  - The third element is the background
palette = [
  ('header', 'light green', 'black'),
  ('default', 'light green', 'black'),
]

# Title text
title_widget = LineBox(Text(' PATCH NODES '))
title_map = AttrMap(title_widget, 'header')

# Selection help text
select_help_widget = Text('Select which hosts you want to patch:\n')
select_help_map = AttrMap(select_help_widget, 'default')

# Host selection
sally_widget = CheckBox(SALLY, state=True)
urwid.connect_signal(sally_widget, 'change', checkbox_callback)
sally_map = AttrMap(sally_widget, 'default')
kermit_widget = CheckBox(KERMIT, state=True)
urwid.connect_signal(kermit_widget, 'change', checkbox_callback)
kermit_map = AttrMap(kermit_widget, 'default')
phoebe_widget = CheckBox(PHOEBE, state=True)
urwid.connect_signal(phoebe_widget, 'change', checkbox_callback)
phoebe_map = AttrMap(phoebe_widget, 'default')
maia_widget = CheckBox(MAIA, state=True)
urwid.connect_signal(maia_widget, 'change', checkbox_callback)
maia_map = AttrMap(maia_widget, 'default')
brat_widget = CheckBox(BRAT, state=True)
urwid.connect_signal(brat_widget, 'change', checkbox_callback)
brat_map = AttrMap(brat_widget, 'default')

host_map_list = [
  select_help_map,
  sally_map,
  kermit_map,
  phoebe_map,
  maia_map,
  brat_map
]

hosts_map = AttrMap(LineBox(Pile(host_map_list)), 'default')

# Okay and cancel buttons
okay_widget = Button("OK")
urwid.connect_signal(okay_widget, 'click', okay_callback)
okay_map = AttrMap(okay_widget, 'header')
cancel_widget = Button("Cancel")
urwid.connect_signal(cancel_widget, 'click', cancel_callback)
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
loop = urwid.MainLoop(fill, palette, unhandled_input=parse_input)

# Run the loop
loop.run()

