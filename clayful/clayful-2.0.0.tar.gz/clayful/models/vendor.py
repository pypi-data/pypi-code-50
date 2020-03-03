class Vendor:

	Clayful = None
	name = 'Vendor'
	path = 'vendors'

	@staticmethod
	def config(clayful):

		Vendor.Clayful = clayful

		return Vendor

	@staticmethod
	def list(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/vendors',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/vendors/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/vendors/{vendorId}',
			'params':           ('vendorId', ),
			'args':             args
		})

	@staticmethod
	def increase_metafield(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'increase_metafield',
			'http_method':      'POST',
			'path':             '/v1/vendors/{vendorId}/meta/{field}/inc',
			'params':           ('vendorId', 'field', ),
			'args':             args
		})

	@staticmethod
	def push_to_metafield(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'push_to_metafield',
			'http_method':      'POST',
			'path':             '/v1/vendors/{vendorId}/meta/{field}/push',
			'params':           ('vendorId', 'field', ),
			'args':             args
		})

	@staticmethod
	def pull_from_metafield(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'pull_from_metafield',
			'http_method':      'POST',
			'path':             '/v1/vendors/{vendorId}/meta/{field}/pull',
			'params':           ('vendorId', 'field', ),
			'args':             args
		})

	@staticmethod
	def delete_metafield(*args):

		return Vendor.Clayful.call_api({
			'model_name':       Vendor.name,
			'method_name':      'delete_metafield',
			'http_method':      'DELETE',
			'path':             '/v1/vendors/{vendorId}/meta/{field}',
			'params':           ('vendorId', 'field', ),
			'args':             args
		})

