# coding=gbk
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from selenium import webdriver

from bs4 import BeautifulSoup
# import urllib
# import string
# import datetime


html = """
<html><head><title>The Dormouse's story</title></head>

<div id="pzDiv" style="display: block;"><input type="checkbox" name="catalogs" id="���Ƹ�" value="���Ƹ�_:_���Ƹ�">���Ƹ�<br><div id="spec_���Ƹ�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="���Ƹ�_:_���Ƹ�:__:HRB335 12MM_:_HRB335_12MM" id="���Ƹ�0">HRB335 12MM<br><input type="checkbox" name="specs" value="���Ƹ�_:_���Ƹ�:__:HRB335 20MM_:_HRB335_20MM" id="���Ƹ�1">HRB335 20MM<br><input type="checkbox" name="specs" value="���Ƹ�_:_���Ƹ�:__:HRB400 20MM_:_HRB400_20MM" id="���Ƹ�2">HRB400 20MM<br></div><input type="checkbox" name="catalogs" id="�Ǹ�" value="�Ǹ�_:_�Ǹ�">�Ǹ�<br><div id="spec_�Ǹ�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�Ǹ�_:_�Ǹ�:__:50*5_:__50*5" id="�Ǹ�0">50*5<br></div><input type="checkbox" name="catalogs" id="�۸�" value="�۸�_:_�۸�">�۸�<br><div id="spec_�۸�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�۸�_:_�۸�:__:16#_:__16#" id="�۸�0">16#<br></div><input type="checkbox" name="catalogs" id="���ָ�" value="���ָ�_:_���ָ�">���ָ�<br><div id="spec_���ָ�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="���ָ�_:_���ָ�:__:25#_:__25#" id="���ָ�0">25#<br></div><input type="checkbox" name="catalogs" id="�߲�" value="�߲�_:_�߲�">�߲�<br><div id="spec_�߲�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�߲�_:_�߲�:__:6����HPB300_:_HPB300_6����" id="�߲�0">6����HPB300<br><input type="checkbox" name="specs" value="�߲�_:_�߲�:__:8.0����HPB300_:_HPB300_8.0����" id="�߲�1">8.0����HPB300<br></div><input type="checkbox" name="catalogs" id="�������" value="�������_:_�������">�������<br><div id="spec_�������" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�������_:_�������:__:0.5mm_:__0.5mm" id="�������0">0.5mm<br><input type="checkbox" name="specs" value="�������_:_�������:__:1.0mm_:__1.0mm" id="�������1">1.0mm<br></div><input type="checkbox" name="catalogs" id="�촬��" value="�촬��_:_�촬��">�촬��<br><div id="spec_�촬��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�촬��_:_�촬��:__:10mm_:__10mm" id="�촬��0">10mm<br><input type="checkbox" name="specs" value="�촬��_:_�촬��:__:20mm_:__20mm" id="�촬��1">20mm<br></div><input type="checkbox" name="catalogs" id="�к��" value="�к��_:_�к��">�к��<br><div id="spec_�к��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�к��_:_�к��:__:��8mm_:__��8mm" id="�к��0">��8mm<br><input type="checkbox" name="specs" value="�к��_:_�к��:__:��20mm_:__��20mm" id="�к��1">��20mm<br><input type="checkbox" name="specs" value="�к��_:_�к��:__:�ͺϽ�20mm_:__�ͺϽ�20mm" id="�к��2">�ͺϽ�20mm<br></div><input type="checkbox" name="catalogs" id="�������" value="�������_:_�������">�������<br><div id="spec_�������" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�������_:_�������:__:3.0_:__%3.0%" id="�������0">3.0<br><input type="checkbox" name="specs" value="�������_:_�������:__:4.75_:__%4.75%" id="�������1">4.75<br></div><input type="checkbox" name="catalogs" id="�޷��" value="�޷��_:_�޷��">�޷��<br><div id="spec_�޷��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�޷��_:_�޷��:__:108*4.5��8163��_:__108*4.5%8163%" id="�޷��0">108*4.5��8163��<br><input type="checkbox" name="specs" value="�޷��_:_�޷��:__:219*6(8163)_:__219*6%8163%" id="�޷��1">219*6(8163)<br><input type="checkbox" name="specs" value="�޷��_:_�޷��:__:108*4.5��8162��_:__108*4.5%8162%" id="�޷��2">108*4.5��8162��<br><input type="checkbox" name="specs" value="�޷��_:_�޷��:__:219*6(8162)_:__219*6%8162%" id="�޷��3">219*6(8162)<br></div><input type="checkbox" name="catalogs" id="��п���" value="��п���_:_��п���">��п���<br><div id="spec_��п���" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��п���_:_��п���:__:0.5mm_:__0.5mm" id="��п���0">0.5mm<br><input type="checkbox" name="specs" value="��п���_:_��п���:__:1.0mm_:__1.0mm" id="��п���1">1.0mm<br></div><input type="checkbox" name="catalogs" id="��Ϳ���" value="��Ϳ���_:_��Ϳ���">��Ϳ���<br><div id="spec_��Ϳ���" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��Ϳ���_:_��Ϳ���:__:0.476mm_:__0.476mm" id="��Ϳ���0">0.476mm<br></div><input type="checkbox" name="catalogs" id="��������" value="��������_:_��������">��������<br><div id="spec_��������" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��������_:_��������:__:3.5mm*685_:__3.5mm*685" id="��������0">3.5mm*685<br><input type="checkbox" name="specs" value="��������_:_��������:__:2.5mm*232_:__2.5mm*232" id="��������1">2.5mm*232<br></div><input type="checkbox" name="catalogs" id="H�͸�" value="H�͸�_:_H�͸�">H�͸�<br><div id="spec_H�͸�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="H�͸�_:_H�͸�:__:200*100_:__200*100" id="H�͸�0">200*100<br><input type="checkbox" name="specs" value="H�͸�_:_H�͸�:__:300*300_:__300*300" id="H�͸�1">300*300<br><input type="checkbox" name="specs" value="H�͸�_:_H�͸�:__:400*200_:__400*200" id="H�͸�2">400*200<br><input type="checkbox" name="specs" value="H�͸�_:_H�͸�:__:588*300_:__588*300" id="H�͸�3">588*300<br></div><input type="checkbox" name="catalogs" id="����" value="����_:_����">����<br><div id="spec_����" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="����_:_����:__:1.5��*3.0_:__1.5��*3.0" id="����0">1.5��*3.0<br><input type="checkbox" name="specs" value="����_:_����:__:1.5��*3.25_:__1.5��*3.25" id="����1">1.5��*3.25<br><input type="checkbox" name="specs" value="����_:_����:__:4��*3.75_:__4��*3.75" id="����2">4��*3.75<br></div><input type="checkbox" name="catalogs" id="���" value="���_:_���">���<br><div id="spec_���" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="���_:_���:__:WW600_:_%WW600_%" id="���0">WW600<br><input type="checkbox" name="specs" value="���_:_���:__:WW800_:_%WW800_%" id="���1">WW800<br></div><input type="checkbox" name="catalogs" id="��������" value="��������_:_��������">��������<br><div id="spec_��������" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��������_:_��������:__:��50-130mm_:__��50-130mm" id="��������0">��50-130mm<br></div><input type="checkbox" name="catalogs" id="Cr�Ͻ��" value="Cr�Ͻ��_:_Cr�Ͻ��">Cr�Ͻ��<br><div id="spec_Cr�Ͻ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="Cr�Ͻ��_:_Cr�Ͻ��:__:��20mm_:__��20mm" id="Cr�Ͻ��0">��20mm<br><input type="checkbox" name="specs" value="Cr�Ͻ��_:_Cr�Ͻ��:__:��80mm_:__��80mm" id="Cr�Ͻ��1">��80mm<br><input type="checkbox" name="specs" value="Cr�Ͻ��_:_Cr�Ͻ��:__:��140mm_:__��140mm" id="Cr�Ͻ��2">��140mm<br></div><input type="checkbox" name="catalogs" id="̼��Բ��" value="̼��Բ��_:_̼��Բ��">̼��Բ��<br><div id="spec_̼��Բ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="̼��Բ��_:_̼��Բ��:__:��20mm_:__��20%" id="̼��Բ��0">��20mm<br><input type="checkbox" name="specs" value="̼��Բ��_:_̼��Բ��:__:��80mm_:__��80%" id="̼��Բ��1">��80mm<br><input type="checkbox" name="specs" value="̼��Բ��_:_̼��Բ��:__:��140mm_:__��140%" id="̼��Բ��2">��140mm<br></div><input type="checkbox" name="catalogs" id="���Բ��" value="���Բ��_:_���Բ��">���Բ��<br><div id="spec_���Բ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="���Բ��_:_���Բ��:__:50mm(����)_:__50mm%����%" id="���Բ��0">50mm(����)<br></div><input type="checkbox" name="catalogs" id="����" value="����_:_����">����<br><div id="spec_����" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="����_:_����:__:H08A_:_H08A_��5.5" id="����0">H08A<br></div><input type="checkbox" name="catalogs" id="��˿��" value="��˿��_:_��˿%">��˿��<br><div id="spec_��˿��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��˿��_:_��˿%:__:��6.5_:__��6.5" id="��˿��0">��6.5<br></div><input type="checkbox" name="catalogs" id="�����" value="�����_:_�����">�����<br><div id="spec_�����" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="�����_:_�����:__:22A��18A��_:_22A��18A��_%" id="�����0">22A��18A��<br><input type="checkbox" name="specs" value="�����_:_�����:__:ML08AL��8A��_:_ML08AL��8A��_%" id="�����1">ML08AL��8A��<br><input type="checkbox" name="specs" value="�����_:_�����:__:ML35��35K��_:_ML35��35K��_%" id="�����2">ML35��35K��<br></div><input type="checkbox" name="catalogs" id="����Բ��" value="����Բ��_:_����Բ��">����Բ��<br><div id="spec_����Բ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="����Բ��_:_����Բ��:__:60Si2Mn_:__60Si2Mn" id="����Բ��0">60Si2Mn<br></div><input type="checkbox" name="catalogs" id="��ģ�߸�" value="��ģ�߸�_:_��ģ�߸�">��ģ�߸�<br><div id="spec_��ģ�߸�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="��ģ�߸�_:_��ģ�߸�:__:Cr12MoV_:_Cr12MoV_%" id="��ģ�߸�0">Cr12MoV<br><input type="checkbox" name="specs" value="��ģ�߸�_:_��ģ�߸�:__:3Cr2W8V_:_3Cr2W8V_%" id="��ģ�߸�1">3Cr2W8V<br><input type="checkbox" name="specs" value="��ģ�߸�_:_��ģ�߸�:__:H13(��¯)_:_H13(��¯)_%" id="��ģ�߸�2">H13(��¯)<br></div><input type="checkbox" name="catalogs" id="���ָ�" value="���ָ�_:_���ָ�">���ָ�<br><div id="spec_���ָ�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="���ָ�_:_���ָ�:__:20CrMnTi��50_:__20CrMnTi%" id="���ָ�0">20CrMnTi��50<br><input type="checkbox" name="specs" value="���ָ�_:_���ָ�:__:20CrMo��50_:__20CrMo%" id="���ָ�1">20CrMo��50<br><input type="checkbox" name="specs" value="���ָ�_:_���ָ�:__:35/42CrMo��50_:__35/42CrMo%" id="���ָ�2">35/42CrMo��50<br></div><input type="checkbox" name="catalogs" id="Crϵ����Բ��" value="Crϵ����Բ��_:_Crϵ����Բ��">Crϵ����Բ��<br><div id="spec_Crϵ����Բ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="Crϵ����Բ��_:_Crϵ����Բ��:__:2Cr13_:__2Cr13" id="Crϵ����Բ��0">2Cr13<br></div><input type="checkbox" name="catalogs" id="̼���" value="̼���_:_̼���">̼���<br><div id="spec_̼���" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="̼���_:_̼���:__:50mm_:__50mm" id="̼���0">50mm<br></div><input type="checkbox" name="catalogs" id="�����" value="�����_:_�����">�����<br><input type="checkbox" name="catalogs" id="���ͭ" value="���ͭ_:_���ͭ">���ͭ<br><input type="checkbox" name="catalogs" id="����" value="����_:_����">����<br><input type="checkbox" name="catalogs" id="����" value="����_:_����">����<br><input type="checkbox" name="catalogs" id="�����" value="�����_:_�����">�����<br><input type="checkbox" name="catalogs" id="Ǧ��" value="Ǧ��_:_Ǧ��">Ǧ��<br><input type="checkbox" name="catalogs" id="п��" value="п��_:_п��">п��<br><input type="checkbox" name="catalogs" id="ADC12" value="ADC12_:_ADC12">ADC12<br><input type="checkbox" name="catalogs" id="A356.2" value="A356.2_:_A356.2">A356.2<br><input type="checkbox" name="catalogs" id="þ��" value="þ��_:_þ��">þ��<br><input type="checkbox" name="catalogs" id="п�Ͻ�" value="п�Ͻ�_:_п�Ͻ�">п�Ͻ�<br><div id="spec_п�Ͻ�" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="п�Ͻ�_:_п�Ͻ�:__:Zamak-5_:__Zamak-5" id="п�Ͻ�0">Zamak-5<br><input type="checkbox" name="specs" value="п�Ͻ�_:_п�Ͻ�:__:Zamak-3_:__Zamak-3" id="п�Ͻ�1">Zamak-3<br><input type="checkbox" name="specs" value="п�Ͻ�_:_п�Ͻ�:__:����_:__����" id="п�Ͻ�2">����<br><input type="checkbox" name="specs" value="п�Ͻ�_:_п�Ͻ�:__:�ȶ�_:__�ȶ�" id="п�Ͻ�3">�ȶ�<br></div><input type="checkbox" name="catalogs" id="Ӳ��" value="Ӳ��_:_Ӳ��">Ӳ��<br><div id="spec_Ӳ��" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="Ӳ��_:_Ӳ��:__:45-70#_:_45-70#_��6.5" id="Ӳ��0">45-70#<br></div><input type="checkbox" name="catalogs" id="�״�" value="�״�_:_�״�">�״�<br><input type="checkbox" name="catalogs" id="��ҵ��" value="��ҵ��_:_��ҵ��">��ҵ��<br></div>

"""
soup = BeautifulSoup(html, 'html.parser')

