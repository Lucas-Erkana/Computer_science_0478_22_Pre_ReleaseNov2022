
parkingStatus=["John N10W","Mike N11W","Anna N12W","Peter N13W","Available","Angel N15W","Samuel N16W","John N17W","Mike N18W","Anna N19W","Peter N110W","Tony N111W","Angel N112W","Samuel N113W","John N114W","Mike N115W","Anna N116W","Peter N117W","Tony N118W","Angel N119W","Samuel N120W","John N121W","Mike N122W","Anna N123W","Peter N124W","Tony N125W","Angel N126W","Samuel N127W","John N128W","Mike N129W","Anna N130W","Peter N131W","Tony N132W","Angel N133W","Samuel N134W","John N135W","Mike N136W","Anna N137W","Peter N138W","Tony N139W","Angel N140W","Samuel N141W","John N142W","Mike N143W","Anna N144W","Peter N145W","Tony N146W","Angel N147W","Samuel N148W","John N149W","Mike N150W","Anna N151W","Peter N152W","Tony N153W","Angel N154W","Samuel N155W","John N156W","Mike N157W","Anna N158W","Peter N159W","Tony N160W","Angel N161W","Samuel N162W","John N163W","Mike N164W","Anna N165W","Peter N166W","Tony N167W","Angel N168W","Samuel N169W","John N170W","Mike N171W","Anna N172W","Peter N173W","Tony N174W","Angel N175W","Samuel N176W","John N177W","Mike N178W","Anna N179W","Peter N180W","Tony N181W","Angel N182W","Samuel N183W","John N184W","Mike N185W","Anna N186W","Peter N187W","Tony N188W","Angel N189W","Samuel N190W","John N191W","Mike N192W","Anna N193W","Peter N194W","Tony N195W","Angel N196W","Samuel N197W","John N198W","Mike N199W","Anna N1100W","Peter N1101W","Tony N1102W","Available","Available","Available","Mike N1106W","Anna N1107W","Peter N1108W","Tony N1109W","Angel N1110W","Samuel N1111W","John N1112W","Mike N1113W","Anna N1114W","Peter N1115W","Tony N1116W","Angel N1117W","Samuel N1118W","John N1119W","Mike N1120W","Anna N1121W","Peter N1122W","Tony N1123W","Angel N1124W","Samuel N1125W","John N1126W","Mike N1127W","Anna N1128W","Peter N1129W","Tony N1130W","Angel N1131W","Samuel N1132W","John N1133W","Mike N1134W","Anna N1135W","Peter N1136W","Tony N1137W","Angel N1138W","Samuel N1139W","John N1140W","Mike N1141W","Anna N1142W","Peter N1143W","Tony N1144W","Angel N1145W","Samuel N1146W","John N1147W","Mike N1148W","Anna N1149W","Peter N1150W","Tony N1151W","Angel N1152W","Samuel N1153W","John N1154W","Mike N1155W","Anna N1156W","Peter N1157W","Tony N1158W","Angel N1159W","Samuel N1160W","John N1161W","Mike N1162W","Anna N1163W","Peter N1164W","Tony N1165W","Angel N1166W","Samuel N1167W","John N1168W","Mike N1169W","Anna N1170W","Peter N1171W","Tony N1172W","Angel N1173W","Samuel N1174W","John N1175W","Mike N1176W","Anna N1177W","Peter N1178W","Tony N1179W","Angel N1180W","Samuel N1181W","John N1182W","Mike N1183W","Anna N1184W","Peter N1185W","Tony N1186W","Angel N1187W","Samuel N1188W","John N1189W","Mike N1190W","Anna N1191W","Peter N1192W","Tony N1193W","Angel N1194W","Samuel N1195W","John N1196W","Mike N1197W","Anna N1198W","Peter N1199W","Tony N1200W","Angel N1201W","Samuel N1202W","John N1203W","Mike N1204W","Anna N1205W","Peter N1206W","Tony N1207W","Angel N1208W","Samuel N1209W","John N1210W","Mike N1211W","Anna N1212W","Peter N1213W","Tony N1214W","Angel N1215W","Samuel N1216W","John N1217W","Mike N1218W","Anna N1219W","Peter N1220W","Tony N1221W","Angel N1222W","Samuel N1223W","John N1224W","Mike N1225W","Anna N1226W","Peter N1227W","Tony N1228W","Angel N1229W","Samuel N1230W","John N1231W","Mike N1232W","Anna N1233W","Peter N1234W","Tony N1235W","Angel N1236W","Samuel N1237W","John N1238W","Mike N1239W","Anna N1240W","Peter N1241W","Tony N1242W","Angel N1243W","Samuel N1244W","John N1245W","Mike N1246W","Anna N1247W","Peter N1248W","Tony N1249W","Angel N1250W","Samuel N1251W","John N1252W","Mike N1253W","Anna N1254W","Peter N1255W","Tony N1256W","Angel N1257W","Samuel N1258W","John N1259W","Mike N1260W","Anna N1261W","Peter N1262W","Tony N1263W","Angel N1264W","Samuel N1265W","John N1266W","Mike N1267W","Anna N1268W","Peter N1269W","Tony N1270W","Angel N1271W","Samuel N1272W","John N1273W","Mike N1274W","Anna N1275W","Peter N1276W","Tony N1277W","Angel N1278W","Samuel N1279W"]
accessibleSpaceUsedPerDay=[] #array to store the acccessible spaces taken for all 14 day
generalSpaceUsedPerDay=[]#array to store the general spaces taken for all 14 days
totalNumberSpacesUsedPerDay=[]#array to store the spaces used for all 14 days
for x in range(0,15): #loop through above arrays and add zero fro days 1 to 14
    accessibleSpaceUsedPerDay.append(0)
    generalSpaceUsedPerDay.append(0)
    totalNumberSpacesUsedPerDay.append(0)
