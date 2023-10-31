from ._anvil_designer import Basic_fiveTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Basic_five(Basic_fiveTemplate):
  def __init__(self, name,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name=name

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_four')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    
    open_form('landingmodule.user_home.Basic_six')
    

    

