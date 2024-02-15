import pandas as pd
import mysql.connector
# MySQL 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root", # 사용자 이름
    password="password", # 비밀번호
    database="2024SparcsHackathon" # 데이터베이스 이름
)

def add_stations():

    # # CSV 파일 읽기
    df = pd.read_csv("new_concatenated_routes.csv")
    # 데이터프레임의 열 데이터 형식 변환
    # 필요한 열 선택
    df_subset = df[['BUS_NODE_ID','latitude','longitude','stopname']]

    # Relation_Routes_Stations 테이블에 데이터 추가
    cursor = conn.cursor()
    q = 'DESC Stations'
    cursor.execute(q)
    print(cursor.fetchall())

    for i, row in df_subset.iterrows():
        print(row['BUS_NODE_ID'])
        sql = "select * from Stations where station_id = %s"
        val = (row['BUS_NODE_ID'],)
        # 쿼리 실행
        cursor.execute(sql, val)
        if cursor.fetchall() == []:
            # SQL 쿼리 생성
            sql = "INSERT INTO Stations (station_id, name, latitude, longitude) VALUES (%s, %s, %s, %s)"
            val = (row['BUS_NODE_ID'],row['stopname'],row['latitude'],row['longitude'])
            # 쿼리 실행
            print(f"INSERT INTO Stations ('station_id','name','latitude','longitude') VALUES ({row['BUS_NODE_ID']},{row['stopname']},{row['latitude']},{row['longitude']})")
            cursor.execute(sql, val)

    # 변경 사항 커밋
    conn.commit()

    # 연결 종료
    conn.close()

def add_routes():
    # CSV 파일 읽기
    df = pd.read_csv("routes.csv")
    # 데이터프레임의 열 데이터 형식 변환
    # 필요한 열 선택
    df_subset = df[['route_id','name']]

    # Relation_Routes_Stations 테이블에 데이터 추가
    cursor = conn.cursor()
    q = 'DESC Routes'
    cursor.execute(q)
    print(cursor.fetchall())

    for i, row in df_subset.iterrows():
        print(i)
        sql = "select * from Routes where route_id = %s"
        val = (row['route_id'],)
        # 쿼리 실행
        cursor.execute(sql, val)
        if cursor.fetchall() == []:
            # SQL 쿼리 생성
            sql = "INSERT INTO Routes (route_id, name) VALUES (%s, %s)"
            val = (row['route_id'],row['name'])
            # 쿼리 실행
            cursor.execute(sql, val)

    # 변경 사항 커밋
    conn.commit()

    # 연결 종료
    conn.close()

def add_rel_route_station():
    # CSV 파일 읽기
    df = pd.read_csv("new_concatenated_routes.csv")
    # 데이터프레임의 열 데이터 형식 변환
    # 필요한 열 선택
    df_subset = df[['route_id','BUS_NODE_ID']]
    origin_route = -1
    route_count = 0

    # Relation_Routes_Stations 테이블에 데이터 추가
    cursor = conn.cursor()
    for i, row in df_subset.iterrows():
        if origin_route == row['route_id']:
            route_count = 0
            origin_route = row['route_id']
        else:
            route_count += 1

        sql = "select * from Relation_Routes_Stations where route_id = %s AND station_id = %s"
        val = (int(row['route_id']), int(row['BUS_NODE_ID']))
        # 쿼리 실행
        print(sql, val)
        cursor.execute(sql, val)
        if cursor.fetchall() == []:
            # SQL 쿼리 생성
            print(sql,val)
            sql = "INSERT INTO Relation_Routes_Stations (route_id, station_id, number) VALUES (%s, %s, %s)"
            val = (int(row['route_id']),int(row['BUS_NODE_ID']), route_count)
            # 쿼리 실행
            cursor.execute(sql, val)

    # 변경 사항 커밋
    conn.commit()

    # 연결 종료
    conn.close()

add_stations()
add_routes()
add_rel_route_station()
