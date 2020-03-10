import json


def get_med_spec_min(medicine):
    """计算药品最小规格，目前该方法不够充分
    """

    SPEC_MIN = {'块': '块', 'ml': "毫升", 'g': '克', '包': "包", '片': "片", '袋': "袋", '粒': "粒", '揿': "揿",
                '瓶': "瓶", '盒': "盒", 'mg': '毫克', 'ug': '微克', '丸': "丸", '板': "板", '贴': "贴", '支': "支",
                's': '片'}
    spec_min = []
    for spm in SPEC_MIN.keys():
        if spm in medicine.spec:
            spec_min.append(SPEC_MIN[spm])
    if "板" in spec_min and len(spec_min) > 1:
        spec_min.remove("板")

    return ",".join(spec_min)


def get_med_brand(medicine):
    """尝试再说明书寻找药品的商标
    """

    BRAND = ['商品名/商标', '商标', '品牌']

    manual = json.loads(medicine.manual, encoding="utf-8")
    for key in manual.keys():
        if key in BRAND:
            return manual[key]

    return None


def compute_completion(medicine):
    """计算基础信息完整度及丰富度
    """
    # 计算数据完整度
    empty_key = 0
    for key in medicine.REQUIRED_KEYS:
        value = medicine.__dict__.get(key, None)
        if not value:
            empty_key += 1

    completion = 1 - empty_key/len(medicine.REQUIRED_KEYS)

    medicine.data_completion = round(completion, 2)

    # 计算数据丰富度
    empty_option = 0
    for option in medicine.OPTIONAL_KEYS:
        value = medicine.__dict__.get(option, None)
        if not value:
            empty_option += 1

    richness = 1 - empty_option/len(medicine.OPTIONAL_KEYS)

    medicine.data_richness = round(richness, 2)

    medicine.save()
