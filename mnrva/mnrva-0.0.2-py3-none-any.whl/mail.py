import sendgrid


class Mail(object):
	def __init__(self):
		self.sg = sendgrid.SendGridClient('')

	def send_message(self, to, subject, body):

		message = sendgrid.Mail()
		message.add_to(to.split(","))
		message.set_subject(subject)
		message.set_html(body)
		message.set_text(body)
		message.set_from('no-reply@mnrva.io')
		status, msg = self.sg.send(message)

		if status == 200:
			return True
		else:
			return False

	def send_file(self, to, subject, body, filename):

		message = sendgrid.Mail()
		message.add_to(to.split(","))
		message.set_subject(subject)
		message.set_html(body)
		message.set_text(body)
		message.set_from('no-reply@mnrva.io')
		message.add_attachment('report_mrnva.xlsx', filename)
		status, msg = self.sg.send(message)

		if status == 200:
			return True
		else:
			return False


if __name__ == '__main__':
	print('*** Welcome to Minerva 4R. Social Data Mining S.A. 2019 ***')
