"""
Code logic:
    The annotator first reads in the field names in the problem and stores them in a list to preseve the order of occurrence.
    Then, for each field, the annotator finds its max value length (for layout arrangement) and its type (list, str, dict...). 
    Lastly, it creates a dashboard, which consists of form widgets for each field (right) and a output preview area (left).
    Custom fields can also be inputted when instantiating an annotator using the following format: [(field_name1, type1, max_length1), (field_name2, type2, max_length2)].   
    E.g. [("aaa", list, 15), ("bbb", dict, 180)] 
"""

import json
import ipywidgets as widgets
from ast import literal_eval
from collections import OrderedDict
from .utility import string_to_list, list_to_string, most_common


class Annotator:
    """
    self.all_fields:           active + skip + filter
    self.fields_no_filter: active + skip
    self.active_fields:     active
    """
    def __init__(self, problems, custom_fields=None, skip_fields=None, filter_fields=None):
        
        # Normalize these three
        custom_fields = custom_fields if custom_fields else []
        skip_fields = skip_fields if skip_fields else []
        filter_fields = filter_fields if filter_fields else []
        
        self.all_fields, self.field_to_type, self.field_to_length= self._handle_field_info(problems, custom_fields) 
        self.fields_no_filter = [f for f in self.all_fields if f not in filter_fields] # active+skip fields
        self.active_fields = [f for f in self.fields_no_filter if f not in skip_fields] # active only
        self.problems = self._copy_problem_info(problems)
        self.current_index = 0
        
    
    
    def _handle_field_info(self, problems, custom_fields):
        """
        Read field information from the problems, filter the unwanted ones, and add custom ones
        Field information includes max length of the text of each field (for layout preparation) and the type of each field
        """

        all_fields = []
        field_to_type = {}
        field_to_length = {}
        
        
        # Get field names
        # To preserve order of the fields, we don't use set here
        for problem in problems:
            prob_fields = problem.keys()
            new_fields = [field for field in prob_fields if field not in all_fields]
            all_fields = all_fields + new_fields
  
        # Get their types and lengths
        for field in all_fields:
            field_to_type[field] = most_common([type(prob[field]) for prob in problems if field in prob])
            field_to_length[field] = max([len(str(prob[field])) for prob in problems if field in prob])
    
        # Handle custom fields
        for field, field_type, field_length in custom_fields:
            if field not in all_fields:
                all_fields.append(field)
                field_to_type[field] = field_type
                field_to_length[field] = field_length
    
        return all_fields, field_to_type, field_to_length

    
    def _copy_problem_info(self, problems):
        """
        Copy the problem information from input problems according to the collected field information
        """
        new_problems = []
        
        for prob in problems:
            new_prob = OrderedDict()
            
            for field in self.all_fields:
                field_type = self.field_to_type[field]
                if field in prob:
                    new_prob[field] = prob[field]
                else:
                    new_prob[field] = field_type()
            
            new_problems.append(new_prob)
        return new_problems
    
        
    def start(self):
        """Initialize the annotation environment and load the values from the current problem (the first problem)
        """
        self.initialize_dashboard()
        self.load_problem_info()

    
    def initialize_dashboard(self):
        """Initialize the annotation environment
        """
        height = 0
  
        # Form widgets
        layout_lg = widgets.Layout(flex='0 1 150px', height='100%', width='90%')
        layout_md = widgets.Layout(flex='0 1 50px', height='100%', width='90%')
        layout_sm = widgets.Layout(flex='0 1 20px', width='90%')        
        
        self.form_widgets = OrderedDict()
        for field in self.active_fields:
            if self.field_to_length[field] <= 20:
                layout = layout_sm
                height += 20
            elif self.field_to_length[field] <= 100:
                layout = layout_md
                height += 50
            else:
                layout = layout_lg
                height += 150
            self.form_widgets[field] = widgets.Textarea(description=f'{field.capitalize()}: ', layout=layout)

        # Buttons
        # The idea of these buttons takes reference from https://github.com/ideonate/jupyter-innotater
        prevbtn = widgets.Button(description='< Previous')
        nextbtn = widgets.Button(description='Next >')
        savebtn = widgets.Button(description='Save')
        restorebtn = widgets.Button(description='Restore')
        prevbtn.on_click(lambda _: self.change_index(-1))
        nextbtn.on_click(lambda _: self.change_index(1))
        savebtn.on_click(self._save)
        restorebtn.on_click(self._restore)
        buttons_layout = widgets.Layout(width='80%', height='35px')
        height += 50
        buttons = widgets.HBox([prevbtn, nextbtn, savebtn, restorebtn], layout=buttons_layout)
        
        # Dashboard
        form_layout = widgets.Layout(width='47%', justify_content ='space-around',  align_items='flex-end')
        preview_layout = widgets.Layout(width='43%')
        dashboard_layout = widgets.Layout(height=f'{height+15*len(self.active_fields)}px')
        form = widgets.VBox([*self.form_widgets.values(), buttons], layout=form_layout)
        form_output = widgets.interactive_output(self.display_func, self.form_widgets)
        preview = widgets.VBox([form_output], layout=preview_layout)
        dashboard = widgets.HBox([preview, form], layout=dashboard_layout)
        display(dashboard)
        
    def display_func(self, **form_widgets):
        """The display function for interactive_output widget
        """
        output = {}
        for field in self.fields_no_filter:
            field_type = self.field_to_type[field]
            if field in self.active_fields:
                if field_type == list:
                    output[field] = string_to_list(form_widgets[field])
                elif field_type == dict:
                    output[field] = literal_eval(form_widgets[field])
                elif field_type == int:
                    output[field] = int(form_widgets[field])
                elif field_type == float:
                    output[field] = float(form_widgets[field])
                else:
                    output[field] = form_widgets[field]
            else:
                    output[field] = self.problems[self.current_index][field]
        print(json.dumps(output, indent=4))

        
    def load_problem_info(self):
        """Load the field values of the current problem
        """
        current_problem = self.problems[self.current_index]
        for field in self.active_fields:
            field_type = self.field_to_type[field]
            if field_type==list:
                self.form_widgets[field].value = list_to_string(current_problem[field])
            elif field_type==dict:
                self.form_widgets[field].value = str(current_problem[field])
            elif field_type == int or field_type == float:
                self.form_widgets[field].value = str(current_problem[field])
            else:
                self.form_widgets[field].value = current_problem[field]
 
 
    def change_index(self, change):
        """Jump to the previous or next problem
        """
        if change < 0 < self.current_index:
            self.current_index -= 1
        elif change > 0 and self.current_index < len(self.problems) -1:
            self.current_index += 1
        
        # Reload the problem info
        self.load_problem_info()
            
            
    def _save(self, change):
        """Save the annotations back to the problem
        """
        current_problem = self.problems[self.current_index]
        for field in self.active_fields:
            field_type = self.field_to_type[field]
            if field_type == list:
                current_problem[field] = string_to_list(self.form_widgets[field].value)
            elif field_type == dict:
                current_problem[field] = literal_eval(self.form_widgets[field].value)
            elif field_type == int:
                current_problem[field] = int(self.form_widgets[field].value)
            elif field_type == float:
                current_problem[field] = float(self.form_widgets[field].value)
            else:
                current_problem[field] = self.form_widgets[field].value
        
        
    def _restore(self, change):
        """Restore 
        """
        # Reload the problem info
        self.load_problem_info()
        
       
    def dumps(self):
        pass