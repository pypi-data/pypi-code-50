#!/usr/bin/python3

import argparse
import prance
import os
import json
import sys

from . import requester
from . import converter
from . import scenario

def parse_yaml(filepath):
	exists = os.path.isfile(filepath)
	if not exists:
		print(filepath + ' does not exist')
		sys.exit(1)
	else:
		try:
			parser = prance.ResolvingParser(filepath, backend = 'openapi-spec-validator', strict = False)
			return parser.specification
		except:
			print(filepath + ' is not a valid contract file')
			sys.exit(1)
	return None

def mock(args):
	scenarios = ''
	yaml = None
	expectations = None

	if args.openapi_file:
		yaml = parse_yaml(args.openapi_file)

	if yaml:
		scenarios = []
		if args.s is not None and len(args.s) > 0:
			validator = scenario.Validator(yaml)
			for mock_scenario in json.loads(args.s)['scenarios']:
				if len(mock_scenario) == 5:
					scenarios.append(scenario.Scenario(mock_scenario[0], mock_scenario[1], mock_scenario[2], mock_scenario[3], mock_scenario[4]))
				elif len(mock_scenario) == 4:
					scenarios.append(scenario.Scenario(mock_scenario[0], mock_scenario[1], mock_scenario[2], mock_scenario[3]))
				else:
					scenarios.append(scenario.Scenario(mock_scenario[0], mock_scenario[1], mock_scenario[2]))
			try:
				validator.validate(scenarios)
			except (scenario.EndpointNotDefinedException, scenario.InvalidResponseBodySchemaException, scenario.InvalidResponseContentTypeException) as e:
				print(e.message)
				sys.exit(1)

		conv = converter.Converter()
		conv.set_scenarios(scenarios)
		conv.convert_opai(yaml)
		expectations = conv.expectations

	if args.mockserver_uri:
		mr = requester.MockserverRequester()
		mr.set_mockserver_uri(args.mockserver_uri)

		if expectations:
			mr.request_expectations(expectations)

def reset(args):
	if args.mockserver_uri:
		mr = requester.MockserverRequester()
		mr.set_mockserver_uri(args.mockserver_uri)
		mr.request_reset()

def arguments():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(title='title', dest='command')
	subparsers.required = True

	parser_mock = subparsers.add_parser('mock')
	parser_mock.set_defaults(func=mock)
	parser_mock.add_argument('mockserver_uri')
	parser_mock.add_argument('openapi_file')
	parser_mock.add_argument("-s", help="The scenarios to mock")

	parser_reset = subparsers.add_parser('reset')
	parser_reset.set_defaults(func=reset)
	parser_reset.add_argument('mockserver_uri')

	args = parser.parse_args()
	args.func(args)


def main():
	arguments()


if __name__ == '__main__':
	main()
