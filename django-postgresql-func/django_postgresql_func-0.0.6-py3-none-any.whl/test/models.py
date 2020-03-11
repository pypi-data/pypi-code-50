from django.db import models


class StringTable(models.Model):
    single_char = models.CharField(
        'single char',
        max_length=10,
        blank=True,
        null=True,
    )
    char = models.CharField(
        'single char',
        max_length=255,
        blank=True,
        null=True,
    )
    text = models.TextField(
        'text',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'string'

    @classmethod
    def init(cls):
        data = [
            {'single_char': " 'A'  ",
             'char': 'in mollis nunc sed id',
             'text': ''},
            {'single_char': '   "B"',
             'char': None,
             'text': 'nam aliquam sem et tortor consequat id porta nibh \n'
                     'venenatis cras sed felis eget velit aliquet \n'
                     'sagittis id consectetur purus ut faucibus pulvinar \n'
                     'elementum integer enim neque volutpat ac tincidunt \n'},
            {'single_char': None,
             'char': 'tellus molestie nunc non \n blandit massa enim nec dui',
             'text': None,
             },
            {'single_char': '\' C "',
             'char': '45.4',
             'text': '"_"',
             }
        ]
        cls.objects.filter().delete()
        cls.objects.bulk_create([cls(**i) for i in data])


class DigitTable(models.Model):
    int_field = models.IntegerField(
        'int_field',
        blank=True,
        null=True,
    )
    dec_field = models.DecimalField(
        'dec_field',
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
    )
    flt_field = models.FloatField(
        'flt_field',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'digit'

    @classmethod
    def init(cls):
        data = [
            {'int_field': -456,
             'dec_field': -123.45,
             'flt_field': -9999.9999},
            {'int_field': None,
             'dec_field': None,
             'flt_field': None},
            {'int_field': 0,
             'dec_field': 0,
             'flt_field': 0},
            {'int_field': 456,
             'dec_field': 123.45,
             'flt_field': 9999.9999},
        ]
        cls.objects.filter().delete()
        cls.objects.bulk_create([cls(**i) for i in data])


class EmptyT1(models.Model):
    text = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    class Meta:
        db_table = 'empty_t1'

    @classmethod
    def init(cls):
        data = [
            {'text': ''},
        ]
        cls.objects.filter().delete()
        cls.objects.bulk_create([cls(**i) for i in data])