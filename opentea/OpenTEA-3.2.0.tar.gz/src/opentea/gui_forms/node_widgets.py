"""
Recursive edicrection according to SCHEMA type
==============================================
This module staets with the recursive redirection
according to SCHEMA types.

Module for containers widgets
=============================

This module take care of all the node elements of the graph,
which correspond to containers in the Form.
At least the three first level of the SCHEMA must be objects,
 and are treated as containers.
 Oll the containers derive from the generic Node-Widget.

The root level:
---------------

The inital node, Not treted here, see root_widget.

The Tab level:
--------------

The second node level. Treated here, see Tabs_widgets.
This one can support two types of callbacks,
either for editing the memory,
or for updating the 3D view.

The Block level :
-----------------

The Thirl level gather parameters into families.
This one can support descriptions, images and documentation.


Special container : The Multiple widget :
-----------------------------------------

This container correspont to an SCHEMA array of objet items.
See it as a list (free or dependent) of similar containers.

Mutliple can be use freely or with a dependency.
In the last case, the items of the multiple is linked to the value
of a string array somewhere else in the SCHEMA.
For exeample, in CFD, This is usefoull for a
set of boundary conditions, found by reading a MESH.


Special container : the XOR widget :
------------------------------------

This is merely a selector between several blocks.
This marks a bifurcation in your graph.
For example in CFD, this is usefull for the selection between
different models taking different parameters.

:warning exception here: XOR is the only node element storing a Value.
The value is implicit : it is *the name of the only child
of the XOR in the memory*.

It could have been designed otherwise, keeping all the children inthe memory,
and a real leaf value to know which one must be taken.
However, thos is impractical here. For example in CFD,
you can have a Multiple of 100 boundary conditions,
with a XOR for each selecting between 30 models of BCs.
Such a graph would be a hassle to read and hack for humans.

"""

#pylint: disable=too-many-lines

import os
import webbrowser
import tempfile
import warnings

from tkinter import ttk
# from tkinter import Canvas as Tk_Canvas
from tkinter import Menu as Tk_Menu
from tkinter import (
    Entry,
    Label,
    Frame,
    StringVar,
    LEFT,
    )
from PIL import ImageTk, Image
import markdown


from opentea.noob.inferdefault import nob_complete
from opentea.noob.noob import nob_pprint
# from opentea.gui_forms.wincanvas import redirect_canvas_items
from opentea.gui_forms.constants import (
    IMAGE_DICT,
    WIDTH_UNIT,
    PARAMS,
    GetException,
    SetException,
    SwitchForm,
    create_scrollable_canvas)
from opentea.gui_forms.leaf_widgets import (OTInteger,
                                            OTNumber,
                                            OTEmpty,
                                            OTList,
                                            OTChoice,
                                            OTComment,
                                            OTBoolean,
                                            OTFileBrowser,
                                            OTString,
                                            OTDocu,
                                            OTDescription)


def redirect_widgets(schema, root_frame, name, tab):
    """Redirect to widgets.

    The schema attributes trigger which widget will be in use.

    Inputs :
    --------
    schema :  a schema object
    root_frame :  a Tk object were the widget will be grafted
    name : name of the element
    tab:  the tab holding this widget

    Outputs :
    --------
    none
    """

    if schema is None:
        out = OTEmpty(dict(), root_frame, name)
    else:
        if "properties" in schema:
            out = OTContainerWidget(schema, root_frame, name, tab)
        elif "oneOf"in schema:
            out = OTXorWidget(schema, root_frame, name, tab)
        elif "enum" in schema:
            out = OTChoice(schema, root_frame, name)
        elif "ot_dyn_choice" in schema:
            out = OTChoice(schema, root_frame, name, dynamic=True)
        elif "type" in schema:
            if schema["type"] == "array":
                if "properties" in schema["items"]:
                    out = OTMultipleWidget(
                        schema,
                        root_frame,
                        name,
                        tab)
                else:
                    out = OTList(schema, root_frame, name)
            elif schema['type'] == 'integer':
                out = OTInteger(schema, root_frame, name)
            elif schema['type'] == 'number':
                out = OTNumber(schema, root_frame, name)
            elif schema['type'] == 'boolean':
                out = OTBoolean(schema, root_frame, name)
            elif schema["type"] == "string":
                out = redirect_string(schema, root_frame, name)
        else:
            out = OTEmpty(schema, root_frame, name)
    return out


