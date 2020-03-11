from eamonn import eamonn

# eamonn.ib_pict(r"F:\Note\文字识别\百度ocr\识别\test\66.png",r"F:\Note\文字识别\百度ocr\识别\test\2456.png")

database = {
    "企业名称" : "山东省鲁商冰轮建筑设计有限公司",
    "企业链接地址" : "http://cx.jlsjsxxw.com/CorpInfo/CorpSwDetailInfo.aspx?rowGuid=ae9f9b3f-e094-4de1-aa93-3f5f0454220e&corpid=49557187-5&VType=1&CertType=2",
    "企业类型" : "设计",
    "企业营业地址" : "延边朝鲜族自治州珲春市边境经济合作区8号小区",
    "采集来源省" : "吉林省",
    "省内或入省" : "省外",
    "企业注册地址" : "山东省济南市济南市高新区新宇路750号14号楼5单元",
    "来源网站" : "吉林省建筑市场监管与诚信信息管理平台",
    "网站代码" : "B--10",
    "采集时间" : "2020-01-14 10:11:54",
    "营业执照号" : "370000018021175",
    "组织机构代码" : "49557187-5"
}

res = eamonn.d2o(database)
print(res.省内或入省)