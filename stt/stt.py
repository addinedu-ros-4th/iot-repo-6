import speech_recognition as sr

# 마이크에서 오디오 소스 생성
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말해보세요!")  # 사용자에게 메시지 출력
    audio = r.listen(source)

# 구글 웹 음성 API를 사용하여 음성 인식 (일일 50회 제한)
try:
    recognized_text = r.recognize_google(audio, language='ko')
    print("Google 음성 인식이 인식한 내용: " + recognized_text)

    # 인식된 텍스트를 개별 문자로 리스트에 저장
    character_list = list(recognized_text)
    print("개별 문자:", character_list)

    # 리스트에서 특정 단어 확인 후 출력
    if "불" in character_list and "꺼" in character_list:
        print("안녕하세요")
        print(character_list)
        
except sr.UnknownValueError:
    print("Google 음성 인식이 오디오를 이해하지 못했습니다.")
except sr.RequestError as e:
    print("Google 음성 인식 서비스에서 결과를 요청할 수 없습니다; {0}".format(e))

# 오디오를 WAV 파일로 저장
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
