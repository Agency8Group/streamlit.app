# 🤖 LangChain 간단한 챗봇 프로젝트

이 프로젝트는 LangChain을 사용하여 만든 간단한 챗봇 애플리케이션입니다. LangChain의 기본 기능들을 이해하고 학습할 수 있도록 구성되었습니다.

## 📋 프로젝트 구성

- `simple_chatbot.py`: 콘솔에서 실행하는 기본 챗봇
- `streamlit_app.py`: 웹 인터페이스를 제공하는 Streamlit 애플리케이션
- `config.py`: API 키 및 설정 관리
- `requirements.txt`: 필요한 패키지 목록

## 🚀 설치 및 실행

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 OpenAI API 키를 설정하세요:

```bash
# .env 파일 생성
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### 3. 실행 방법

#### 콘솔 버전 (simple_openai_chatbot.py)
```bash
python simple_openai_chatbot.py
```

#### 웹 버전 (Streamlit)
```bash
streamlit run simple_streamlit_app.py
```

## 🌐 Git 배포 시 주의사항

1. **API 키 보안**: 환경 변수로 관리 (Git에 노출되지 않음)
2. **환경 변수**: 배포 플랫폼에서 `OPENAI_API_KEY` 설정 필요
3. **의존성**: `requirements.txt`에 모든 패키지 포함

### **Streamlit Cloud 배포 방법:**

1. **GitHub에 코드 푸시:**
```bash
git add .
git commit -m "Add NEURAL INTERFACE v2.1.3"
git push origin main
```

2. **Streamlit Cloud에서 배포:**
   - https://share.streamlit.io 접속
   - GitHub 저장소 연결
   - 환경 변수 설정: `OPENAI_API_KEY=your_api_key_here`

3. **배포 완료:**
   - 공개 URL 생성 (예: `https://your-app.streamlit.app`)
   - 인터넷 어디서든 접속 가능

## 🔧 주요 기능

### AI 챗봇 기능
- **OpenAI GPT-3.5-turbo**: 고급 AI 모델 연동
- **실시간 대화**: 즉시 응답 생성
- **대화 기록 관리**: 이전 대화 내용 기억 및 초기화
- **다국어 지원**: 한국어/영어 자연스러운 대화

### 이메일 전송 기능
- **Gmail SMTP**: 안전한 이메일 전송
- **실시간 전송**: 즉시 메일 발송
- **보안 인증**: App Password 사용
- **해커 스타일 UI**: 전문적인 인터페이스

### 사용자 인터페이스
- **웹 인터페이스**: 브라우저에서 대화 (Streamlit)
- **다크 테마**: 해커/사이버펑크 스타일
- **실시간 통계**: 대화 활동 모니터링
- **반응형 디자인**: 모든 기기에서 최적화

## 💡 사용법

### 콘솔 버전
1. `python simple_chatbot.py` 실행
2. 메시지 입력 후 Enter
3. `quit` 또는 `exit`로 종료
4. `clear`로 대화 기록 초기화

### 웹 버전
1. `streamlit run streamlit_app.py` 실행
2. 브라우저에서 자동으로 열리는 페이지에서 대화
3. 사이드바에서 챗봇 초기화 및 대화 기록 삭제 가능

## 🎯 LangChain 학습 포인트

이 프로젝트를 통해 다음 LangChain 개념들을 학습할 수 있습니다:

1. **LLM (Large Language Model) 연동**
   - OpenAI API와의 연결
   - 모델 파라미터 설정 (temperature, model_name)

2. **메모리 관리**
   - ConversationBufferMemory를 통한 대화 기록 저장
   - 메모리 초기화 및 관리

3. **체인 (Chain)**
   - ConversationChain을 통한 대화 흐름 관리
   - 입력과 출력의 연결

4. **메시지 스키마**
   - HumanMessage, SystemMessage 사용
   - 대화 형식의 구조화

## 🔒 보안 주의사항

- API 키는 실제 프로덕션 환경에서는 환경 변수로 관리하세요
- `.env` 파일을 사용하여 API 키를 안전하게 관리할 수 있습니다

## 📚 추가 학습 자료

- [LangChain 공식 문서](https://python.langchain.com/)
- [OpenAI API 문서](https://platform.openai.com/docs)
- [Streamlit 문서](https://docs.streamlit.io/)

## 🛠️ 확장 아이디어

이 기본 프로젝트를 확장하여 다음과 같은 기능들을 추가할 수 있습니다:

- 문서 검색 기능 (RAG - Retrieval Augmented Generation)
- 다양한 메모리 타입 사용 (ConversationSummaryMemory 등)
- 프롬프트 템플릿 활용
- 에이전트 (Agent) 기능 추가
- 벡터 데이터베이스 연동

---

**즐거운 LangChain 학습 되세요! 🎉**
