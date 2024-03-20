# 세계 최고의 스마트 스위치
![switch image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/113657807/3f9b8017-81a0-4a49-ba8a-426bc93dd1f0)
## 프로젝트 소개
**쾌적한 강의환경을 위한 스마트 스위치 제작**
- 강의실 내 환경 데이터를 실시간 측정
- 서보모터를 활용하여 스위치 원격 제어
- 사용자에게 실시간 강의실 환경데이터 제공

## 시스템 구성
![Screenshot from 2024-03-13 13-27-29](https://github.com/addinedu-ros-4th/iot-repo-6/assets/157962186/f81c89c4-7104-4c0f-aacf-7c4f0fdefd57)

## 팀원 소개 및 역할
|구분|이름|역할|
|---|---|---|
|팀장|송용탁|통신 (Wifi, Serial), MCU GUI 연동, 하드웨어 제작, 프로세스 총괄|
|팀원|임대환|모터 작동 테스트 및 원격제어 알고리즘 구성, 하드웨어 제작, 회로 설계, 딥러닝 (객체인식)|
|팀원|양혜경|MCU GUI 연동, DB 설계, Query 작성, 음성인식, RFID 인식|
|팀원|장하린|GUI(PyQt), 제작 및 작동 테스트 진행|

## 기능리스트
||기능|설명|
|---|---|---|
|1|리모컨 스위치 제어|IR을 이용하여 스위치 원격 제어|
|2|강의실 환경 측정|온습도 센서, 공기질 센서로 센서값 측정 후 DB저장|
|3|GUI- RFID 등록|GUI에서 RFID 관리자 등록 |
|4|GUI- RFID 인증|GUI에서 등록된 관리자 태그 시 인증 확인 후 DB저장|
|5|GUI- 스위치 제어|GUI에서 버튼 클릭 시 스위치 제어|
|6|GUI- 센서 값 모니터링|GUI에서 실시간 센서 값 모니터링|
|7|통신|아두이노-PC (Serial 통신), ESP32-PC(Wifi 통신)|
|8|음성인식|STT를 통한 음성인식 후 스위치 제어|
|9|GUI- 카메라|카메라 버튼 클릭 시 웹캠 화면 표시|
|10|GUI- DB조회|콤보박스, SQL을 이용한 DB조회|

## 기술스택 
### 개발환경 
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Arduino](https://img.shields.io/badge/arduino-00878F?style=for-the-badge&logo=arduino&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=Qt&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)
### 언어 
![C++](https://img.shields.io/badge/c++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
### DBMS
![Mysql](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
### 커뮤니케이션 
![Slack](https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

## 영상
### 1. 리모컨 원격제어
[![Video Label](http://img.youtube.com/vi/vmIu6hCUOD0/0.jpg)](https://youtu.be/vmIu6hCUOD0)

### 2. GUI 제어
[![Video Label](http://img.youtube.com/vi/HrK0cDhgM44/0.jpg)](https://youtu.be/HrK0cDhgM44)

### 3. 음성인식
[![Video Label](http://img.youtube.com/vi/0gaTNLKtJvw/0.jpg)](https://youtu.be/0gaTNLKtJvw)

## 구성 
### 하드웨어 구성도 (스위치)
![Screenshot from 2024-03-14 14-49-28](https://github.com/addinedu-ros-4th/iot-repo-6/assets/157962186/7daa4fdf-db7b-4a73-9496-0c7b09f7e53f)
### 하드웨어 구성도 (센서, RFID)
![Screenshot from 2024-03-14 14-51-42](https://github.com/addinedu-ros-4th/iot-repo-6/assets/157962186/52963895-7be9-448c-b53b-3c9e26e26df3)
### 소프트 웨어 구성도 ( 추가예정 )
![Screenshot from 2024-03-14 16-00-39](https://github.com/addinedu-ros-4th/iot-repo-6/assets/157962186/4b4ba14d-27cb-464d-be5c-0541981431a9)
### DB
##### iot_project
* 공기질 센서, 온도 센서, 습도 센서, 현재 시간 정보 저장
<br>

##### rfid_cards
* 카드 ID, 사용자 이름, 현재 시간 정보 저장
<br>

![image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/113657807/80e5dc77-c411-4a3b-877a-fc4769e6a789)
<br>
### GUI
![image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/113657807/e3cf8b80-db44-4d88-8757-d7f224069227)

