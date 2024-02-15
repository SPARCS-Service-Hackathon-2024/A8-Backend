import requests
import xmltodict
import pandas as pd

def xml_to_dict(xml_string):
    # XML 문자열을 딕셔너리로 변환
    xml_dict = xmltodict.parse(xml_string)
    return xml_dict

SERVICEKEY = '/ge1Zxi2zb+ink5lEeeZU3G+AM90G9+5mUPd9U5hMj6MKaVrcjVMdfBI5adHWYfe7nu0nnGT16C8r0IQ6/SLZg=='
def gsbra(page):
    #getStaionByRouteAll
    # url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRouteAll'
    # params ={'serviceKey' : '/ge1Zxi2zb+ink5lEeeZU3G+AM90G9+5mUPd9U5hMj6MKaVrcjVMdfBI5adHWYfe7nu0nnGT16C8r0IQ6/SLZg==', 'reqPage' : '2' }

    ##getRouteInfoAll
    url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getRouteInfoAll'
    params ={'serviceKey' : SERVICEKEY, 'reqPage' : str(page) }

    response = requests.get(url, params=params)
    response.content
    data = xml_to_dict(response.content)['ServiceResult']['msgBody']['itemList']

    df = pd.DataFrame(data)
    return df[['ROUTE_CD', 'ROUTE_NO']]

###routes.csv만들기
# routes = pd.concat([gsbra(1), gsbra(2)], ignore_index=True)
# print(routes)
# # routes DataFrame의 칼럼명 변경
# routes.rename(columns={'ROUTE_CD': 'route_id', 'ROUTE_NO': 'name'}, inplace=True)

# # csv 파일로 저장
# routes.to_csv('routes.csv', index=False)

def gsbr(route_id):
    url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRoute'
    params ={'serviceKey' : SERVICEKEY, 'busRouteId' : route_id }

    response = requests.get(url, params=params)
    data = xml_to_dict(response.content)['ServiceResult']['msgBody']['itemList']

    df = pd.DataFrame(data)

    return df[['ROUTE_CD','BUS_NODE_ID', "GPS_LATI", "GPS_LONG", "BUSSTOP_NM", "BUSSTOP_ENG_NM"]].rename(columns={'ROUTE_CD': 'route_id', 'BUS_STOP_ID': 'name', 'GPS_LATI': 'latitude', 'GPS_LONG': 'longitude',  "BUSSTOP_NM" : 'stopname', "BUSSTOP_ENG_NM": "stopname_eng"})

def gri(route_id):


    url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getRouteInfo'
    params ={'serviceKey' :  SERVICEKEY, 'busRouteId' : route_id}

    response = requests.get(url, params=params)
    data = xml_to_dict(response.content)['ServiceResult']['msgBody']['itemList']
    print(data)
    df = pd.DataFrame([data])
    print(df)
    return df[['ROUTE_CD', 'ROUTE_NO', "ROUTE_TP"]]

import pandas as pd

# concatenated_routes_name.csv 파일 읽기
concatenated_routes = pd.read_csv('concatenated_routes_name.csv')

# subway_station.csv 파일 읽기
subway_stations = pd.read_csv('subway_station.csv', encoding='euc-kr')

# 새로운 열 추가 및 값 할당
subway_stations['route_id'] = 10000001
subway_stations[['route_id', 'BUS_NODE_ID', 'latitude', 'longitude', 'stopname', 'stopname_eng']] = subway_stations[['route_id', '역번호', '위도', '경도', '한 글', '로 마 자']]


# 필요한 열만 선택
subway_stations = subway_stations[['route_id', 'BUS_NODE_ID', 'latitude', 'longitude', 'stopname', 'stopname_eng']]

# 두 데이터프레임 연결
new_concatenated_routes = pd.concat([concatenated_routes, subway_stations], ignore_index=True)

# 새로운 데이터프레임을 CSV 파일로 저장
new_concatenated_routes.to_csv('new_concatenated_routes.csv', index=False)
print(new_concatenated_routes)

# # 기존 데이터 파일 읽기
# routes = pd.read_csv('routes.csv')

# # 새로운 데이터 생성
# new_data = pd.DataFrame({'route_id': [10000001], 'name': ['지하철 1호선']})

# # 새로운 데이터 추가
# routes = pd.concat([routes, new_data], ignore_index=True)

# # 변경된 데이터를 CSV 파일에 씀
# routes.to_csv('routes.csv', index=False)

# #### routes.csv 파일 조절
# # routes.csv 파일을 읽어와서 route_id 값을 추출
# routes = pd.read_csv('routes.csv')
# route_ids = routes['route_id'].tail(20)  # 최대 5개의 route_id 값만 사용
# # print(route_ids[0])
# # print(gsbr(route_ids[0]))
# # route_id 값들에 대한 gsbra 결과를 모두 concat하여 DataFrame으로 만듦
# concatenated_df = pd.concat([gri(str(route_id)) for route_id in route_ids], ignore_index=True)
# print(concatenated_df)
# # csv 파일로 저장
# concatenated_df.to_csv('route_names.csv', index=False)
