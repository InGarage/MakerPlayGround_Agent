import sys,os
import subprocess
import json

if __name__ == '__main__':
    input_filename = 'config.json'
    name = 'project'  

    # Temporary variable to store data to be written to the json file
  #data = []
 
    with open(input_filename) as file:
      data=json.load(file)
      
    full_path = os.path.realpath(__file__)    
    path = os.path.dirname(full_path)
    
    
    subprocess.call(["RD" ,"/S" ,"/Q", name],shell=True,cwd=path)  

  
    filenamecpp = path+'\\'+"main.cpp"
    filenamecppnew = path+'\\'+name+'\\'+"src"
    pathlib = path
    pathlib = pathlib[:(-1)*len("temp")]+'\\'+"lib"
    print (pathlib) 
    pathlibnew = path+'\\'+name+'\\'+"lib"
  
    print (filenamecpp)
            #subprocess.call(["mkdir","test"],shell=True)
    subprocess.call(["mkdir",name],shell=True,cwd=path)
    subprocess.call(["pio","init","--board",data["board"]],shell=True,cwd=path+'\\'+name)
    subprocess.call(["COPY",filenamecpp,filenamecppnew],shell=True,cwd=path+'\\'+name)
    for lib in data["lib"]:
      print (lib)
      #Generate lib sub folder to match the platformIO structure
      subprocess.call(["mkdir",lib],shell=True,cwd=pathlibnew)
      subprocess.call(["COPY",pathlib+'\\'+lib+'.cpp',pathlibnew+'\\'+lib],shell=True,cwd=path+'\\'+name)
      subprocess.call(["COPY",pathlib+'\\'+lib+'.h',pathlibnew+'\\'+lib],shell=True,cwd=path+'\\'+name)
    subprocess.call(["platformio", "run" ],shell=True,cwd=path+'\\'+name)
      #subprocess.call(["platformio", "run" ,"--target", "upload"],shell=True,cwd=path+'\\'+name)
