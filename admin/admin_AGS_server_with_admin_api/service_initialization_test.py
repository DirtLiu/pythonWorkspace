#coding:cp936
__author__ = 'jiangmb'
from Get_site_information_helper import *
import datetime

server=raw_input("������GIS��������Ip:")
port=raw_input("������GIS���ӵĶ˿ںţ�Ĭ��Ϊ6080������Ĭ��ֵ��ֱ�ӻس���")
if port=='':
    port='6080'
username=raw_input("������վ�����Ա�û���:")
password=raw_input("���������Ա����:")
path=raw_input("���������ļ������ַ:")

def writeOutPut(path,contents):
    file=open(path,'w')
    file.write("������,��ʼ��ʱ��\n")
    for content in contents:
      line=content[0].encode('utf-8')+","+str(content[1]).encode('utf-8')+"\n"

      file.write(line)

    file.close()


"""
server="localhost"
port='6080'
username='arcgis'
password='Super123'
"""

adminself=ADMINself(username,password,server,port)

folderList=adminself.getFolders()
print folderList
serviceList=adminself.getServiceList()
# s
Dict_service={}
for singleService in serviceList:

    singleService.replace('.','/')

    url="http://{}:{}/arcgis/rest/services/{}".format(server,port,singleService)

    timeStart=datetime.datetime.now()
    results= adminself.sendAGSReq(url+adminself.basicQ,"")
    #print results
    timeEnd=datetime.datetime.now()
    timeElapse=(timeEnd-timeStart).microseconds/1000
    Dict_service[singleService]=timeElapse

print Dict_service

#���ֵ������
results=sorted(Dict_service.items(), key=lambda Dict_service:Dict_service[1])
writeOutPut(path+"\\result.txt",results)
