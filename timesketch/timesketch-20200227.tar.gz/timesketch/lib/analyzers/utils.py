# Copyright 2019 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This file contains utilities for analyzers."""

from __future__ import unicode_literals

from six.moves import urllib_parse as urlparse

from timesketch.lib.analyzers import interface


# CDN domain list based on:
# https://github.com/WPO-Foundation/webpagetest/blob/master/agent/wpthook/cdn.h
# Last updated: 2019-01-11
KNOWN_CDN_DOMAINS = {
    '.att-dsa.net': 'AT&T',
    '.pix-cdn.org': 'Advanced Hosters CDN',
    '.akamai.net': 'Akamai',
    '.akamaiedge.net': 'Akamai',
    '.akamaihd.net': 'Akamai',
    '.akamaitechnologies.com': 'Akamai',
    '.akamaitechnologies.fr': 'Akamai',
    '.akamaized.net': 'Akamai',
    '.edgekey.net': 'Akamai',
    '.edgesuite.net': 'Akamai',
    '.srip.net': 'Akamai',
    '.tl88.net': 'Akamai China CDN',
    '.gslb.tbcache.com': 'Alimama',
    '.cloudfront.net': 'Amazon CloudFront',
    '.aads-cn.net': 'Aryaka',
    '.aads-cng.net': 'Aryaka',
    '.aads1.net': 'Aryaka',
    '.azion.net': 'Azion',
    '.azioncdn.com': 'Azion',
    '.azioncdn.net': 'Azion',
    '.bo.lt': 'BO.LT',
    '.bisongrid.net': 'Bison Grid',
    '.bitgravity.com': 'BitGravity',
    '.bluehatnetwork.com': 'Blue Hat Network',
    '.b-cdn.net': 'BunnyCDN',
    '.cdn77.net': 'CDN77',
    '.cdn77.org': 'CDN77',
    '.cdngc.net': 'CDNetworks',
    '.gccdn.net': 'CDNetworks',
    '.panthercdn.com': 'CDNetworks',
    '.cdnsun.net': 'CDNsun',
    '.cdnvideo.net': 'CDNvideo',
    '.cdnvideo.ru': 'CDNvideo',
    '.cachefly.net': 'Cachefly',
    '.caspowa.com': 'Caspowa',
    '.cedexis.net': 'Cedexis',
    '.ccgslb.com': 'ChinaCache',
    '.lxdns.com': 'ChinaNetCenter',
    '.ourwebpic.com': 'ChinaNetCenter',
    '.wscdns.com': 'ChinaNetCenter',
    '.wscloudcdn.com': 'ChinaNetCenter',
    '.cloudflare.com': 'Cloudflare',
    '.cotcdn.net': 'Cotendo CDN',
    '.systemcdn.net': 'Edgecast',
    '.transactcdn.net': 'Edgecast',
    '.v1cdn.net': 'Edgecast',
    '.v2cdn.net': 'Edgecast',
    '.v3cdn.net': 'Edgecast',
    '.v4cdn.net': 'Edgecast',
    '.v5cdn.net': 'Edgecast',
    '.edgecastcdn.net': 'Edgecast',
    '.cdninstagram.com': 'Facebook',
    '.fbcdn.net': 'Facebook',
    '.fastly.net': 'Fastly',
    '.fastlylb.net': 'Fastly',
    '.nocookie.net': 'Fastly',
    '.cdn.gocache.net': 'GoCache',
    '.doubleclick.net': 'Google',
    '.googleusercontent.com': 'Google',
    '.gstatic.com': 'Google',
    '.googlehosted.com': 'Google',
    '.googlesyndication.': 'Google',
    '.hiberniacdn.com': 'HiberniaCDN',
    '.hwcdn.net': 'Highwinds',
    '.hosting4cdn.com': 'Hosting4CDN',
    '.incapdns.net': 'Incapsula',
    '.inscname.net': 'Instart Logic',
    '.insnw.net': 'Instart Logic',
    '.internapcdn.net': 'Internap',
    '.kinxcdn.com': 'KINX CDN',
    '.kinxcdn.net': 'KINX CDN',
    '.kxcdn.com': 'KeyCDN',
    '.lswcdn.eu': 'LeaseWeb CDN',
    '.lswcdn.net': 'LeaseWeb CDN',
    '.footprint.net': 'Level 3',
    '.fpbns.net': 'Level 3',
    '.llnwd.net': 'Limelight',
    '.cdncloud.net.au': 'MediaCloud',
    '.mncdn.com': 'Medianova',
    '.mncdn.net': 'Medianova',
    '.mncdn.org': 'Medianova',
    '.azure.microsoft.com': 'Microsoft Azure',
    '.azureedge.net': 'Microsoft Azure',
    '.vo.msecnd.net': 'Microsoft Azure',
    '.instacontent.net': 'Mirror Image',
    '.mirror-image.net': 'Mirror Image',
    '.ngenix.net': 'NGENIX',
    '.nyiftw.com': 'NYI FTW',
    '.nyiftw.net': 'NYI FTW',
    '.netdna-cdn.com': 'NetDNA',
    '.netdna-ssl.com': 'NetDNA',
    '.netdna.com': 'NetDNA',
    '.netlify.com': 'Netlify',
    '.r.worldcdn.net': 'OnApp',
    '.r.worldssl.net': 'OnApp',
    '.optimalcdn.com': 'Optimal CDN',
    '.pagerain.net': 'PageRain',
    '.raxcdn.com': 'Rackspace',
    '.resrc.it': 'ReSRC.it',
    '.rlcdn.com': 'Reapleaf',
    '.rncdn1.com': 'Reflected Networks',
    '.rncdn7.com': 'Reflected Networks',
    '.revcn.net': 'Rev Software',
    '.revdn.net': 'Rev Software',
    '.roast.io': 'Roast.io',
    '.streamprovider.net': 'Rocket CDN',
    '.cdn.sfr.net': 'SFR',
    '.simplecdn.net': 'Simple CDN',
    '.singularcdn.net.br': 'Singular CDN',
    '.stackpathdns.com': 'StackPath',
    '.swiftcdn1.com': 'SwiftCDN',
    '.swiftserve.com': 'SwiftCDN',
    '.trbcdn.ru': 'TRBCDN',
    '.gslb.taobao.com': 'Taobao',
    '.taobaocdn.com': 'Taobao',
    '.tbcdn.cn': 'Taobao',
    '.cdntel.net': 'Telenor',
    '.twimg.com': 'Twitter',
    '.unicorncdn.net': 'UnicornCDN',
    '.voxcdn.net': 'VoxCDN',
    '.gravatar.com': 'WordPress',
    '.wordpress.com': 'WordPress',
    '.wp.com': 'WordPress',
    '.ay1.b.yahoo.com': 'Yahoo',
    '.yahooapis.com': 'Yahoo',
    '.yimg.': 'Yahoo',
    '.yottaa.net': 'Yottaa',
    '.zenedge.net': 'Zenedge',
    '.afxcdn.net': 'afxcdn.net',
    '.cubecdn.net': 'cubeCDN',
    '.cdn.jsdelivr.net': 'jsDelivr',
    '.squixa.net': 'section.io'}


