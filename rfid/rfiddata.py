import serial
import time
import mysql.connector

# MySQL 연결 설정
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "0320",
    "database": "rfid"
}

# 시리얼 통신 설정
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# 이전 UID 저장 변수
previous_UID = ""

# MySQL 연결
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

try:
    while True:
        # 시리얼 데이터 읽기
        ser.flushInput()  # 시리얼 입력 버퍼 비우기
        serial_data = ser.readline().decode('utf-8').strip()

        # 데이터가 유효하면 출력
        if serial_data:
            if "UID:" in serial_data:
                # UID 데이터 추출
                card_UID = serial_data.split("UID:")[1].strip()

                # 이전 UID와 다를 때만 출력 및 MySQL에 추가
                if card_UID != previous_UID:
                    print("Card UID:", card_UID)

                    # MySQL에 추가
                    query = "INSERT INTO rfid_cards (card_uid) VALUES (%s)"
                    values = (card_UID,)
                    cursor.execute(query, values)
                    connection.commit()

                    previous_UID = card_UID

        time.sleep(0.1)  # 루프 사이에 적절한 지연 추가

except KeyboardInterrupt:
    # 프로그램 종료 시 시리얼 포트와 MySQL 연결 종료
    ser.close()
    cursor.close()
    connection.close()