"""
The root widget
===============

The root widget is the fisrt called by otinker.
It corresponds to the firts node ot the SCHEMA.

At the root widget, the whole window is created.
The root host the main Tab-notebook,
and if necessary the wiew 3D tab.

Tabs callbacks:
===============

As tabs callbacks can change any part of the memory,
These callbacks are passed down to the root widget,
trigerring two subprocesses.

Execute:
--------

Execute is about memory modification.
The callback associated shows the following singature:

nested object > callback > nested object

Update_3d_view:
---------------

Update_3d_view is about 3D feedback.
The callback associated shows the following singature:

nested object, 3D scene > callback > 3D scene

"""

import os
import time
import subprocess
from tkinter import ttk
from tkinter import filedialog as Tk_filedlg
from tkinter import Menu as Tk_Menu
from tkinter import Toplevel as Tk_Toplevel
from tkinter import Variable as Tk_Variable

import yaml

from opentea.gui_forms.constants import (
    PARAMS,
    load_icons,
    set_root,
    TextConsole)
from opentea.gui_forms.node_widgets import (OTNodeWidget,
                                            OTTabWidget)


# from opentea.noob.noob import (nob_pprint,
#                                nob_get)
# from opentea.noob.validation import main_validate

from opentea.noob.validation import (opentea_clean_data,
                                     opentea_resolve_require)
from opentea.noob.asciigraph import nob_asciigraph
from opentea.noob.inferdefault import nob_complete


from tiny_3d_engine import (Engine3D, load_geo_as_scene)

ABOUT = """
This is GUI FORMS, front ends provided by OpenTEA.

OpenTEA is an open source python package to help
the setup of complex softwares.
OpenTEA is currently developed at Cerfacs by the COOP team.
Meet us at coop@cerfacs.fr.
"""


