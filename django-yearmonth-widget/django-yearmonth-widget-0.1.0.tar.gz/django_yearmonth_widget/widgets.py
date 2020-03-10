from django.forms.widgets import Input
from django.utils import timezone


class DjangoYearMonthWidget(Input):
    input_type = "text"
    template_name = "django-yearmonth-widget/django-yearmonth-widget.html"

    class Media:
        js = [
            "jquery3/jquery.js",
            "django-yearmonth-widget/js/django-yearmonth-widget.js",
        ]

    def __init__(self, attrs=None, years=None, prev_years=10, next_years=0, day_value=1):
        super().__init__(attrs)
        self.day_value = day_value
        if years:
            self.years = years
        else:
            now = timezone.now()
            self.years = list(range(now.year - prev_years,  now.year + next_years + 1))

    def get_context(self, name, value, attrs):
        attrs = attrs or {}
        attrs["class"] = attrs.get("class", "") + " django-yearmonth-widget-input"
        attrs["data-day-value"] = self.day_value
        attrs["hidden"] = "hidden"
        context = super().get_context(name, value, attrs)
        context["years"] = self.years
        context["months"] = list(range(1, 13))
        context["value"] = value
        return context
