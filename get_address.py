import requests
import pandas as pd

# Client ID와 Client Secret 설정
client_id = "Useyours"
client_secret = "****"



# 헤더에 추가
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
}


# 변환하고자 하는 주소
def write_address(address):
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # 'addresses' 키가 있는지 확인
        if 'addresses' in data and data['addresses']:
            address_data = data['addresses'][0]
            latitude = address_data['y']  # 위도
            longitude = address_data['x']  # 경도
            return latitude, longitude
    return None, None



df = pd.read_csv('Knowledge_Center.csv', encoding="CP949")
ds = pd.read_csv('my_result.csv', encoding="CP949")


for index, address in df['소재지지번주소'].items():
    # 'write_address' 함수를 사용하여 위도와 경도를 얻습니다.
    latitude, longitude = write_address(address)
    print(latitude, longitude)
    # 'A'와 'B' 열에 위도와 경도를 각각 저장합니다.
    ds.at[index, 'A'] = latitude
    ds.at[index, 'B'] = longitude
    print(latitude, longitude)
    ds.to_csv('result1.csv', index=False)    
# 변경된 데이터프레임의 현재 상태를 CSV 파일에 저장합니다.














# 먼저, 'A'와 'B' 열을 데이터프레임에 추가합니다.
# 이는 초기에 모든 값이 NaN인 열을 생성합니다.

# # ExcelWriter 객체를 사용하여 엑셀 파일 생성/업데이트
# with pd.ExcelWriter('result.csv', engine='openpyxl', mode='w') as writer:
#     for index, address in df['소재지지번주소'].items():
#         # 'write_address' 함수를 사용하여 위도와 경도를 얻습니다.
#         latitude, longitude = write_address(address)
        
#         # 'A'와 'B' 열에 위도와 경도를 각각 저장합니다.
#         df.at[index, 'A'] = latitude
#         df.at[index, 'B'] = longitude
        
#         # 변경된 데이터프레임의 현재 상태를 엑셀 파일에 저장합니다.
#         # 여기서는 각 반복마다 전체 데이터프레임을 쓰므로, 이전 데이터를 덮어쓰게 됩니다.
#         # 이는 데이터를 받을 때마다 엑셀에 쓰기를 원하는 경우에 적합한 방법입니다.
#         df.to_csv(writer, index=False)



# # 위도와 경도를 저장할 리스트
# latitudes = []
# longitudes = []

# for i in df['소재지지번주소']:
#     # 각 행의 주소를 함수에 전달하여 위도와 경도를 얻음
#     latitude, longitude = write_address(i)
#     # 얻은 위도와 경도를 리스트에 추가
#     latitudes.append(latitude)
#     longitudes.append(longitude)
#     ds["A"]=latitudes
#     ds["B"]=longitudes
#     ds.to_csv('test1.csv')
# 리스트를 이용해 최종 데이터프레임 생성
# ds["A"]=latitudes
# ds["B"]=longitudes

# 결과 데이터프레임을 CSV 파일로 저장
# ds.to_csv('test1.csv')

# 4. 데이터프레임 저장
# ds.to_csv("test.csv")