def redirect_string(schema, root_frame, name):
    """Redirect to string widgets.

    The schema attributes trigger which string widget will be in use.

    Inputs :
    --------
    schema :  a schema object
    root_frame :  a Tk object were the widget will be grafted
    name : name of the element

    Outputs :
    --------
    none
    """
    out = OTString(schema, root_frame, name)
    if "ot_type" in schema:
        if schema["ot_type"] == "desc":
            wng = " at: " + name + "> attribute"
            wng += "\n ot_type : desc is deprecated"
            wng += "\n prefer description attribute on blocks"
            warnings.warn(wng, DeprecationWarning)
            out = OTDescription(schema, root_frame, name)
        elif schema["ot_type"] == "docu":
            wng = " at: " + name + "> attribute"
            wng += "\n ot_type : docu is deprecated"
            wng += "\n prefer documentation attribute on blocks"
            warnings.warn(wng, DeprecationWarning)
            out = OTDocu(schema, root_frame, name)
        elif schema["ot_type"] == "comment":
            out = OTComment(schema, root_frame, name)
        elif schema["ot_type"] == "file":
            out = OTFileBrowser(schema, root_frame, name)
        else:
            raise NotImplementedError(
                "At node" + name
                + ": cannot resolve ot_type=" + schema["ot_type"])
    return out


class OTNodeWidget():
    """Factory for OpenTea Widgets Containers."""

    def __init__(self, schema):
        """Startup class."""
        self.tree = dict()
        try:
            self.properties = schema["properties"]
        except:
            msg_err = "properties missing in schema:\n" + nob_pprint(schema)
            raise RuntimeError(msg_err)

    def get(self):
        """Get the data of children widgets.

        Returns :
        ---------
        a dictionnary with the get result of childrens
        """
        out = {}
        for child in self.properties:
            try:
                found = self.tree[child].get()
                if found is not None:
                    out[child] = found
            except GetException:
                pass
        if out == {}:
            out = None
        return out

    def set(self, dict_):
        """Get the data of children widgets.

        Input :
        -------
        a dictionnary with the value of the childrens"""
        for child in self.properties:
            if child in dict_:
                try:
                    self.tree[child].set(dict_[child])
                except SetException:
                    pass

    def get_status(self):
        """Return the minimal status of children."""
        status = 1
        for child in self.properties:
            status = min(
                status,
                self.tree[child].get_status())
        return status


