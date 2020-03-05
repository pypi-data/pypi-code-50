# -*- coding: utf-8 -*-
# copyright 2012 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

"""cubicweb-seo views/forms/actions/components for web ui"""

from io import StringIO
from datetime import date
import gzip
import os
import tempfile
import urllib.parse
import zipfile

from cubicweb import Unauthorized
from cubicweb.view import View
from cubicweb.predicates import none_rset
from cubicweb.appobject import AppObject
from cubicweb.web import httpcache
from cubicweb.web.views.urlrewrite import SimpleReqRewriter, rgx


class SeoReqRewriter(SimpleReqRewriter):
    rules = [
        (rgx('/robots.txt$'), dict(vid='robotstxt')),
        (rgx('/sitemap.xml$'), dict(vid='sitemapxml')),
    ]


class RobotsRule(AppObject):
    """abstract base class for robots rules

    A custom rule should be built by extending this class. For instance::

      from cubicweb_seo.views import RobotsRule

      class VcsfileRobotsRule(RobotsRule):
          __regid__ = 'vcsfile'
          STANZA = ['User-Agent: *',
                    'Disallow: /versioncontent',
                    'Disallow: /testexecution',
                    'Disallow: /versionedfile',
                    'Disallow: /deletedversioncontent']

    To get more control, override the items() method.
    """
    __registry__ = 'robotstxt'
    __abstract__ = True
    STANZA = []

    def stanza(self):
        return u'\n'.join(self.STANZA)


class CwRobotsRule(RobotsRule):
    __regid__ = 'cubicweb.admin'
    STANZA = ["User-Agent: *",
              "Disallow: /schema",
              "Disallow: /cwetype",
              "Disallow: /cwrtype",
              "Disallow: /search",
              "Disallow: /login",
              "Disallow: /cwuser",
              "Disallow: /cwgroup",
              "Disallow: /cwsource",
              "Disallow: /_registry",
              "Disallow: /siteconfig",
              "Disallow: /siteinfo",
              "Disallow: /notfound",
              "Disallow: /processinfo",
              "Disallow: /changelog",
              "Disallow: /add/",
              ]


class RobotsTxt(View):
    """A view that implements the http://robotstxt.org standard"""
    __regid__ = 'robotstxt'
    content_type = 'text/plain'
    templatable = False
    __select__ = none_rset()

    def call(self):
        self.w(u'Sitemap: %s\n\n' % self._cw.build_url('sitemap.xml'))
        if 'robotstxt' in self._cw.vreg:  # XXX or make sure it exists by creating it in this cube
            for rule in self._cw.vreg['robotstxt'].possible_objects(self._cw):
                self.w(rule.stanza())
                self.w(u'\n')


CHANGEFREQS = frozenset(('always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'))


class SitemapRule(AppObject):
    """abstract base class for sitemap rules

    A custom rule should be built by extending this class. For instance::

      from cubicweb_seo.views import SitemapRule

      class CardSitemapRule(SitemapRule):
          __regid__ = 'card'
          query = 'Any X WHERE X is Card'
          priority = 1.0
          chfreq = 'monthly'

    To get more control, override the items() method.
    """
    __registry__ = 'sitemap'
    __abstract__ = True
    query = None
    priority = None  # optional
    chfreq = None   # optional

    def items(self):
        rset = self._cw.execute(self.query)
        for item in rset.entities():
            yield (item.absolute_url(), item.modification_date, self.chfreq, self.priority)


