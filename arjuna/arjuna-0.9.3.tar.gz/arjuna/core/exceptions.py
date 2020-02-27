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

from arjuna.interact.gui.auto.finder.emd import GuiElementMetaData

class ArjunaException(Exception):
    def __init__(self, message, scrreenshots_path=None, child=None):
        # child is child exception
        super().__init__(message)

        self.screenshot_path = scrreenshots_path
        self.child_Exceptions = []
        if child:
            try:
                raise child
            except ArjunaException as e:
                self.__extract_child_Exceptions(e);
                # } catch (java.lang.reflect.Invocation_target_exception f) {
                #     if (ArjunaException.class.is_assignable_from(f.get_target_exception().get_class())) {
                #         ArjunaException z = (ArjunaException) f.get_target_exception();
                #         extract_child_Exceptions(z);
                #     } else {
                #         insert_child_Exception(f);
                #     }
            except Exception as f:
                self.__insert_child_Exception(f);

    def contains_screenshot(self):
        return self.screenshot_path is not None

    def get_screenshot_path(self):
        return self.screenshot_path

    def set_screenshot_path(self, path):
        self.screenshot_path = path

    def __insert_child_Exception(self, e):
        self.child_Exceptions.append(e)

    def __extract_child_Exceptions(self, e):
        child_Exceptions = e.get_child_Exceptions()
        self.child_Exceptions.extend(child_Exceptions)

    def get_child_Exceptions(self):
        return self.child_Exceptions


def message_formatter(text, component=None, object_name=None, method_name=None, code=None):
    m = ""
    m = m + component and "{}::".format(component) or ""
    m = m + object_name and "{}::".format(object_name) or ""
    m = m + method_name and "{}::".format(method_name) or ""
    m = m + code and "{}::".format(code) or ""
    m = m + text
    return m


class Problem(ArjunaException):
    def __init__(self, text, screenshot_path, exc, component=None, object_name=None, method_name=None, code=None):
        super().__init__(message_formatter(text, component, object_name, method_name, code), exc, screenshot_path);
        self.problem_component = component;
        self.problem_object = object_name;
        self.problem_method = method_name;
        self.problem_code = code;

    def get_problem_component(self):
        return self.problem_component

    def get_problem_object(self):
        return self.problem_object

    def get_problem_method(self):
        return self.problem_method

    def get_problem_code(self):
        return self.problem_code

    def get_problem_text(self):
        return self.get_message()


class DirReaderFinishedException(Exception):
    def __init__(self):
        super().__init__("No more files.")


class UnsupportedRepresentationException(Exception):
    def __init__(self, klass_user_friendly_name, method, str_source_value, target_value_type):
        super().__init__(
            "Value.{}(): Can not represent {} types containing >>{}<< as {}.".format(method, str_source_value,
                                                                                     klass_user_friendly_name,
                                                                                     target_value_type))


class IncompatibleInputForValueException(Exception):
    def __init__(self, value, actual, value_type):
        super().__init__(
            "Incompatible input types >>{}<< (type: {}) supplied for creating {}.".format(value, actual, value_type))


class StringKeyValueContainerLookupException(Exception):
    def __init__(key):
        super().__init__("Invalid Key [{}] used for string key types container lookup.".format(key))

class WaitableError(Exception):

    def __init__(self, message):
        super().__init__(message)

class _ElementNotFoundError(WaitableError):

    def __init__(self, elem_name, *locators, message=None):
        message = message and  "Error message: {}".format(message) or ""
        super().__init__("{} not found using any of the locators: {}.{}".format(elem_name, GuiElementMetaData.locators_as_str(locators), message))

class _ElementPresentError(WaitableError):

    def __init__(self, elem_type, *locators, message=None):
        message = message and  "Error message: {}".format(message) or ""
        super().__init__("{} expected to be absent but still present for one of the locators: {}.{}".format(elem_type, GuiElementMetaData.locators_as_str(locators), message))

class GuiElementNotFoundError(_ElementNotFoundError):

    def __init__(self, *locators, message=None):
        super().__init__("GuiElement(s)", *locators, message=message)

class GuiElementPresentError(_ElementPresentError):

    def __init__(self, *locators, message=None):
        super().__init__("GuiElement(s)", *locators, message=message)

class GuiElementNotReadyError(WaitableError):

    def __init__(self, message):
        super().__init__("GuiElement(s) is/are NOT ready for interaction. Tool message: {}".format(message))

class GuiElementTextNotSetError(WaitableError):

    def __init__(self, message):
        super().__init__(". Tool message: {}".format(message))

class ChildWindowNotFoundError(_ElementNotFoundError):

    def __init__(self, *locators):
        super().__init__("Child window", *locators)

class ChildFrameNotFoundError(_ElementNotFoundError):

    def __init__(self, *locators):
        super().__init__("Frame", *locators)

class TimeoutError(WaitableError):

    def __init__(self, context, message):
        super().__init__(". Timeout in {}. Error Message: {}".format(context, message))  

class DataSourceFinished(StopIteration):
    def __init__(self, msg=None):
        super().__init__(msg is None and "Done" or msg)

class GuiNotLoadedError(WaitableError):

    def __init__(self, gui, msg):
        message = msg and  " Error message: {}.".format(msg) or ""
        super().__init__("GUI [{}] did not load as expected.{}".format(gui.qual_name, message))

class GuiLabelNotPresentError(Exception):

    def __init__(self, gns_name, label, context=None):
        context_msg = context and  " for context {}".format(context) or ""
        super().__init__("Gui namespace >{}< does not contain element with name: {}{}.".format(gns_name, label, context_msg))

class GuiNamespaceLoadingError(Exception):

    def __init__(self, gui, msg):
        message = msg and  " Error message: {}".format(msg) or ""
        super().__init__("Gui namespace was not loaded for >{}<.{}".format(gui.qual_name, message))