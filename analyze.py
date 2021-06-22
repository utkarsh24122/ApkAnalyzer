import os
import re

def isValidPath(apkFilePath):
	global apkFileName
	Print("I: Checking APK File path", "INFO_WS")
	if (os.path.exists(apkFilePath)==False):
		Print("E: Incorrect APK file path found. Please try again with correct file name.", "ERROR")
		
		exit(1)
	else:
		Print("I: APK File Found.", "INFO_WS")
		apkFileName=ntpath.basename(apkFilePath)
    
    def reverseEngineerApplication(apkFileName):
	global projectDir
	Print("I: Decompilation Started", "INFO_WS")
	projectDir=rootDir+apkFileName+"_"+hashlib.md5().hexdigest()
	if (os.path.exists(projectDir)==True):
		myPrint("I: The APK is already decompiled.", "INFO_WS")
		return projectDir
	os.mkdir(projectDir)
	myPrint("I: Decompiling the APK file using APKtool.", "INFO_WS")
	result=os.system("java -jar "+apktoolPath+" d "+"--output "+'"'+projectDir+"/apktool/"+'"'+' "'+apkFilePath+'"'+'>/dev/null')
	if (result!=0):
		myPrint("E: Apktool failed with exit status "+str(result)+". Please try updating the APKTool binary.", "ERROR")
		print
		exit(1)
	myPrint("I: Successfully decompiled the application. Proceeding with scanning code.", "INFO_WS")

  
  s3Regex1="https*://(.+?)\.s3\..+?\.amazonaws\.com\/.+?"
s3Regex2="https*://s3\..+?\.amazonaws\.com\/(.+?)\/.+?"
s3Regex3="S3://(.+?)/"

def findS3Bucket(line):
	temp=re.findall(s3Regex1,line)
	if (len(temp)!=0):
		for element in temp:
			s3List.append(element)


	temp=re.findall(s3Regex2,line)
	if (len(temp)!=0):
		for element in temp:
			s3List.append(element)


	temp=re.findall(s3Regex3,line)
	if (len(temp)!=0):
		for element in temp:
			s3List.append(element)
