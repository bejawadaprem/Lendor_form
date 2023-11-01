from ._anvil_designer import Institutional_step_oneTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Institutional_step_one(Institutional_step_oneTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Lender_main_form')
    """This method is called when the button is clicked"""

  def button_2_show(self, **event_args):
    open_form('landingmodule.user_home.Lender_main_form.Institutional_step_one.Institutional_step_two')
    """This method is called when the Button is shown on the screen"""
    
    

