from typing import Collection, Any


# region Form methods mixins

class FormMethodsMixin:
    """
    Extends forms functionality with some useful methods.
    """

    DISABLED_FIELD_CSS_CLASS: str = 'disabled-field'

    def disable_fields(self, *fields_to_process, by_css_class_only: bool = False) -> None:
        # disable fields by 'disable' attribute or special css-class.
        for field in fields_to_process:
            if field in self.fields:
                field_obj = self.fields[field]
                self.add_fields_classes(
                    field, fields_classes=(self.DISABLED_FIELD_CSS_CLASS,)
                )
                if not by_css_class_only:
                    field_obj.disabled = True

    def add_fields_classes(self, *fields_to_process, fields_classes: Collection[str]) -> None:
        # adds classes to group of fields.
        for field in fields_to_process:
            if field in self.fields:
                widget_classes = self.fields[field].widget.attrs.get('class', '').split(' ')
                widget_classes += fields_classes
                self.fields[field].widget.attrs['class'] = ' '.join(set(widget_classes))

    def set_fields_attr(self, *fields_to_process, attr: str, value: Any, reverse: bool = False) -> None:
        if not reverse:
            for field in fields_to_process:
                if field in self.fields:
                    setattr(self.fields[field], attr, value)
        else:
            for field in self.fields:
                if field not in fields_to_process:
                    setattr(self.fields[field], attr, value)

    def set_widget_attr(self, *fields_to_process, attr: str, value: Any, reverse: bool = False) -> None:
        if not reverse:
            for field in fields_to_process:
                if field in self.fields:
                    self.fields[field].widget.attrs[attr] = value
        else:
            for field in self.fields:
                if field not in fields_to_process:
                    self.fields[field].widget.attrs[attr] = value

    def del_fields(self, *fields_to_process, reverse: bool = False) -> None:
        if not reverse:
            for field in fields_to_process:
                if field in self.fields:
                    del self.fields[field]
        else:
            for field in self.fields:
                if field not in fields_to_process:
                    del self.fields[field]


class ModelFormMethodsMixin:
    """
    Mixin such as CommonFormMethods but only for model forms.
    """

    def check_for_unique(self, *fields_to_process, error_message: str, error_field: str = None) -> None:
        # check instance for unique by fields values.
        filter_kwargs = {
            field_name: self.cleaned_data.get(field_name)
            for field_name in fields_to_process if self.cleaned_data.get(field_name, None) is not None
        }
        if len(filter_kwargs) == len(fields_to_process):
            same_objects = self.Meta.model.objects.filter(**filter_kwargs)
            if self.instance_exists:
                same_objects = same_objects.exclude(id=self.instance.id)
            if same_objects.exists():
                self.add_error(error_field, error_message)

    @property
    def instance_exists(self) -> bool:
        instance_exists = False
        if self.instance and self.instance.id:
            instance_exists = True
        return instance_exists

# endregion


class DetachedFormObjectMediaMixin:

    @property
    def media_css(self):
        return self.media['css']

    @property
    def media_js(self):
        return self.media['js']
