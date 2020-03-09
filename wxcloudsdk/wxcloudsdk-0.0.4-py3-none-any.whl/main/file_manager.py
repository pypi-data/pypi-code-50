# -*- coding: utf-8 -*-  

import requests
import json
import hashlib

def get_md5(url):
	if isinstance(url, str):
		url = url.encode("utf-8")
		md = hashlib.md5()
		md.update(url)
		return md.hexdigest()



def upload_file(token, env_id, cloud_path, cloud_dir, local_path):
	"""
    一步上传文件
    :param token: 传入API返回的token
    :param env_id: 传入云环境ID
    :param cloud_path: 传入云文件预定路径 demo/file.json
	:param cloud_dir: 云文件预定文件夹 demo/
	:param local_path: 本地文件路径 ~/demo/file.json
    """
	post_url ="https://api.weixin.qq.com/tcb/uploadfile?access_token="+ token

	payload=json.dumps({"env":env_id,"path":cloud_path})

	try:	 
		upload = requests.post(post_url, data=payload)
		res = upload.json()

		form = {} 
		form["key"] = cloud_dir + res["url"].split("/")[-1]
		form["Signature"] = res["authorization"]
		form["x-cos-security-token"] = res["token"]
		form["x-cos-meta-fileid"] = res["cos_file_id"]
		res = (form, res["url"])

		form = res[0] 
		upload_url = res[1]
		with open(local_path,"rb") as f:
			form["file"] = f.read()		 
			try:
				success= requests.post(upload_url, files=form)
				print(success)
			except Exception as e:	 
				print(e)
	except Exception as e:	 
		print(e)

def rebuild(file, env, token):
	collection_name = file.split("-")[1].split(".")[0]

	data = {
		"env": env,
		"collection_name": collection_name,
		"file_path": "datas/" + file,
		"file_type":1,
		"stop_on_error": False,
		"conflict_mode": 2
	}

	payload = json.dumps({"env": env, "collection_name": collection_name})

	requests.post("https://api.weixin.qq.com/tcb/databasecollectiondelete?access_token=" + token, data=payload)
	requests.post("https://api.weixin.qq.com/tcb/databasecollectionadd?access_token=" + token, data=payload)
	r = requests.post("https://api.weixin.qq.com/tcb/databasemigrateimport?access_token=" + token, data=json.dumps(data))

	return r