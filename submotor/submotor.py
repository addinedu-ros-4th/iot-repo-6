import socket
import errno

# Arduino의 IP 주소와 포트
arduino_ip = "192.168.0.12"  # 아두이노의 IP 주소로 변경해야 합니다.
arduino_port = 80

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 아두이노에 연결
client_socket.connect((arduino_ip, arduino_port))

while True:
    # 사용자로부터 명령 입력 받기 (l, r, 또는 c)
    command = input("Enter command (l, r, or c): ")

    if command == 'c':
        print("프로그램 종료")
        break

    # 입력받은 명령을 아두이노로 전송
    client_socket.sendall(command.encode())

    # 아두이노에서 받은 응답 출력
    response = client_socket.recv(1024).decode()
    print("Arduino response:", response)
