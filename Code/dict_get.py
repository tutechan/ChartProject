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

<div id="pzDiv" style="display: block;"><input type="checkbox" name="catalogs" id="螺纹钢" value="螺纹钢_:_螺纹钢">螺纹钢<br><div id="spec_螺纹钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="螺纹钢_:_螺纹钢:__:HRB335 12MM_:_HRB335_12MM" id="螺纹钢0">HRB335 12MM<br><input type="checkbox" name="specs" value="螺纹钢_:_螺纹钢:__:HRB335 20MM_:_HRB335_20MM" id="螺纹钢1">HRB335 20MM<br><input type="checkbox" name="specs" value="螺纹钢_:_螺纹钢:__:HRB400 20MM_:_HRB400_20MM" id="螺纹钢2">HRB400 20MM<br></div><input type="checkbox" name="catalogs" id="角钢" value="角钢_:_角钢">角钢<br><div id="spec_角钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="角钢_:_角钢:__:50*5_:__50*5" id="角钢0">50*5<br></div><input type="checkbox" name="catalogs" id="槽钢" value="槽钢_:_槽钢">槽钢<br><div id="spec_槽钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="槽钢_:_槽钢:__:16#_:__16#" id="槽钢0">16#<br></div><input type="checkbox" name="catalogs" id="工字钢" value="工字钢_:_工字钢">工字钢<br><div id="spec_工字钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="工字钢_:_工字钢:__:25#_:__25#" id="工字钢0">25#<br></div><input type="checkbox" name="catalogs" id="线材" value="线材_:_线材">线材<br><div id="spec_线材" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="线材_:_线材:__:6高线HPB300_:_HPB300_6高线" id="线材0">6高线HPB300<br><input type="checkbox" name="specs" value="线材_:_线材:__:8.0高线HPB300_:_HPB300_8.0高线" id="线材1">8.0高线HPB300<br></div><input type="checkbox" name="catalogs" id="冷轧板卷" value="冷轧板卷_:_冷轧板卷">冷轧板卷<br><div id="spec_冷轧板卷" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="冷轧板卷_:_冷轧板卷:__:0.5mm_:__0.5mm" id="冷轧板卷0">0.5mm<br><input type="checkbox" name="specs" value="冷轧板卷_:_冷轧板卷:__:1.0mm_:__1.0mm" id="冷轧板卷1">1.0mm<br></div><input type="checkbox" name="catalogs" id="造船板" value="造船板_:_造船板">造船板<br><div id="spec_造船板" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="造船板_:_造船板:__:10mm_:__10mm" id="造船板0">10mm<br><input type="checkbox" name="specs" value="造船板_:_造船板:__:20mm_:__20mm" id="造船板1">20mm<br></div><input type="checkbox" name="catalogs" id="中厚板" value="中厚板_:_中厚板">中厚板<br><div id="spec_中厚板" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="中厚板_:_中厚板:__:普8mm_:__普8mm" id="中厚板0">普8mm<br><input type="checkbox" name="specs" value="中厚板_:_中厚板:__:普20mm_:__普20mm" id="中厚板1">普20mm<br><input type="checkbox" name="specs" value="中厚板_:_中厚板:__:低合金20mm_:__低合金20mm" id="中厚板2">低合金20mm<br></div><input type="checkbox" name="catalogs" id="热轧板卷" value="热轧板卷_:_热轧板卷">热轧板卷<br><div id="spec_热轧板卷" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="热轧板卷_:_热轧板卷:__:3.0_:__%3.0%" id="热轧板卷0">3.0<br><input type="checkbox" name="specs" value="热轧板卷_:_热轧板卷:__:4.75_:__%4.75%" id="热轧板卷1">4.75<br></div><input type="checkbox" name="catalogs" id="无缝管" value="无缝管_:_无缝管">无缝管<br><div id="spec_无缝管" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="无缝管_:_无缝管:__:108*4.5（8163）_:__108*4.5%8163%" id="无缝管0">108*4.5（8163）<br><input type="checkbox" name="specs" value="无缝管_:_无缝管:__:219*6(8163)_:__219*6%8163%" id="无缝管1">219*6(8163)<br><input type="checkbox" name="specs" value="无缝管_:_无缝管:__:108*4.5（8162）_:__108*4.5%8162%" id="无缝管2">108*4.5（8162）<br><input type="checkbox" name="specs" value="无缝管_:_无缝管:__:219*6(8162)_:__219*6%8162%" id="无缝管3">219*6(8162)<br></div><input type="checkbox" name="catalogs" id="镀锌板卷" value="镀锌板卷_:_镀锌板卷">镀锌板卷<br><div id="spec_镀锌板卷" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="镀锌板卷_:_镀锌板卷:__:0.5mm_:__0.5mm" id="镀锌板卷0">0.5mm<br><input type="checkbox" name="specs" value="镀锌板卷_:_镀锌板卷:__:1.0mm_:__1.0mm" id="镀锌板卷1">1.0mm<br></div><input type="checkbox" name="catalogs" id="彩涂板卷" value="彩涂板卷_:_彩涂板卷">彩涂板卷<br><div id="spec_彩涂板卷" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="彩涂板卷_:_彩涂板卷:__:0.476mm_:__0.476mm" id="彩涂板卷0">0.476mm<br></div><input type="checkbox" name="catalogs" id="热轧带钢" value="热轧带钢_:_热轧带钢">热轧带钢<br><div id="spec_热轧带钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="热轧带钢_:_热轧带钢:__:3.5mm*685_:__3.5mm*685" id="热轧带钢0">3.5mm*685<br><input type="checkbox" name="specs" value="热轧带钢_:_热轧带钢:__:2.5mm*232_:__2.5mm*232" id="热轧带钢1">2.5mm*232<br></div><input type="checkbox" name="catalogs" id="H型钢" value="H型钢_:_H型钢">H型钢<br><div id="spec_H型钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="H型钢_:_H型钢:__:200*100_:__200*100" id="H型钢0">200*100<br><input type="checkbox" name="specs" value="H型钢_:_H型钢:__:300*300_:__300*300" id="H型钢1">300*300<br><input type="checkbox" name="specs" value="H型钢_:_H型钢:__:400*200_:__400*200" id="H型钢2">400*200<br><input type="checkbox" name="specs" value="H型钢_:_H型钢:__:588*300_:__588*300" id="H型钢3">588*300<br></div><input type="checkbox" name="catalogs" id="焊管" value="焊管_:_焊管">焊管<br><div id="spec_焊管" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="焊管_:_焊管:__:1.5寸*3.0_:__1.5寸*3.0" id="焊管0">1.5寸*3.0<br><input type="checkbox" name="specs" value="焊管_:_焊管:__:1.5寸*3.25_:__1.5寸*3.25" id="焊管1">1.5寸*3.25<br><input type="checkbox" name="specs" value="焊管_:_焊管:__:4寸*3.75_:__4寸*3.75" id="焊管2">4寸*3.75<br></div><input type="checkbox" name="catalogs" id="硅钢" value="硅钢_:_硅钢">硅钢<br><div id="spec_硅钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="硅钢_:_硅钢:__:WW600_:_%WW600_%" id="硅钢0">WW600<br><input type="checkbox" name="specs" value="硅钢_:_硅钢:__:WW800_:_%WW800_%" id="硅钢1">WW800<br></div><input type="checkbox" name="catalogs" id="热轧管坯" value="热轧管坯_:_热轧管坯">热轧管坯<br><div id="spec_热轧管坯" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="热轧管坯_:_热轧管坯:__:∮50-130mm_:__∮50-130mm" id="热轧管坯0">∮50-130mm<br></div><input type="checkbox" name="catalogs" id="Cr合结钢" value="Cr合结钢_:_Cr合结钢">Cr合结钢<br><div id="spec_Cr合结钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="Cr合结钢_:_Cr合结钢:__:Φ20mm_:__Φ20mm" id="Cr合结钢0">Φ20mm<br><input type="checkbox" name="specs" value="Cr合结钢_:_Cr合结钢:__:Φ80mm_:__Φ80mm" id="Cr合结钢1">Φ80mm<br><input type="checkbox" name="specs" value="Cr合结钢_:_Cr合结钢:__:Φ140mm_:__Φ140mm" id="Cr合结钢2">Φ140mm<br></div><input type="checkbox" name="catalogs" id="碳结圆钢" value="碳结圆钢_:_碳结圆钢">碳结圆钢<br><div id="spec_碳结圆钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="碳结圆钢_:_碳结圆钢:__:Φ20mm_:__Φ20%" id="碳结圆钢0">Φ20mm<br><input type="checkbox" name="specs" value="碳结圆钢_:_碳结圆钢:__:Φ80mm_:__Φ80%" id="碳结圆钢1">Φ80mm<br><input type="checkbox" name="specs" value="碳结圆钢_:_碳结圆钢:__:Φ140mm_:__Φ140%" id="碳结圆钢2">Φ140mm<br></div><input type="checkbox" name="catalogs" id="轴承圆钢" value="轴承圆钢_:_轴承圆钢">轴承圆钢<br><div id="spec_轴承圆钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="轴承圆钢_:_轴承圆钢:__:50mm(连铸)_:__50mm%连铸%" id="轴承圆钢0">50mm(连铸)<br></div><input type="checkbox" name="catalogs" id="焊线" value="焊线_:_焊线">焊线<br><div id="spec_焊线" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="焊线_:_焊线:__:H08A_:_H08A_φ5.5" id="焊线0">H08A<br></div><input type="checkbox" name="catalogs" id="拉丝材" value="拉丝材_:_拉丝%">拉丝材<br><div id="spec_拉丝材" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="拉丝材_:_拉丝%:__:Φ6.5_:__Φ6.5" id="拉丝材0">Φ6.5<br></div><input type="checkbox" name="catalogs" id="冷镦钢" value="冷镦钢_:_冷镦钢">冷镦钢<br><div id="spec_冷镦钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="冷镦钢_:_冷镦钢:__:22A（18A）_:_22A（18A）_%" id="冷镦钢0">22A（18A）<br><input type="checkbox" name="specs" value="冷镦钢_:_冷镦钢:__:ML08AL（8A）_:_ML08AL（8A）_%" id="冷镦钢1">ML08AL（8A）<br><input type="checkbox" name="specs" value="冷镦钢_:_冷镦钢:__:ML35（35K）_:_ML35（35K）_%" id="冷镦钢2">ML35（35K）<br></div><input type="checkbox" name="catalogs" id="弹簧圆钢" value="弹簧圆钢_:_弹簧圆钢">弹簧圆钢<br><div id="spec_弹簧圆钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="弹簧圆钢_:_弹簧圆钢:__:60Si2Mn_:__60Si2Mn" id="弹簧圆钢0">60Si2Mn<br></div><input type="checkbox" name="catalogs" id="工模具钢" value="工模具钢_:_工模具钢">工模具钢<br><div id="spec_工模具钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="工模具钢_:_工模具钢:__:Cr12MoV_:_Cr12MoV_%" id="工模具钢0">Cr12MoV<br><input type="checkbox" name="specs" value="工模具钢_:_工模具钢:__:3Cr2W8V_:_3Cr2W8V_%" id="工模具钢1">3Cr2W8V<br><input type="checkbox" name="specs" value="工模具钢_:_工模具钢:__:H13(电炉)_:_H13(电炉)_%" id="工模具钢2">H13(电炉)<br></div><input type="checkbox" name="catalogs" id="齿轮钢" value="齿轮钢_:_齿轮钢">齿轮钢<br><div id="spec_齿轮钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="齿轮钢_:_齿轮钢:__:20CrMnTiΦ50_:__20CrMnTi%" id="齿轮钢0">20CrMnTiΦ50<br><input type="checkbox" name="specs" value="齿轮钢_:_齿轮钢:__:20CrMoΦ50_:__20CrMo%" id="齿轮钢1">20CrMoΦ50<br><input type="checkbox" name="specs" value="齿轮钢_:_齿轮钢:__:35/42CrMoΦ50_:__35/42CrMo%" id="齿轮钢2">35/42CrMoΦ50<br></div><input type="checkbox" name="catalogs" id="Cr系不锈圆钢" value="Cr系不锈圆钢_:_Cr系不锈圆钢">Cr系不锈圆钢<br><div id="spec_Cr系不锈圆钢" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="Cr系不锈圆钢_:_Cr系不锈圆钢:__:2Cr13_:__2Cr13" id="Cr系不锈圆钢0">2Cr13<br></div><input type="checkbox" name="catalogs" id="碳结板" value="碳结板_:_碳结板">碳结板<br><div id="spec_碳结板" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="碳结板_:_碳结板:__:50mm_:__50mm" id="碳结板0">50mm<br></div><input type="checkbox" name="catalogs" id="电解镍" value="电解镍_:_电解镍">电解镍<br><input type="checkbox" name="catalogs" id="电解铜" value="电解铜_:_电解铜">电解铜<br><input type="checkbox" name="catalogs" id="锡锭" value="锡锭_:_锡锭">锡锭<br><input type="checkbox" name="catalogs" id="钨铁" value="钨铁_:_钨铁">钨铁<br><input type="checkbox" name="catalogs" id="电解铝" value="电解铝_:_电解铝">电解铝<br><input type="checkbox" name="catalogs" id="铅锭" value="铅锭_:_铅锭">铅锭<br><input type="checkbox" name="catalogs" id="锌锭" value="锌锭_:_锌锭">锌锭<br><input type="checkbox" name="catalogs" id="ADC12" value="ADC12_:_ADC12">ADC12<br><input type="checkbox" name="catalogs" id="A356.2" value="A356.2_:_A356.2">A356.2<br><input type="checkbox" name="catalogs" id="镁锭" value="镁锭_:_镁锭">镁锭<br><input type="checkbox" name="catalogs" id="锌合金" value="锌合金_:_锌合金">锌合金<br><div id="spec_锌合金" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="锌合金_:_锌合金:__:Zamak-5_:__Zamak-5" id="锌合金0">Zamak-5<br><input type="checkbox" name="specs" value="锌合金_:_锌合金:__:Zamak-3_:__Zamak-3" id="锌合金1">Zamak-3<br><input type="checkbox" name="specs" value="锌合金_:_锌合金:__:铸造_:__铸造" id="锌合金2">铸造<br><input type="checkbox" name="specs" value="锌合金_:_锌合金:__:热镀_:__热镀" id="锌合金3">热镀<br></div><input type="checkbox" name="catalogs" id="硬线" value="硬线_:_硬线">硬线<br><div id="spec_硬线" style="padding-left: 15px; display: none;"><input type="checkbox" name="specs" value="硬线_:_硬线:__:45-70#_:_45-70#_Φ6.5" id="硬线0">45-70#<br></div><input type="checkbox" name="catalogs" id="甲醇" value="甲醇_:_甲醇">甲醇<br><input type="checkbox" name="catalogs" id="工业萘" value="工业萘_:_工业萘">工业萘<br></div>

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

