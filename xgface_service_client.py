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
	print(response)
	if len(response.faces):
		boxs = []
		landmarks = []
		features = []
		re_attributes=[[]]
		pitches = []
		yaws = []
		rolls = []

		print(len(response.faces))

		for i in range(0,len(response,faces)):
			boxs.append(response.faces[i].box)
			landmarks.append(response.faces[i].landmark)
			features.append(response.faces[i].feature)
			for attribute in response.faces[i].attributes:
				re_attributes[i].append(response.faces[i].attributes)
			pitches.append(response.faces[i].pitch)
			yaws.append(response.faces[i].pitch)
			rolls.append(response.faces[i].roll)
			#print(feature)
			#box = re.findall(r'box(.*)landmark',response,re.S)[0].replace('\n','  ')
			#landmark = re.findall(r'landmark(.*)feature',response,re.S)[0].replace('\n','  ')
			#feature = re.findall(r'feature(.*)attributes',response,re.S)[0].split('attributes')[0].replace('\n','  ')
			#print(feature)
		return boxs,landmarks,features,re_attributes,pitches,yaws,rolls
	else:
		print('不存在人脸')


def GetFaceID(feature):
	feature_points = feature.__str__().split('values:')[1: ]
	pointlist = [float(x.replace('\n',' ').strip()) for x in feature_points]
	#print(featurelist)
	#print(len(featurelist))

	channel = grpc.insecure_channel(_HOST+':'+_PORT2)
	stub = index_service_pb2_grpc.IndexServiceStub(channel)
	response = stub.InsertPoint(index_service_pb2.Feature(value=pointlist))
	print(response)

	return response


if __name__ == '__main__':
	path  = "/Users/junjieluo/MyGit/xgface/photos"
	filename = '3.jpg'
	data = convert_base64(path+'/'+filename)
	alist = DetectInfo(data)
	if alist:
		for i in range(len(alist[0])):
			box = str(alist[0][i]).replace('\n','  ')
			landmark = str(alist[1][i]).replace('\n','  ').replace('{','').replace('}','').replace('points','').replace('coordinate_x:','').replace('coordinate_y:','')
			feature = str(alist[2][i]).replace('\n','  ').replace('{','').replace('}','').replace('values:','')
			attributes = [str(x).replace('\n','  ') for x in alist[3][i]] 
			pitch = str(alist[4][i])
			yaw = str(alist[5][i])
			roll = str(alist[6][i])

			ID = str(GetFaceID(alist[2][i])).replace('\n','  ')
			with open('1.txt','a+') as f:
				f.write(filename+' ')
				f.write(ID.strip('id:')+' ')
				f.write(landmark+' ')
				f.write(feature +' ')
				for attribute in attributes:
					f.write(attribute+'  ')
				f.write(pitch+'  ')
				f.write(yaw+'  ')
				f.write(roll+'  ')
				f.write('\n')






