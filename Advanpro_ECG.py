#coding:utf-8
import json
import matplotlib.pyplot as plt
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class ECG(object):
    def __init__(self,pathname,docname):
        self.pathname = pathname
        self.docname = docname

    def get_arg_rr_interval(self,record):
        self.arg_rr_interval = record['arg_rr_interval']
        return self.arg_rr_interval

    def get_chest_lead_gain(self,record):
        self.chest_lead_gain = record['chest_lead_gain']
        return self.chest_lead_gain

    def get_collect_duration(self,record):
        self.collect_duration  = record['collect_duration']
        return self.collect_duration

    def get_collect_end_utc(self,record):
        self.collect_end_utc = record['collect_end_utc']
        return self.collect_end_utc

    def get_collect_start_utc(self,record):
        self.collect_start_utc = record['collect_start_utc']
        return self.collect_start_utc

    def get_device_name(self,record):
        self.device_name = record['device_name']
        return self.device_name

    def get_device_number(self,record):
        self.device_number = record['device_number']
        return self.device_number

    def get_gender(self,record):
        self.gender = record['gender']
        return self.gender

    def get_given_name(self,record):
        self.given_name = record['given_name']
        return self.given_name

    def get_identifier(self,record):
        self.identifier = record['identifier']
        return self.identifier

    def get_interp(self,record):
        self.interp = record['interp']
        return self.interp

    def get_name(self,record):
        self.name = record['name']
        return self.name

    def get_rr_inerval(self,record):
        self.rr_interval = record['rr_interval']
        return self.rr_interval

    def get_sample_rate(self,record):
        self.sample_rate = record['sample_rate']
        return self.sample_rate

    def get_ecg_xml(self,record):
        self.ecg_xml = record['xml']
        return self.ecg_xml

    def readecg_json(self):
        self.jsonstr = []
        for line in open('./'+self.pathname+'/'+self.docname,'r'):
            self.jsonstr.append(json.loads(line))
        return self.jsonstr

    def getecgdata(self,record):
        ecg = []
        ecg_xml = self.get_ecg_xml(record)
        root = ET.fromstring(ecg_xml.encode('utf-8'))
        ecgstr = root[1][0][5][3][4][0][0][1][0][4].attrib['V'] #1053400104 是xml文件中ecg数据相对于根节点数据的标识
        ecgstr = ecgstr.split()
        for data in ecgstr:
            ecg.append(int(data))
        return ecg

    def ecg_plot(self,ecg):
        plt.figure('Orginal ECG Signal ')
        plt.plot(ecg)
        plt.show()

if __name__ == '__main__':
    path = 'data_to_Tsinghua_20170731/ecg'
    docname = 'part-r-00000-9e0f7249-e255-4a13-8524-e2e023ff0cbd.json'
    ecg = ECG(path,docname)
    ecgjson = ecg.readecg_json()
    for record in ecgjson:
        ecgdata = ecg.getecgdata(record)
        ecgidentifier = ecg.get_identifier(record)
        ecginterp = ecg.get_interp(record)
        print ecgidentifier
        print ecginterp
        ecg.ecg_plot(ecgdata)