dict2 = {"螺纹钢":"螺纹钢_:_螺纹钢",
        "角钢":"角钢_:_角钢",
        "槽钢":"槽钢_:_槽钢",
        "工字钢":"工字钢_:_工字钢",
        "线材":"线材_:_线材",
        "冷轧板卷":"冷轧板卷_:_冷轧板卷",
        "造船板":"造船板_:_造船板",
        "中厚板":"中厚板_:_中厚板",
        "热轧板卷":"热轧板卷_:_热轧板卷",
        "无缝管":"无缝管_:_无缝管",
        "镀锌板卷":"镀锌板卷_:_镀锌板卷",
        "彩涂板卷":"彩涂板卷_:_彩涂板卷",
        "热轧带钢":"热轧带钢_:_热轧带钢",
        "H型钢":"H型钢_:_H型钢",
        "焊管":"焊管_:_焊管",
        "硅钢":"硅钢_:_硅钢",
        "热轧管坯":"热轧管坯_:_热轧管坯",
        "Cr合结钢":"Cr合结钢_:_Cr合结钢",
        "碳结圆钢":"碳结圆钢_:_碳结圆钢",
        "轴承圆钢":"轴承圆钢_:_轴承圆钢",
        "焊线":"焊线_:_焊线",
        "拉丝材":"拉丝材_:_拉丝%25",
        "冷镦钢":"冷镦钢_:_冷镦钢",
        "弹簧圆钢":"弹簧圆钢_:_弹簧圆钢",
        "工模具钢":"工模具钢_:_工模具钢",
        "齿轮钢":"齿轮钢_:_齿轮钢",
        "Cr系不锈圆钢":"Cr系不锈圆钢_:_Cr系不锈圆钢",
        "碳结板":"碳结板_:_碳结板",
        "电解镍":"电解镍_:_电解镍",
        "电解铜":"电解铜_:_电解铜",
        "锡锭":"锡锭_:_锡锭",
        "钨铁":"钨铁_:_钨铁",
        "电解铝":"电解铝_:_电解铝",
        "铅锭":"铅锭_:_铅锭",
        "锌锭":"锌锭_:_锌锭",
        "ADC12":"ADC12_:_ADC12",
        "A356.2":"A356.2_:_A356.2",
        "镁锭":"镁锭_:_镁锭",
        "锌合金":"锌合金_:_锌合金",
        "硬线":"硬线_:_硬线",
        "甲醇":"甲醇_:_甲醇",
        "工业萘":"工业萘_:_工业萘"}