# pylint: disable=too-many-arguments
class OTContainerWidget(OTNodeWidget):
    """OT container widget."""

    def __init__(self, schema, root_frame, name, tab, n_width=1):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        root_frame :  a Tk object were the widget will be grafted
        name: string naming the widget
        n_width : float
             relative size of the widget

        """
        super().__init__(schema)
        #title = "#" + name

        if "title" in schema:
            title = schema["title"]
        else:
            title = ""
        self.tab = tab
        self._holder = ttk.Frame(root_frame,
                                 relief="ridge",
                                 width=n_width*WIDTH_UNIT)
        self._holder.pack(side="top", fill="x",
                          padx=2, pady=2, expand=False)

        self.head = ttk.Label(
            self._holder,
            text=title)
        self.head.pack(side="top", fill="both", expand=False)
        self.body = ttk.Frame(
            self._holder,
            width=n_width*WIDTH_UNIT)

        """Forcing the widget size"""
        self._forceps = ttk.Frame(self._holder,
                                  width=n_width*WIDTH_UNIT,
                                  height=1)
        self.head.pack(side="top", fill="x",
                       padx=2, pady=2, expand=False)
        self._forceps = ttk.Frame(self._holder,
                                  width=WIDTH_UNIT,
                                  height=1)
        self._forceps.pack(side="top", padx=2, pady=2)

        self.expert = False
        self.packed = True
        if "expert" in schema:
            self.expert = schema['expert']

        if self.expert:
            self.packed = False
            self.head.configure(
                compound=LEFT,
                image=IMAGE_DICT["plus"])
            self.head.bind("<Button-1>", self.pack_unpack_body)

        if self.packed:
            self.body.pack(side="top", fill="x", expand=False, padx=2, pady=2)

        if "image" in schema:
            path = os.path.join(PARAMS["calling_dir"], schema['image'])
            img = ImageTk.PhotoImage(Image.open(path))
            self._img = Label(
                self.body,
                background=PARAMS["bg"],
                image=img
                )
            self._img.image = img
            self._img.pack(side="bottom", fill="x")

        if "documentation" in schema:
            self.docu_ct = schema["documentation"]
            self._docu = Label(
                self.body,
                text="learn more...",
                background=PARAMS["bg"],
                foreground="blue",
                justify="right")
            self._docu.pack(side="bottom", fill="x")
            self._docu.bind("<Button-1>", self.show_docu)

        if "description" in schema:
            self._desc = create_description(self.body, schema["description"])
            self._desc.pack(side="bottom", fill="x")

        # CHILDREN
        for name_child in self.properties:
            schm_child = self.properties[name_child]
            self.tree[name_child] = redirect_widgets(schm_child,
                                                     self.body,
                                                     name_child,
                                                     tab)

    def show_docu(self, event):
        """Call the documentation browser
        """
        show_docu_webpage(self.docu_ct)

    def pack_unpack_body(self, event):
        """swtich on or off the packing of the body"""
        if self.packed:
            self.packed = False
            self.body.pack_forget()
            self.head.configure(
                compound=LEFT,
                image=IMAGE_DICT["plus"])
        else:
            self.packed = True
            self.body.pack(side="top", fill="x", expand=False, padx=2, pady=2,)
            self.head.configure(
                compound=LEFT,
                image=IMAGE_DICT["minus"])
        PARAMS["top"].update_idletasks()
        self.tab.holder.event_generate("<Configure>")


class OTTabWidget(OTNodeWidget):
    """OT Tab widget container.

    Called for the 1st layer of nodes in the global schema
    """

    def __init__(self, schema, root, name):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        root :  the parent
        name: string naming the widget
        """
        super().__init__(schema)
        self.root = root
        self.icon = None
        self.title = "#" + name
        if "title" in schema:
            self.title = schema["title"]

        self._tab = ttk.Frame(self.root.toptabs.nb, name=name)
        self.root.toptabs.nb.add(self._tab, text=self.title)

        self.tabid = self.root.toptabs.nb.index("end")-1

        # SCROLL FORM
        self.scan = create_scrollable_canvas(self._tab)
        self.holder = ttk.Frame(self.scan)
        self.scan.create_window(
            (0, 0),
            window=self.holder,
            anchor='nw')
        # FOOTER
        _footer_f = ttk.Frame(self._tab)
        _footer_f.pack(side="top", fill="both", padx=2, pady=3)
        self.button_text = StringVar()
        self.button_lb = ttk.Label(_footer_f, textvariable=self.button_text)

        self.process = None
        self.update_scene_3d = None
        actions = list()
        if "process" in schema:
            self.process = schema["process"]
            actions.append("Process")
        if "update_scene_3d" in schema:
            self.update_scene_3d = schema["update_scene_3d"]
            actions.append("Update 3D")

        if not actions:
            txt_btn = "Validate"
        else:
            txt_btn = "/".join(actions)

        _button_bt = ttk.Button(_footer_f,
                                text=txt_btn,
                                command=self.process_button)

        _button_bt.pack(side="right", padx=2, pady=2)
        self.button_lb.pack(side="right", padx=2, pady=2)
        if "description" in schema:
            self._desc = create_description(
                _footer_f, schema["description"], size=1.)
            self._desc.pack(side="left", fill="x")

        # CHILDREN
        for name_ in schema["properties"]:
            self.tree[name_] = redirect_widgets(schema["properties"][name_],
                                                self.holder,
                                                name_,
                                                self)

        self.holder.bind(
            "<Configure>",
            self.smartpacker)

        self.root.toptabs.nb.bind_all(
            '<<mem_check>>',
            self.on_memory_check, add="+")
        self.root.toptabs.nb.bind_all(
            '<<mem_change>>',
            self.on_memory_change, add="+")
        self.update_tab_icon('unknown')

    def update_tab_icon(self, icon_name):
        """Update the Tab icon upon status."""
        if self.icon != icon_name:
            self.root.toptabs.nb.tab(
                self.tabid,
                image=IMAGE_DICT[icon_name],
                compound='left')
            self.icon = icon_name

    def on_memory_change(self, event):
        """Check if the sender is child of this tab.process.
        set to unknown if so"""
        found_parent_tab = False
        parent = event.widget
        while not found_parent_tab:
            parent = parent.master
            if parent is None:
                break
            parent_name = parent.winfo_name()
            if parent_name == 'tk':
                break
            if parent_name == self._tab.winfo_name():
                if isinstance(parent, type(self._tab)):
                    found_parent_tab = True
        if found_parent_tab:
            self.update_tab_icon('unknown')

    def on_memory_check(self, event):
        """Update content upon status of children."""
        state = self.get_status()
        state_icon = 'unknown'
        if state == 1:
            state_icon = 'valid'
        elif state == -1:
            state_icon = 'invalid'

        self.update_tab_icon(state_icon)

    def process_button(self):
        """Procees the main tab button."""
        self.button_text.set("")
        state = self.get_status()
        self.root.toptabs.nb.event_generate('<<mem_check>>')
        if state == -1:
            self.button_text.set("Can not process with errors in tabs")
        else:
            if self.process is None:
                pass
            else:
                success, duration, returnstr = self.root.execute(self.process)
                if success:
                    self.button_lb.configure(foreground="black")
                    self.button_text.set(
                        "Done in " + duration + ", successful")
                    self.root.toptabs.nb.event_generate('<<mem_change>>')
                    self.root.toptabs.nb.event_generate('<<mem_check>>')
                else:
                    self.button_lb.configure(foreground="red")
                    self.button_text.set(
                        "Failed after "
                        + duration
                        + ", "
                        + returnstr)
                    self.update_tab_icon('invalid')

            if self.update_scene_3d is None:
                pass
            else:
                self.root.update_3d_view(self.update_scene_3d)

    def smartpacker(self, event=None):
        """Smart grid upon widget size.

        Regrid the object according to the width of the window
        from the inside
        """
        self.scan.configure(scrollregion=self.scan.bbox("all"))
        ncols = max(int(self.root.toptabs.nb.winfo_width()/WIDTH_UNIT + 0.5),
                    1)
        height = 0

        large_children = list()
        normal_childen = list()
        for child in self.holder.winfo_children():
            if child.winfo_width() > 1.1*WIDTH_UNIT:
                large_children.append(child)
            else:
                normal_childen.append(child)

        # Large children
        x_pos = 10
        y_pos = 10
        for child in large_children:
            height = child.winfo_height()
            child.place(x=x_pos,
                        y=y_pos,
                        anchor="nw")
            y_pos += height + 2

        limit_y_large_normal = y_pos
        max_depth = limit_y_large_normal

        # Normal children
        for child in normal_childen:
            height += child.winfo_height() + 2
        limit_depth = height / ncols + limit_y_large_normal

        for child in normal_childen:
            child.place(x=x_pos,
                        y=y_pos,
                        anchor="nw")
            y_pos += child.winfo_height() + 2

            if y_pos > limit_depth and ncols > 1:
                max_depth = y_pos
                x_pos += WIDTH_UNIT + 20
                y_pos = limit_y_large_normal
            else:
                max_depth = height

        self.holder.configure(
            height=max_depth+200,
            width=ncols*(WIDTH_UNIT+20)+20)