def get_domain_from_url(url):
    """Extract domain from URL.

    Args:
        url: URL to parse.

    Returns:
        String with domain from URL.
    """
    # TODO: See if we can optimize this because it is rather slow.
    domain_parsed = urlparse.urlparse(url)
    domain_full = domain_parsed.netloc
    domain, _, _ = domain_full.partition(':')
    return domain


def get_tld_from_domain(domain):
    """Get the top level domain from a domain string.

    Args:
        domain: string with a full domain, eg. www.google.com

    Returns:
        string: TLD or a top level domain extracted from the domain,
        eg: google.com
    """
    return '.'.join(domain.split('.')[-2:])


def strip_www_from_domain(domain):
    """Strip www. from beginning of domain names.

    Args:
        domain: string with a full domain, eg. www.google.com

    Returns:
        string: Domain without any www, eg: google.com
    """
    if domain.startswith('www.'):
        return domain[4:]
    return domain


def get_cdn_provider(domain):
    """Return name of CDN provider if domain is recognized as a CDN.

    Args:
        domain: Domain name to check against CDN list.

    Returns:
        String of names of CDN providers or empty string if not found.

    """
    cdn_providers = [v for k, v in iter(KNOWN_CDN_DOMAINS.items()) if
                     domain.endswith(k.lower())]
    return ' '.join(set(cdn_providers))


def get_events_from_data_frame(frame, datastore):
    """Generates events from a data frame.

    Args:
        frame: a pandas DataFrame object.
        datastore: Elasticsearch datastore client.

    Yields:
        An event (interface.Event) object for each row
        in the DataFrame.
    """
    for row in frame.iterrows():
        _, entry = row
        event_id = entry.get('_id')
        if not event_id:
            continue
        event_index = entry.get('_index')
        if not event_index:
            continue
        event_type = entry.get('_type')

        event_dict = dict(
            _id=event_id, _type=event_type, _index=event_index,
            _source=entry.to_dict())
        yield interface.Event(event_dict, datastore)
