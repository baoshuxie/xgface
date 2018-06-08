from __future__ import print_function

import grpc

import xgface_service_pb2
import xgface_service_pb2_grpc
import index_service_pb2
import index_service_pb2_grpc

import base64
from array import array
import re 
import os

_HOST = '10.58.122.237'
_PORT1 = '50000'
_PORT2 = '50001'


def convert_base64(path):
	with open(path,'rb+') as f:
		data =  base64.b64encode(f.read())
	return [data]


def DetectInfo(data):
	channel = grpc.insecure_channel(_HOST+':'+_PORT1)
	stub = xgface_service_pb2_grpc.XgfaceServiceStub(channel)
	response = stub.GetDetectInfo(xgface_service_pb2.Request(images=data))#.__str__()
	#print(response)
	if len(response.faces):
		for i in range(len(response.faces)):
			box[i] = response.faces[i].box
			landmark[i] = response.faces[i].landmark
			feature[i]= response.faces[i].feature
			print(feature)
			#box = re.findall(r'box(.*)landmark',response,re.S)[0].replace('\n','  ')
			#landmark = re.findall(r'landmark(.*)feature',response,re.S)[0].replace('\n','  ')
			#feature = re.findall(r'feature(.*)attributes',response,re.S)[0].split('attributes')[0].replace('\n','  ')
			#print(feature)
		return box,landmark,feature
	else:
		print('不存在人脸')


def GetFaceID(feature):
	features = feature.__str__().split('values:')[1: ]
	featurelist = [float(x.replace('\n',' ').strip()) for x in features]
	print(featurelist)
	print(len(featurelist))

	channel = grpc.insecure_channel(_HOST+':'+_PORT2)
	stub = index_service_pb2_grpc.IndexServiceStub(channel)
	response = stub.InsertPoint(index_service_pb2.Feature(value=featurelist))
	print(response)

	return response


if __name__ == '__main__':
	path  = "/Users/junjieluo/MyGit/xgface/photos"
	filename = '1.jpg'
	data = convert_base64(path+'/'+filename)
	alist = DetectInfo(data)
	if alist:
		box = alist[0]
		landmark = alist[1]
		feature = alist[2]
		ID = GetFaceID(alist[2])
		with open('1.txt','a+') as f:
			f.write(filename+' ')
			f.write(str(ID)+' ')
			f.write(str(landmark)+' ')
			f.write(str(feature)+' ')






