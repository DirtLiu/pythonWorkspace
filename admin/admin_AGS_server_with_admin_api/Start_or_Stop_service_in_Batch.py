#coding:cp936
__author__ = 'jiangmb'

from Get_site_information_helper import *

# server="localhost"
# port='6080'
# username='arcgis'
# password='Super123'
#
# operation='started'
# count=4


server=raw_input("������GIS��������IP��ַ:")
port=raw_input("������GIS���ӵĶ˿ںţ�Ĭ��Ϊ6080������Ĭ��ֵ��ֱ�ӻس���")
if port=='':
    port='6080'
username=raw_input("������վ�����Ա�û���:")
password=raw_input("���������Ա����:")

operation=raw_input("�����������(stopped/started)��")
if not str.upper(operation) in ('STARTED,STOPPED'):
    print "++++ERROR:��������ȷ�Ĳ���!!!++++"
    sys.exit(1)
count=raw_input("����������ķ�����:")
adminself=ADMINself(username,password,server,port)

if str.upper(operation)=='STOPPED':

    serviceList=adminself.getStartedOrStopedServiceList('STARTED')
    if len(serviceList)<count:
        count=len(serviceList)
    adminself.stopStartServices('stop',adminself.getServiceList()[0:count])
else:
    serviceList=adminself.getStartedOrStopedServiceList('STOPPED')
    if len(serviceList)<count:
        count=len(serviceList)
    adminself.stopStartServices('start',adminself.getServiceList()[0:count])







