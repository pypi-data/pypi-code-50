# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.meta
    ~~~~~~~~~~~~

    Meta information retrieval from markdown post file.

    Meta fields are set in English, Portuguese, Spanish, Catalan,
    Galician and Esperanto (using the X-system), although there cannot
    be any accent in the field names, so "título" has to be "titulo" in
    order to work properly.

    There may be diacritics in field values (UTF-8 by default) but not
    in field names.

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
from dateutil.parser import parse
import datetime
import markdown
import re


class Meta:
    """Meta information retriever.

    .. todo: Use a more Pythonic code
    """

    def __init__(self, meta):
        """Intializer.

        :param meta: Meta information
        :type meta: list
        """
        self.meta = meta


    def category(self, default_category='Miscellaneous'):
        """Gets category as a string from post meta information.

        :return: Category field
        :rtype: str
        """
        category = self.meta.get('category') or \
                   self.meta.get('categoria') or self.meta.get('kategorio')
        return ' '.join(category) if category else default_category


    def author(self, default_author='Nobody'):
        """Gets the author as a string from post meta information.

        :return: Author field
        :rtype: str
        """
        authors = self.meta.get('authors') or self.meta.get('author') or \
                  self.meta.get('autores') or self.meta.get('autors') or \
                  self.meta.get('autor') or self.meta.get('autoro') or \
                  self.meta.get('auxtoro')
        return ', '.join(authors) if authors else default_author


    def email(self):
        """Gets the author's email as a string from post meta information.

        :return: Email field
        :rtype: str
        """
        emails = self.meta.get('email') or self.meta.get('e-mail') or \
                 self.meta.get('correo electronico') or \
                 self.meta.get('correo') or self.meta.get('correu') or \
                 self.meta.get('e-correo') or \
                 self.meta.get('retposto') or self.meta.get('retposxto')
        return ', '.join(emails) if emails else ''


    def language(self, default_language="en"):
        """Gets the author's email as a string from post meta information.

        :return: Language field
        :rtype: str
        """
        language = self.meta.get('language') or self.meta.get('idioma') or \
                   self.meta.get('lengua') or self.meta.get('lingua') or \
                   self.meta.get('llengua') or self.meta.get('lingvo')
        return language if language else default_language


    def title(self):
        """Gets post title as a string from post meta information.

        :return: Title field
        :rtype: str
        """
        title = self.meta.get('title') or self.meta.get('titulo')  or \
                self.meta.get('entry') or self.meta.get('entrada') or \
                self.meta.get('titol') or self.meta.get('post') or \
                self.meta.get('titolo')
        #return ''.join(title) if title else ''
        fmttitle = markdown.markdown(' '.join(title) if title else '')
        return re.sub(r'</*(p|br)[^>]*?>', '', fmttitle)


    def summary(self):
        """Gets post summary as a string from post meta information.

        :return: Summary field
        :rtype: str
        """
        summary = self.meta.get('summary') or self.meta.get('resumo') or \
                  self.meta.get('resumen') or self.meta.get('resum')
        fmtsummary = markdown.markdown(' '.join(summary) if summary else '')
        return re.sub(r'</*(p|br)[^>]*?>', '', fmtsummary)


    def copyright(self):
        """Gets post copyright as a string from post meta information.

        :return: Copyright field
        :rtype: str
        """
        copyright = self.meta.get('copyright') or \
                    self.meta.get('license')   or \
                    self.meta.get('licencia')  or \
                    self.meta.get('licenza')   or \
                    self.meta.get('llicencia') or \
                    self.meta.get('permesilo') or \
                    self.meta.get('kopirajto') or \
                    self.meta.get('(c)')
        fmtcopyright = markdown.markdown(' '.join(copyright) if copyright \
                                                             else '')
        return re.sub(r'</*(p|br)[^>]*?>', '', fmtcopyright)


    def date_info(self):
        """Gets post date as a datetime object.

        :return: Date field
        :rtype: datetime
        """
        date = self.meta.get('date') or self.meta.get('data') or \
               self.meta.get('fecha') or self.meta.get('dato')
        return parse(''.join(date)) if date else ''


    def date(self, date_format='%c'):
        """Gets post date as a string.

        :param date_format: Date locale
        :type date_format: str
        :return: Date field
        :rtype: str
        """
        return self.date_info().strftime(date_format) \
               if self.date_info() else ''


    def up_date_info(self):
        """Gets updated post date as a datetime object.

        :return: Date field
        :rtype: datetime
        """
        up_date = self.meta.get('updated') or \
                        self.meta.get('actualizado') or \
                        self.meta.get('actualitzat') or \
                        self.meta.get('gisdatigita') or \
                        self.meta.get('gxisdatigita')
        return parse(''.join(up_date)) if up_date else ''


    def up_date(self, date_format='%c'):
        """Gets updated post date as a string.

        :param date_format: Date locale
        :type date_format: str
        :return: Date field
        :rtype: str
        """
        return self.up_date_info().strftime(date_format) \
               if self.up_date_info() else ''


    def comments(self):
        """Gets comments status.

        :return: True if entry has comments, or False otherwise
        :rtype: bool
        """
        comments = self.meta.get('comments')    or \
                   self.meta.get('comentarios') or \
                   self.meta.get('comentaris')  or \
                   self.meta.get('komentoj') or ['']
        com_bool = False if comments[0].lower() == "no"  or \
                            comments[0].lower() == "non" or \
                            comments[0].lower() == "não" or \
                            comments[0].lower() == "ne"     \
                         else True
        return com_bool


    def private(self):
        """Gets private status.

        :return: True if entry is private, or False otherwise
        :rtype: bool
        """
        private = self.meta.get('private') or \
                  self.meta.get('privado') or self.meta.get('privat') \
                  or ['']
        piv_bool = True if private[0].lower() == "yes" or \
                           private[0].lower() == "si"  or \
                           private[0].lower() == "sí"  or \
                           private[0].lower() == "sim" or \
                           private[0].lower() == "jes"    \
                        else False
        return piv_bool


    def tag_list(self):
        """Gets the tags as a list from post meta information.

        :return: List of tags
        :rtype: list
        """
        tag_list = self.meta.get('tags') or self.meta.get('labels') or \
                   self.meta.get('etiquetas') or \
                   self.meta.get('etiquetes') or \
                   self.meta.get('etikedoj') or ['']
        tag_list = [x.strip() for x in tag_list[0].split(',') if x.strip()]
        return tag_list if tag_list else []


    def tags(self):
        """Gets the tags as a list from post meta information.

        :return: List of tags
        :rtype: str
        """
        return ', '.join(tag_list(self.meta)) if tag_list(self.meta) else ''

