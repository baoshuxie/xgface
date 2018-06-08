from __future__ import print_function

import grpc

import xgface_service_pb2
import xgface_service_pb2_grpc
import index_service_pb2
import index_service_pb2_grpc
from datetime import datetime
import base64
import re 
import os



_HOST = '10.58.122.237'
_PORT1 = '50000'		#xgface_service端口,输入一个base64数组返回fea
_PORT2 = '50001'		#index_service端口


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
		boxs = []
		landmarks = []
		features = []
		re_attributes=[{} for i in range(5)]
		pitches = []
		yaws = []
		rolls = []

		print(len(response.faces))
		s = ['age','gender','glass','hat','race']
		for i in range(0,len(response.faces)):
			boxs.append(response.faces[i].box)
			landmarks.append(response.faces[i].landmark)
			features.append(response.faces[i].feature)
			print(response.faces[i].attributes['age'])
			for j in range(5):
				re_attributes[i]['%s'%s[j]] = response.faces[i].attributes['%s'%s[j]]
			pitches.append(response.faces[i].pitch)
			yaws.append(response.faces[i].pitch)
			rolls.append(response.faces[i].roll)
			#print(re_attributes)
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

def travel(path,filename_list):
	if os.path.isfile(path) :
		if 'jpg' in path:
			filename_list.append(path)
	else:
		for dir in os.listdir(path):
			travel(path+'/'+dir,filename_list)

	return filename_list


if __name__ == '__main__':
	start_time = datetime.now()
	start_date = start_time.strftime('%b' '%d')
	root_dir  = "/Users/junjieluo/MyGit/xgface/photos"
	filename_list = travel(root_dir,[])
	print(filename_list)
	face_count = 0
	noface_count = 0
	file_count = 0

	for filename in filename_list:
		try:
			data = convert_base64(filename)
			alist = DetectInfo(data)
			#print(alist[3])
			if alist:
				for i in range(len(alist[0])):
					box = str(alist[0][i]).replace('\n','  ')
					landmark = str(alist[1][i]).replace('\n','  ').replace('{','').replace('}','').replace('points','').replace('coordinate_x:','').replace('coordinate_y:','')
					feature = str(alist[2][i]).replace('\n','  ').replace('{','').replace('}','').replace('values:','')
					attributes = str(alist[3][i])

					pitch = str(alist[4][i])
					yaw = str(alist[5][i])
					roll = str(alist[6][i])

					ID = str(GetFaceID(alist[2][i])).replace('\n','  ')
					with open('1.txt','a+') as f:
						f.write(filename+' ')
						f.write(ID.strip('id:')+' ')
						f.write(landmark+' ')
						f.write(feature +' ')
						f.write(attributes + '  ')
						f.write(pitch+'  ')
						f.write(yaw+'  ')
						f.write(roll+'  ')
						f.write('\n')
					face_count += 1

				print(filename+'写入成功')

			else:
				noface_count += 1
				os.remove(filename)

		except:
			continue
			print('一个图片错误')

		file_count += 1

	end_time = datetime.now()
	do_time = (end_time - start_time).seconds//3600
	with open('/Users/junjieluo/MyGit/xgface/photos/log.txt','a+',encoding='utf-8') as f:
		f.write("{} 处理了 {} 张图片,得到 {} 个 face_id,丢弃了{} 张无脸的图,耗时 {} 小时\n".format(start_date,file_count,face_count,noface_count,do_time))