class OTMultipleWidget():
    """OT multiple widget."""

    def __init__(self, schema, root_frame, name, tab):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        root_frame :  a Tk object were the widget will be grafted
        name: string naming the widget
        """
        self.tree = list()
        self.tab = tab
        self.status = 1
        self.item_schema = schema["items"]
        title = "#" + name
        if "title" in schema:
            title = schema["title"]

        holder = ttk.LabelFrame(
            root_frame,
            text=title,
            name=name,
            relief="sunken",
            width=2*WIDTH_UNIT)
        holder.pack(side="top", fill="x", padx=2, pady=2, expand=False)
        forceps = ttk.Frame(holder, width=2*WIDTH_UNIT, height=1)
        self.tvw = ttk.Treeview(
            holder,
            selectmode="browse",
            height=15)
        scroll_vert = ttk.Scrollbar(
            holder,
            orient="vertical",
            command=self.tvw.yview)
        self.tvw.configure(yscrollcommand=scroll_vert.set)
        self.switchform = SwitchForm(
            holder,
            width=WIDTH_UNIT,
            name='tab_holder')

        # Controls panel ---------
        self.ctrls = ttk.Frame(holder)
        if "ot_require" not in schema:
            self.ctrls.butt_add = ttk.Button(
                self.ctrls,
                text="add " + title,
                command=self.add_item_on_cursel)
            self.ctrls.butt_del = ttk.Button(
                self.ctrls,
                text="del " + title,
                command=self.del_item_on_cursel)
            self.ctrls.butt_add.pack(side="left")
            self.ctrls.butt_del.pack(side="left")

        # Grids the main layout ------------
        forceps.grid(column=0, row=1, columnspan=3)
        scroll_vert.grid(column=1, row=1, sticky="news")
        self.tvw.grid(column=0, row=1, sticky="news")
        self.ctrls.grid(column=0, row=2, sticky="news")
        self.switchform.grid(column=2, row=1, rowspan=2, sticky="news")
        self.switchform.grid_propagate(0)

        item_props = self.item_schema["properties"]
        self.tvw["columns"] = tuple(item_props.keys())
        self.tvw["show"] = 'headings'
        col_width = int(WIDTH_UNIT/(len(self.tvw["columns"])))
        self.tvw.column("#0", width=20)
        self.title_to_key = dict()
        for key in item_props:
            title = key
            if "title" in item_props[key]:
                title = item_props[key]["title"]
            self.tvw.column(key, width=col_width)
            self.tvw.heading(key, text=title)
            self.title_to_key[title] = key

        def tv_simple_click(event):
            """Handle a simple click on treeview."""
            # col = self.tvw.identify_column(event.x)
            row = self.tvw.identify_row(event.y)
            self.switchform.sf_raise(row)

        def tv_double_click(event):
            """Handle a simple click on treeview."""
            col = self.tvw.identify_column(event.x)
            row = self.tvw.identify_row(event.y)
            if col == "#0":
                self.rename_callback(row)

        self.tvw.bind("<Button-1>", tv_simple_click)

        if "ot_require" not in schema:
            self.tvw.bind("<Double-1>", tv_double_click)

        self.refresh_view()
        self.tvw.bind_all('<<mem_change>>', self.refresh_view, add='+')

    def refresh_view(self, event=None):
        """Refresh items values on tree view."""
        headings = [self.tvw.heading(i)['text']
                    for i, _ in enumerate(self.title_to_key, 0)]

        for item in self.tree:
            uid = item.tree['name'].get()
            values = [None]*len(self.title_to_key)
            for title in self.title_to_key:
                key = self.title_to_key[title]
                value = item.tree[key].get()
                if isinstance(value, dict):
                    value = next(iter(value))
                values[headings.index(title)] = str(value)
            self.tvw.item(uid, values=values)

    def get(self):
        """Get the data of children widgets.

        Returns :
        ---------
        a list with the get result of childrens
        """
        out = list()
        for child in self.tree:
            try:
                found = child.get()
                if found is not None:
                    out.append(found)
            except GetException:
                pass
        #if not out:
        #    out = None
        return out

    def set(self, list_):
        """Get the data of children widgets.

        Input :
        -------
        a list with the value of the childrens"""

        ingoing_childs = [item["name"] for item in list_]
        childs_to_add = ingoing_childs.copy()
        childs_to_del = []

        for item_id, item in enumerate(self.tree):
            item_name = item.get()['name']
            if item_name not in ingoing_childs:
                childs_to_del.append(item_name)
            else:
                data_in = list_[ingoing_childs.index(item_name)]
                self.tree[item_id].set(data_in)
                childs_to_add.remove(item_name)

        # print("Ingoing:", ingoing_childs)
        # print("childs_to_add:", childs_to_add)
        # print("childs_to_del", childs_to_del)

        for child_name in childs_to_del:
            self.del_item_by_name(child_name)

        for item_name in childs_to_add:
            data_in = list_[ingoing_childs.index(item_name)]
            multiple_item = OTMultipleItem(self, item_name, self.tab)
            multiple_item.set(data_in)
            self.tree.insert(-1, multiple_item)

        self.tree = [self.tree[self.index_of_item(name)]
                     for name in ingoing_childs]

    def rename_callback(self, item_name):
        """Trigger renaming if dialog conditions are met."""
        trans_frame = Frame(
            self.tvw,
            background="red",
            borderwidth=2)
        bbox = self.tvw.bbox(item_name, "#0")
        trans_frame.place(
            x=bbox[0]-1,
            y=bbox[1]-1,
            width=bbox[2]+2,
            height=bbox[3]+2)

        custom_name = StringVar()
        custom_name.set(item_name)
        trans_entry = Entry(trans_frame, textvariable=custom_name)
        trans_entry.pack(fill="both")

        def _withdraw(args):
            trans_frame.destroy()

        def _tryupdate(args):
            self.rename_item(item_name, custom_name.get())
            trans_frame.destroy()

        trans_entry.bind("<Return>", _tryupdate)
        trans_entry.bind("<FocusOut>", _withdraw)
        trans_entry.bind("<Escape>", _withdraw)

    def rename_item(self, item_name, new_name):
        """Rename one element of the multiple."""
        id_item = self.index_of_item(item_name)
        new_list = self.get()
        list_names = [item["name"] for item in new_list]

        while new_name in list_names:
            new_name += "#"
        new_list[id_item]["name"] = new_name
        self.set(new_list)

    def add_item_on_cursel(self):
        """Add an item in the multiple.

        Item will be added before the current selection.
        """
        cursel = self.tvw.selection()
        if not cursel:
            id_cursel = 0
        else:
            id_cursel = self.index_of_item(cursel[0])

        new_list = self.get()
        if new_list is None:
            new_list = list()

        list_names = [item["name"] for item in new_list]

        # create a new item with default value
        new_item = nob_complete(self.item_schema)
        new_name = new_item["name"]
        while new_name in list_names:
            new_name += "#"
        new_item["name"] = new_name
        new_list.insert(id_cursel, new_item)
        self.set(new_list)

    def del_item_on_cursel(self):
        """Delete a Multiple item from tv selection."""
        cursel = self.tvw.selection()
        if not cursel:
            print("No item selected...")
        else:
            id_cursel = self.index_of_item(cursel[0])
            new_list = self.get()
            new_list.pop(id_cursel)
            self.set(new_list)

    def del_item_by_name(self, name):
        """Delete a Multiple item by its name."""
        self.tvw.delete(name)
        del self.tree[self.index_of_item(name)]

    def index_of_item(self, name):
        """Find index of a Multiple item by its name."""
        index = None
        for item_id, item in enumerate(self.tree):
            item_name = item.get()['name']
            if item_name == name:
                index = item_id
        return index

    def get_status(self):
        """Compute the minimal status in children."""
        status = 1
        for child in self.tree:
            status = min(
                status,
                child.get_status())
        return status


class OTMultipleItem(OTContainerWidget):
    """OT  multiple widget."""

    def __init__(self, multiple, name, tab):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        multiple :  a Tk object were the widget will be grafted
        """
        self.tab = multiple.switchform.add(name, title=name.lower())
        super().__init__(multiple.item_schema, self.tab, name, tab)
        multiple.tvw.insert("", "end", iid=name, text=name)


