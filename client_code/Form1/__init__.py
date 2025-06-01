from ._anvil_designer import Form1Template
from anvil import *


from anvil.js.window import jQuery
from anvil.js import get_dom_node
from datetime import datetime 
import base64
import json


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    dashboardprofile = jQuery("<iframe>", {
      "id": "dashbaordsample",
      "style": """
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        min-height: 100vh;
        border: none;
        overflow: auto;
    """
    }).attr("src", "_/theme/taxpro.html")
    get_dom_node(self.flowmain).innerHTML = ""
    dashboardprofile.appendTo(get_dom_node(self.flowmain))