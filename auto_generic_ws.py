import os
import argparse

#Folder & files 
def createFactory(name):
	folderPath = os.path.join(name, 'factory')
	filePath = os.path.join(folderPath, name+'Factory.ts')
	os.makedirs(folderPath)
	with open(filePath, "w"):
		pass

def createMapper(name):
	folderPath = os.path.join(name, 'mapper')
	filePath = os.path.join(folderPath, name+'Mapper.ts')
	os.makedirs(folderPath)
	with open(filePath, "w"):
		pass
	#TODO check if a mapper will include both request/response or not.

def createDataModel(name):
	folderPath = os.path.join(name, 'model')
	responsePath = os.path.join(folderPath, 'response')
	requestPath = os.path.join(folderPath, 'request')

	responseFilePath = os.path.join(responsePath, name+'Response.ts')
	requestFilePath = os.path.join(requestPath, name+'Request.ts')

	os.makedirs(folderPath)
	os.makedirs(responsePath)
	os.makedirs(requestPath)
	with open(responseFilePath, "w"):
		pass
	with open(requestFilePath, "w"):
		pass

def createService(name):
	httpPath = name+'HttpService.ts'
	mockPath = name+'MockService.ts'

	with open(httpPath, "w"):
		pass
	with open(mockPath, "w"):
		pass
		
#args
parser = argparse.ArgumentParser()

parser.add_argument('--repo', type=str, default='CustomRepository')
args = parser.parse_args()

repoName = args.repo
#Structure definition
if not os.path.exists(repoName):
	os.makedirs(repoName) #Repository folder
	createFactory(repoName)
	createMapper(repoName)
	createDataModel(repoName)