# pylint: disable=too-many-arguments
class OTXorWidget():
    """OT  Or-exclusive / oneOf widget."""

    def __init__(self, schema, root_frame, name, tab, n_width=1):
        """Startup class.

        Inputs :
        --------
        schema : a schema as a nested object
        root_frame :  a Tk object were the widget will be grafted
        name: string naming the widget
        n_width : float
             relative size of the widget
        """
        self.tree = dict()
        self.current_child = None
        self.tab = tab
        self._schema = schema
        title = "#" + name
        if "title" in schema:
            title = schema["title"]

        self.current_child = self._schema["oneOf"][0]["required"][0]
        self._holder = ttk.LabelFrame(root_frame,
                                      text=title,
                                      name=name,
                                      relief="sunken",
                                      width=n_width*WIDTH_UNIT)

        self._forceps = ttk.Frame(self._holder,
                                  width=n_width*WIDTH_UNIT,
                                  height=1)
        self._menu_bt = ttk.Menubutton(self._holder,
                                       text="None")

        self._xor_holder = ttk.Frame(self._holder)

        self._holder.pack(side="top", fill="x",
                          padx=2, pady=2, expand=False)
        self._forceps.pack(side="top")
        self._menu_bt.pack(side="top")
        self._xor_holder.pack(side="top", fill="x",
                              padx=2, pady=2, expand=False)

        self._menu_bt.menu = Tk_Menu(self._menu_bt, tearoff=False)
        self._menu_bt["menu"] = self._menu_bt.menu

        for oneof_item in self._schema["oneOf"]:
            nam = oneof_item["required"][0]
            ch_s = oneof_item["properties"][nam]
            title = nam
            if "title" in ch_s:
                title = ch_s["title"]
            self._menu_bt.menu.add_command(
                label=title,
                command=lambda nam=nam: self.xor_callback(nam))

        if "image" in schema:
            path = os.path.join(PARAMS["calling_dir"], schema['image'])
            img = ImageTk.PhotoImage(Image.open(path))
            self._img = Label(
                self._holder,
                background=PARAMS["bg"],
                image=img
                )
            self._img.image = img
            self._img.pack(side="bottom", fill="x")

        if "documentation" in schema:
            self.docu_ct = schema["documentation"]
            self._docu = Label(
                self._holder,
                text="learn more...",
                background=PARAMS["bg"],
                foreground="blue",
                justify="right")
            self._docu.pack(side="bottom", fill="x")
            self._docu.bind("<Button-1>", self.show_docu)
        if "description" in schema:
            self._desc = create_description(
                self._holder, schema["description"])
            self._desc.pack(side="left", fill="x")

        self.update_xor_content(self.current_child)

    def show_docu(self, event):
        """Call the documentation browser
        """
        show_docu_webpage(self.docu_ct)

    def xor_callback(self, name_child):
        """Event on XOR menu selection."""
        self.update_xor_content(name_child, data_in=None)
        self._menu_bt.event_generate('<<mem_change>>')

    def update_xor_content(self, name_child, data_in=None):
        """Reconfigure XOR button.

        Inputs :
        --------
        name_child : sting, naming the child object
        data_in : dictionary used to pre-fill the data
        """
        self.current_child = name_child
        child_schema = None
        for possible_childs in self._schema["oneOf"]:
            if possible_childs["required"][0] == name_child:
                child_schema = possible_childs["properties"][name_child]

        for child_widget in self._xor_holder.winfo_children():
            child_widget.destroy()

        self.tree = dict()
        self.tree[name_child] = OTContainerWidget(child_schema,
                                                  self._xor_holder,
                                                  name_child,
                                                  self.tab)
        if data_in is None:
            self.tree[name_child].set(nob_complete(child_schema))
        else:
            self.tree[name_child].set(data_in)

        title = name_child
        if "title" in child_schema:
            title = child_schema["title"]
        self._menu_bt.configure(text=title)

    def get(self):
        """Get the data of children widgets.

        Returns :
        ---------
        a dictionnary with the get result of current children
        """
        out = dict()
        #print(">>>", self.current_child)
        try:
            found = self.tree[self.current_child].get()
            if found is not None:
                out[self.current_child] = found
            else:
                out[self.current_child] = None
        except GetException:
            pass

        if out == {}:
            out = None
        return out

    def set(self, dict_):
        """Get the data of children widgets.

        Input :
        -------
        a dictionnary with the value of the childrens
        """
        given_keys = dict_.keys()
        if len(given_keys) > 1:
            raise SetException("Multiple matching option, skipping...")

        for one_of in self._schema["oneOf"]:
            child = next(iter(one_of['properties']))
            if child in dict_:
                try:
                    self.update_xor_content(child, dict_[child])
                except SetException:
                    pass

    def get_status(self):
        """Proxy to the get_status of the current child."""
        return self.tree[self.current_child].get_status()