totalAccessibleSpacesUsed=0 #variable to add up all the accessible spaces used over 14 days
totalGeneralSpacesUsed=0 #variable to add up all the general spaces used over 14 days
totalNumberSpacesUsed=0 #variable to add up all the spaces used over 14 days
y=0 #variable that will store index of a parking space
d=0 # the  will temporarily hold the day of the booking status
for x in parkingStatus: #loop through the parking status tand store in x
    if x!="Available":
        totalNumberSpacesUsed=totalNumberSpacesUsed+1
    if y>=0 and y<5 and x!="Available":
        d=0
       # print(parkingStatus[y]," ",parkingSpace[y], " day ",str(d+1))
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif y<20 and x!="Available":
        d=0
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=20 and y<25 and x!="Available":
        d=1
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif y>=25 and y<40 and x!="Available":
        d=1
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=40 and y<45 and x!="Available":
        d=2
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=45 and y<60 and x!="Available":
        d=2
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=60 and y<65 and x!="Available":
        d=3
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif y>=65 and y<80 and x!="Available":
        d=3
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=80 and y<85 and x!="Available":
        d=4
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=85 and y<100 and x!="Available":
        d=4
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=100 and y<105 and x!="Available":
        d=5
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=105 and  y<120 and x!="Available":
        d=5
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=120 and y<125 and x!="Available":
        d=6
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=125 and y<140 and x!="Available":
        d=6
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=140 and y<145 and x!="Available":
        d=7
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=145 and y<160 and x!="Available":
        d=7
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=160 and y<165 and x!="Available":
        d=8
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=165 and y<180 and x!="Available":
        d=8
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=180 and y<185 and x!="Available":
        d=9
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=185 and y<200 and x!="Available":
        d=9
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=200 and y<205 and x!="Available":
        d=10
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=205 and y<220 and x!="Available":
        d=10
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=220 and y<225 and x!="Available":
        d=11
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=225 and y<240 and x!="Available":
        d=11
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=240 and y<245 and x!="Available":
        d=12
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=245 and y<260 and x!="Available":
        d=12
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    if y>=260 and y<265 and x!="Available":
        d=13
        accessibleSpaceUsedPerDay[d]=accessibleSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalAccessibleSpacesUsed=totalAccessibleSpacesUsed+1
    elif  y>=265 and y<280 and x!="Available":
        d=13
        generalSpaceUsedPerDay[d]=generalSpaceUsedPerDay[d]+1
        totalNumberSpacesUsedPerDay[d]=totalNumberSpacesUsedPerDay[d]+1
        totalGeneralSpacesUsed=totalGeneralSpacesUsed+1
    y=y+1 #increase to the next index(parking space)

for x in range(1,15):
    if x<15:
        print("The number of Accessible spaces used on day ",str(x)," is ",accessibleSpaceUsedPerDay[x-1])
        print("The number of General spaces used on day ",str(x)," is ",generalSpaceUsedPerDay[x-1])
        print("The total number of spaces used on day ",str(x),' is ', totalNumberSpacesUsedPerDay[x-1])
print("The number of accessible spaces used in the whole 14-day period is ",totalAccessibleSpacesUsed)
print("The number of general spaces used in the whole 14-day period is ",totalGeneralSpacesUsed)   
print("The total number of spaces used in the whole 14-day period is ", totalNumberSpacesUsed)