class Sitemaps(View):
    """A view that implements the http://sitemaps.org standard

    Content types must append rules to the sitemap registry in order to appear
    in the list at /sitemap.xml.
    """

    __regid__ = 'sitemapxml'
    content_type = 'text/xml'
    templatable = False
    __select__ = none_rset()

    def add_url(self, url, lastmod=None, chfreq=None, priority=None):
        self.w(u'<url><loc>%s</loc>' % url)
        if lastmod:
            self.w(u'<lastmod>%s</lastmod>' % lastmod.strftime('%Y-%m-%d'))
        if chfreq:
            if chfreq in CHANGEFREQS:
                self.w(u'<changefreq>%s</changefreq>' % chfreq)
            else:
                self.error('url %s gave %s which is not a valid changefreq according to '
                           'http://sitemaps.org' % (url, chfreq))
        if priority:
            if 0 <= float(priority) <= 1:
                self.w(u'<priority>%.2f</priority>' % priority)
            else:
                self.error('url %s gave %s which is not a valid priority according to '
                           'http://sitemaps.org' % (url, priority))
        self.w(u'</url>')

    def call(self):
        # XXX have a look at databnf/file/stable/sitemap.py for cases where the sitemap file is
        # too big (>10Mb) or has too many entries (>50k)
        self.w(u'<?xml version="1.0" encoding="%s"?>\n' % self._cw.encoding)
        self.w(u'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        self.add_url(self._cw.base_url())
        if 'sitemap' in self._cw.vreg:  # XXX or make sure it exists by creating it in this cube...
            count = 0
            for rule in self._cw.vreg['sitemap'].possible_objects(self._cw):
                try:
                    for item in rule.items():
                        self.add_url(*item)
                        count += 1
                        if count > 50000:
                            self.error('too many items for this sitemap (limit is 50,000)')
                            break
                    if count > 50000:
                        break
                except Unauthorized as exc:
                    self.info('sitemap rule %s raised Unauthorized: %s' % (rule.__regid__, exc))
                except Exception:
                    self.exception('sitemap rule %s raised exception' % rule.__regid__)
        else:
            self.debug('no sitemap registry found')
        self.w(u'</urlset>')


class GzippedSitemap(Sitemaps):
    """Allows to download a Gzipped sitemap.xml."""

    __regid__ = 'sitemapxmlgz'
    content_type = 'application/gzip'
    binary = True
    http_cache_manager = httpcache.EntityHTTPCacheManager
    add_to_breadcrumbs = False

    def add_url(self, buf, url, lastmod=None, chfreq=None, priority=None):
        buf.write(u'<url>')
        buf.write(u'<loc>{0}</loc>'.format(urllib.parse.quote(url.encode('utf-8'), safe=':/')))
        if lastmod:
            buf.write(u'<lastmod>{0}</lastmod>'.format(lastmod.strftime('%Y-%m-%d')))
        if chfreq:
            if chfreq in CHANGEFREQS:
                buf.write(u'<changefreq>{0}</changefreq>'.format(chfreq))
            else:
                self.error('url %s gave %s which is not a valid changefreq according to '
                           'http://sitemaps.org' % (url, chfreq))
        if priority:
            if 0 <= float(priority) <= 1:
                buf.write(u'<priority>{0}</priority>'.format(priority))
            else:
                self.error('url %s gave %s which is not a valid priority according to '
                           'http://sitemaps.org' % (url, priority))
        buf.write(u'</url>')

    def call(self):
        buf = StringIO()
        buf.write(u'<?xml version="1.0" encoding="{0}"?>\n'.format(self._cw.encoding))
        buf.write(u'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        self.add_url(buf, self._cw.base_url())
        if 'sitemap' in self._cw.vreg:  # XXX or make sure it exists by creating it in this cube...
            count = 0
            for rule in self._cw.vreg['sitemap'].possible_objects(self._cw):
                try:
                    for item in rule.items():
                        self.add_url(buf, *item)
                        count += 1
                        if count > 50000:
                            self.error('too many items for this sitemap (limit is 50,000)')
                            break
                    if count > 50000:
                        break
                except Unauthorized as exc:
                    self.info('sitemap rule %s raised Unauthorized: %s' % (rule.__regid__, exc))
                except Exception:
                    self.exception('sitemap rule %s raised exception' % rule.__regid__)
        else:
            self.debug('no sitemap registry found')
        buf.write(u'</urlset>')
        with tempfile.NamedTemporaryFile(delete=False) as f:
            with gzip.open(f.name, mode='wb') as gz:
                gz.write(buf.getvalue().encode('utf-8'))
        self._cw.set_content_type(self.content_type,
                                  filename='sitemap.xml.gz',
                                  disposition='attachment')
        with open(f.name, 'rb') as gz:
            self.w(gz.read())
        os.remove(f.name)


class ZippedMultipleSitemaps(GzippedSitemap):
    """Allows to download a ZIP archive containing multiple Sitemap files and a Sitemap index.

    This view should be used when number of URLs in sitemap will exceed the 50,000 limit.
    Thus URLs must be dispatched among multiple Sitemap files and a Sitemap index file must be
    created.

    Sitemap files will always be gzipped in this case.
    """

    __regid__ = 'massive-sitemaps'
    content_type = 'application/zip'
    binary = True
    http_cache_manager = httpcache.EntityHTTPCacheManager
    add_to_breadcrumbs = False

    def new_sitemap_buffer(self, index=False):
        """Create a new buffer storing content about a Sitemap file in memory.

        If ``index`` is True, start a buffer for a Sitemap index file."""
        buf = StringIO()
        buf.write(u'<?xml version="1.0" encoding="{0}"?>\n'.format(self._cw.encoding))
        tagname = u'urlset' if not index else u'sitemapindex'
        buf.write(u'<{0} xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'.format(tagname))
        return buf

    def save_partial_sitemap(self, sitemap_buf, fname, index_buf):
        """Save content in ``sitemap_buf`` into ``fname``, and add an index entry in
        ``index_buf``."""
        sitemap_buf.write(u'</urlset>')
        with gzip.open(fname, mode='wb') as gz:
            gz.write(sitemap_buf.getvalue().encode('utf-8'))
        index_buf.write('<sitemap>')
        index_buf.write('<loc>{0}</loc>'.format(self._cw.build_url(os.path.basename(fname))))
        index_buf.write('<lastmod>{0}</lastmod>'.format(date.today().strftime('%y-%m-%d')))
        index_buf.write('</sitemap>')

    def save_sitemap_index(self, index_buf, index_fname):
        """Save content in ``sitemap_buf`` into ``fname``, and add an index entry in
        ``index_buf``."""
        index_buf.write(u'</sitemapindex>')
        with gzip.open(index_fname, mode='wb') as gz:
            gz.write(index_buf.getvalue().encode('utf-8'))

    def call(self):
        index_fname = os.path.join(tempfile.gettempdir(), 'sitemap.xml.gz')
        fname_templ = os.path.join(tempfile.gettempdir(), 'sitemap{0}.xml.gz')
        buf = self.new_sitemap_buffer()
        index_buf = self.new_sitemap_buffer(index=True)
        self.add_url(buf, self._cw.base_url())
        if 'sitemap' in self._cw.vreg:  # XXX or make sure it exists by creating it in this cube...
            entries = file_number = 1
            for rule in self._cw.vreg['sitemap'].possible_objects(self._cw):
                try:
                    for item in rule.items():
                        entries += 1
                        if entries > 50000:
                            self.save_partial_sitemap(buf, fname_templ.format(file_number),
                                                      index_buf)
                            file_number += 1
                            buf = self.new_sitemap_buffer()
                            entries = 1
                        self.add_url(buf, *item)
                except Unauthorized as exc:
                    self.info('sitemap rule %s raised Unauthorized: %s' % (rule.__regid__, exc))
                except Exception:
                    self.exception('sitemap rule %s raised exception' % rule.__regid__)
            self.save_partial_sitemap(buf, fname_templ.format(file_number), index_buf)
            self.save_sitemap_index(index_buf, index_fname)
        else:
            self.debug('no sitemap registry found')
        with tempfile.NamedTemporaryFile(delete=False) as f:
            with zipfile.ZipFile(f.name, mode='w') as zf:
                zf.write(index_fname, os.path.basename(index_fname))
                for i in range(1, file_number + 1):
                    fname = fname_templ.format(i)
                    zf.write(fname, os.path.basename(fname))
        self._cw.set_content_type(self.content_type,
                                  filename='sitemaps.zip',
                                  disposition='attachment')
        with open(f.name, 'rb') as zf:
            self.w(zf.read())
        os.remove(f.name)
        for i in range(1, file_number + 1):
            os.remove(fname_templ.format(i))
