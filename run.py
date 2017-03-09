import sys,os
import subprocess
import json

if __name__ == '__main__':
    input_filename = 'config.json'
    name = 'Test'	

    # Temporary variable to store data to be written to the json file
	#data = []
 
    with open(input_filename) as file:
   		data=json.load(file)
   		
		full_path = os.path.realpath(__file__)		
		path = os.path.dirname(full_path)
   	
		
   		subprocess.call(["RD" ,"/S" ,"/Q", name],shell=True,cwd=path)
   

	
   		filenamecpp = path+'\\'+"main.cpp"
   		filenamecppnew = path+'\\'+name+'\\'+"src"
	
		print (filenamecpp)
		    		#subprocess.call(["mkdir","test"],shell=True)
   		subprocess.call(["mkdir",name],shell=True,cwd=path)
   		subprocess.call(["pio","init","--board",data["board"]],shell=True,cwd=path+'\\'+name)
   		subprocess.call(["move",filenamecpp,filenamecppnew],shell=True,cwd=path+'\\'+name)
		subprocess.call(["platformio", "run" ],shell=True,cwd=path+'\\'+name)
   		#subprocess.call(["platformio", "run" ,"--target", "upload"],shell=True,cwd=path+'\\'+name)
   		
    		#print subprocess.call(["mkdir","test\test1"],shell=True)
    		#print subprocess
    		#print repr(os.getcwd())