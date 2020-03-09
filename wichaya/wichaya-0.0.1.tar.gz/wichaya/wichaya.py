class Wichaya:

	def __init__(self):
		 self.name = "Wichaya"
		 self.lastname = "Charuchinda"
		 self.nickname = "Parn"
		 self.company = "PPowerPlus"

	def WhoIAm(self):
		'''
		This is a function will show the name
		'''
		print(f"My name is :{self.name}")
		print(f"My lastname is :{self.lastname}")
		print(f"My nickname is :{self.nickname}")

	@property
	def email(self):
		return f"{self.name.lower()}.{self.company.lower()}@gmail.com"

	def thainame(self):
		print('วิชญะ จารุจินดา')

	def __str__(self):
		return 'This a Wichaya class'

if __name__ == '__main__':
	Pan = Wichaya()

	print(help(Pan.WhoIAm))

	print(Pan) #print object name to show __str__
	print(Pan.name)
	print(Pan.lastname)
	print(Pan.nickname)
	Pan.WhoIAm()
	print(Pan.email) #ใช้ @property เพื่อแปลง def ให้เวลาเรียกใช้ไม่ต้องใส่ ()

	print("---------")

	pp = Wichaya()
	pp.WhoIAm()
	pp.name = "วิชญะ"
	pp.lastname = "จารุจินดา"
	pp.nickname = "ป่าน"


	print(pp.name)
	print(pp.lastname)
	print(pp.nickname)

	pp.WhoIAm()
