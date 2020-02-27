from werkzeug.exceptions import MethodNotAllowed
from flask import jsonify, Response, g, abort, request, current_app
from flask_restplus import Resource, Api
from datetime import datetime
from openstg.utils import ArgumentsParser, get_season
from openstg.models import *
from primestg.service import Service


supported_reports = {
    'instant-data': ['sync', 'reg_only'],  # PRIME code: S01
    'daily-incremental': ['async', 'reg_n_cnc'],  # PRIME code: S02
    'monthly-billing': ['async', 'reg_n_cnc'],  # PRIME code: S04
    'daily-absolute': ['async', 'reg_n_cnc'],  # PRIME code: S05
    'meter-parameters': ['async', 'reg_only'],  # PRIME code: S06
    'meter-events': ['async', 'reg_n_cnc'],  # PRIME code: S09
    'cnc-parameters': ['async', 'cnc_only'],  # PRIME code: S12
    'advanced-instant-data': ['sync', 'reg_only'],  # PRIME code: S21
    'contract-definition': ['async', 'reg_n_cnc'],  # PRIME code: S23
}

supported_orders = {
    'order-request': ['async', 'cnc_only'],  # PRIME code: B11
}

class GisceStg(Api):
    pass


class BaseResource(Resource):
    pass


def get_url_from_cnc(cnc_name):
    """
    Gets the web services URL from the DB. Using the concentrator name.
    :param cnc_name: Concentrator name
    :return: An string with the URL of the web service
    """
    try:
        search_params, limit, offset = ArgumentsParser.parse()
    except (ValueError, SyntaxError) as e:
        response = jsonify({
            'status': 'ERROR',
            'errors': {'filter': e.message}
        })
        response.status_code = 422
        return response
    try:
        search_params = [('name', '=', cnc_name)]
        model = ConcentratorModel()
        result = model.get(search_params, limit=limit,
                           offset=offset)
    except ModelException:
        response = jsonify({'status': 'ERROR'})
        response.status_code = 422
        return response

    return '{}'.format(result.items[0]['dc_address'])


def get_cnc_url_from_register(register_name):
    """
    Gets the web services URL from the DB. Using the register name.
    :param register_name: The name of the register
    :return: The URL of the web services of the concentrator
    """
    try:
        search_params, limit, offset = ArgumentsParser.parse()
    except (ValueError, SyntaxError) as e:
        response = jsonify({
            'status': 'ERROR',
            'errors': {'filter': e.message}
        })
        response.status_code = 422
        return response
    try:
        register_name = register_name.split(',')[0]
        search_params = [('name', '=', register_name)]
        model = RegisterModel()
        result = model.get(search_params, limit=limit,
                           offset=offset)
    except ModelException:
        response = jsonify({'status': 'ERROR'})
        response.status_code = 422
        return response
    return '{}'.format(result.items[0]['cnc']['dc_address'])


def get_required_info(request):
    """
    Gets the information needed to ask for every report
    :param request: Contains the parameters given in the path
    :return: A dictionary containing the required information
    """
    date_from = date_to = datetime.now()
    if request.args.get('from'):
        date_from = '{}{}{}'.format(request.args.get('from'), '000',
                                    get_season(request.args.get('from')))
    if request.args.get('to'):
        date_to = '{}{}{}'.format(request.args.get('to'), '000',
                                  get_season(request.args.get('to')))
    return {
        'date_from': date_from,
        'date_to': date_to,
        'source': request.args.get('source'),
        'request_id': current_app.counter.next()
    }


class ApiCatchall(BaseResource):

    def get(self, path):
        abort(404)

    post = get
    put = get
    delete = get
    patch = get


class ReadOnlyResource(BaseResource):

    def not_allowed(self):
        raise MethodNotAllowed

    post = patch = not_allowed


# Utilities


class SupportedReports(ReadOnlyResource):

    def get(self):
        return jsonify(supported_reports)


class SupportedOrders(ReadOnlyResource):

    def get(self):
        return jsonify(supported_orders)


# Send Orders