dict1 = {"螺纹钢":["HRB335 12MM","HRB335 20MM","HRB400 20MM"],
         "角钢":["50*5"],
         "槽钢":["16#"],
        "工字钢":["25#"],
        "线材":["6高线HPB300","8.0高线HPB300"],
        "冷轧板卷":["0.5mm_","1.0mm_"],
        "造船板":["10mm","20mm"],
        "中厚板":["普8mm","普20mm","低合金20mm"],
        "热轧板卷":["3.0","4.75"],
        "无缝管":["108*4.5（8163）","219*6(8163)","108*4.5（8162）","219*6(8162)"],
        "镀锌板卷":["0.5mm","1.0mm"],
        "彩涂板卷":["0.476mm"],
        "热轧带钢":["3.5mm*685","2.5mm*232"],
        "H型钢":["200*100","300*300","400*200","588*300"],
        "焊管":["1.5寸*3.0","1.5寸*3.25","4寸*3.75"],
        "硅钢":["WW600","WW800"],
        "热轧管坯":["∮50-130mm"],
        "Cr合结钢":["Φ20mm_","Φ80mm_","Φ140mm_"],
        "碳结圆钢":["Φ20mm","Φ80mm","Φ140mm"],
        "轴承圆钢":["50mm(连铸)"],
        "焊线":["H08A"],
        "拉丝材":["Φ6.5"],
        "冷镦钢":["22A（18A）","ML08AL（8A）","ML35（35K）"],
        "弹簧圆钢":["60Si2Mn"],
        "工模具钢":["Cr12MoV","3Cr2W8V","H13(电炉)"],
        "齿轮钢":["20CrMnTiΦ50","20CrMoΦ50","35/42CrMoΦ50"],
        "Cr系不锈圆钢":["2Cr13"],
        "碳结板":["50mm"],
        "锌合金":["Zamak-5","Zamak-3","铸造","热镀"],
        "硬线":["45-70#"],
        "电解镍":[],
        "电解铜":[],
        "锡锭":[],
        "钨铁":[],
        "电解铝":[],
        "铅锭":[],
        "ADC12":[],
        "A356.2":[],
        "镁锭":[],
        "甲醇":[],
        "工业萘":[]
                 }