# for i in soup.find_all("div")[1:]:
#     # print(i.get_text())
#     print(i["id"].replace("spec_","")+" "+i.get_text())

list1 = []
list2 = []
for i in soup.find_all('input',{"name":"catalogs"}):
    # dict=dict(zip("'"+i["id"]+"'","'"+i["value"]+"'"))
    list1.append(i["id"])
    list2.append(i["value"])
data = dict(zip(list1,list2))
print(data)

dict2 = {"���Ƹ�":"���Ƹ�_:_���Ƹ�",
        "�Ǹ�":"�Ǹ�_:_�Ǹ�",
        "�۸�":"�۸�_:_�۸�",
        "���ָ�":"���ָ�_:_���ָ�",
        "�߲�":"�߲�_:_�߲�",
        "�������":"�������_:_�������",
        "�촬��":"�촬��_:_�촬��",
        "�к��":"�к��_:_�к��",
        "�������":"�������_:_�������",
        "�޷��":"�޷��_:_�޷��",
        "��п���":"��п���_:_��п���",
        "��Ϳ���":"��Ϳ���_:_��Ϳ���",
        "��������":"��������_:_��������",
        "H�͸�":"H�͸�_:_H�͸�",
        "����":"����_:_����",
        "���":"���_:_���",
        "��������":"��������_:_��������",
        "Cr�Ͻ��":"Cr�Ͻ��_:_Cr�Ͻ��",
        "̼��Բ��":"̼��Բ��_:_̼��Բ��",
        "���Բ��":"���Բ��_:_���Բ��",
        "����":"����_:_����",
        "��˿��":"��˿��_:_��˿%25",
        "�����":"�����_:_�����",
        "����Բ��":"����Բ��_:_����Բ��",
        "��ģ�߸�":"��ģ�߸�_:_��ģ�߸�",
        "���ָ�":"���ָ�_:_���ָ�",
        "Crϵ����Բ��":"Crϵ����Բ��_:_Crϵ����Բ��",
        "̼���":"̼���_:_̼���",
        "�����":"�����_:_�����",
        "���ͭ":"���ͭ_:_���ͭ",
        "����":"����_:_����",
        "����":"����_:_����",
        "�����":"�����_:_�����",
        "Ǧ��":"Ǧ��_:_Ǧ��",
        "п��":"п��_:_п��",
        "ADC12":"ADC12_:_ADC12",
        "A356.2":"A356.2_:_A356.2",
        "þ��":"þ��_:_þ��",
        "п�Ͻ�":"п�Ͻ�_:_п�Ͻ�",
        "Ӳ��":"Ӳ��_:_Ӳ��",
        "�״�":"�״�_:_�״�",
        "��ҵ��":"��ҵ��_:_��ҵ��"}