#PRIME code: B11
class OrderRequest(ReadOnlyResource):

    def get(self, cnc_name, txx):
        info = get_required_info(request)
        generic_values = {
            'id_req': 'B11',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name
        }
        payload = {
            'txx': txx,
            'date_from': info['date_from'],
            'date_to': info['date_to']
        }
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        order = s.get_order_request(generic_values, payload)
        resp = Response(order, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# Synchronous requests

# PRIME code: S01
class InstantData(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_instant_data(register_name)
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S02
class DailyIncremental(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_daily_incremental(register_name, info['date_from'],
                                      info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllDailyIncremental(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_daily_incremental(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S04
class MonthlyBilling(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_monthly_billing(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllMonthlyBilling(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_monthly_billing(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S05
class DailyAbsolute(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_daily_absolute(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllDailyAbsolute(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_daily_absolute(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S06
class RegisterParameters(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_meter_parameters(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllRegisterParameters(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_meter_parameters(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S09
class RegisterEvents(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_meter_events(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllRegisterEvents(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_meter_events(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S12
class ConcentratorParameters(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=True)
        rep = s.get_concentrator_parameters(cnc_name, info['date_from'],
                                            info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S21
class AdvancedInstantData(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_advanced_instant_data(register_name)
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S23
class ContractDefinition(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_contract_definition(register_name, info['date_from'],
                                        info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllContractDefinition(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_contract_definition(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# Asynchronous requests

# PRIME code: S02
class DailyIncrementalAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_daily_incremental(register_name, info['date_from'],
                                      info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllDailyIncrementalAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_daily_incremental(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S04
class MonthlyBillingAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_monthly_billing(register_name, info['date_from'],
                                    info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllMonthlyBillingAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_monthly_billing(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S05
class DailyAbsoluteAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_daily_absolute(register_name, info['date_from'],
                                   info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllDailyAbsoluteAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_daily_absolute(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S06
class RegisterParametersAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_meter_parameters(register_name, info['date_from'],
                                        info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllRegisterParametersAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_meter_parameters(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S09
class RegisterEventsAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_meter_events(register_name, info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllRegisterEventsAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_meter_events(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S12
class ConcentratorParametersAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_concentrator_parameters(cnc_name, info['date_from'],
                                            info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S23
class ContractDefinitionAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_contract_definition(register_name, info['date_from'],
                                      info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllContractDefinitionAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_contract_definition(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


resources = [
    # Utilities
    (SupportedReports, '/supported_reports'),
    (SupportedOrders, '/supported_orders'),

    # Synchronous requests
    # PRIME code: S01
    (InstantData, '/instant-data/<string:register_name>'),
    # PRIME code: S02
    (DailyIncremental, '/daily-incremental/<string:register_name>'),
    (AllDailyIncremental, '/<string:cnc_name>/daily-incremental'),
    # PRIME code: S04
    (MonthlyBilling, '/monthly-billing/<string:register_name>'),
    (AllMonthlyBilling, '/<string:cnc_name>/monthly-billing'),
    # PRIME code: S05
    (DailyAbsolute, '/daily-absolute/<string:register_name>'),
    (AllDailyAbsolute, '/<string:cnc_name>/daily-absolute'),
    # PRIME code: S06
    (RegisterParameters, '/meter-parameters/<string:register_name>'),
    (AllRegisterParameters, '/<string:cnc_name>/meter-parameters'),
    # PRIME code: S09
    (RegisterEvents, '/meter-events/<string:register_name>'),
    (AllRegisterEvents, '/<string:cnc_name>/meter-events'),
    # PRIME code: S12
    (ConcentratorParameters, '/<string:cnc_name>/cnc-parameters'),
    # PRIME code: S21
    (AdvancedInstantData, '/advanced-instant-data/<string:register_name>'),
    # PRIME code: S23
    (ContractDefinition, '/contract-definition/<string:register_name>'),
    (AllContractDefinition, '/<string:cnc_name>/contract-definition'),


    # Asynchronous requests
    # PRIME code: S02
    (DailyIncrementalAsync, '/daily-incremental/async/<string:register_name>'),
    (AllDailyIncrementalAsync, '/<string:cnc_name>/daily-incremental/async'),
    # PRIME code: S04
    (MonthlyBillingAsync, '/monthly-billing/async/<string:register_name>'),
    (AllMonthlyBillingAsync, '/<string:cnc_name>/monthly-billing/async'),
    # PRIME code: S05
    (DailyAbsoluteAsync, '/daily-absolute/async/<string:register_name>'),
    (AllDailyAbsoluteAsync, '/<string:cnc_name>/daily-absolute/async'),
    # PRIME code: S06
    (RegisterParametersAsync, '/meter-parameters/async/<string:register_name>'),
    (AllRegisterParametersAsync, '/<string:cnc_name>/meter-parameters/async'),
    # PRIME code: S09
    (RegisterEventsAsync, '/meter-events/async/<string:register_name>'),
    (AllRegisterEventsAsync, '/<string:cnc_name>/meter-events/async'),
    # PRIME code: S12
    (ConcentratorParametersAsync, '/<string:cnc_name>/cnc-parameters/async'),
    # PRIME code: S23
    (ContractDefinitionAsync, '/contract-definition/async/<string:register_name>'),
    (AllContractDefinitionAsync, '/<string:cnc_name>/contract-definition/async'),

    # Send Orders
    # PRIME code: B11
    (OrderRequest, '/<string:cnc_name>/order-request/<string:txx>/async'),

]
