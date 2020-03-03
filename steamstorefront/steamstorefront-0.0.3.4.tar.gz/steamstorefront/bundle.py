import requests, re, math, w3lib.html
from bs4 import BeautifulSoup

class Bundle:
    store_url = "https://store.steampowered.com/bundle/"
    data = {}
    appid = 0

    def _getList(self, text, term, space=None):
        temp = text.find(term)
        if not temp:
            return None
        text = text[temp+len(term)+5:text.find('<br/>', temp)]
        text = w3lib.html.remove_tags(text)
        if space == "space":
            return text.replace("\t","").replace("</div","").replace("\n","")
        text = text.replace(", ",",").split(",")
        return text

    '''
        DATA
        App ID:
            sucess
            data:
                name
                bundle_id
                header_image
                bundle_description
                genre (list)
                developer (list)
                publisher (list)
                franchise (list)
                language (list)
                drm 
                categories (list)
                price: (dict)
                    initial
                    final
                    discount_percent
                    initial_formatted
                    final_formatted
                package_item: (list)
                    app_name
                    app_id
                    app_link
                    app_image
                    app_price: (dict)
                        final
                        final_formatted
                    platforms: (dict)
                        windows
                        mac
                        linux
                    categories (list)
    '''

    # returns raw data
    def getRaw(self, appid):
        # caching appid
        self.appid = appid

        cookies = {'birthtime': '28801', 'lastagecheckage':'9-1-1991', 'mature_content': '1', 'wants_mature_content': '1'}

        # following steam json format
        data = {}
        data[appid] = {}
        data[appid]['success'] = False
        data[appid]['data'] = {}

        res = requests.get(self.store_url+appid, cookies=cookies)

        # checking if bundle exists
        # if bundle does not exist it redirects to store home, thus we check for any redirects
        if not res.history:
            data[appid]['success'] = True


        # if bundle exists procced with parsing
        if data[appid]['success']:
            details = {}
            soup = BeautifulSoup(res.content, 'html5lib')
            # get name of bundle and bundle_id
            details['name'] = soup.select('.pageheader')[0].text
            details['bundle_id'] = soup.select('.game_area_purchase_game')[0].get('data-ds-bundleid')
            # selecting the correct div
            leftcol = soup.find('div', {'class':'leftcol'})
            rightcol = soup.find('div', {'class':'rightcol'})
            
            # header image
            details['header_image'] = leftcol.select('.package_header')[0].get('src')
            
            # description
            if leftcol.select('.bundle_description'):
                details['bundle_description'] = leftcol.select('.bundle_description')[0].select('p')[0].text
            
            # from rightcol
            right_detail = str(rightcol.findAll('div', {'class':'details_block'})[0])
            details['genres'] = self._getList(right_detail, 'Genre:')
            details['developers'] = self._getList(right_detail, 'Developer:')
            details['publishers'] = self._getList(right_detail, 'Publisher:')
            details['franchise'] = self._getList(right_detail, 'Franchise:')
            details['languages'] = self._getList(right_detail, 'Languages:')
            details['drm'] = self._getList(right_detail, 'DRM:', 'space')
            
            details['categories'] = []
            for category in rightcol.findAll('div', {'class':'game_area_details_specs'}):
                dict = {}
                id = re.sub(r'^[\w:\/\.\?]+=', '', category.find('a').get('href'))
                id = int(re.sub(r'\D[\w]+', '', id))
                dict[id] = w3lib.html.remove_tags(str(category))
                details['categories'].append(dict)
            
            # prices
            details['price'] = {}
            details['price']['initial'] = 0
            details['price']['final'] = int(leftcol.select('.discount_block')[0].get('data-price-final'))
            details['price']['discount_percent'] = int(re.findall(r'\d+',leftcol.select('.bundle_base_discount')[0].text)[0])
            details['price']['initial_formatted'] = leftcol.select('.bundle_final_package_price')[0].text
            details['price']['final_formatted'] = leftcol.select('.discount_final_price')[0].text
            details['price']['initial'] = math.ceil((details['price']['final']/100)/((100-details['price']['discount_percent'])/100))*100
            
            
            # package items
            details['package_item'] = []
            for item in leftcol.findAll('div', {'class':'tab_item'}):
                package_item = {}
                package_item['name'] = item.select('.tab_item_name')[0].text
                if item.get('data-ds-packageid'):
                    package_item['packageid'] = item.get('data-ds-packageid')
                    package_item['appid'] = item.get('data-ds-appid').split(",")
                    for i in range(len(package_item['appid'])):
                        package_item['appid'][i] = int(package_item['appid'][i])
                else:
                    package_item['appid'] = int(item.get('data-ds-appid'))
                
                package_item['app_link'] = item.select('.tab_item_overlay')[0].get('href')
                package_item['app_image'] = item.select('.tab_item_cap_img')[0].get('src')
                
                # app prices
                package_item['app_price'] = {}
                package_item['app_price']['final'] = int(item.select('.discount_block')[0].get('data-price-final'))
                package_item['app_price']['final_formatted'] = item.select('.discount_final_price')[0].text
                
                # platforms
                package_item['platforms'] = {}
                package_item['platforms']['windows'] = True if item.select('.win') else False
                package_item['platforms']['mac'] = True if item.select('.mac') else False
                package_item['platforms']['linux'] = True if item.select('.linux') else False
                
                # categories
                package_item['categories'] = item.select('.tab_item_details')[0].text.strip().split(",")
                
                details['package_item'].append(package_item)
                
            data[appid]['data'] = details

        # if game exists
        if data[appid]['success']:
            self.data = data[appid]['data']
            return self.data
        else:
            return None

    # populate internal data dictionary
    def _populate(self, appid):
        if not self.data or appid != self.appid or self.appid == 0:
            self.getRaw(appid)

    # returns name
    def getName(self, appid):
        self._populate(appid)
        return self.data['name'] if 'name' in self.data else None

    # returns header image
    def getHeaderImage(self, appid):
        self._populate(appid)
        return self.data['header_image'] if 'header_image' in self.data else None

    # returns bundle description
    def getBundleDescription(self, appid):
        self._populate(appid)
        return self.data['bundle_description'] if 'bundle_description' in self.data else None

    # returns genre
    def getGenres(self, appid):
        self._populate(appid)
        return self.data['genres'] if 'genres' in self.data else None

    # returns developer
    def getDevelopers(self, appid):
        self._populate(appid)
        return self.data['developers'] if 'developers' in self.data else None

    # returns publisher
    def getPublishers(self, appid):
        self._populate(appid)
        return self.data['publishers'] if 'publishers' in self.data else None

    # returns franchise
    def getFranchise(self, appid):
        self._populate(appid)
        return self.data['franchise'] if 'franchise' in self.data else None

    # returns languages
    def getLanguages(self, appid):
        self._populate(appid)
        return self.data['languages'] if 'languages' in self.data else None

    # returns drm
    def getDRM(self, appid):
        self._populate(appid)
        return self.data['drm'] if 'drm' in self.data else None

    # returns categories
    def getCategories(self, appid):
        self._populate(appid)
        return self.data['categories'] if 'categories' in self.data else None

    # returns price
    def getPrice(self, appid):
        self._populate(appid)
        return self.data['price'] if 'price' in self.data else None

    # returns package items
    def getPackageItem(self, appid):
        self._populate(appid)
        return self.data['package_item'] if 'package_item' in self.data else None