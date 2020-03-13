"""Generate a Tk from upon a Gui schema.

A GUI schema is a JSON-Schema dictionnary,
with tags require and existifs added to declare explicit cyclic depenencies
"""
from tkinter import Tk, ttk
from opentea.gui_forms.root_widget import OTRoot
from opentea.gui_forms.constants import set_constants
from opentea.noob.validation import validate_opentea_schema


def main_otinker(
        schema,
        calling_dir=None,
        start_mainloop=True,
        tab_3d=False,
        theme="clam"):
    """Startup the gui generation.

    Inputs :
    --------
    schema : dictionary compatible with json-schema
    calling_dir : directory from which otinker was called
    test_only : only for testing

    Outputs :
    ---------
    a tkinter GUI
    """
    #global CALLING_DIR
    #CALLING_DIR = calling_dir

    validate_opentea_schema(schema)
    tksession = Tk()
    sty = ttk.Style()

    sty.theme_use(theme)
    set_constants(tksession, calling_dir, theme)

    OTRoot(
        schema,
        tksession,
        start_mainloop=start_mainloop,
        tab_3d=tab_3d)