def show_docu_webpage(markdown_str):
    """ Show documentation in the web browser

    Use package `markdown`to translate markown into HTML.
    Dump is into a temporary file using `tempfile`package.
    Finally call the browser using `webbrowser`package.
    """
    md_ = markdown.Markdown()
    html = str()
    html += '''
 <style type="text/css">
 body {
    font-family: Helvetica, Geneva, Arial, SunSans-Regular,sans-serif ;
    margin-top: 100px;
    margin-bottom: 100px;
    margin-right: 150px;
    margin-left: 80px;
    color: black;
    background-color: BG_COLOR
 }

 h1 {
    color: blue
}
 </style>
'''
    html = html.replace('BG_COLOR', PARAMS["bg"])
    html += md_.convert(markdown_str)
    html = html.replace('src="', 'src="'+PARAMS["calling_dir"] + '/')

    with tempfile.NamedTemporaryFile(
            'w', delete=False, suffix='.html') as fout:
        url = 'file://' + fout.name
        fout.write(html)
    webbrowser.open(url)


def create_description(parent, description, size=0.9):
    """Interpret the description to tkae into account font modifiers"""
    text = description
    fontname = None
    fontsize = 13
    fonthyphen = "normal"

    if "<small>" in text:
        text = text.replace("<small>", "")
        fontsize = 12
    if "<tiny>" in text:
        text = text.replace("<tiny>", "")
        fontsize = 11
    if "<bold>" in text:
        text = text.replace("<bold>", "")
        fonthyphen = "bold"
    if "<italic>" in text:
        text = text.replace("<italic>", "")
        fonthyphen = "italic"
    desc = Label(
        parent,
        font=(fontname, fontsize, fonthyphen),
        text=text,
        background=PARAMS["bg_lbl"],
        justify="left",
        wraplength=int(size*WIDTH_UNIT))
    return desc
