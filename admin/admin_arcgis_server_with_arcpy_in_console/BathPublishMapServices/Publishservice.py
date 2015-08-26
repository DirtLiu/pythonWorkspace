#coding:cp936
import os

import arcpy
import time
import sys

from createsddraft import *


class publishServices:

    def checkfileValidation(self,mxdLists):
        print "____��ʼ����ĵ�����Ч��...."
        file_to_be_published=[]
        for file in mxdLists:
            mxd=mapping.MapDocument(file)
            brknlist=mapping.ListBrokenDataSources(mxd)
            if not len(brknlist)==0:
                print "____��ͼ�ĵ�,"+os.path.split(file)[1]+"�𻵣��޷���������...."
            else:
                file_to_be_published.append(file)
        print "____��ͼ�ĵ���Ч�Լ�����...."
        return file_to_be_published


    def publishServices(self,mxdLists,con,clusterName='default',copy_data_to_server=True,folder=None):


        for file in self.checkfileValidation(mxdLists):

            serviceName=os.path.splitext(os.path.split(file)[1])[0]

            print "____����:"+serviceName+"��ʼ�����������ļ�...."
            clsCreateSddraft=CreateSddraft()
            sddraft=clsCreateSddraft.CreateSddraft(file,con,serviceName,copy_data_to_server,folder)
            print "____��ʼ��������:"+serviceName+"...."
            analysis = arcpy.mapping.AnalyzeForSD(sddraft)
            dirName=os.path.split(file)[0]
            if analysis['errors'] == {}:
               print "____�����ڴ��󣬵�����������ʾ��Ϣ����Щ���ݿ��ܻ�Ӱ���������...."
               print analysis['warnings']
               if(not self.checkWarnings(analysis['warnings'])):
                   try:
                        sd=dirName+"\\"+serviceName+".sd"
                        if(os.path.exists(sd)):
                            os.remove(sd)
                        arcpy.StageService_server(sddraft, sd)
                        print "____����:"+serviceName+"����ɹ�...."
                        arcpy.UploadServiceDefinition_server(sd, con,in_cluster=clusterName)
                        print "____����:"+str(serviceName)+"�����ɹ�...."
                        os.remove(sd)
                   except Exception,msg:
                        print msg


               else:
                   print "____ǿ�ҽ��飬�˳���ǰ����ȥע������Դ���粻�˳���6s�󷢲��������...."
                   time.sleep(10)
                   try:
                    sd=dirName+"\\"+serviceName+".sd"
                    if(os.path.exists(sd)):
                        os.remove(sd)
                    arcpy.StageService_server(sddraft, sd)
                    print "____����ɹ�...."
                    arcpy.UploadServiceDefinition_server(sd, con,in_cluster=clusterName)
                    print "____"+str(file)+"�����ɹ�...."
                    os.remove(sd)
                   except Exception,msg:
                    print msg




            else:
                print '____�������´���:'+analysis['errors']+'....'
                print '____���ȴ�����������....'
                #������˳�����̨
                time.sleep(5)
                sys.exit(1)


    def  checkWarnings(self,warnings):
        for warning in warnings:
            if warning[1]==24011:
                print "____��ǰ����λ��û��ע�ᣬ���ݻ´������������,�������̻�Ӱ�췢���ٶ�...."
        return True

if __name__=='__main__':
    clsPublishservice=publishServices()
    fileList=['d:\\workspace\\testCopy.mxd', 'd:\\workspace\\test.mxd']
    contionfile=r"d:\localhost.ags"
    clusterName='default'
    servic_dir='test3'

    clsPublishservice.publishServices(fileList,contionfile,clusterName,copy_data_to_server=False,folder=servic_dir)
