# Python code to split a list of two element  
# at a time and insert it into excel. 
  
# Importing pandas as pd 
import pandas as pd 
  
# List initialization 
station = [
    "BS", 0 ,10 ,20, 
30, 40, 50,60, 70, "BS", 80 ,90, 100, 110, 120, 130, 140, "BS", 150, 160, 170, 180, 190, 200, "BS"
] 

time = [
"15:48", "16:01", "16:09", "16:16", "16:22", "16:27", "16:33", "16:40", "16:45", "16:52", "16:49", "17:10", "17:18", "17:24", "17:30", "17:35", "17:50", "17:57", "18:05", "18:14", "18:21", "18:26", "18:32", "18:38", "18:50"
]

elevation = [
    158.90,1045.60,1403.80,144.80,145.60,148.10,147.80,147.8,149.1,149.8,149.8,149.8,152.6,153.1,151.8,149.6,145.6,145.6,155.3,152.3,152.3,152.3,150.6,151.3,152.3,151.8,151.8
]

averageReading = [
    1474.28,1474.30,1474.26,1474.34,1474.43,1474.43,1474.41,1474.58,1474.55,1474.43,1474.66,1474.73,1474.83,1474.94,1474.94,1474.49,1474.53,1474.53,1475.27,1475.39,1457.44,1475.57,1475.64,1475.74,1475.54
]

changeinTime = [
    0,13,21,28,34,39,45,52,57,64,61,82,90,96,102,107,122,129,137,146,153,158,164,170,182
]

driftCorrection = [
    0,0.0899,0.1453,0.1937,0.2352,0.2698,0.3114,0.3944,0.4428,0.4221,0.5674,0.6228,0.6643,0.7058,0.7404,0.8442,0.8926,0.9480,1.0103,1.0587,1.0933,1.1348,1.1764,1.2594
]

changeinElevation = [
    0,886.7,1244.9,-14.1,-13.2,-10.8,-11.1,-11.1,-9.8,-9.1,-9.1,-9.1,-6.3,-5.8,-7.1,-9.3,-13.3,-3.6,-6.6,-6.6,-8.3,-7.6,-7.6,-7.1,-7.1
]

gCorrected = [
    1414.28,1474.210,1474.1147,1474.1436,1474.1948,1474.1602,1474.0986,1474.2262,1474.1556,1473.9872,1474.2379,1474.1626,1474.2072,1474.2757,1474.2342,1474.7496,1473.6858,1473.6374,1474.322,1474.3797,1474.3813,1474.4717,1474.5052,1474.5736,1474.2806
]

FAC = [
    0,273.635,384.176,-4.351,-4.104,-3.333,-3.425,-3.425,-3.024,-2.808,-2.808,-2.808,-1.944,-1.789,-2.191,-2.869,-4.104,-1.110,-2.036,-2.036,-2.561,-2.345,-2.345,-2.191,-2.191
]

BC = [
    0,99.221,139.304,-1.577,-1.488,-1.208,-1.242,-1.242,-1.242,-1.096,-1.018,-1.018,-1.018,-0.704,-0.649,-0.794,-1.041,-1.488,-0.403,-0.738,-0.738,-0.928,-0.850,-0.850,-0.794,-0.794
]

BA = [
    -976646.64, -976472.294,-977646.686,-976649.546,-976649.339,-976648.883,-976649.002,-976648.881,-976648.690,-976648.721,-976648.470,-976648.545,-976647.951,-976647.782,-976648.081,-976648.996,-976649.848,-976647.988,-976647.894,-976647.836,-976648.169,-976647.936,-976647.908,-976647.751,-976648.034
]

df = pd.DataFrame() 
  
# Creating two columns 
df['Staion'] = station[0::] 
df['Time'] = time[0::]
df['Elevation'] = elevation[0::]
df['averageReading'] = averageReading[0::]
df['changeinTime'] = changeinTime[0::]
df['driftCorrection'] = driftCorrection[0::]
df['changeinElevation'] = changeinElevation[0::]
df['gCorrected'] = gCorrected[0::]
df['FAC'] = FAC[0::]
df['BC'] = BC[0::]
df['BA'] = BA[0::]
  
# Converting to excel 
df.to_excel('result.xlsx', index = False) 
