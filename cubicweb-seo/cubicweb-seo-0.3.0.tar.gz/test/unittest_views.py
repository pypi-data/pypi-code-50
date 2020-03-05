# copyright 2017 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for cubicweb-seo views."""

from io import BytesIO
from datetime import date, datetime
import gzip
import os
import tempfile
import zipfile

from lxml import etree

from cubicweb.devtools.testlib import CubicWebTC

from cubicweb_seo.views import SitemapRule

SITEMAP_NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


def _sitemap_tag(tag_name):
    """Return the complete tag_name in the Sitemap XML namespace from the given short one."""
    return '{0}{1}'.format(SITEMAP_NS, tag_name)


#
# Test sitemap rules for the test schema.py in test/data
#

_TITLEDTHING_PRIORITY = 1.0
_TITLEDTHING_CHFREQ = 'monthly'


class TitledThingSitemapRule(SitemapRule):
    __regid__ = 'titledthing'
    query = 'Any X WHERE X is TitledThing'
    priority = _TITLEDTHING_PRIORITY
    chfreq = _TITLEDTHING_CHFREQ


class NamedThingSitemapRule(SitemapRule):
    __regid__ = 'namedthing'
    query = 'Any X WHERE X is NamedThing'


#
# Mixin to parse Sitemap XML
#

class SitemapXMLCheckMixin(object):

    def assertSitemapContains(self, sitemap_data, expected_url, expected_lastmod=None,
                              expected_priority=None, expected_chfreq=None):
        """Return True if the entry described by the parameters is found in the Sitemap data."""
        root_node = etree.fromstring(sitemap_data)
        for url_node in root_node.findall(_sitemap_tag('url')):
            if expected_lastmod is not None:
                expected_lastmod = (expected_lastmod.strftime('%Y-%m-%d')
                                    if isinstance(expected_lastmod, (date, datetime))
                                    else str(expected_lastmod))
                if url_node.findtext(_sitemap_tag('lastmod')) != expected_lastmod:
                    continue
            if (expected_priority is not None
                    and url_node.findtext(_sitemap_tag('priority')) is not None
                    and (float(url_node.findtext(_sitemap_tag('priority')))
                         != float(expected_priority))):
                continue
            if (expected_chfreq is not None
                    and url_node.findtext(_sitemap_tag('changefreq')) != str(expected_chfreq)):
                continue
            if url_node.findtext(_sitemap_tag('loc')) == expected_url:
                break
        else:
            raise AssertionError('Not found in Sitemap: {0} (lastmod={1!r}, priority={2!r}, '
                                 'chfreq={3!r})'.format(expected_url, expected_lastmod,
                                                        expected_priority, expected_chfreq))

    def assertSitemapLengthEqual(self, sitemap_data, expected_length):
        """Return True if the Sitemap data has the correct number of entries."""
        root_node = etree.fromstring(sitemap_data)
        length = len(list(root_node.findall(_sitemap_tag('url'))))
        if length != expected_length:
            raise AssertionError('Sitemap length is {0} (expected: {1})'.format(length,
                                                                                expected_length))

    def assertIndexContains(self, index_data, expected_url):
        """Return True if the given URL is found in the Sitemap index data."""
        root_node = etree.fromstring(index_data)
        for url_node in root_node.findall(_sitemap_tag('sitemap')):
            if url_node.findtext(_sitemap_tag('loc')) == expected_url:
                break
        else:
            raise AssertionError('Not found in Sitemap index: {0}'.format(expected_url))


#
# Actual test cases
#