dict1 = {"���Ƹ�":["HRB335 12MM","HRB335 20MM","HRB400 20MM"],
         "�Ǹ�":["50*5"],
         "�۸�":["16#"],
        "���ָ�":["25#"],
        "�߲�":["6����HPB300","8.0����HPB300"],
        "�������":["0.5mm_","1.0mm_"],
        "�촬��":["10mm","20mm"],
        "�к��":["��8mm","��20mm","�ͺϽ�20mm"],
        "�������":["3.0","4.75"],
        "�޷��":["108*4.5��8163��","219*6(8163)","108*4.5��8162��","219*6(8162)"],
        "��п���":["0.5mm","1.0mm"],
        "��Ϳ���":["0.476mm"],
        "��������":["3.5mm*685","2.5mm*232"],
        "H�͸�":["200*100","300*300","400*200","588*300"],
        "����":["1.5��*3.0","1.5��*3.25","4��*3.75"],
        "���":["WW600","WW800"],
        "��������":["��50-130mm"],
        "Cr�Ͻ��":["��20mm_","��80mm_","��140mm_"],
        "̼��Բ��":["��20mm","��80mm","��140mm"],
        "���Բ��":["50mm(����)"],
        "����":["H08A"],
        "��˿��":["��6.5"],
        "�����":["22A��18A��","ML08AL��8A��","ML35��35K��"],
        "����Բ��":["60Si2Mn"],
        "��ģ�߸�":["Cr12MoV","3Cr2W8V","H13(��¯)"],
        "���ָ�":["20CrMnTi��50","20CrMo��50","35/42CrMo��50"],
        "Crϵ����Բ��":["2Cr13"],
        "̼���":["50mm"],
        "п�Ͻ�":["Zamak-5","Zamak-3","����","�ȶ�"],
        "Ӳ��":["45-70#"],
        "�����":[],
        "���ͭ":[],
        "����":[],
        "����":[],
        "�����":[],
        "Ǧ��":[],
        "ADC12":[],
        "A356.2":[],
        "þ��":[],
        "�״�":[],
        "��ҵ��":[]
                 }

