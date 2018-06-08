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
_PORT1 = '50000'		#xgface_service端口,使用 detectinfo 方法输入一个base64数组返回box,landmark,feature,attributes,pitch,yaw,roll
_PORT2 = '50001'		#index_service端口,使用 insertpoint 方法输入 feature 返回一个id


#将图片转化为 base64方法
def convert_base64(path):
	with open(path,'rb+') as f:
		data =  base64.b64encode(f.read())
	return [data]

#调用xgface_service 服务
def DetectInfo(data):
	channel = grpc.insecure_channel(_HOST+':'+_PORT1)
	stub = xgface_service_pb2_grpc.XgfaceServiceStub(channel)
	response = stub.GetDetectInfo(xgface_service_pb2.Request(images=data))#.__str__()
	#print(response)

	#可能返回多个 face( 若图中包含多个 face)
	if len(response.faces):
		boxs = []
		landmarks = []
		features = []
		re_attributes=[{} for i in range(5)]		#这是一个包含五个字典的数组
		pitches = []
		yaws = []
		rolls = []

		#print(len(response.faces))
		s = ['age','gender','glass','hat','race']

		#每一个 face 中的特征存入对应数组
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

		#返回一个包含各特征数组的数组
		return boxs,landmarks,features,re_attributes,pitches,yaws,rolls
	else:
		print('不存在人脸')

#调用index_service服务
def GetFaceID(feature):
	feature_points = feature.__str__().split('values:')[1: ]		#将 feature 中的字符串切分处理得到192个 value
	pointlist = [float(x.replace('\n',' ').strip()) for x in feature_points]	#将这些 value 组成一个 float数组
	#print(featurelist)
	#print(len(featurelist))

	channel = grpc.insecure_channel(_HOST+':'+_PORT2)
	stub = index_service_pb2_grpc.IndexServiceStub(channel)
	response = stub.InsertPoint(index_service_pb2.Feature(value=pointlist))
	#print(response)

	return response

#递归遍历一个路径下的所有文件夹与子文件夹,并把名称中包含 jpg 的文件路径加入 filename_list 列表
def travel(path,filename_list):
	if os.path.isfile(path) :
		if 'jpg' in path:
			filename_list.append(path)
	else:
		for dir in os.listdir(path):
			travel(path+'/'+dir,filename_list)

	return filename_list


#执行主程序,给定各初始条件并做记录
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

			#返回的 alist是一个二维数组,alist[i]包含第 i 张脸的各特征
			#去掉各个特征中多余的字符与换行符
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

					#写入1.txt,每张 face 占一行
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

			#如果没有 face, 删除此图片
			else:
				noface_count += 1
				os.remove(filename)

		except:
			continue
			print('一个图片错误')

		file_count += 1

	end_time = datetime.now()
	do_time = (end_time - start_time).seconds//3600

	#记录执行时间,日期与数量
	with open('/Users/junjieluo/MyGit/xgface/photos/log.txt','a+',encoding='utf-8') as f:
		f.write("{} 处理了 {} 张图片,得到 {} 个 face_id,丢弃了{} 张无脸的图,耗时 {} 小时\n".format(start_date,file_count,face_count,noface_count,do_time))




