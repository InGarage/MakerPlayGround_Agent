from flask import Flask
from flask import request
import sys,os
import subprocess
import json

app = Flask(__name__)
name = "temp"


@app.route('/', methods=['POST'])
def home():
	if request.method == 'POST':
		data = request.get_json(silent=True)
		full_path = os.path.realpath(__file__)
		path = os.path.dirname(full_path)
		subprocess.call(["mkdir",name],shell=True,cwd=path)
		subfolder = path + '\\' + name
		subprocess.call(["COPY",path+"\\"+"run.py",path+'\\'+name],shell=True,cwd=path)
		os.chdir(subfolder)
		with open("main.cpp","w+") as file:
			file.write(data["code"])
		
		print (data)
		with open("config.json","w+") as file:
			json.dump({'lib': data['lib'], 'board': data['board']}, file, indent=2)
		print (path+'\\'+name)
		subprocess.call(["python","run.py"],shell=True,cwd=path+'\\'+name)
		return "ok"
	else:
		return "fail"