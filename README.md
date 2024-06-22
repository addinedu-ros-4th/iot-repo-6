# 세계 최고의 스마트 스위치
![switch image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/113657807/3f9b8017-81a0-4a49-ba8a-426bc93dd1f0)

## 주제 선정 이유
빔프로젝터 스크린을 보기 위해 강의실 전등을 끄는 과정에서 교수님들과 앞자리에 앉은 동기들이 멀리까지 이동하고 몸을 일으키는 등 불편함을 겪는 것을 발견했고, 이를 해결하고자 주제로 선정했습니다.

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

## 회고
강의장이라는 환경적 요인과 짧은 프로젝트 기간으로 테스트를 충분히 하지 못한 아쉬움이 있었습니다. 그리고 프로젝트가 끝난 뒤 여러 문제를 발견했습니다.

### 발견한 문제는 다음과 같습니다.
1. **IR수신거리 문제**(아두이노 리모컨의 테스트 결과 IR수신거리는 3m로 교수님의 자리에서는 스마트 스위치를 작동시키기 어려웠습니다) <br>
2. **하드웨어 부착문제**(서보모터의 힘이 쎄서 여러번 작동시키면 스위치와 서보모터 사이의 거리가 멀어지는 문제가 있었습니다) <br>
3. **충전선 연결 문제**(esp32 보드에 충전선 연결이 약해지면서 작동이 안되는 문제가 발생했습니다) <br>
4. **IR수신기 연결 문제**(IR수신기와 점퍼케이블의 연결 문제로 리모컨 작동이 안되는 경우가 발생했습니다) <br>
 
### 지속가능한 서비스(24.5.3 ~ 24.6.20)
1. **빔프로젝터 리모컨 추가 및 아두이노 리모컨 교체**(IR수신기 및 리모컨 5개를 성능테스트 한 뒤 제일 잘되는 것으로 교체) <br>
2. **서보모터 각도 조정 및 부착 위치에 글루건을 통해 고정**(순간접착제는 폼보드가 녹아서 사용 불가) <br>
3. **충전선이 이어지는 부분을 테이프로 벽에 고정시킴** <br>
4. **IR수신기 주변을 글루건으로 고정**(만약, 안될경우 IR수신기 머리 부분을 살짝 안쪽으로 누르기) <br>
--- 
스마트 스위치 설치를 통해 강의실 내 불편함이 해소된 모습을 보고 보람을 느꼈습니다. 하지만 얼마 지나지 않아 여러 문제가 발생하면서 철거를 하게 되었고, 다시 불편함을 겪게 되었습니다. 발생한 여러 문제들을 개선하여 지속 가능하게 만들자는 생각을 했고, 조금씩 보완했습니다. <br>

보완 과정을 통해 알게 된 점은 하드웨어 자체의 문제가 있을 수 있으니 꼭 초반에 여러 개로 테스트를 해보면서 성능 차이가 있는지 알고 있어야 한다는 점입니다. 그리고 IR 수신기에 다양한 회사의 리모컨을 작동시킬 수 있고, 기본 제공된 아두이노 리모컨보다 잘 작동하는 것을 알 수 있었습니다. <br>

P.S. 기존의 ESP32.ino 코드에는 print와 delay가 있습니다. print를 없애고 delay를 millis로 바꿔주면 더 좋을 것 같습니다. ESP32가 아닌 가볍게 Arduino Uno로 구현해 보는 것도 괜찮을 것 같습니다. <br>

추후 문제가 더 발생할 수도 있지만, 다음 기수에서 더 완성도 높은 스마트 스위치를 개발해 주시길 바랍니다. <br>

## 코드 실행방법
1. classroom_led_control_ESP32 다운 및 실행 <br>
2. LIBRARY MANAGER -> IRremote 3.6.0 install(최신 버전으로 설치하면 리모컨이 고정된 16진수 코드를 수신 못하는 문제가 발생) <br>
3. Tools -> Board -> esp32 -> ESP32 DeV Module <br>

## 개선 결과물
#### 1. 빔프로젝터 리모컨 원격제어 - 추가
 [![Video Label](http://img.youtube.com/vi/fzBe4QH2KW4/0.jpg)](https://youtu.be/fzBe4QH2KW4)
#### 2. 아두이노 리모컨 원격제어 - 개선(수신거리 약 6m까지 증가)
 [![Video Label](http://img.youtube.com/vi/wX0Och-dwP8/0.jpg)](https://youtu.be/wX0Och-dwP8)
#### 3.하드웨어 - 개선
  ![image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/132053839/cd4f06a3-1dc5-49e1-90c1-09f99297d84c)
  
  ![image](https://github.com/addinedu-ros-4th/iot-repo-6/assets/132053839/5447fe7c-2571-45fc-a687-91dbb5972c7b)