# for i in soup.find_all('input',{"name":"specs"}):
#     print('"'+i['value']+'"')

dict3 = {"HRB335 12MM":"���Ƹ�_:_���Ƹ�:__:HRB335 12MM_:_HRB335_12MM",
        "HRB335 20MM":"���Ƹ�_:_���Ƹ�:__:HRB335 20MM_:_HRB335_20MM",
        "HRB400 20MM":"���Ƹ�_:_���Ƹ�:__:HRB400 20MM_:_HRB400_20MM",
        "50*5":"�Ǹ�_:_�Ǹ�:__:50*5_:__50*5",
        "16#":"�۸�_:_�۸�:__:16#_:__16#",
        "25#":"���ָ�_:_���ָ�:__:25#_:__25#",
        "6����HPB300":"�߲�_:_�߲�:__:6����HPB300_:_HPB300_6����",
        "8.0����HPB300":"�߲�_:_�߲�:__:8.0����HPB300_:_HPB300_8.0����",
        "0.5mm_":"�������_:_�������:__:0.5mm_:__0.5mm",
        "1.0mm_":"�������_:_�������:__:1.0mm_:__1.0mm",
        "10mm":"�촬��_:_�촬��:__:10mm_:__10mm",
        "20mm":"�촬��_:_�촬��:__:20mm_:__20mm",
        "��8mm":"�к��_:_�к��:__:��8mm_:__��8mm",
        "��20mm":"�к��_:_�к��:__:��20mm_:__��20mm",
        "�ͺϽ�20mm":"�к��_:_�к��:__:�ͺϽ�20mm_:__�ͺϽ�20mm",
        "3.0":"�������_:_�������:__:3.0_:__%253.0%25",
        "4.75":"�������_:_�������:__:4.75_:__%254.75%25",
        "108*4.5��8163��":"�޷��_:_�޷��:__:108*4.5��8163��_:__108*4.5%258163%25",
        "219*6(8163)":"�޷��_:_�޷��:__:219*6(8163)_:__219*6%258163%25",
        "108*4.5��8162��":"�޷��_:_�޷��:__:108*4.5��8162��_:__108*4.5%258162%25",
        "219*6(8162)":"�޷��_:_�޷��:__:219*6(8162)_:__219*6%258162%25",
        "0.5mm":"��п���_:_��п���:__:0.5mm_:__0.5mm",
        "1.0mm":"��п���_:_��п���:__:1.0mm_:__1.0mm",
        "0.476mm":"��Ϳ���_:_��Ϳ���:__:0.476mm_:__0.476mm",
        "3.5mm*685":"��������_:_��������:__:3.5mm*685_:__3.5mm*685",
        "2.5mm*232":"��������_:_��������:__:2.5mm*232_:__2.5mm*232",
        "200*100":"H�͸�_:_H�͸�:__:200*100_:__200*100",
        "300*300":"H�͸�_:_H�͸�:__:300*300_:__300*300",
        "400*200":"H�͸�_:_H�͸�:__:400*200_:__400*200",
        "588*300":"H�͸�_:_H�͸�:__:588*300_:__588*300",
        "1.5��*3.0":"����_:_����:__:1.5��*3.0_:__1.5��*3.0",
        "1.5��*3.25":"����_:_����:__:1.5��*3.25_:__1.5��*3.25",
        "4��*3.75":"����_:_����:__:4��*3.75_:__4��*3.75",
        "WW600":"���_:_���:__:WW600_:_%25WW600_%25",
        "WW800":"���_:_���:__:WW800_:_%25WW800_%25",
        "��50-130mm":"��������_:_��������:__:��50-130mm_:__��50-130mm",
        "��20mm_":"Cr�Ͻ��_:_Cr�Ͻ��:__:��20mm_:__��20mm",
        "��80mm_":"Cr�Ͻ��_:_Cr�Ͻ��:__:��80mm_:__��80mm",
        "��140mm_":"Cr�Ͻ��_:_Cr�Ͻ��:__:��140mm_:__��140mm",
        "��20mm":"̼��Բ��_:_̼��Բ��:__:��20mm_:__��20%25",
        "��80mm":"̼��Բ��_:_̼��Բ��:__:��80mm_:__��80%25",
        "��140mm":"̼��Բ��_:_̼��Բ��:__:��140mm_:__��140%25",
        "50mm(����)":"���Բ��_:_���Բ��:__:50mm(����)_:__50mm%25����%25",
        "H08A":"����_:_����:__:H08A_:_H08A_��5.5",
        "��6.5":"��˿��_:_��˿%25:__:��6.5_:__��6.5",
        "22A��18A��":"�����_:_�����:__:22A��18A��_:_22A��18A��_%25",
        "ML08AL��8A��":"�����_:_�����:__:ML08AL��8A��_:_ML08AL��8A��_%25",
        "ML35��35K��":"�����_:_�����:__:ML35��35K��_:_ML35��35K��_%25",
        "60Si2Mn":"����Բ��_:_����Բ��:__:60Si2Mn_:__60Si2Mn",
        "Cr12MoV":"��ģ�߸�_:_��ģ�߸�:__:Cr12MoV_:_Cr12MoV_%25",
        "3Cr2W8V":"��ģ�߸�_:_��ģ�߸�:__:3Cr2W8V_:_3Cr2W8V_%25",
        "H13(��¯)":"��ģ�߸�_:_��ģ�߸�:__:H13(��¯)_:_H13(��¯)_%25",
        "20CrMnTi��50":"���ָ�_:_���ָ�:__:20CrMnTi��50_:__20CrMnTi%25",
        "20CrMo��50":"���ָ�_:_���ָ�:__:20CrMo��50_:__20CrMo%25",
        "35/42CrMo��50":"���ָ�_:_���ָ�:__:35/42CrMo��50_:__35/42CrMo%25",
        "2Cr13":"Crϵ����Բ��_:_Crϵ����Բ��:__:2Cr13_:__2Cr13",
        "50mm":"̼���_:_̼���:__:50mm_:__50mm",
        "Zamak-5":"п�Ͻ�_:_п�Ͻ�:__:Zamak-5_:__Zamak-5",
        "Zamak-3":"п�Ͻ�_:_п�Ͻ�:__:Zamak-3_:__Zamak-3",
        "����":"п�Ͻ�_:_п�Ͻ�:__:����_:__����",
        "�ȶ�":"п�Ͻ�_:_п�Ͻ�:__:�ȶ�_:__�ȶ�",
        "45-70#":"Ӳ��_:_Ӳ��:__:45-70#_:_45-70#_��6.5"}






























































# for i in soup.find_all("input"):
#     print(i)