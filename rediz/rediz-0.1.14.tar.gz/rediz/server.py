from flask_restx import Resource, reqparse
import flask

singular_set_parser = reqparse.RequestParser()
singular_set_parser.add_argument('write_key', required=True)
singular_set_parser.add_argument('values', required=True)
singular_set_parser.add_argument('budget', required=True)

singular_del_parser = reqparse.RequestParser()
singular_del_parser.add_argument('write_key', required=True)

class Singular(Resource):

    def __init__(self, rdz):
        self.rdz = rdz

    def put(self, name):
        """ Set current stream value """
        args = singular_set_parser.parse_args()
        response = self.rdz.set(names=name, write_key=args["write_key"], value=args["value"], budgets=args["budget"])
        return flask.jsonify(response)

    def get(self, name):
        """ Retrieve current value (or derived if prefix used) """
        value = self.rdz.get(name=name)
        return flask.jsonify(value)

    def delete(self):
        """ Delete multiple streams """
        args = singular_del_parser.parse_args()
        response = self.rdz.delete(names=args["names"], write_key=args["write_key"])
        return flask.jsonify(response)


multi_set_parser = reqparse.RequestParser()
multi_set_parser.add_argument('names', required=True, action='split')
multi_set_parser.add_argument('write_keys', required=True, action='split')
multi_set_parser.add_argument('values', required=True, action='split')
multi_set_parser.add_argument('budgets', required=True, action='split')

multi_get_parser = reqparse.RequestParser()
multi_get_parser.add_argument('names', required=True, action='split')

multi_del_parser = reqparse.RequestParser()
multi_del_parser.add_argument('names', required=True, action='split')
multi_del_parser.add_argument('write_key', required=True)


class Multi(Resource):

    def __init__(self, rdz):
        self.rdz = rdz

    def put(self):
        """ Set multiple stream values """
        args = multi_set_parser.parse_args()
        fvalues = [ float(v) for v in args["values"] ]
        fbudgets = [ float(b) for b in args["budgets"] ]
        response = self.rdz.mset(names=args["names"],write_keys=args["write_keys"],values=fvalues,budgets=fbudgets)
        return flask.jsonify(response)

    def get(self):
        """ Retrieve values for multiple names """
        names = multi_get_parser.parse_args()["names"]
        values = self.rdz.mget(names=names)
        return flask.jsonify(values)

    def delete(self):
        """ Delete multiple streams """
        args = multi_set_parser.parse_args()
        response = self.rdz.mdelete(names=args["names"], write_keys=args["write_keys"] )
        return flask.jsonify(response)


predictions_put_parser = reqparse.RequestParser()
predictions_put_parser.add_argument('write_key', required=True)
predictions_put_parser.add_argument('delay', required=True)
predictions_put_parser.add_argument('values', required=True, action='split')

predictions_get_parser = reqparse.RequestParser()
predictions_get_parser.add_argument('delay', required=True)
predictions_get_parser.add_argument('values', required=True, action='split')

predictions_delete_parser = reqparse.RequestParser()
predictions_delete_parser.add_argument('write_key', required=True)
predictions_delete_parser.add_argument('delay', required=True)

class Predictions(Resource):

    def __init__(self, rdz):
        self.rdz = rdz

    def get(self, name, delay, values):
        """ Retrieve approximate cdf """
        args = predictions_get_parser.parse_args()
        values = [ float(v) for v in args["values"] ]
        percentiles = self.rdz.get_cdf(name=name,values=values,delay=int(args["delay"]))
        return flask.jsonify(percentiles)

    def put(self, name):
        """ Overwrite existing scenarios """
        args = predictions_put_parser.parse_args()
        write_key = args["write_key"]
        delay = int(args["delay"])
        values = [float(v) for v in args["values"]]
        feedback = self.rdz.predict(name=name, write_key=write_key, delay=delay, values=values)
        return flask.jsonify(feedback)

    def delete(self, name):
        """ Withdraw from contest """
        args = predictions_delete_parser.parse_args()
        result = self.rdz.delete_scenarios(name=name, write_key=args["write_key"], delay=int(args["delay"]))
        return flask.jsonify(result)