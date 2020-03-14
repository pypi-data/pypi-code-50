# -*- coding: utf-8 -*-
import json

from flask import jsonify
from flask_restful import Api, Resource, reqparse


from aishow_model_app.models.resource_model import DouyinSpecialLive, ResourceTable, DouyinSingleChainLive, DouyinViewExport, \
    KuaiShouLive, RedbookImageTextLink, TaobaoLive, QitengTaobaoExportLiveOffer, QitengRedbookPrice, \
    QitengDouyinViewPrice


from aishow_model_app.apis.base import BaseAPI
from aishow_model_app.ext import db

ResourceApi = Api(prefix='/platformresource/list')
#达人的增删改查
class TotalResource(Resource,BaseAPI):

    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('page', type=int)
        self.parse.add_argument('limit', type=int)
        self.parse.add_argument('user_id', type=str)
        self.parse.add_argument('flag', type=str)
        self.parse.add_argument('select_type', type=int)
        self.parse.add_argument('kol_id', type=str)
        self.parse.add_argument('kol_name', type=str)
        self.parse.add_argument('platform', type=str)
        self.parse.add_argument('type_datil', type=str)
        self.parse.add_argument('company', type=str)
        self.parse.add_argument('contact_name', type=str)
        self.parse.add_argument('contact_phone', type=str)
        self.parse.add_argument('fans', type=float)
        self.parse.add_argument('status', type=str)

    def get(self):
        args = self.parse.parse_args()
        print('resourcetable args get',args)
        print('resourcetable args get',args['select_type'])
        print('resourcetable args get',type(args['select_type']))
        all_list = []
        totle = 0
        #抖音专场直播
        if args['select_type'] == 1:
            dysl_query = DouyinSpecialLive.query.offset((args['page'] - 1) * args['limit']).limit(args['limit']).all()
            totle = DouyinSpecialLive.query.count()
            for item in dysl_query:
                dict = {}
                dict['dysl'] = DouyinSpecialLive.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    dict['rsst'] = res_dict
                all_list.append(dict)
        #抖音单链接
        elif args['select_type'] == 2:
            dyscl_query = DouyinSingleChainLive.query.offset((args['page'] - 1) * args['limit']).limit(args['limit']).all()
            totle = DouyinSingleChainLive.query.count()
            for item in dyscl_query:
                dict = {}
                dict['dyscl'] = DouyinSingleChainLive.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    dict['rsst'] = res_dict
                all_list.append(dict)
        #抖音短视频
        elif args['select_type'] == 3:
            dyscl_query = DouyinViewExport.query.offset((args['page'] - 1) * args['limit']).limit(
                args['limit']).all()
            totle = DouyinViewExport.query.count()
            for item in dyscl_query:
                dict = {}
                dict['dyve'] = DouyinViewExport.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    dict['rsst'] = res_dict
                dysl2_query = QitengDouyinViewPrice.query.filter(QitengDouyinViewPrice.douyin_view_export_id == item.id).first()
                if dysl2_query:
                    dysl_dict = QitengDouyinViewPrice.queryToDict(dysl2_query)
                    for k,v in dysl_dict.items():
                        dict['dyve'][k] = v
                all_list.append(dict)
        #快手直播
        elif args['select_type'] == 4:
            dyscl_query = KuaiShouLive.query.offset((args['page'] - 1) * args['limit']).limit(
                args['limit']).all()
            totle = KuaiShouLive.query.count()
            for item in dyscl_query:
                dict = {}
                dict['ksl'] = KuaiShouLive.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    dict['rsst'] = res_dict
                all_list.append(dict)
        #小红书图文链接
        elif args['select_type'] == 5:
            dyscl_query = RedbookImageTextLink.query.offset((args['page'] - 1) * args['limit']).limit(
                args['limit']).all()
            totle = RedbookImageTextLink.query.count()
            for item in dyscl_query:
                dict = {}
                dict['rbitl'] = RedbookImageTextLink.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    dict['rsst'] = res_dict
                dysl2_query = QitengRedbookPrice.query.filter(
                    QitengRedbookPrice.redbook_image_text_link_id ==  item.id).first()
                if dysl2_query:
                    dysl_dict = QitengDouyinViewPrice.queryToDict(dysl2_query)
                    for k,v in dysl_dict.items():
                        dict['rbitl'][k] = v
                all_list.append(dict)
        #淘宝直播
        elif args['select_type'] == 6:
            dyscl_query = TaobaoLive.query.offset((args['page'] - 1) * args['limit']).limit(
                args['limit']).all()
            totle = TaobaoLive.query.count()
            for item in dyscl_query:
                dict = {}
                dict['tbl'] = TaobaoLive.queryToDict(item)
                res_query = item.resource_tables
                if res_query:
                    res_dict = ResourceTable.queryToDict(res_query)
                    print('res_dict',res_dict)
                    dict['rsst'] = res_dict
                dysl2_query = QitengTaobaoExportLiveOffer.query.filter(
                    QitengTaobaoExportLiveOffer.taobao_live_id == item.id).first()
                if dysl2_query:
                    dysl_dict = QitengTaobaoExportLiveOffer.queryToDict(dysl2_query)
                    print(dysl_dict)
                    for k,v in dysl_dict.items():
                        dict['tbl'][k] = v
                all_list.append(dict)
        # print('all_list',all_list)
        else:
            dict = {}
            rsst_query = ResourceTable.query.all()
            if rsst_query:
                res_dict = ResourceTable.queryToDict(rsst_query)
                # print('res_dict', res_dict)
                # dict['rsst'] = res_dict
                all_list=res_dict
        print('all_list',json.dumps({'code': 20000, 'data': {'total': totle, 'items': all_list }},ensure_ascii=False))
        return jsonify({'code': 20000, 'data': {'total': totle, 'items': all_list }})

    def post(self):
        print('resource post')
        args = self.parse.parse_args()
        res = self.add_updata(args)
        if res:
            return jsonify({'code': 20000, 'data': {'total': 0, 'items': [],'msg':'失败，请输入正确的数据'}})
        else:
        # res_query = ResourceTable.query.offset((int(args['page']) - 1) * int(args['limit'])).limit(
        #     int(args['limit'])).all()
        # totle = ResourceTable.query.count()
        # res_dict = ResourceTable.queryToDict(res_query)
        #
            return self.get()

    def put(self):
        print('resource put')
        args = self.parse.parse_args()
        res = self.add_updata(args)
        if res:
            return jsonify({'code': 20000, 'data': {'total': 0, 'items': [],'msg':'更新失败，请输入正确的数据'}})
        else:
            return self.get()

    def delete(self):
        args = self.parse.parse_args()
        print('resourcetable delete args',args)
        res_obj = ResourceTable.query.filter(ResourceTable.id == int(args['user_id'])).first()
        res_id = res_obj.id
        print('res_id',res_id)
        flag = args.get('flag')
        if flag == '抖音专场直播':  # 抖音专场直播
            print('抖音专场直播')
            douyinsl_obj = DouyinSpecialLive.query.filter(DouyinSpecialLive.resource_table_id == res_id).first()
            if douyinsl_obj:
                try:
                    db.session.delete(douyinsl_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        elif flag == '抖音单链直播':  # 抖音专场直播
            print('抖音单链直播')
            douyinscl_obj = DouyinSingleChainLive.query.filter(DouyinSingleChainLive.resource_table_id == res_id).first()
            if douyinscl_obj:
                try:
                    db.session.delete(douyinscl_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        elif flag == '抖音短视频':  # 抖音专场直播
            print('抖音短视频')
            douyinve_obj = DouyinViewExport.query.filter(DouyinViewExport.resource_table_id == res_id).first()
            if douyinve_obj:
                try:
                    db.session.delete(douyinve_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        elif flag == '快手直播':  # 抖音专场直播
            print('快手直播')
            ks_obj = KuaiShouLive.query.filter(KuaiShouLive.resource_table_id == res_id).first()
            if ks_obj:
                try:
                    db.session.delete(ks_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        elif flag == '小红书图文链接':  # 抖音专场直播
            print('小红书图文链接')
            rebbookitl_obj = RedbookImageTextLink.query.filter(RedbookImageTextLink.resource_table_id == res_id).first()
            if rebbookitl_obj:
                try:
                    db.session.delete(rebbookitl_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        elif flag == '淘宝直播':  # 抖音专场直播
            print('淘宝直播')
            tbl_obj = TaobaoLive.query.filter(TaobaoLive.resource_table_id == res_id).first()
            if tbl_obj:
                try:
                    db.session.delete(tbl_obj)
                    db.session.commit()
                except Exception as e:
                    print('e', e)
        if res_obj:
            try:
                db.session.delete(res_obj)
                db.session.commit()
            except Exception as e:
                print('e', e)
        res_query = ResourceTable.query.offset((int(args['page']) - 1) * int(args['limit'])).limit(
            int(args['limit'])).all()
        totle = ResourceTable.query.count()
        res_dict = ResourceTable.queryToDict(res_query)
        return jsonify({'code': 20000, 'data': {'total': totle, 'items': res_dict}})

    def add_updata(self,args):
        status =args['status']
        if status=='create':
            rsourcetab = ResourceTable()
        else :
            rsourcetab = ResourceTable.query.filter(ResourceTable.kol_id==args['kol_id']).first()
        rsourcetab.kol_id = args.get('kol_id')
        rsourcetab.kol_name = args.get('kol_name')
        rsourcetab.platform = args.get('platform')
        rsourcetab.avatar = args.get('avatar')
        rsourcetab.type_datil = args.get('type_datil')
        rsourcetab.company = args.get('company')
        rsourcetab.contact_name = args.get('contact_name')
        rsourcetab.fans = args.get('fans')
        try:
            try:
                rsourcetab.save(rsourcetab)
            except Exception as e:
                print('TotalResource post except', e)
            resource_obj = ResourceTable.query.filter(ResourceTable.kol_id == args.get('kol_id')).all()[0]
            resource_id = resource_obj.id
            print(resource_id)
            flag = args.get('flag')
            if flag == '抖音专场直播':  # 抖音专场直播
                print('抖音专场直播')
                self.parse.add_argument('export_tag', type=str)
                self.parse.add_argument('special_offer', type=int)
                self.parse.add_argument('export_city', type=str)
                self.parse.add_argument('cooperation_case', type=str)
                self.parse.add_argument('douyin_special_cost_price', type=int)
                args1 = self.parse.parse_args()
                print('抖音专场直播 args1', args1)
                douyinsl = DouyinSpecialLive()
                douyinsl.resource_table_id = resource_id
                douyinsl.export_tag = args1.get('export_tag')
                douyinsl.special_offer = args1.get('special_offer')
                douyinsl.export_city = args1.get('export_city')
                douyinsl.cooperation_case = args1.get('cooperation_case')
                douyinsl.douyin_special_cost_price = args1.get('douyin_special_cost_price')
                try:
                    douyinsl.save(douyinsl)
                    # dysl_query = DouyinSpecialLive.query.offset((args1['page']) - 1 * args1['limit']).limit(args1['limit']).all()
                    # print('ok7')
                    # totle = DouyinSpecialLive.query.count()
                    # dysl_dict = DouyinSpecialLive.queryToDict(dysl_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': dysl_dict}})
                except Exception as e:
                    print('DouyinSpecialLive save except', e)
            elif flag == '抖音单链直播':  # 抖音单链直播
                self.parse.add_argument('douyin_export_classification', type=str)
                self.parse.add_argument('Single_chain_offer', type=int)
                self.parse.add_argument('introduction', type=str)
                self.parse.add_argument('live_time', type=str)
                self.parse.add_argument('selection_requirements', type=str)
                self.parse.add_argument('remarks', type=str)
                self.parse.add_argument('douyin_single_cost_price', type=int)
                args = self.parse.parse_args()
                print('抖音单链直播',args)
                douyinscl = DouyinSingleChainLive()
                douyinscl.resource_table_id = resource_id
                douyinscl.douyin_export_classification = args.get('douyin_export_classification')
                douyinscl.Single_chain_offer = args.get('Single_chain_offer')
                douyinscl.introduction = args.get('introduction')
                douyinscl.live_time = args.get('live_time')
                douyinscl.selection_requirements = args.get('selection_requirements')
                douyinscl.remarks = args.get('remarks')
                douyinscl.douyin_single_cost_price = args.get('douyin_single_cost_price')
                try:
                    douyinscl.save(douyinscl)
                    dyscl_query = DouyinSpecialLive.query.offset((args['page']) - 1 * args['limit']).limit(
                        args['limit']).all()
                    # totle = DouyinSingleChainLive.query.count()
                    # dyscl_dict = DouyinSingleChainLive.queryToDict(dyscl_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': dyscl_dict}})
                except Exception as e:
                    print('DouyinSpecialLive save except', e)
            elif flag == '抖音短视频':  # 抖音短视频
                self.parse.add_argument('export_tag', type=str)
                self.parse.add_argument('introduction', type=str)
                self.parse.add_argument('douyin_home_page', type=str)
                self.parse.add_argument('export_city', type=str)
                self.parse.add_argument('cooperation_case', type=str)
                self.parse.add_argument('better_sell_goods', type=str)
                self.parse.add_argument('douyin_export_classification', type=str)
                self.parse.add_argument('cooperation_mode', type=str)
                self.parse.add_argument('offer_less', type=int)
                self.parse.add_argument('offer_more', type=int)
                self.parse.add_argument('offer_less', type=int)
                self.parse.add_argument('star_offer', type=int)
                self.parse.add_argument('douyin_view_cost_price', type=int)
                args = self.parse.parse_args()
                douyinve = DouyinViewExport()
                douyinve.resource_table_id = resource_id
                douyinve.export_tag = args.get('export_tag')
                douyinve.introduction = args.get('introduction')
                douyinve.douyin_home_page = args.get('douyin_home_page')
                douyinve.export_city = args.get('export_city')
                douyinve.cooperation_case = args.get('cooperation_case')
                douyinve.better_sell_goods = args.get('better_sell_goods')
                douyinve.douyin_export_classification = args.get('douyin_export_classification')
                douyinve.cooperation_mode = args.get('cooperation_mode')
                douyinve.offer_less = args.get('offer_less')
                douyinve.offer_more = args.get('offer_more')
                douyinve.star_offer = args.get('star_offer')
                douyinve.douyin_view_cost_price = args.get('douyin_view_cost_price')
                try:
                    douyinve.save(douyinve)
                    # dyve_query = DouyinViewExport.query.offset((args['page']) - 1 * args['limit']).limit(
                    #     args['limit']).all()
                    # totle = DouyinViewExport.query.count()
                    # dyve_dict = DouyinViewExport.queryToDict(dyve_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': dyve_dict}})
                except Exception as e:
                    print('DouyinViewExport save except', e)
            elif flag == '快手直播':  # 快手直播
                self.parse.add_argument('avg_online_num', type=float)
                self.parse.add_argument('sell_classification', type=str)
                self.parse.add_argument('commission_less', type=int)
                self.parse.add_argument('commission_more', type=int)
                self.parse.add_argument('attributes', type=str)
                self.parse.add_argument('better_sell_goods', type=str)
                self.parse.add_argument('kuaishou_offer', type=int)
                self.parse.add_argument('kuaishou_cost_price', type=int)
                self.parse.add_argument('remarks', type=str)
                args = self.parse.parse_args()
                ksl = KuaiShouLive()
                ksl.resource_table_id = resource_id
                ksl.avg_online_num = args.get('avg_online_num')
                ksl.sell_classification = args.get('sell_classification')
                ksl.commission_less = args.get('commission_less')
                ksl.commission_more = args.get('commission_more')
                ksl.attributes = args.get('attributes')
                ksl.kuaishou_offer = args.get('kuaishou_offer')
                ksl.kuaishou_cost_price = args.get('kuaishou_cost_price')
                ksl.remarks = args.get('remarks')
                try:
                    ksl.save(ksl)

                    ksl_query = KuaiShouLive.query.offset((args['page']) - 1 * args['limit']).limit(
                        args['limit']).all()
                    # totle = KuaiShouLive.query.count()
                    # ksl_dict = KuaiShouLive.queryToDict(ksl_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': ksl_dict}})
                except Exception as e:
                    print('KuaiShouLive save except', e)
            elif flag == '小红书图文链接':  # 小红书图文链接
                print('抖音专场直播 args1')
                self.parse.add_argument('dianzan', type=int)
                self.parse.add_argument('redbook_link', type=str)
                self.parse.add_argument('export_city', type=str)
                self.parse.add_argument('export_tag', type=str)
                self.parse.add_argument('brand_partner', type=bool)
                self.parse.add_argument('redbook_cost_price', type=int)
                args = self.parse.parse_args()
                print('抖音专场直播 args1',args)
                rdltl = RedbookImageTextLink()
                rdltl.resource_table_id = resource_id
                rdltl.dianzan = args.get('dianzan')
                rdltl.redbook_link = args.get('redbook_link')
                rdltl.export_city = args.get('export_city')
                rdltl.export_tag = args.get('export_tag')
                rdltl.brand_partner = args.get('brand_partner')
                rdltl.redbook_cost_price = args.get('redbook_cost_price')
                try:
                    rdltl.save(rdltl)
                    rdltl_query = RedbookImageTextLink.query.offset((args['page']) - 1 * args['limit']).limit(
                        args['limit']).all()
                    # totle = RedbookImageTextLink.query.count()
                    # rdltl_dict = RedbookImageTextLink.queryToDict(rdltl_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': rdltl_dict}})
                except Exception as e:
                    print('RedbookImageTextLink save except', e)
            elif flag == '淘宝直播':  # 淘宝直播
                print('抖音专场直播 args')
                self.parse.add_argument('avg_viewing_num', type=float)
                self.parse.add_argument('main_category', type=str)
                self.parse.add_argument('introduction', type=str)
                self.parse.add_argument('taobao_offer', type=int)
                self.parse.add_argument('taobao_cost_price', type=int)
                args = self.parse.parse_args()
                print('抖音专场直播 args1', args)
                tbl = TaobaoLive()
                tbl.resource_table_id = resource_id
                tbl.avg_viewing_num = args.get('avg_viewing_num')
                tbl.main_category = args.get('main_category')
                tbl.introduction = args.get('introduction')
                tbl.taobao_offer = args.get('taobao_offer')
                tbl.taobao_cost_price = args.get('taobao_cost_price')
                try:
                    tbl.save(tbl)
                    # tbl_query = TaobaoLive.query.offset((args['page']) - 1 * args['limit']).limit(
                    #     args['limit']).all()
                    # totle = TaobaoLive.query.count()
                    # tbl_dict = TaobaoLive.queryToDict(tbl_query)
                    # return jsonify({'code': 20000, 'data': {'total': totle, 'items': tbl_dict}})
                except Exception as e:
                    print('TaobaoLive save except', e)
        except Exception as e:
            db.session.rollback()
            print('TotalResource post except', e)
            return e

    def update(self, department_data):
        """
        更新部门

        :param department_data: 部门信息
        :return: 已经更新的部门id
        """
        if 'id' not in department_data:
            raise AttributeError('必须包含Id')
        return self._post(
            '/department/update',
            department_data,
            result_processor=lambda x: x['id']
        )

    def xx_get(self,select_type,page,limit):
        """
        资源

        :param page: 页码
        :param limit: 标签数量
        :return:
        """
        res = self._get('/platformresource/list/resourcetable',params={'select_type':select_type,'page':page,'limit':limit})
        print('xx__gte',res)

        return res


    @classmethod
    def get_datas(self, request, model=None):

        headers = request.headers
        content_type = headers.get('Content-Type')
        print(content_type)
        if request.method == "GET":
            return request.args
        if content_type == 'application/x-www-form-urlencoded':
            print("1")
            return request.form
        if content_type.startswith('application/json'):
            print("2")
            return request.get_json()

        content_type_list = str(content_type).split(';')
        if len(content_type_list) > 0:
            if content_type_list[0] == 'multipart/form-data':
                print("3")
                return request.form

#     def list(self, department_id, offset=0, size=100, order='custom', lang='zh_CN'):
#         """
#         获取部门成员（详情）
#
#         :param department_id: 获取的部门id
#         :param offset: 偏移量
#         :param size: 表分页大小，最大100
#         :param order: 排序规则
#                       entry_asc     代表按照进入部门的时间升序
#                       entry_desc    代表按照进入部门的时间降序
#                       modify_asc    代表按照部门信息修改时间升序
#                       modify_desc   代表按照部门信息修改时间降序
#                       custom        代表用户定义排序
#         :param lang: 通讯录语言(默认zh_CN另外支持en_US)
#         :return:
#         """
#         return self._get(
#             '/user/list',
#             {
#                 'department_id': department_id,
#                 'offset': offset,
#                 'size': size,
#                 'order': order,
#                 'lang': lang
#             }
#         )
#
# class DingTalkBaseAPI(object):
#     API_BASE_URL = None
#     def __init__(self, client=None):
#         self._client = client
#
#     def _get(self, url, params=None, **kwargs):
#         if self.API_BASE_URL:
#             kwargs['api_base_url'] = self.API_BASE_URL
#         return self._client.get(url, params, **kwargs)
#
# class BaseClient(object):
#
#     _http = requests.Session()
#
#     API_BASE_URL = 'https://oapi.dingtalk.com/'
#     def get(self, uri, params=None, **kwargs):
#         """
#         get 接口请求
#
#         :param uri: 请求url
#         :param params: get 参数（dict 格式）
#         """
#         if params is not None:
#             kwargs['params'] = params
#         return self.request('GET', uri, **kwargs)
#
#     def request(self, method, uri, **kwargs):
#         method, uri_with_access_token, kwargs = self._handle_pre_request(method, uri, kwargs)
#
#         def _handle_pre_request(self, method, uri, kwargs):
#             return method, uri, kwargs
#         try:
#             return self._request(method, uri_with_access_token, **kwargs)
#         except DingTalkClientException as e:
#             return self._handle_request_except(e, self.request, method, uri, **kwargs)



ResourceApi.add_resource(TotalResource, '/resourcetable')


