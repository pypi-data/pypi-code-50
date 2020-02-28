
import barcode
from barcode.writer import ImageWriter

from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel


class BarCode(SingletonModel):

    next_code = models.IntegerField(
        _('Next bar code'), null=True, blank=True, default=1)

    def __str__(self):
        return 'Bar code'

    def get_next_codes(self, count):

        next_codes = list(range(self.next_code, self.next_code + count))

        self.next_code += count
        self.save(update_fields=['next_code'])

        return next_codes

    @classmethod
    def format_code(cls, code):
        return "{:013d}".format(code)

    @classmethod
    def get_image(cls, code):

        EAN = barcode.get_barcode_class('ean13')

        formatted_code = cls.format_code(code)

        ean = EAN(formatted_code, writer=ImageWriter())

        return ean.render(text=formatted_code)

    class Meta:
        db_table = 'barcode_barcode'
        verbose_name = _('Bar code')
        verbose_name_plural = _('Bar codes')
