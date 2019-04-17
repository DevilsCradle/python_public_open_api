##해당 코드는 한국 환경공단 국가 대기 오염정보에서 제공하는 시도별 실시간 측정 정보데이터를 조회하는 sample code이다.
##간단하게 json data로 요청하여 받은 응답에서 Data만 출력한다.

import requests
import pandas as pd
import json

##input your key
auth_key = "[your key]"

area = "서울"
pageNum = 1
rowsNum = 20

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName={0}&pageNo={1}&numOfRows={2}&ServiceKey={3}&ver=1.3&_returnType=json".format(area,pageNum,rowsNum,auth_key)

#http request and receive response (data = json type)
response = requests.get(url)
print(response.content)

#json data convert
python_data = json.loads(response.content)
print(python_data)
data = python_data['list']

df = pd.DataFrame(data)
print(df)
