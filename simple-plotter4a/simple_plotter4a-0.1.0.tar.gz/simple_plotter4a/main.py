"""
main.py - kivy based front-end for simple_plotter
Copyright (C) 2020  Thies Hecker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from simple_plotter.core.code_generator import *

# import faulthandler
# faulthandler.enable()
import warnings
import os
import pathlib
import pkg_resources
import copy
import webbrowser

# increase double tap time for filechooser - 250 ms is to fast for Android
from kivy.config import Config
Config.set('postproc', 'double_tap_time', '2000')

import kivy
kivy.require('1.11.1')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import FocusBehavior
# FocusBehavior.keyboard_mode = 'managed'
from kivy.clock import Clock

from kivy.core.window import Window
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import platform

# get some android specific info, if we are Android
if platform == 'android':
    from android.storage import app_storage_path
    settings_path = app_storage_path()
    from android.storage import primary_external_storage_path
    primary_ext_storage = primary_external_storage_path()
    from android.storage import secondary_external_storage_path
    secondary_ext_storage = secondary_external_storage_path()


def check_valid_input(input_value):
    """Checks if an input value corresponds to a valid value - i.e. not None, "", "None",..."""

    if input_value is None or input_value == "" or input_value == "None":
        valid = False
    else:
        valid = True

    return valid


def open_url(*args):
    """Opens url"""
    webbrowser.open(args[1])


class FileDialog(Screen):

    def __init__(self, kivy_app, action, default_path=None, butLabel='Save'):
        """Opens a file chooser dialog and saves project file

        Args;
            kivy_app(KivyGui): parent GUI application
            action(function): A method or function to call, when a file is selected (the method must accept only one
                              argument, which is the filename(str)
            default_file(str): Default path - if none cwd() or external data storage path will be used (Android)
            butLabel(str): Label for the button, which starts the action (e.g. 'Save' or 'Open')
        """

        super().__init__()

        self.app = kivy_app
        self.default_path = default_path
        self.action = action

        # get current path
        if self.default_path is None:
            print('Platform is:', platform)
            if platform == 'android':
                project_path = primary_ext_storage
            else:
                project_path = str(os.getcwd())
        else:
            project_path = str(pathlib.Path(self.default_path).parent)

        # create new screen
        # self.file_screen = Screen()
        file_screen_layout = BoxLayout(padding=10, orientation='vertical')
        file_screen_layout.add_widget(Label(text='Select and double-tap to open folder / select file', size_hint_y=0.1))
        file_top_layout = BoxLayout(padding=10, orientation='horizontal', size_hint_y=0.1)
        txtFileName = TextInput(text='filename')
        butSave = Button(text=butLabel, size_hint_x=0.2)
        butSave.create_property('TextInput')
        butSave.TextInput = txtFileName
        butSave.bind(on_press=self.save_file)
        file_top_layout.add_widget(txtFileName)
        file_top_layout.add_widget(butSave)
        file_chooser = FileChooserIconView(size_hint_y=0.9, dirselect=True, show_hidden=True, path=project_path)
        file_chooser.create_property('TextInput')
        file_chooser.TextInput = txtFileName
        file_screen_layout.add_widget(file_top_layout)
        file_screen_layout.add_widget(file_chooser)
        self.add_widget(file_screen_layout)

        file_chooser.bind(on_entries_cleared=self.dir_select)
        file_chooser.bind(on_submit=self.file_select)
        self.app.sm.switch_to(self, direction='left')

        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

    def dir_select(self, instance, file_name=None, pos=None):
        """Updates the selected text field to the selected directory"""
        # print('Called by {}, value: {}, value2: {}'.format(instance, file_name, pos))
        print('Called by {} - current dir: {}'.format(instance, instance.path))
        instance.TextInput.text = instance.path

    def file_select(self, instance, file_names, pos):
        """Updates the text field to the selected file"""
        instance.TextInput.text = file_names[0]

    def save_file(self, instance):
        """Saves the file"""
        filename = instance.TextInput.text

        self.action(filename)

        # return to main screen
        self.app.sm.switch_to(self.app.screens[0], direction='right')


class CenteredTextInput(TextInput):

    def __init__(self, **kwargs):
        """A text input, which opens up a new full screen TextInput and vertically centers the returned text"""

        super().__init__(**kwargs)

        self.bind(focus=self.input_text)

        # unfortunately there seems to no event for finishing render of the UI widget, so all inputs will be centered
        # on the first touch event in the app...
        Window.bind(on_touch_down=self.center_text)

    def center_text(self, instance=None, value=None, pos=None):
        """Recalculates vertical padding to center text"""
        self.select_all()
        text_rows = self.cursor_row + 1
        pad_space = (self.height - text_rows * self.line_height) / 2
        print("Text rows: {}, box height: {}, line_height: {}, pad_space {}".format(text_rows, self.height,
                                                                                    self.line_height, pad_space))
        self.cancel_selection()
        self.padding[1] = pad_space
        self.padding[3] = pad_space
        self.scroll_y = 0
        Window.unbind(on_touch_down=self.center_text)

    def input_text(self, instance, focus):
        """Opens a text input at the top of the screen to input a value.

        Note:

            This method should be bound to the text inputs 'focus' event
        """
        if focus:
            print('Text input called by {} with text: {}'.format(self, self.text,))
            dialog_content = BoxLayout(padding=10, orientation='vertical')
            self.focus = False
            txtInput = TextInput(text=self.text, multiline=False, size_hint_y=0.3)
            txtInput.input_type = self.input_type
            # txtInput.show_keyboard()
            txtInput.create_property('caller')
            txtInput.caller = self
            dialog_content.add_widget(txtInput)
            popup = Popup(title='Enter value', content=dialog_content, auto_dismiss=True)
            txtInput.create_property('popup')
            txtInput.popup = popup
            txtInput.bind(on_text_validate=self.return_input_text)
            popup.create_property('txtInput')
            popup.txtInput = txtInput
            popup.bind(on_open=self.set_focus)
            popup.open()

    def set_focus(self, instance):
        instance.txtInput.focus = True
        if instance.txtInput.text == 'None':
            instance.txtInput.select_all()

    def return_input_text(self, instance):
        """Returns the text of an input and closes the pop-up"""
        instance.caller.text = instance.text
        instance.caller.center_text()
        instance.popup.dismiss(force=True)


# class CenteredTextInput(Label):
#
#     def __init__(self, **kwargs):
#         """A text input with vertically centered text"""
#
#         if 'text' in kwargs:
#             print(kwargs['text'])
#             reftext = '[ref=]{}[/ref]'.format(kwargs['text'])
#         else:
#             reftext = '[ref=]None[/ref]'
#         self.__text = reftext
#
#         super().__init__()
#
#         # self.text = 'a[ref=test]{}[/ref]a'.format(kwargs['text'])
#         self.markup = True
#         print(self.text)
#
#         self.color = [1, 0, 0, 1]
#         # self.canvas.color = [0, 1, 1, 1]
#         # self.bind(text=self.center_text)
#         # self.bind(focus=self.center_text)
#         self.bind(on_ref_press=self.input_text)
#
#         if 'input_type' in kwargs:
#             self.input_type = kwargs['input_type']
#         else:
#             self.input_type = 'text'
#         # self.bind(on_draw=self.center_text)
#
#         # self.register_event_type('on_center_text')
#         # self.center_text()
#
#     @property
#     def text(self):
#         return self.__text
#
#     def get_formatted_text(self):
#         text = self.__text.split('[ref=]')[1].split('[/ref]')[0]
#         return text
#
#     @text.setter
#     def text(self, text):
#         self.__text = '[ref=]{}[/ref]'.format(text)
#         self.text_size = [self.width, None]
#         self.texture_update()
#
#     def center_text(self, instance=None, value=None, pos=None):
#         """Recalculates vertical padding to center text"""
#         # self.select_all()
#         # text_rows = self.cursor_row + 1
#         # pad_space = (self.height - text_rows * self.line_height) / 2
#         # print("Text rows: {}, box height: {}, line_height: {}, pad_space {}".format(text_rows, self.height,
#         #                                                                             self.line_height, pad_space))
#         # self.cancel_selection()
#         # self.padding[1] = pad_space
#         # self.padding[3] = pad_space
#         # self.scroll_y = 0
#
#     def input_text(self, *args):
#         """Opens a text input at the top of the screen to input a value.
#
#         Note:
#
#             This method should be bound to the text inputs 'focus' event
#         """
#         # if focus:
#         print('Text input called by {} with text: {}'.format(self, self.text,))
#         dialog_content = BoxLayout(padding=10, orientation='vertical')
#         # self.focus = False
#         txtInput = TextInput(text=self.get_formatted_text(), multiline=False, size_hint_y=0.3)
#         txtInput.input_type = self.input_type
#         # txtInput.show_keyboard()
#         txtInput.create_property('caller')
#         txtInput.caller = self
#         dialog_content.add_widget(txtInput)
#         popup = Popup(title='Enter value', content=dialog_content, auto_dismiss=True)
#         txtInput.create_property('popup')
#         txtInput.popup = popup
#         txtInput.bind(on_text_validate=self.return_input_text)
#         popup.create_property('txtInput')
#         popup.txtInput = txtInput
#         popup.bind(on_open=self.set_focus)
#         popup.open()
#
#     def set_focus(self, instance):
#         instance.txtInput.focus = True
#         if instance.txtInput.text == 'None':
#             instance.txtInput.select_all()
#
#     def return_input_text(self, instance):
#         """Returns the text of an input and closes the pop-up"""
#         instance.caller.text = instance.text
#         # instance.caller.center_text()
#         instance.popup.dismiss(force=True)
#         # instance.hide_keyboard()
#         # self.readGUIInputs()
#         # instance.popup.parent.remove_widget(instance.popup)
#         # self.sm.switch_to(self.screens[0], direction='right')


class KivyGui(App):

    def __init__(self, data_handler, version, base_version):
        """kivy-based GUI for simple-plotter

        Args:
            data_handler(simple_plotter.core.code_generator.DataHandler): Data handler
            version(str): Version string for simple_plotter4a (kivy-GUI)
            base_version(str): Version string for simple_plotter (base package)
        """
        self.version = version
        self.base_version = base_version
        self.ConstList = []
        self.xpos = []
        self.ypos = []
        self.data_handler = data_handler
        self.projectfile = None
        self.screens = []
        self.const_table_header_items = ['Const. name', 'Value', 'Unit', 'Comment', '']
        self.version = version

        self.data_path = Path(__file__).parent / "data"
        print('Data path:', self.data_path)

        super().__init__()

    def build(self):
        """Initializes the GUI"""

        print('Operating system:', os.name)

        self.sm = ScreenManager()

        # scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        accordion = Accordion(orientation='vertical')

        # main screen for plot inputs
        home_screen_name = 'Plot config'
        input_screen = Screen(name=home_screen_name)

        # input_screen.bind(on_enter=self.refreshGUI)

        self.screens.append(input_screen)

        self.main_layout = BoxLayout(padding=10, orientation='vertical')

        # add main buttons - plot, save, load, export
        main_buttons = BoxLayout(padding=10, orientation='horizontal', size_hint_y=0.2)
        plotButton = Button(text='Plot')
        # plotButton.setToolTip('Creates a plot')
        saveButton = Button(text='Save')
        # saveButton.setToolTip('Save the project to a file')
        loadButton = Button(text='Load')
        # loadButton.setToolTip('Load a project from file')
        exportButton = Button(text='Export code')
        # exportButton.setToolTip('Export project to python code file')

        plotButton.bind(on_press=self.plotButClicked)
        saveButton.bind(on_press=self.open_save_project_dialogue)
        loadButton.bind(on_press=self.open_load_project_dialogue)
        exportButton.bind(on_press=self.open_export_plotcode_dialogue)

        main_buttons.add_widget(saveButton)
        main_buttons.add_widget(loadButton)
        main_buttons.add_widget(exportButton)
        main_buttons.add_widget(plotButton)

        self.main_layout.add_widget(main_buttons)

        self.main_layout.add_widget(Label(text='Use \'np.\' - e.g. np.sin(x) - to access numpy methods',
                                          size_hint_y=0.1))

        # add equation inputs
        # -------------------

        layout_eq = BoxLayout(padding=10, orientation='horizontal', size_hint_y=0.2)

        self.lefunctionName = CenteredTextInput(text=str(self.data_handler.formula.function_name), size_hint_x=0.2,
                                                halign='center')
        self.levarName = CenteredTextInput(text=str(self.data_handler.formula.var_name), size_hint_x=0.2,
                                           halign='center')
        self.leFormula = CenteredTextInput(text=str(self.data_handler.formula.equation), size_hint_x=0.5)

        layout_eq.add_widget(self.lefunctionName)
        layout_eq.add_widget(Label(text='(', size_hint_x=0.05))
        layout_eq.add_widget(self.levarName)
        layout_eq.add_widget(Label(text=')=', size_hint_x=0.05))
        layout_eq.add_widget(self.leFormula)

        self.main_layout.add_widget(layout_eq)

        # constants
        # ---------

        item_constants = AccordionItem(title='Constants')

        layout_constants = BoxLayout(padding=10, orientation='vertical')

        layout_const_buttons = BoxLayout(padding=10, orientation='horizontal', size_hint_y=0.2)
        butAddConstant = Button(text='Add')
        butAddConstant.bind(on_press=self.add_constant)
        layout_const_buttons.add_widget(butAddConstant)
        layout_constants.add_widget(layout_const_buttons)

        self.layout_const_table = GridLayout(padding=10, cols=5, row_default_height=80, row_force_default=True,
                                             size_hint_y=None)
        self.layout_const_table.bind(minimum_height=self.layout_const_table.setter('height'))

        for item in self.const_table_header_items:
            self.layout_const_table.add_widget(Label(text=item))

        const_table_view = ScrollView(size_hint=(1, 0.8), # size=(300, 100),
                                      scroll_type=['bars', 'content'], bar_width=20,
                                      do_scroll_x=False, do_scroll_y=True)
        const_table_view.add_widget(self.layout_const_table)

        layout_constants.add_widget(const_table_view)

        #self.main_layout.add_widget(layout_constants)

        item_constants.add_widget(layout_constants)

        accordion.add_widget(item_constants)

        # plot labels (units, title)
        # --------------------------

        item_vardef = AccordionItem(title='Plot labels')
        layout_vardef = GridLayout(padding=10, cols=2)

        lblVarUnit = Label(text='Unit x:')
        lblUnit = Label(text='Unit y:')
        self.leVarUnit = CenteredTextInput(text=str(self.data_handler.formula.var_unit))
        self.leFuncUnit = CenteredTextInput(text=str(self.data_handler.formula.function_unit)) # , multiline=False)
        lbl_plot_title = Label(text='Plot title:')
        self.le_plot_title = CenteredTextInput(text=str(self.data_handler.plot_data.plot_title))

        # self.leVarUnit.bind(focus=self.input_text)
        # self.leFuncUnit.bind(focus=self.input_text)
        # self.le_plot_title.bind(focus=self.input_text)

        layout_vardef.add_widget(lblVarUnit)
        layout_vardef.add_widget(self.leVarUnit)
        layout_vardef.add_widget(lblUnit)
        layout_vardef.add_widget(self.leFuncUnit)
        layout_vardef.add_widget(lbl_plot_title)
        layout_vardef.add_widget(self.le_plot_title)
        # var_const_group.setLayout(layout_vardef)
        # self.main_layout.add_widget(layout_vardef)
        item_vardef.add_widget(layout_vardef)
        accordion.add_widget(item_vardef)
        
        # curve set constants
        # -------------------

        item_sets = AccordionItem(title='Curve set parameters')
        layout_sets = GridLayout(padding=10, cols=3)

        lblsetvarName = Label(text='Set constant name:')
        self.lesetvarName = CenteredTextInput(text=str(self.data_handler.formula.set_var_name))
        lblsetStartVal = Label(text='min:')
        self.lesetStartVal = CenteredTextInput(text=str(self.data_handler.formula.set_min_val)) #, input_type='number')
        self.lesetStartVal.input_type = 'number'
        lblsetEndVal = Label(text='max:')
        self.lesetEndVal = CenteredTextInput(text=str(self.data_handler.formula.set_max_val)) #, input_type='number')
        lblsetNoPts = Label(text='No. of curve sets:')
        self.lesetNoPts = CenteredTextInput(text=str(self.data_handler.formula.no_sets)) #, input_type='number')
        lblsetUnit = Label(text='Unit:')
        self.leSetUnit = CenteredTextInput(text=str(self.data_handler.formula.set_var_unit))
        lblSetListValues = Label(text='Explicit set const. values:', text_size=[0.3 * Window.width, None])
        self.leSetConstValues = CenteredTextInput(text=str(self.data_handler.formula.explicit_set_values)) #,
                                                 #  input_type='number')
        lblInfoExplicit = Label(text='This will override min./max.and number of sets', text_size=[0.3 * Window.width,
                                                                                                  None])

        layout_sets.add_widget(lblsetvarName)
        layout_sets.add_widget(self.lesetvarName)
        layout_sets.add_widget(Label(text=''))
        layout_sets.add_widget(Label(text='min./max. value:'))
        layout_sets.add_widget(self.lesetStartVal)
        layout_sets.add_widget(self.lesetEndVal)
        layout_sets.add_widget(lblsetNoPts)
        layout_sets.add_widget(self.lesetNoPts)
        layout_sets.add_widget(Label(text=''))
        layout_sets.add_widget(lblsetUnit)
        layout_sets.add_widget(self.leSetUnit)
        layout_sets.add_widget(Label(text=''))
        layout_sets.add_widget(lblSetListValues)
        layout_sets.add_widget(self.leSetConstValues)
        layout_sets.add_widget(lblInfoExplicit)

        # self.main_layout.add_widget(layout_sets)
        item_sets.add_widget(layout_sets)
        accordion.add_widget(item_sets)

        # add elements for plot config
        # ----------------------------

        # group_plotconf = QGroupBox("Plot settings")
        item_plot_options = AccordionItem(title='Plot settings')
        layout_plotconf = BoxLayout(padding=10, orientation='vertical')

        layout_plotconf_s1 = GridLayout(padding=10, cols=3, size_hint_y=0.8)

        lblXScale = Label(text='x-scale:')
        self.butXscale_lin = ToggleButton(text='lin.', group='x_scale', state='down', allow_no_selection=False)
        self.butXscale_log = ToggleButton(text='log.', group='x_scale', allow_no_selection=False)

        lblYScale = Label(text='y-scale:')
        self.butYscale_lin = ToggleButton(text='lin.', group='y_scale', state='down', allow_no_selection=False)
        self.butYscale_log = ToggleButton(text='log.', group='y_scale', allow_no_selection=False)

        layout_plotconf_s1.add_widget(lblXScale)
        layout_plotconf_s1.add_widget(self.butXscale_lin)
        layout_plotconf_s1.add_widget(self.butXscale_log)
        layout_plotconf_s1.add_widget(lblYScale)
        layout_plotconf_s1.add_widget(self.butYscale_lin)
        layout_plotconf_s1.add_widget(self.butYscale_log)

        self.xySwapToggle = ToggleButton(text='Swap XY')

        self.gridToggle = ToggleButton(text='Show grid')

        lbl_xminmax = Label(text='x min./max.:')
        self.leStartVal = CenteredTextInput(text=str(self.data_handler.plot_data.start_val)) #, input_type='number')
        self.leEndVal = CenteredTextInput(text=str(self.data_handler.plot_data.end_val)) #, input_type='number')

        lblNoPts = Label(text='Data points:')
        self.leNoPts = CenteredTextInput(text=str(self.data_handler.plot_data.no_pts)) #, input_type='number')

        lbl_yminmax = Label(text='y min./max.:')
        self.le_ymin = CenteredTextInput(text=str(self.data_handler.plot_data.y_min)) #, input_type='number')
        self.le_ymax = CenteredTextInput(text=str(self.data_handler.plot_data.y_max)) #, input_type='number')

        layout_plotconf_s1.add_widget(Label(text=''))
        # TODO: re-implemment XY swap functionality for kivy front-end, if really needed...
        # layout_plotconf_s1.add_widget(self.xySwapToggle)
        layout_plotconf_s1.add_widget(self.gridToggle)
        layout_plotconf_s1.add_widget(Label(text=''))
        # # layout_plotconf.add_widget(self.csvExpToggle, 0, 4)

        layout_plotconf_s1.add_widget(lbl_xminmax)
        layout_plotconf_s1.add_widget(self.leStartVal)
        layout_plotconf_s1.add_widget(self.leEndVal)

        layout_plotconf_s1.add_widget(lblNoPts)
        layout_plotconf_s1.add_widget(self.leNoPts)
        layout_plotconf_s1.add_widget(Label(text=''))

        layout_plotconf_s1.add_widget(lbl_yminmax)
        layout_plotconf_s1.add_widget(self.le_ymin)
        layout_plotconf_s1.add_widget(self.le_ymax)

        layout_plotconf.add_widget(layout_plotconf_s1)

        item_plot_options.add_widget(layout_plotconf)
        accordion.add_widget(item_plot_options)

        # add about item
        item_about = AccordionItem(title='About')
        about_layout = BoxLayout(orientation='vertical', padding=10)

        version_text = 'simple-plotter4a v{}' \
                       '\n(built on simple-plotter base v{})' \
                       '\nCopyright (c) 2019-2020 Thies Hecker'.format(self.version, self.base_version)

        about_layout.add_widget(Label(text=version_text))

        butHelp = Button(text='Open Help')
        about_layout.add_widget(butHelp)
        butHelp.fbind('on_press', open_url, None, 'https://simple-plotter.readthedocs.io/en/latest/index.html')
        butLicenseInfo = Button(text='Show license information')
        about_layout.add_widget(butLicenseInfo)

        butLicenseInfo.bind(on_press=self.show_license_screen)

        item_about.add_widget(about_layout)

        accordion.add_widget(item_about)

        # finalize accordion, screen manager
        self.main_layout.add_widget(accordion)

        accordion.select(item_plot_options)

        input_screen.add_widget(self.main_layout)

        self.sm.add_widget(input_screen)

        # Window events
        # -------------

        # keyboard events
        # This is required to capture the Android 'back'-button (which is interpreted as Escape - keycode 27
        Window.bind(on_keyboard=self.key_input)

        # Window resize for alignement of text in CenteredTextInputs (only required for desktop)
        Window.bind(on_cursor_enter=self.center_text_inputs)
        # self.bind(on_resize=self.refreshGUI)  # works but is extremely slow
        Window.bind(on_maximize=self.center_text_inputs)

        return self.sm

    def init_gui(self, *args):
        """initiates the GUI elements"""
        self.refreshGUI()
        Window.unbind(on_draw=self.init_gui)

    def key_input(self, window, key, scancode, codepoint, modifier):
        """Handle key input - e.g. Android back button (escape)"""
        # this is escape or the Android back button
        if key == 27:
            self.return_home(None)
            try:
                self.scroll_clock.cancel()  # avoid license scroll speed-up
            except AttributeError:
                pass
            return True
        else:
            return False

    def read_const_table(self):
        """Reads the entries from the const table"""

        # get number of const entries
        cols = self.layout_const_table.cols
        no_entries = int(len(self.layout_const_table.children) / cols - 1)   # substract 1 for header

        header_items = copy.copy(self.const_table_header_items)
        header_items.reverse()

        constants = []
        for i in range(no_entries):
            item_dict = {}
            for j in range(cols):
                child = self.layout_const_table.children[i*cols + j]
                if j > 0:  # first column is delete button
                    item_dict[header_items[j]] = child.text
                    print(item_dict)
            constants.append(item_dict)

        return constants

    def readGUIInputs(self, *args):
        """
        reads the constants, start-endval and formula from GUI
        """
        constants = self.read_const_table()
        print(constants)

        self.data_handler.formula.constants = constants
        self.data_handler.plot_data.start_val = self.leStartVal.text
        self.data_handler.plot_data.end_val = self.leEndVal.text
        self.data_handler.formula.equation = self.leFormula.text
        self.data_handler.formula.function_name = self.lefunctionName.text
        self.data_handler.formula.function_unit = self.leFuncUnit.text
        self.data_handler.plot_data.no_pts = self.leNoPts.text
        self.data_handler.formula.var_name = self.levarName.text
        self.data_handler.formula.var_unit = self.leVarUnit.text
        self.data_handler.formula.set_min_val = self.lesetStartVal.text
        self.data_handler.formula.set_max_val = self.lesetEndVal.text
        self.data_handler.formula.no_sets = self.lesetNoPts.text
        self.data_handler.formula.set_var_name = self.lesetvarName.text
        self.data_handler.formula.set_var_unit = self.leSetUnit.text
        self.data_handler.formula.explicit_set_values = self.leSetConstValues.text
        self.data_handler.plot_data.x_log = True if self.butXscale_log.state == 'down' else False
        self.data_handler.plot_data.y_log = True if self.butYscale_log.state == 'down' else False
        self.data_handler.plot_data.swap_xy = True if self.xySwapToggle.state == 'down' else False
        # self.data_handler.export_csv = self.csvExpToggle.isChecked()
        self.data_handler.plot_data.grid = True if self.gridToggle.state == 'down' else False
        self.data_handler.plot_data.y_min = self.le_ymin.text
        self.data_handler.plot_data.y_max = self.le_ymax.text
        self.data_handler.plot_data.plot_title = self.le_plot_title.text
    
    @staticmethod
    def get_str_from_datahandler(dh_property):
        """Returns a string from a data handler property"""
        
        return 'None' if str(dh_property) == 'None' else str(dh_property)
        
    def refreshGUI(self, instance=None):
        """
        resets and freshes text fields in GUI (retrieves data from data_handler)
        """
        self.leStartVal.text = self.get_str_from_datahandler(self.data_handler.plot_data.start_val)
        self.leEndVal.text = self.get_str_from_datahandler(self.data_handler.plot_data.end_val) 
        self.leFormula.text = self.get_str_from_datahandler(self.data_handler.formula.equation)
        self.lefunctionName.text = self.get_str_from_datahandler(self.data_handler.formula.function_name)
        self.leFuncUnit.text = self.get_str_from_datahandler(self.data_handler.formula.function_unit)
        self.leNoPts.text = self.get_str_from_datahandler(self.data_handler.plot_data.no_pts)
        self.levarName.text = self.get_str_from_datahandler(self.data_handler.formula.var_name)
        self.leVarUnit.text = self.get_str_from_datahandler(self.data_handler.formula.var_unit)
        self.lesetStartVal.text = self.get_str_from_datahandler(self.data_handler.formula.set_min_val)
        self.lesetEndVal.text = self.get_str_from_datahandler(self.data_handler.formula.set_max_val)
        self.lesetNoPts.text = self.get_str_from_datahandler(self.data_handler.formula.no_sets)
        self.lesetvarName.text = self.get_str_from_datahandler(self.data_handler.formula.set_var_name)
        self.leSetUnit.text = self.get_str_from_datahandler(self.data_handler.formula.set_var_unit)
        self.leSetConstValues.text = self.get_str_from_datahandler(self.data_handler.formula.explicit_set_values)
        self.butXscale_log.state = 'down' if self.data_handler.plot_data.x_log else 'normal'
        self.butXscale_lin.state = 'normal' if self.data_handler.plot_data.x_log else 'down'
        self.butYscale_log.state = 'down' if self.data_handler.plot_data.y_log else 'normal'
        self.butYscale_lin.state = 'normal' if self.data_handler.plot_data.y_log else 'down'
        self.xySwapToggle.state = 'down' if self.data_handler.plot_data.swap_xy else 'normal'
        self.gridToggle.state = 'down' if self.data_handler.plot_data.grid else 'normal'
        # self.csvExpToggle.setChecked(self.data_handler.export_csv)
        self.le_ymin.text = self.get_str_from_datahandler(self.data_handler.plot_data.y_min)
        self.le_ymax.text = self.get_str_from_datahandler(self.data_handler.plot_data.y_max)
        self.le_plot_title.text = self.get_str_from_datahandler(self.data_handler.plot_data.plot_title)

        # delete constants table
        self.clear_constants()

        # new write constants from constants dictionary into table
        for i, const_set in enumerate(self.data_handler.formula.constants):
            const_name = const_set['Const. name']
            value = const_set['Value']
            unit = const_set['Unit']
            comment = const_set['Comment']
            self.add_constant(None, const_name, value, unit, comment)

        self.center_text_inputs()

    def center_text_inputs(self, *args):
        # center all CenteredTextInput widgets
        self.leStartVal.center_text()
        self.leEndVal.center_text()
        self.leFormula.center_text()
        self.lefunctionName.center_text()
        self.leFuncUnit.center_text()
        self.leNoPts.center_text()
        self.levarName.center_text()
        self.leVarUnit.center_text()
        self.lesetStartVal.center_text()
        self.lesetEndVal.center_text()
        self.lesetNoPts.center_text()
        self.lesetvarName.center_text()
        self.leSetUnit.center_text()
        self.leSetConstValues.center_text()
        self.le_ymin.center_text()
        self.le_ymax.center_text()
        self.le_plot_title.center_text()

        #FIXME: centering of constant text labels does not work...
        # for txtinput in self.layout_const_table.children:
        #     if type(txtinput) == CenteredTextInput:
        #         txtinput.center_text()

    def return_home(self, instance):
        """Go back to main screen"""
        self.sm.switch_to(self.screens[0], direction='right')

    def plotButClicked(self, instance):
        """
        read GUI inputs and plot graph
        """
        self.readGUIInputs()
        error_codes, error_logs = self.data_handler.plot()

        if error_codes:
            error_msg = ""
            for i, code in enumerate(error_codes):
                error_msg += "Error code: {} - {}\n".format(code, self.data_handler.error_codes[code])
                for log in error_logs[i]:
                    error_msg += "   " + log + "\n"
                # add line breaks for long error messages
                # new_error_msg = ''
                # max_length = 200
                # if len(error_msg) > max_length:
                #     for i in range(int(len(error_msg)/max_length)):
                #         if i == 0:
                #             new_error_msg = new_error_msg + '\n' + error_msg[0:max_length]
                #         else:
                #             new_error_msg = new_error_msg + '\n' + error_msg[i*max_length:(i+1)*max_length]
                #     new_error_msg = new_error_msg + '\n' + error_msg[(i+1)*max_length:]
                #     error_msg = new_error_msg

            # QMessageBox.critical(self, "Plot code generator error", error_msg)
            dialog_content = BoxLayout(padding=10, orientation='vertical')
            error_label = Label(text=error_msg, text_size=[900, None])
            butClose = Button(text='Close', size_hint_y=0.2)
            dialog_content.add_widget(error_label)
            dialog_content.add_widget(butClose, )
            popup = Popup(title='Plot code generator error', content=dialog_content, auto_dismiss=False)
            butClose.bind(on_press=popup.dismiss)
            popup.open()
        else:
            # a new screen for each plot will be created
            screen_layout = BoxLayout(padding=10, orientation='vertical')

            # Buttons are currently really require - back button is used to return to main menu...
            # button_row = BoxLayout(padding=10, orientation='horizontal', size_hint_y=0.1)
            #
            # butClose = Button(text='Close')
            # button_row.add_widget(butClose)
            # butHome = Button(text='Home')
            # button_row.add_widget(butHome)

            # butHome.bind(on_press=self.return_home)
            #
            # screen_layout.add_widget(button_row)

            screen_name = 'Plot {}'.format(len(self.screens))
            plot_screen = Screen(name=screen_name)

            code_str = self.data_handler.combine_code()
            print(code_str)
            # graph = Graph()

            if self.data_handler.plot_lib == 'matplotlib':
                if 'plt' not in locals():
                    import matplotlib.pyplot as plt
                    from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
            else:  # assume this uses kivy-garden/graph
                if 'AnnotatedLinePlot' not in locals():
                    from simple_plotter.core.advanced_graph import AnnotatedLinePlot

            if self.data_handler.plot_lib == 'matplotlib':
                plt.figure()
                exec(code_str)
                plot_canvas = FigureCanvasKivyAgg(plt.gcf())
            elif self.data_handler.plot_lib == 'kivy-garden/graph':
                exec(code_str)
                plot_canvas = locals()['graph']
            else:
                raise ValueError('Unsupported plotting library: {}'.format(self.data_handler.plot_lib))

            screen_layout.add_widget(plot_canvas)

            plot_screen.add_widget(screen_layout)
            self.screens.append(plot_screen)

            self.sm.add_widget(plot_screen)

            self.sm.switch_to(self.screens[-1], direction='left')

    def add_constant(self, instance=None, const_name=None, value=None, unit=None, comment=None):
        """Adds a new constant row to the constants table

        Note:
            To adjust the row height change row_default_height for the layout_const_table in self.build!
        """
        # add for text inputs (i.e. const. name, value, unit and comment
        const_data = [const_name, value, unit, comment]

        for data in const_data:
            if data:
                txtInput = CenteredTextInput(text=data)
            else:
                txtInput = CenteredTextInput()
            # txtInput.bind(focus=self.input_text)
            self.layout_const_table.add_widget(txtInput)

        butRemove = Button(text='X')
        butRemove.bind(on_press=self.remove_constant)
        self.layout_const_table.add_widget(butRemove)


    def remove_constant(self, instance):
        """Removes a constant definition"""
        cols = self.layout_const_table.cols

        # for child in self.layout_const_table.children:
        #     print(child)

        # get row idx
        widgets_to_remove = []
        for i, child in enumerate(self.layout_const_table.children):
            if instance == child:
                row_idx = int(i/cols)
                for j in range(cols):
                    child_widget = self.layout_const_table.children[i + j]
                    widgets_to_remove.append(child_widget)
                break

        for widget in widgets_to_remove:
            self.layout_const_table.remove_widget(widget)

        print('Const. definition {} removed.'.format(row_idx))

    def clear_constants(self):
        """Clears all constants"""
        cols = self.layout_const_table.cols

        no_widgets_to_remove = len(self.layout_const_table.children) - cols

        for i in range(no_widgets_to_remove):
            self.layout_const_table.remove_widget(self.layout_const_table.children[0])

        print('Const. table cleared - {} const. definitions removed.'.format(no_widgets_to_remove))

    def open_save_project_dialogue(self, instance):
        """Opens a save project_dialogue"""
        FileDialog(kivy_app=self, action=self.save_project_file, default_path=self.projectfile, butLabel='Save')

    def open_load_project_dialogue(self, instance):
        """Opens a load project_dialogue"""
        FileDialog(kivy_app=self, action=self.load_project_file, default_path=self.projectfile, butLabel='Open')

    def open_export_plotcode_dialogue(self, instance):
        """Opens a export plot code_dialogue"""
        FileDialog(kivy_app=self, action=self.export_code, default_path=self.projectfile, butLabel='Export')

    def save_project_file(self, filename):
        """Saves the file"""
        self.readGUIInputs()

        if filename not in ['', None]:
            self.projectfile = filename
            self.data_handler.save_project(filename)
            
    def export_code(self, filename):
        """Export the python code of the current project to a file"""
        self.readGUIInputs()

        if filename not in ['', None]:
            self.data_handler.write_py_file(filename)
            
    def load_project_file(self, filename):
        """Loads a project from a file"""

        if filename not in ['', None]:
            self.projectfile = filename
            self.data_handler.load_project(filename)
            self.refreshGUI()

    def show_license_screen(self, *args):
        """Shows the license screen"""

        license_screen = Screen()

        license_screen_layout = BoxLayout(orientation='vertical')

        credits_text = 'simple-plotter4a v{}' \
                       '\n(built on simple-plotter base v{})' \
                       '\nCopyright (c) 2019-2020 Thies Hecker' \
                       '\n' \
                       '\nReleased under the [ref=https://www.gnu.org/licenses/gpl-3.0-standalone.html][color=AAAAEE]' \
                       'GNU GPLv3+ license[/color][/ref]' \
                       '\n' \
                       '\nVisit the project homepage for help and further information:' \
                       '\n[ref=https://simple-plotter.readthedocs.io/en/latest/license.html][color=AAAAEE]' \
                       'https://simple-plotter.readthedocs.io/en/latest/license.html[/color][/ref]' \
                       '\n\nsimple_plotter4a is build on following 3rd party components:\n\n'.format(self.version,
                                                                                                     self.base_version)

        credits_label = Label(text=credits_text, markup=True, text_size=[0.95 * Window.width, None], halign='center')
        credits_label.texture_update()
        credits_label.height = credits_label.texture_size[1]

        credits_label.bind(on_ref_press=open_url)

        license_screen_layout.add_widget(credits_label)

        if platform == 'android':
            attr_file = 'attributions_android_{}.txt'.format(self.version)
        else:
            attr_file = 'attributions_python_{}.txt'.format(self.version)

        try:
            with open(self.data_path / attr_file, 'r') as file:
                attr_str = file.read()
        except FileNotFoundError:
            raise FileNotFoundError('Could not find the attributions text file for version {}.'
                                    'Make sure you have correctly defined '
                                    'the dependencies and run the \'create_attributions.py\' script!'.format(self.version))

        attr_label = Label(text=attr_str, markup=True, size_hint_y=None, text_size=[0.95 * Window.width, None],
                           halign='center')
        attr_label.texture_update()
        attr_label.height = attr_label.texture_size[1]

        self.credits_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-credits_label.height),
                                       scroll_type=['bars', 'content'], bar_width=20,
                                       do_scroll_x=False, do_scroll_y=True)

        self.credits_view.add_widget(attr_label)
        license_screen_layout.add_widget(self.credits_view)

        license_screen.add_widget(license_screen_layout)

        self.sm.add_widget(screen=license_screen)
        self.sm.switch_to(license_screen, direction='up')

        Clock.schedule_once(self.start_scroll_license, 2.)

    def start_scroll_license(self, *args):
        """Starts the scroller"""
        # Clock.max_iteration = 100
        self.scroll_clock = Clock.schedule_interval(self.scroll_licenses, 0.1)

    def scroll_licenses(self, *args):
        """Scrolls the licenses"""
        if self.credits_view.scroll_y > 0:
            self.credits_view.scroll_y -= 0.001
        else:
            self.scroll_clock.cancel()


