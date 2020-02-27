'''
This file is a part of Arjuna
Copyright 2015-2020 Rahul Verma

Website: www.RahulVerma.net

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os

from .nsloader import GuiNamespaceLoaderFactory
from arjuna.interact.gui.auto.finder.emd import SimpleGuiElementMetaData, GuiElementMetaData, Locator
from arjuna.interact.gui.helpers import With
from arjuna.core.exceptions import GuiLabelNotPresentError

class GuiDef:
    '''
        A GuiDef object is attached to a Gui, which in turn is attached to an automator and hence to a fixed auto context.

        Arjuna does a lazy loading of Gui Definitions. This means a context A GuiDef will lead to loading of all contexts centrally, but use only the one it needs to avoid repeat processing.
    '''

    def __init__(self, name_store, automator, label, def_file_path): # namespace_dir, 
        self.__name_store = name_store
        # self.__namespace_dir = namespace_dir
        self.__automator = automator
        self.__config = automator.config
        self.__auto_context = self.config.guiauto_context
        self.__file_def_path = def_file_path
        self.__ns = None
        ns_name = "file_ns::" + self.__file_def_path.lower()
        if name_store.has_namespace(ns_name):
            self.__ns = name_store.get_namespace(ns_name)
        else:
            self.__ns = name_store.load_namespace(
                ns_name, 
                GuiNamespaceLoaderFactory.create_namespace_loader(
                    self.config,
                    self.__file_def_path
            )
        )

        self.__children = []

    @property
    def config(self):
        return self.__config

    # def add_child(self, label, automator, file_def_path):
    #     self.__children.append(
    #         Gui(self.__name_store, self.__namespace_dir, label, self.__automator, file_def_path)
    # )

    def convert_to_lmd(self, *locators):
        final_locators = []
        for raw_locator in locators:
            if raw_locator.wtype.upper().strip() == "LABEL":
                emd = self.__ns.get_meta_data(raw_locator.wvalue, self.__auto_context)
                for loc in emd.raw_locators:
                    if not raw_locator.named_args:
                        final_locators.append(Locator(ltype=loc.ltype, lvalue=loc.lvalue), named_args={})
                    else:
                        final_locators.append(Locator(ltype=loc.ltype, lvalue=loc.lvalue), named_args=raw_locator.named_args)
            else:
                if not raw_locator.named_args:
                    final_locators.append(Locator(ltype=raw_locator.wtype, lvalue=raw_locator.wvalue), named_args={})
                else:
                    final_locators.append(Locator(ltype=raw_locator.ltype, lvalue=raw_locator.lvalue), named_args=raw_locator.named_args)
        import sys
        sys.exit(1)
        return GuiElementMetaData(final_locators)

    def __gns_locators_as_with_locators(self, label):
        emd = self.__ns.get_meta_data(label, self.__auto_context)
        out = []
        for loc in emd.raw_locators:
            underscore = loc.ltype.lower().endswith("attr") and "_" or ""
            wobj = getattr(With, underscore + loc.ltype.lower()) (loc.lvalue)# e.g. getattr(With, "_" + "ID".lower())("abc")
            out.append(wobj)
        return out

    def convert_to_with(self, locator):
        from arjuna.interact.gui.helpers import With
        out_list = []
        impl_with = locator.as_impl_locator()
        for wobj in self.__gns_locators_as_with_locators(impl_with.wvalue):
            # underscore = loc.ltype.lower().endswith("attr") and "_" or ""
            # wobj = getattr(With, underscore + loc.ltype.lower()) (loc.lvalue)# e.g. getattr(With, "_" + "ID".lower())("abc")
            if locator.named_args:
                wobj.format(**locator.named_args)
            out_list.append(wobj)
        return out_list

    @property
    def root_element_with_locators(self):
        try:
            return self.__gns_locators_as_with_locators("__root__")
        except GuiLabelNotPresentError:
            # Defining __root__ is optional for GNS files.
            return None

    @property
    def anchor_element_with_locators(self):
        try:
            return self.__gns_locators_as_with_locators("__anchor__")
        except GuiLabelNotPresentError:
            # Defining __load__ is optional for GNS files.
            return None

    def create_dispatcher(self):
        # Pages don't use any dispatcher
        pass

class GuiFactory:

    @classmethod
    def create_appdef_from_dir(cls, name, automator, app_def_dir):
        from arjuna.core.enums import ArjunaOption
        considered_path = app_def_dir
        if not os.path.isdir(considered_path):
            gns_dir = automator.config.value(ArjunaOption.GUIAUTO_NAMESPACE_DIR)
            full_path = os.path.join(gns_dir, considered_path)
            considered_path = os.path.abspath(full_path)
            if not os.path.isdir(considered_path):
                raise Exception("Provided root definition path is not a directory: {}".format(app_def_dir))

        app = GuiDef(automator, os.path.join(considered_path, "HomePage.yaml"), label=name)
        children_dir = os.path.join(considered_path, "children")
        if os.path.isdir(children_dir):
            lfiles = os.listdir(children_dir)
            for f in lfiles:
                cpath = os.path.join(children_dir, f)
                if os.path.isfile(cpath):
                    base_name = os.path.basename(cpath)
                    app.add_child(base_name, cpath)

    @classmethod
    def create_guidef(cls, automator, def_path):
        return GuiDef(automator, def_path)