class SitemapViewTC(SitemapXMLCheckMixin, CubicWebTC):
    """Test about the ``sitemapxml`` view."""

    def test_sitemap_view_one_entity(self):
        """Check that an XML sitemap is correctly generated with one entity."""
        with self.temporary_appobjects(TitledThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                thing = cnx.create_entity('TitledThing', title=u'A thing')
                cnx.commit()
            with self.admin_access.web_request() as req:
                thing = req.entity_from_eid(thing.eid)
                sitemap_data = req.view('sitemapxml').encode('utf-8')
                self.assertSitemapLengthEqual(sitemap_data, 2)  # Counting the root URL
                self.assertSitemapContains(sitemap_data, thing.absolute_url(),
                                           thing.modification_date, _TITLEDTHING_PRIORITY,
                                           _TITLEDTHING_CHFREQ)

    def test_sitemap_view_multiple_entities(self):
        """Check that an XML sitemap is correctly generated with multiple entities."""
        with self.temporary_appobjects(NamedThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                thing1 = cnx.create_entity('NamedThing', name=u'A thing')
                thing2 = cnx.create_entity('NamedThing', name=u'A second thing')
                cnx.commit()
            with self.admin_access.web_request() as req:
                thing1 = req.entity_from_eid(thing1.eid)
                thing2 = req.entity_from_eid(thing2.eid)
                sitemap_data = req.view('sitemapxml').encode('utf-8')
                self.assertSitemapLengthEqual(sitemap_data, 3)  # Counting the root URL
                self.assertSitemapContains(sitemap_data, thing1.absolute_url(),
                                           thing1.modification_date)
                self.assertSitemapContains(sitemap_data, thing2.absolute_url(),
                                           thing2.modification_date)

    def test_sitemap_view_multiple_etypes(self):
        """Check that an XML sitemap is correctly generated with multiple entities of multiple
        etypes."""
        with self.temporary_appobjects(TitledThingSitemapRule, NamedThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                thing0 = cnx.create_entity('TitledThing', title=u'A thing')
                thing1 = cnx.create_entity('NamedThing', name=u'A second thing')
                thing2 = cnx.create_entity('NamedThing', name=u'A third thing')
                cnx.commit()
            with self.admin_access.web_request() as req:
                thing0 = req.entity_from_eid(thing0.eid)
                thing1 = req.entity_from_eid(thing1.eid)
                thing2 = req.entity_from_eid(thing2.eid)
                sitemap_data = req.view('sitemapxml').encode('utf-8')
                self.assertSitemapLengthEqual(sitemap_data, 4)  # Counting the root URL
                self.assertSitemapContains(sitemap_data, thing0.absolute_url(),
                                           thing0.modification_date, _TITLEDTHING_PRIORITY,
                                           _TITLEDTHING_CHFREQ)
                self.assertSitemapContains(sitemap_data, thing1.absolute_url(),
                                           thing1.modification_date)
                self.assertSitemapContains(sitemap_data, thing2.absolute_url(),
                                           thing2.modification_date)


class GzippedSitemapViewTC(SitemapXMLCheckMixin, CubicWebTC):
    """Test about the ``sitemapxmlgz`` view."""

    def test_gz_sitemap_view(self):
        """Check that a Gzipped XML sitemap is correctly generated."""
        with self.temporary_appobjects(TitledThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                thing = cnx.create_entity('TitledThing', title=u'A thing')
                cnx.commit()
            with self.admin_access.web_request() as req:
                thing = req.entity_from_eid(thing.eid)
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    f.write(req.view('sitemapxmlgz'))
                sitemap_data = BytesIO()
                with gzip.open(f.name, mode='rb') as gz:
                    sitemap_data.write(gz.read())
                os.remove(f.name)
                sitemap_data = sitemap_data.getvalue()
                self.assertSitemapLengthEqual(sitemap_data, 2)  # Counting the root URL
                self.assertSitemapContains(sitemap_data, thing.absolute_url(),
                                           thing.modification_date, _TITLEDTHING_PRIORITY,
                                           _TITLEDTHING_CHFREQ)


class ZippedSitemapsViewTC(SitemapXMLCheckMixin, CubicWebTC):
    """Test about the ``massive-sitemaps`` view."""

    def create_many_things(self, cnx, n):
        """Create as many as ``n`` ``NamedThing`` using the given connection."""
        for i in range(n):
            cnx.create_entity('NamedThing', name=u'Thing {0}'.format(i))
            if (i % 1000 == 0):
                print(i)
        cnx.commit()

    def extract_file(self, fname):
        """Extract the given ZIP file and return list of extracted filenames."""
        tmpdir = tempfile.gettempdir()
        sitemaps = []
        with zipfile.ZipFile(fname, mode='r') as zf:
            zf.extractall(tmpdir)
            for gz_fname in zf.namelist():
                sitemap_data = BytesIO()
                with gzip.open(os.path.join(tmpdir, gz_fname), mode='rb') as gz:
                    sitemap_data.write(gz.read())
                sitemaps.append(sitemap_data)
        return sitemaps

    def clean(self, zip_fname, gz_number):
        """Remove temporary files."""
        os.remove(zip_fname)
        os.remove(os.path.join(tempfile.gettempdir(), 'sitemap.xml.gz'))
        for i in range(1, gz_number):
            os.remove(os.path.join(tempfile.gettempdir(), 'sitemap{0}.xml.gz'.format(i)))

    def test_zip_sitemaps_view_one_file(self):
        """Check that a bunch of XML sitemaps is correctly generated and archived in a ZIP file."""
        with self.temporary_appobjects(TitledThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                thing = cnx.create_entity('TitledThing', title=u'A thing')
                cnx.commit()
            with self.admin_access.web_request() as req:
                thing = req.entity_from_eid(thing.eid)
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    f.write(req.view('massive-sitemaps'))
                sitemaps = self.extract_file(f.name)
                os.remove(f.name)
                self.assertEqual(len(sitemaps), 2)
                index_data = sitemaps[0].getvalue()
                self.assertIndexContains(index_data, req.build_url('sitemap1.xml.gz'))
                sitemap_data = sitemaps[1].getvalue()
                self.assertSitemapLengthEqual(sitemap_data, 2)  # Counting the root URL
                self.assertSitemapContains(sitemap_data, thing.absolute_url(),
                                           thing.modification_date, _TITLEDTHING_PRIORITY,
                                           _TITLEDTHING_CHFREQ)

    def test_zip_sitemaps_view_one_full_file(self):
        """Check that an XML sitemap is correctly generated, gzipped, and archived in a ZIP file
        with a Sitemap index file."""
        with self.temporary_appobjects(NamedThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                self.create_many_things(cnx, 49999)
            with self.admin_access.web_request() as req:
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    f.write(req.view('massive-sitemaps'))
                sitemaps = self.extract_file(f.name)
                self.clean(f.name, len(sitemaps))
                self.assertEqual(len(sitemaps), 2)
                index_data = sitemaps[0].getvalue()
                self.assertIndexContains(index_data, req.build_url('sitemap1.xml.gz'))
                sitemap_data = sitemaps[1].getvalue()
                self.assertSitemapLengthEqual(sitemap_data, 50000)  # Counting the root URL

    def test_zip_sitemaps_view_two_files(self):
        """Check that a bunch of XML sitemaps are correctly generated, gzipped, and archived in a
        ZIP file with a Sitemap index file."""
        with self.temporary_appobjects(NamedThingSitemapRule):
            with self.admin_access.repo_cnx() as cnx:
                self.create_many_things(cnx, 50000)
            with self.admin_access.web_request() as req:
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    f.write(req.view('massive-sitemaps'))
                sitemaps = self.extract_file(f.name)
                self.clean(f.name, len(sitemaps))
                self.assertEqual(len(sitemaps), 3)
                index_data = sitemaps[0].getvalue()
                self.assertIndexContains(index_data, req.build_url('sitemap1.xml.gz'))
                self.assertIndexContains(index_data, req.build_url('sitemap2.xml.gz'))
                sitemap_data = sitemaps[1].getvalue()
                self.assertSitemapLengthEqual(sitemap_data, 50000)  # Counting the root URL
                sitemap_data = sitemaps[2].getvalue()
                self.assertSitemapLengthEqual(sitemap_data, 1)