#pylint: disable=too-many-arguments
class OTRoot(OTNodeWidget):
    """OT root widget."""

    def __init__(
            self,
            schema,
            tksession,
            start_mainloop=True,
            tab_3d=False):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        tksession : the main TKsession
        """
        self._root = tksession
        set_root(self)
        self.icons = load_icons()
        self.schema = schema
        self.toplevel = None
        super().__init__(schema)
        title = "untitled"
        if "title" in schema:
            title = schema["title"]

        self._root.title(title)
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

        self._main_frame = ttk.Frame(self._root, padding="3 3 12 12")
        self._main_frame.grid(column=0, row=0, sticky="news")

        self.main_nb = ttk.Notebook(self._main_frame, name='top_nb')
        self.main_nb.pack(fill="both", padx=2, pady=3, expand=True)

        self.toptabs = ttk.Frame(self.main_nb, name="forms")
        self.main_nb.add(self.toptabs, text="Forms")

        if tab_3d:
            self.view3d_fr = ttk.Frame(self.main_nb, name="3D view")
            self.main_nb.add(self.view3d_fr, text="3D view")
            self.view3d = Engine3D(
                scene=None,
                root=self.view3d_fr,
                width=1000,
                height=700,
                background="#666699"
            )

        self.toptabs.nb = ttk.Notebook(self.toptabs, name='tab_nb')
        self.toptabs.nb.pack(fill="both", padx=2, pady=3, expand=True)

        ttk.Style().configure("TNotebook", background=PARAMS["bg"])
        self._init_gui()
        self._init_file_menu()
        if start_mainloop:
            self._root.mainloop()

    def _init_file_menu(self):
        """Create the top menu dialog."""
        self._menubar = Tk_Menu(self._root)
        self._filemenu = Tk_Menu(self._menubar, tearoff=0)
        self._filemenu.add_command(label="New  (Ctrl+N)",
                                   image=self.icons['new'],
                                   compound='left',
                                   command=self._menu_new_command)

        self._filemenu.add_command(label="Load  (Ctrl+O)",
                                   image=self.icons['load'],
                                   compound='left',
                                   command=self._menu_load_command)

        self._filemenu.add_command(label="Save  (Ctrl+S)",
                                   image=self.icons['save'],
                                   compound='left',
                                   command=self._menu_save_command)

        self._filemenu.add_separator()
        self._filemenu.add_command(label="Quit   (Ctrl+W)",
                                   image=self.icons['quit'],
                                   compound='left',
                                   command=self._menu_quit_command)
        self._menubar.add_cascade(label="File", menu=self._filemenu)

        self._treeviewmenu = Tk_Menu(self._menubar, tearoff=0)

        self._treeviewmenu.add_command(label="Show tree",
                                       image=self.icons['tree'],
                                       compound='left',
                                       command=self._dump_tree_data)

        self._menubar.add_cascade(label="Debug", menu=self._treeviewmenu)

        self._helpmenu = Tk_Menu(self._menubar, tearoff=0)

        self._helpmenu.add_command(label="About",
                                   image=self.icons['about'],
                                   compound='left',
                                   command=self._menu_about_command)

        self._menubar.add_cascade(label="Help", menu=self._helpmenu)

        self._root.bind('<Control-o>', self._menu_load_command)
        self._root.bind('<Control-s>', self._menu_save_command)
        self._root.bind('<Control-n>', self._menu_new_command)
        self._root.bind('<Control-w>', self._menu_quit_command)
        self._root.bind('<Control-h>', self._dump_tree_data)
        self._root.config(menu=self._menubar)
        self.toplevel = None
        self._root.bind_all('<<mem_check>>', self._mem_check, add="+")
        # DEBUG
        self._root.bind_all('<<mem_change>>', self._mem_change, add="+")

    def _mem_change(self, event):
        # print("Ping mem_change" + str(event.widget))
        pass

    def _mem_check(self, event):
        # print("Ping mem_check" + str(event.widget))
        checked_mem = opentea_resolve_require(self.get(), self.schema)
        self.set(checked_mem)
        self._root.event_generate('<<mem_change>>')

    def _init_gui(self):
        """Start the recursive spawning of widgets."""
        for child in self.properties:
            self.tree[child] = OTTabWidget(
                self.properties[child],
                self,
                child)

        compl1 = nob_complete(self.schema)
        compl2 = opentea_clean_data(compl1)
        compl3 = opentea_resolve_require(compl2, self.schema)
        self.set(compl3)

    def _menu_quit_command(self, event=None):
        """Quit full application."""
        self._root.quit()

    def _dump_tree_data(self, event=None):
        """Show memory."""
        if self.toplevel is not None:
            self.toplevel.destroy()
        self.toplevel = Tk_Toplevel(self._root)
        self.toplevel.title('Tree View')
        self.toplevel.transient(self._root)
        memory = Tk_Variable(value=nob_asciigraph(self.get()))
        TextConsole(self.toplevel, memory, search=True)

    def _menu_new_command(self, event=None):
        """Start new application."""
        self._init_gui()

    def _menu_load_command(self, event=None):
        """Load data in current application."""
        state_file = Tk_filedlg.askopenfilename(
            title="Select file")
        with open(state_file, "r") as fin:
            state = yaml.load(fin, Loader=yaml.FullLoader)
        self.set(state)
        self._root.event_generate('<<mem_check>>')

    def _menu_save_command(self, event=None):
        """Save data in current application."""
        output = Tk_filedlg.asksaveasfilename(
            title="Select file",
            defaultextension='.yml')

        if output != '':
            dump = yaml.dump(self.get(), default_flow_style=False)
            with open(output, 'w') as fout:
                fout.writelines(dump)

    def _menu_about_command(self):
        """Splashscreen about openTEA."""
        if self.toplevel is not None:
            self.toplevel.destroy()
        self.toplevel = Tk_Toplevel(self._root)
        self.toplevel.title('About')
        self.toplevel.transient(self._root)
        memory = Tk_Variable(value=ABOUT)
        TextConsole(self.toplevel, memory)

        # pylint: disable=too-many-locals
    def execute(self, script):
        """execute a script"""
        full_script = os.path.join(PARAMS["calling_dir"], script)
        print("Mem update : Executing in subprocess ", full_script)
        start = time.time()
        dump = yaml.dump(self.get(), default_flow_style=False)
        try:
            os.remove("dataset_to_gui.yml")
        except FileNotFoundError:
            pass

        with open("dataset_from_gui.yml", 'w') as fout:
            fout.writelines(dump)

        subp = subprocess.run(
            ["python", full_script, "dataset_from_gui.yml"],
            capture_output=True,
            check=False
        )

        end = time.time()
        duration = str(round(end-start, 3)) + "s"

        returnstr = ""
        success = False
        if subp.returncode == 0:
            success = True
            msg_out = "Return code : " + str(subp.returncode)
            msg_out += "\n" + "### STD-OUT ###" + "\n"
            msg_out += subp.stdout.decode("utf-8")

            print("Process succesful...")
            print(msg_out)
            with open("dataset_to_gui.yml", 'r') as fin:
                data_in = yaml.load(fin, Loader=yaml.FullLoader)
                # main_validate(data_in, self.schema)
                self.set(data_in)
        else:
            msg_err = "Return code : " + str(subp.returncode)
            msg_err += "\n" + "### STD-OUT ###" + "\n"
            msg_err += subp.stdout.decode("utf-8")
            msg_err += "\n" + "### STD-ERR ###" + "\n"
            msg_err += subp.stderr.decode("utf-8")

            print("Process failed...")
            print(msg_err)

            for line in subp.stderr.decode("utf-8").split("\n"):
                for tag in ['RuntimeError']:
                    if line.startswith(tag):
                        returnstr = line

        print("Process finished in " + duration)

        return success, duration, returnstr

    def update_3d_view(self, script):
        """execute a script for 3d view update"""
        full_script = os.path.join(PARAMS["calling_dir"], script)
        print("3D-view : Executing in subprocess ", full_script)

        try:
            scene_file = "scene_from_gui.geo"
            self.view3d.dump("scene_from_gui")
        except ValueError:
            scene_file = "no_scene"

        dump = yaml.dump(self.get(), default_flow_style=False)

        with open("dataset_from_gui.yml", 'w') as fout:
            fout.writelines(dump)

        subp = subprocess.run(
            ["python", full_script, "dataset_from_gui.yml", scene_file],
            capture_output=True,
            check=False
        )
        success = False
        if subp.returncode == 0:
            success = True
            #msg_out = "Return code : " + str(subp.returncode)
            #msg_out += "\n" + "### STD-OUT ###" + "\n"
            #msg_out += subp.stdout.decode("utf-8")

            print("Update scene 3D successfull...")
            new_scene = load_geo_as_scene("scene_to_gui.geo")
            self.view3d.update(new_scene)

        else:
            msg_err = "Return code : " + str(subp.returncode)
            msg_err += "\n" + "### STD-OUT ###" + "\n"
            msg_err += subp.stdout.decode("utf-8")
            msg_err += "\n" + "### STD-ERR ###" + "\n"
            msg_err += subp.stderr.decode("utf-8")

            print("Process failed...")
            print(msg_err)

        return success