def start_mpl():
    """Entry point with matplotlib as plotting library"""

    __version__, base_version = get_versions()

    formula1 = Formula()
    plot_data1 = PlotData()

    cc = setup_code_checker()
    data_handler1 = DataHandler(formula1, plot_data1, code_checker=cc, plot_lib='matplotlib')

    gui1 = KivyGui(data_handler1, __version__, base_version)

    gui1.run()


def start_garden_graph():
    """Entry point with kivy-garden.graph based plotting library"""

    __version__, base_version = get_versions()

    formula1 = Formula()
    plot_data1 = PlotData()

    cc = setup_code_checker()
    data_handler1 = DataHandler(formula1, plot_data1, code_checker=cc, plot_lib='kivy-garden/graph')

    gui1 = KivyGui(data_handler1, __version__, base_version)

    gui1.run()


def get_versions():
    """tuple: Extracts and returns the package version simple_plotter4a and simple_plotter (base)"""

    # get version string
    try:
        __version__ = pkg_resources.get_distribution('simple_plotter4a').version  # if this is an installed package
    except UnboundLocalError:
        try:
            __package__ = 'simple_plotter4a'
            from simple_plotter4a import __version__
        except ImportError:
            try:
                with open('version.txt', 'r') as file:
                    __version__ = file.read()
            except FileNotFoundError:
                print('Could not identify version...')
                __version__ = '0.0.0'

    # get the version of simple-plotter (base package)
    base_version = pkg_resources.get_distribution('simple_plotter').version
    # try:
    #     version = __version__  # version from source code repo
    # except LookupError:
    #     version = pkg_resources.get_distribution(name).version  # if this is an installed package

    return __version__, base_version


def setup_code_checker():
    """CodeChecker: Sets up the code checker"""

    # code checker setup
    allowed_imports = ['numpy', 'matplotlib.pyplot', 'csv', 'simple_plotter.core.advanced_graph']
    allowed_calls = ['f', 'str', 'Graph', 'MeshLinePlot', 'range', 'len', 'append', 'min', 'max', 'int', 'check_value',
                     'enumerate', 'float', 'AnnotatedLinePlot']
    allowed_FunctionDefs = ['f', 'check_value']
    allowed_aliases = ['np', 'plt', 'points', 'graph', 'x_values', 'y_values', 'xy_values', 'kv', 'kv_graph']
    allowed_names = ['points', 'xy0']
    cc = CodeChecker(allowed_imports=allowed_imports, allowed_calls=allowed_calls, allowed_names=allowed_names,
                     allowed_aliases=allowed_aliases, allowed_FunctionDefs=allowed_FunctionDefs)

    return cc


if __name__ == '__main__':
    # default plotting library is garden.graph
    start_garden_graph()
    # start_mpl()
