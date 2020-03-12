import random
def company(cid):
	if cid == 1:
		return "中国移动"
	elif cid ==2:
		return "中国电信"
	else:
		return"中国联通"
randomNumber = random.randint(100000,999999)
def loginMage(name):
	print("尊敬的用户:%s,您好,您本次登录的验证码是:%d,请在%d分钟内登录![%s]" % (name,randomNumber,timer,company(1)))
timer = 5