# for i in soup.find_all('input',{"name":"specs"}):
#     print('"'+i['value']+'"')

dict3 = {"HRB335 12MM":"螺纹钢_:_螺纹钢:__:HRB335 12MM_:_HRB335_12MM",
        "HRB335 20MM":"螺纹钢_:_螺纹钢:__:HRB335 20MM_:_HRB335_20MM",
        "HRB400 20MM":"螺纹钢_:_螺纹钢:__:HRB400 20MM_:_HRB400_20MM",
        "50*5":"角钢_:_角钢:__:50*5_:__50*5",
        "16#":"槽钢_:_槽钢:__:16#_:__16#",
        "25#":"工字钢_:_工字钢:__:25#_:__25#",
        "6高线HPB300":"线材_:_线材:__:6高线HPB300_:_HPB300_6高线",
        "8.0高线HPB300":"线材_:_线材:__:8.0高线HPB300_:_HPB300_8.0高线",
        "0.5mm_":"冷轧板卷_:_冷轧板卷:__:0.5mm_:__0.5mm",
        "1.0mm_":"冷轧板卷_:_冷轧板卷:__:1.0mm_:__1.0mm",
        "10mm":"造船板_:_造船板:__:10mm_:__10mm",
        "20mm":"造船板_:_造船板:__:20mm_:__20mm",
        "普8mm":"中厚板_:_中厚板:__:普8mm_:__普8mm",
        "普20mm":"中厚板_:_中厚板:__:普20mm_:__普20mm",
        "低合金20mm":"中厚板_:_中厚板:__:低合金20mm_:__低合金20mm",
        "3.0":"热轧板卷_:_热轧板卷:__:3.0_:__%253.0%25",
        "4.75":"热轧板卷_:_热轧板卷:__:4.75_:__%254.75%25",
        "108*4.5（8163）":"无缝管_:_无缝管:__:108*4.5（8163）_:__108*4.5%258163%25",
        "219*6(8163)":"无缝管_:_无缝管:__:219*6(8163)_:__219*6%258163%25",
        "108*4.5（8162）":"无缝管_:_无缝管:__:108*4.5（8162）_:__108*4.5%258162%25",
        "219*6(8162)":"无缝管_:_无缝管:__:219*6(8162)_:__219*6%258162%25",
        "0.5mm":"镀锌板卷_:_镀锌板卷:__:0.5mm_:__0.5mm",
        "1.0mm":"镀锌板卷_:_镀锌板卷:__:1.0mm_:__1.0mm",
        "0.476mm":"彩涂板卷_:_彩涂板卷:__:0.476mm_:__0.476mm",
        "3.5mm*685":"热轧带钢_:_热轧带钢:__:3.5mm*685_:__3.5mm*685",
        "2.5mm*232":"热轧带钢_:_热轧带钢:__:2.5mm*232_:__2.5mm*232",
        "200*100":"H型钢_:_H型钢:__:200*100_:__200*100",
        "300*300":"H型钢_:_H型钢:__:300*300_:__300*300",
        "400*200":"H型钢_:_H型钢:__:400*200_:__400*200",
        "588*300":"H型钢_:_H型钢:__:588*300_:__588*300",
        "1.5寸*3.0":"焊管_:_焊管:__:1.5寸*3.0_:__1.5寸*3.0",
        "1.5寸*3.25":"焊管_:_焊管:__:1.5寸*3.25_:__1.5寸*3.25",
        "4寸*3.75":"焊管_:_焊管:__:4寸*3.75_:__4寸*3.75",
        "WW600":"硅钢_:_硅钢:__:WW600_:_%25WW600_%25",
        "WW800":"硅钢_:_硅钢:__:WW800_:_%25WW800_%25",
        "∮50-130mm":"热轧管坯_:_热轧管坯:__:∮50-130mm_:__∮50-130mm",
        "Φ20mm_":"Cr合结钢_:_Cr合结钢:__:Φ20mm_:__Φ20mm",
        "Φ80mm_":"Cr合结钢_:_Cr合结钢:__:Φ80mm_:__Φ80mm",
        "Φ140mm_":"Cr合结钢_:_Cr合结钢:__:Φ140mm_:__Φ140mm",
        "Φ20mm":"碳结圆钢_:_碳结圆钢:__:Φ20mm_:__Φ20%25",
        "Φ80mm":"碳结圆钢_:_碳结圆钢:__:Φ80mm_:__Φ80%25",
        "Φ140mm":"碳结圆钢_:_碳结圆钢:__:Φ140mm_:__Φ140%25",
        "50mm(连铸)":"轴承圆钢_:_轴承圆钢:__:50mm(连铸)_:__50mm%25连铸%25",
        "H08A":"焊线_:_焊线:__:H08A_:_H08A_φ5.5",
        "Φ6.5":"拉丝材_:_拉丝%25:__:Φ6.5_:__Φ6.5",
        "22A（18A）":"冷镦钢_:_冷镦钢:__:22A（18A）_:_22A（18A）_%25",
        "ML08AL（8A）":"冷镦钢_:_冷镦钢:__:ML08AL（8A）_:_ML08AL（8A）_%25",
        "ML35（35K）":"冷镦钢_:_冷镦钢:__:ML35（35K）_:_ML35（35K）_%25",
        "60Si2Mn":"弹簧圆钢_:_弹簧圆钢:__:60Si2Mn_:__60Si2Mn",
        "Cr12MoV":"工模具钢_:_工模具钢:__:Cr12MoV_:_Cr12MoV_%25",
        "3Cr2W8V":"工模具钢_:_工模具钢:__:3Cr2W8V_:_3Cr2W8V_%25",
        "H13(电炉)":"工模具钢_:_工模具钢:__:H13(电炉)_:_H13(电炉)_%25",
        "20CrMnTiΦ50":"齿轮钢_:_齿轮钢:__:20CrMnTiΦ50_:__20CrMnTi%25",
        "20CrMoΦ50":"齿轮钢_:_齿轮钢:__:20CrMoΦ50_:__20CrMo%25",
        "35/42CrMoΦ50":"齿轮钢_:_齿轮钢:__:35/42CrMoΦ50_:__35/42CrMo%25",
        "2Cr13":"Cr系不锈圆钢_:_Cr系不锈圆钢:__:2Cr13_:__2Cr13",
        "50mm":"碳结板_:_碳结板:__:50mm_:__50mm",
        "Zamak-5":"锌合金_:_锌合金:__:Zamak-5_:__Zamak-5",
        "Zamak-3":"锌合金_:_锌合金:__:Zamak-3_:__Zamak-3",
        "铸造":"锌合金_:_锌合金:__:铸造_:__铸造",
        "热镀":"锌合金_:_锌合金:__:热镀_:__热镀",
        "45-70#":"硬线_:_硬线:__:45-70#_:_45-70#_Φ6.5"}






























































# for i in soup.find_all("input"):
#     print(i)