import sqlite3


class Database:
    def __init__(self, database=':memory:'):
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

    def createDatabase(self):
        self.__cursor.execute("PRAGMA foreign_keys = ON")

        self.__cursor.execute("DROP TABLE IF EXISTS image_product")
        self.__cursor.execute("DROP TABLE IF EXISTS images")
        self.__cursor.execute("DROP TABLE IF EXISTS document_product")
        self.__cursor.execute("DROP TABLE IF EXISTS documents")
        self.__cursor.execute("DROP TABLE IF EXISTS product_property_value")
        self.__cursor.execute("DROP TABLE IF EXISTS property_values")
        self.__cursor.execute("DROP TABLE IF EXISTS properties")
        self.__cursor.execute("DROP TABLE IF EXISTS products")
        self.__cursor.execute("DROP TABLE IF EXISTS categories")
        self.__cursor.execute("DROP TABLE IF EXISTS brands")

        self.__cursor.execute("CREATE TABLE brands \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            name varchar(255));")

        self.__cursor.execute("CREATE TABLE categories \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            name varchar(255));")

        self.__cursor.execute("CREATE TABLE products \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            name varchar(255), \
                            sku varchar(255), \
                            url varchar(255), \
                            code varchar(255), \
                            brand_id int REFERENCES brands(id), \
                            category_id int REFERENCES categories(id), \
                            description text, \
                            short_description text);")

        self.__cursor.execute("CREATE TABLE images \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            url varchar(255));")

        self.__cursor.execute("CREATE TABLE image_product \
                            (product_id int REFERENCES products(id), \
                            image_id int REFERENCES images(id));")

        self.__cursor.execute("CREATE TABLE documents \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            url varchar(255), \
                            name varchar(255));")

        self.__cursor.execute("CREATE TABLE document_product \
                            (product_id int REFERENCES products(id), \
                            document_id int REFERENCES documents(id));")

        self.__cursor.execute("CREATE TABLE properties \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            name varchar(255));")

        self.__cursor.execute("CREATE TABLE property_values \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            property_id int REFERENCES properties(id), \
                            value varchar(255));")

        self.__cursor.execute("CREATE TABLE product_property_value \
                        (product_id int REFERENCES products(id), \
                        property_value_id int REFERENCES property_values(id));")

    def __saveBrand(self, name):
        brand_id = self.__cursor.execute(
            "SELECT id FROM brands WHERE name = '"+name+"' LIMIT 1"
        ).fetchone()
        if brand_id != None:
            return brand_id[0]
        self.__cursor.execute("INSERT INTO brands (name) VALUES (?)", (name,))
        return self.__cursor.lastrowid

    def __saveCategory(self, name):
        category_id = self.__cursor.execute(
            "SELECT id FROM categories WHERE name = '"+name+"' LIMIT 1"
        ).fetchone()
        if category_id != None:
            return category_id[0]
        self.__cursor.execute(
            "INSERT INTO categories (name) VALUES (?)", (name,)
        )
        return self.__cursor.lastrowid

    def __saveProperty(self, name):
        property_id = self.__cursor.execute(
            "SELECT id FROM properties WHERE name ='"+name.replace("'", "").replace('"', '')+"' LIMIT 1").fetchone()
        if property_id != None:
            return property_id[0]
        self.__cursor.execute(
            "INSERT INTO properties (name) VALUES (?)", (name.replace("'", "").replace('"', ''),))
        return self.__cursor.lastrowid

    def __saveImage(self, url):
        image_id = self.__cursor.execute(
            "SELECT id FROM images WHERE url = '"+url+"' LIMIT 1").fetchone()
        if image_id != None:
            return image_id[0]
        self.__cursor.execute("INSERT INTO images (url) VALUES (?)", (url,))
        return self.__cursor.lastrowid

    def __saveDocument(self, name, url):
        document_id = self.__cursor.execute(
            "SELECT id FROM documents WHERE name = '"+name+"' AND \
            url = '"+url+"' LIMIT 1"
        ).fetchone()
        if document_id != None:
            return document_id[0]
        self.__cursor.execute(
            "INSERT INTO documents (name, url) VALUES (?,?)", (name, url)
        )
        return self.__cursor.lastrowid

    def __savePropertyValue(self, property_id, value):
        if value == '':
            return
        while value[0] == ' ':
            value = value[1:]
            if value == '':
                return
        while value[-1] == ' ':
            value = value[:-1]
            if value == '':
                return
        property_value_id = self.__cursor.execute(
            "SELECT id FROM property_values WHERE \
                property_id = ? AND value = ? LIMIT 1", (str(property_id), value)
        ).fetchone()
        if property_value_id != None:
            return property_value_id[0]
        self.__cursor.execute("INSERT INTO property_values \
                            (property_id, value) VALUES (?,?)", (
            str(property_id), value
        ))
        self.__connection.commit()
        return self.__cursor.lastrowid

    def __connectPropertyValue(self, product_id, value_id):
        if value_id == None:
            return False
        if self.__cursor.execute("SELECT * FROM product_property_value WHERE \
                                product_id = ? AND property_value_id = ? \
                                LIMIT 1", (
            product_id,
            value_id
        )).fetchone() != None:
            return True
        self.__cursor.execute(
            "INSERT INTO product_property_value (product_id, property_value_id) \
            VALUES (?,?)", (product_id, value_id)
        )
        return True

    def __buildBrands(self, brands):
        output = []
        for brand in brands:
            output.append(Brand(id=brand[0],
                                name=brand[1]))
        return output

    def __getProductDocuments(self, product_id):
        documents = []
        for row in self.__cursor.execute(
            "SELECT documents.url from documents join \
            document_product on documents.id = document_product.document_id \
            WHERE document_product.product_id = "+str(product_id)
        ):
            documents.append(row[0])
        return documents

    def __getProductImages(self, product_id):
        images = []
        for row in self.__cursor.execute(
            "SELECT images.url from images join \
            image_product on images.id = image_product.image_id \
            WHERE image_product.product_id = "+str(product_id)
        ):
            images.append(row[0])
        return images

    def __getProductProperties(self, product_id):
        properties = {}
        for row in self.__cursor.execute(
            "SELECT properties.name, property_values.value from products \
            join product_property_value on \
            products.id = product_property_value.product_id \
            join property_values on \
            product_property_value.property_value_id = property_values.id \
            join properties on property_values.property_id = properties.id \
            WHERE products.id = ?", (str(product_id),)
        ):
            if row[0] not in properties:
                properties[row[0]] = []
            properties[row[0]].append(row[1])
        return properties

    def getBrandsById(self, ids):
        query = "SELECT name FROM brands WHERE id IN ("+str(ids)+")"
        query = query.replace('((', '(').replace('))', ')')
        return self.__cursor.execute(query).fetchone()[0]

    def getBrandByName(self, name):
        return self.__buildBrands(
            self.__cursor.execute(
                "SELECT id, name FROM brands WHERE name = ?", (name,)
            ).fetchall()
        )[0]

    def getCategoryById(self, category_id):
        return self.__cursor.execute(
            "SELECT name FROM categories WHERE id = "+str(category_id)
        ).fetchone()[0]

    def getProductsById(self, ids):
        query = "SELECT * FROM products WHERE id IN ("+str(ids)+")"
        query = query.replace('((', '(').replace('))', ')')
        response = self.__cursor.execute(query).fetchall()
        return self.__buildProducts(response)

    def getProducts(self, category_id='%', brand_id='%'):
        query = "SELECT * FROM products WHERE category_id LIKE ? AND brand_id LIKE ?"
        response = self.__cursor.execute(query, (category_id, brand_id)).fetchall()
        return self.__buildProducts(response)

    def __buildProducts(self, response):
        products = []
        for item in response:
            products.append(Product({
                'id': item[0],
                'name': item[1],
                'sku': item[2],
                'url': item[3],
                'code': item[4],
                'brand': self.getBrandsById(item[5]),
                'category': self.getCategoryById(item[6]),
                'description': item[7],
                'short_description': item[8],
                'documents': self.__getProductDocuments(item[0]),
                'images': self.__getProductImages(item[0]),
                'properties': self.__getProductProperties(item[0])
            }))
        return products

    def __processImagesField(self, data):
        return data.split(',')

    def __processDocementsField(self, data):
        documents = {}
        data = data[1:-1].split('},{')
        for i in range(int(len(data)/2)):
            documents[data[i*2]] = data[i*2+1]
        return documents

    def __processPropertyValueField(self, value):
        return value.split('\\\\\\\\\\')

    def saveProduct(self, data):
        product = data.copy()
        # Trim empty values
        for key, value in dict(product).items():
            if value == None or value == '':
                del product[key]

        # Saving images and documents
        image_ids = []
        if 'Изображения' in product:
            for image in self.__processImagesField(product.pop('Изображения')):
                image_ids.append(self.__saveImage(image))
        document_ids = []
        if 'Документация' in product:
            documents = self.__processDocementsField(
                product.pop('Документация'))
            for doc_name in list(documents.keys()):
                document_ids.append(self.__saveDocument(
                    doc_name, documents[doc_name]))

        # Removing default fields and saving it to variables
        name = product.pop('Наименование')
        if 'Описание' in product:
            description = product.pop('Описание')
        else:
            description = ''
        if 'Доп. описание' in product:
            short_description = product.pop('Доп. описание')
        else:
            short_description = ''
        if 'Артикул' in product:
            sku = product.pop('Артикул')
        else:
            sku = ''
        url = sku.replace(' ', '-').lower()
        if 'Код товара' in product:
            code = product.pop('Код товара')
        else:
            code = ''
        if 'Производитель' in product:
            brand_id = self.__saveBrand(product.pop('Производитель'))
        else:
            brand_id = self.__saveBrand('NO_BRAND')
        category_id = self.__saveCategory(product.pop('Категория'))

        # Check if product exists
        check = self.__cursor.execute("SELECT id FROM products WHERE \
                            name = ? AND \
                            sku = ? AND \
                            url = ? AND \
                            code = ? AND \
                            brand_id = ? AND \
                            category_id = ? AND \
                            description = ? AND \
                            short_description = ? \
                            LIMIT 1", (
            name,
            sku,
            url,
            code,
            brand_id,
            category_id,
            description,
            short_description
        )
        ).fetchone()

        if check == None:
            # Saving product in database
            self.__cursor.execute("INSERT INTO products (name, sku, url, code, \
                                brand_id, category_id, description, \
                                short_description) VALUES (?,?,?,?,?,?,?,?);", (
                name,
                sku,
                url,
                code,
                brand_id,
                category_id,
                description,
                short_description
            ))
            product_id = self.__cursor.lastrowid
        else:
            product_id = check[0]

        # Creating connection between product and images/documents
        for image_id in image_ids:
            self.__cursor.execute("INSERT INTO image_product \
                                (product_id, image_id) VALUES (?,?)", (
                product_id, image_id
            ))
        for document_id in document_ids:
            self.__cursor.execute("INSERT INTO document_product \
                                (product_id, document_id) VALUES (?,?)", (
                product_id, document_id
            ))

        # Creating propertiest and property values
        property_values_id = []
        keys = list(product.keys())
        for property_name in keys:
            # Creating property
            property_id = self.__saveProperty(property_name)
            property_value = product.pop(property_name)
            # Creating property values
            for value in self.__processPropertyValueField(property_value):
                property_values_id.append(
                    self.__savePropertyValue(property_id, value)
                )

        # Creating connection between product and property values
        for value_id in property_values_id:
            self.__connectPropertyValue(product_id, value_id)

        # Commiting to database and returning id of created product
        self.__connection.commit()
        return product_id


class Brand:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Product:
    def __init__(self, attributes):
        for key in attributes.keys():
            setattr(self, key, attributes[key])


class Property:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PropertyValue:
    def __init__(self, id, property, value):
        self.id = id
        self.property = property
        self.value = value


class Document:
    def __init__(self, id, url, name):
        self.id = id
        self.url = url
        self.name = name


class Image:
    def __init__(self, id, url):
        self.id = id
        self.url = url
