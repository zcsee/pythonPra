import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
jsonData1 = '{"data":[{"IP":"1.1.1.1", "SN":2100000202002}],"version":1.0}'
jsonData2 = '{"D":[{"d":"test"}]}'

text = json.loads(jsonData)
# text1 = json.loads(jsonData1)
text1 = json.loads(jsonData2)
print(text1)