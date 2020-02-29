# coding=utf-8
import json
from os import path
from pod_base import PodBase, calc_offset, ConfigException, InvalidDataException


def convert_list_to_string(data, separator=","):
    """
    تبدیل لیست به رشته

    :type data: list
    :type separator: str
    :return: str
    """
    if type(data) == list:
        return separator.join(data)
    if data:
        return data

    return ''


class PodProduct(PodBase):
    """لیست کلیه محصولات کسب و کار بدون فیلتر در خروجی نمایش داده خواهد شد"""
    SCOPE_PARENT_PRODUCT = "PARENT_PRODUCT"
    """لیست محصولاتی از کسب  و کار خودتان که در کسب و کار دیگری، parent شده است به انضمام اطلاعات کسب و کار مذکور."""
    SCOPE_BUSINESS_PRODUCT = "BUSINESS_PRODUCT"
    """لیست محصولاتی از کسب و کار خودتان، که روی آن محصول به کسب و کار واسطی اجازه صدور فاکتور داده اید."""
    SCOPE_DEALER_PRODUCT_PERMISSION = "DEALER_PRODUCT_PERMISSION"

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodProduct, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                         sc_voucher_hash, path.join(here, "json_schema.json"))

    def __get_private_call_address(self):
        """
        دریافت آدرس سرور پرداخت از فایل کانفیگ

        :return: str
        :raises: :class:`ConfigException`
        """
        private_call_address = self.config.get("private_call_address", self._server_type)
        if private_call_address:
            return private_call_address

        raise ConfigException("config `private_call_address` in {} not found".format(self._server_type))

    def add_product(self, name, price, description, available_count=0, **kwargs):
        """
        تعریف محصول

        :param str name: نام محصول
        :param float price: قیمت محصول (ریال)
        :param str description:  توضیحات
        :param int available_count:  موجودی
        :return: dict
        """
        return self.__add_product(name=name, price=price, description=description, available_count=available_count,
                                  **kwargs)

    def add_sub_product(self, group_id, name, description, price, attributes, available_count=0, **kwargs):
        """
        اضافه کردن زیر محصول

        :param int group_id: شناسه گروه محصول
        :param str name: نام زیر محصول
        :param str description: توضیحات محصول
        :param float price: قیمت زیر محصول
        :param list attributes: لیست خصوصیت های زیر محصول
        :param int available_count: موجودی محصول
        :return: dict
        """
        kwargs["groupId"] = group_id
        kwargs["attributes"] = attributes
        return self.__add_product(name=name, price=price, available_count=available_count, description=description,
                                  validation_schema_name="addSubProduct", **kwargs)

    def __add_product(self, name, price, description, available_count=0, validation_schema_name="addProduct", **kwargs):
        kwargs["name"] = name
        kwargs["price"] = price
        kwargs["availableCount"] = available_count
        kwargs["description"] = description

        kwargs = self.__set_default_value_for_product(kwargs)
        self._validate(kwargs, validation_schema_name)

        kwargs = self.__prepare_product_info(kwargs)

        return self._request.call(
            super(PodProduct, self)._get_sc_product_settings("/nzh/biz/addProduct", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __prepare_attribute_value(attributes):
        att_code = []
        att_value = []
        att_group = []

        for attribute in attributes:
            att_code.append(attribute.get("code", ""))
            att_value.append(attribute.get("value", ""))
            att_group.append(attribute.get("group", ""))

        return att_code, att_value, att_group

    def __prepare_product_info(self, data):
        if "metaData" in data:
            data["metaData"] = json.dumps(data["metaData"])

        (data["attCode[]"], data["attValue[]"], data["attGroup[]"]) = \
            self.__prepare_attribute_value(data.pop("attributes", []))

        return self.__prepare_tags(data)

    @staticmethod
    def __prepare_tags(data):
        data["tags"] = convert_list_to_string(data.pop("tags", []))
        if not data["tags"]:
            del data["tags"]

        data["tagTrees"] = convert_list_to_string(data.pop("tagTrees", []))
        if not data["tagTrees"]:
            del data["tagTrees"]

        return data

    @staticmethod
    def __set_default_value_for_product(data):
        data.setdefault("unlimited", True)
        data.setdefault("enable", True)
        data.setdefault("canComment", True)
        data.setdefault("canLike", True)
        data.setdefault("canRate", True)
        data.setdefault("discount", 0)
        data.setdefault("availableCount", data.pop("available_count", 0))

        if int(data["availableCount"]) > 0:
            del data["unlimited"]
        else:
            del data["availableCount"]

        return data

    @staticmethod
    def __prepare_products(product):
        product["attCode"] = product.pop("attCode[]", [])
        product["attValue"] = product.pop("attValue[]", [])
        product["attGroup"] = product.pop("attGroup[]", [])

        if "metaData" in product:
            product["metadata"] = json.dumps(product.pop("metaData", []))

        if "tags" in product:
            product["tags"] = convert_list_to_string(product["tags"])

        return product

    def add_products(self, products, **kwargs):
        """
        افزودن گروهی محصولات

        :param list products: لیست محصولات
        :return: list
        """
        data = []
        for product in products:
            product = self.__set_default_value_for_product(product)
            self._validate(product, "addProduct")
            product = self.__prepare_product_info(product)

            if "metaData" in product:
                product["metadata"] = product.pop("metaData", {})
            product = self.__prepare_products(product)
            data.append(product)

        kwargs["data"] = json.dumps(data)

        return self._request.call(
            super(PodProduct, self)._get_sc_product_settings("/nzh/biz/addProducts", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def update_product(self, entity_id, name, description, price, **kwargs):
        """
        ویرایش محصول

        :param int entity_id:   شناسه محصول
        :param str name: نام محصول
        :param str description: توضیحات محصول
        :param float price:  قیمت محصول
        :return: dict
        """
        kwargs["entityId"] = entity_id
        kwargs["name"] = name
        kwargs["description"] = description
        kwargs["price"] = price
        kwargs.setdefault("changePreview", False)
        kwargs = self.__set_default_value_for_product(kwargs)

        self._validate(kwargs, "updateProduct")

        kwargs = self.__prepare_product_info(kwargs)

        return self._request.call(
            super(PodProduct, self)._get_sc_product_settings("/nzh/biz/updateProduct", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def update_products(self, products, **kwargs):
        """
        ویرایش گروهی محصولات

        :param list products:
        :return: list
        """
        data = []
        for product in products:
            product.setdefault("changePreview", False)
            product = self.__set_default_value_for_product(product)
            self._validate(product, "updateProducts")

            if "metaData" in product:
                product["metadata"] = product.pop("metaData", {})

            product = self.__prepare_product_info(product)
            product = self.__prepare_products(product)
            data.append(product)

        kwargs["data"] = json.dumps(data)

        return self._request.call(
            super(PodProduct, self)._get_sc_product_settings("/nzh/biz/updateProducts", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def get_product_list(self, token=None, **kwargs):
        """
        لیست محصولات تمام کسب و کارها

        :param str token: توکن دسترسی کاربر - در صورتی که ارسال نکنید توکن کسب و کاریتان ست می شود
        :return: list
        """
        headers = self._get_headers()
        if token is not None:
            headers["_token_"] = token

        kwargs = self.__set_pagination_params(kwargs)

        self._validate(kwargs, "getProductList")

        if "attributes" in kwargs:
            kwargs["attributeCode[]"], kwargs["attributeValue[]"] = \
                self.__prepare_attribute_value_for_product_list(kwargs.pop("attributes", []))

        return self._request.call(super(PodProduct, self)._get_sc_product_settings("/nzh/productList"), params=kwargs,
                                  headers=headers, **kwargs)

    def get_business_product_list(self, **kwargs):
        """
        دریافت لیست محصولات کسب و کار

        :return: list
        """
        kwargs = self.__set_pagination_params(kwargs)
        self._validate(kwargs, "getBusinessProductList")

        if "attributes" in kwargs:
            kwargs["attributeCode[]"], kwargs["attributeValue[]"] = \
                self.__prepare_attribute_value_for_product_list(kwargs.pop("attributes", []))

        if "attributeSearchQuery" in kwargs:
            kwargs["attributeSearchQuery"] = json.dumps(kwargs["attributeSearchQuery"])

        return self._request.call(super(PodProduct, self)._get_sc_product_settings("/nzh/biz/productList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __set_pagination_params(params):
        if "id" in params:
            params.pop("offset", 0)
            params.pop("lastId", 0)
            params.pop("firstId", 0)
            params.pop("page", 0)
            params.pop("size", 0)
            return params

        if "firstId" not in params and "lastId" not in params and "page" not in params:
            params.setdefault("page", 1)

        params.setdefault("size", 50)
        if "page" in params:
            params["offset"] = calc_offset(params["page"], params["size"])
            del params["page"]

        return params

    @staticmethod
    def __prepare_attribute_value_for_product_list(attributes):
        code = []
        value = []
        for attribute in attributes:
            code.append(attribute.get("code", ""))
            value.append(attribute.get("value", ""))

        return code, value

    def get_attribute_template_list(self, **kwargs):
        """
        دریافت لیست قالب مشخصات

        :return: list
        """
        kwargs = self.__set_pagination_params(kwargs)
        self._validate(kwargs, "getAttributeTemplateList")

        return self._request.call(super(PodProduct, self)._get_sc_product_settings("/nzh/getAttributeTemplateList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def search_product(self, **kwargs):
        """
        جستجو در محصولات

        :return: dict,
        """
        kwargs = self.__set_pagination_params(kwargs)
        self._validate(kwargs, "searchProduct")

        if "attributes" in kwargs:
            kwargs["attributeCode[]"], kwargs["attributeValue[]"] = \
                self.__prepare_attribute_value_for_product_list(kwargs.pop("attributes", []))

        kwargs = self.__prepare_tags(kwargs)

        return self._request.call(super(PodProduct, self)._get_sc_product_settings("/nzh/searchProduct"), params=kwargs,
                                  headers=self._get_headers(), **kwargs)

    def search_sub_product(self, product_group_id, **kwargs):
        """
        جستجو در زیر محصولات

        :param list product_group_id:
        :return: list
        """
        if type(product_group_id) == list:
            kwargs["productGroupId"] = product_group_id
        else:
            kwargs["productGroupId"] = [product_group_id]
        kwargs = self.__set_pagination_params(kwargs)
        self._validate(kwargs, "searchSubProduct")

        if "attributes" in kwargs:
            kwargs["attributeCode[]"], kwargs["attributeValue[]"] = \
                self.__prepare_attribute_value_for_product_list(kwargs.pop("attributes", []))

        kwargs = self.__prepare_tags(kwargs)

        return self._request.call(super(PodProduct, self)._get_sc_product_settings("/nzh/searchSubProduct"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)
