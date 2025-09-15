"""
NEURAL INTERFACE v2.1.3
Advanced AI Communication Protocol
Direct OpenAI API Integration - No Dependencies
"""

import streamlit as st
import openai
from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 페이지 설정
st.set_page_config(
    page_title="NEURAL INTERFACE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS 스타일
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #0a0a0a 0%, #1a1a1a 50%, #000000 100%);
        color: #00ff00;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        border: 2px solid #00ff00;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
        font-family: 'Courier New', monospace;
    }
    .chat-container {
        background-color: #0d1117;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #30363d;
    }
    .user-message {
        background-color: #161b22;
        border-left: 4px solid #00ff00;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: #f0f6fc;
        font-family: 'Courier New', monospace;
    }
    .bot-message {
        background-color: #0d1117;
        border-left: 4px solid #ff6b35;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: #f0f6fc;
        font-family: 'Courier New', monospace;
    }
    .sidebar-content {
        background-color: #161b22;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    .metric-card {
        background-color: #0d1117;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 255, 0, 0.1);
        margin: 0.5rem 0;
        border: 1px solid #30363d;
        color: #f0f6fc;
    }
    .terminal-text {
        color: #00ff00;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
    }
    .warning-text {
        color: #ff6b35;
        font-family: 'Courier New', monospace;
    }
    .success-text {
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

# API 키 설정 (Streamlit Secrets 또는 환경 변수에서 가져오기)
import os

# Streamlit Secrets에서 API 키 가져오기 (Streamlit Cloud용)
try:
    API_KEY = st.secrets["OPENAI_API_KEY"]
except:
    # 백업: 환경 변수에서 가져오기 (로컬 개발용)
    API_KEY = os.getenv("OPENAI_API_KEY", "")

# API 키가 없으면 오류 메시지 표시
if not API_KEY:
    st.error("⚠️ [SYSTEM ERROR] OPENAI_API_KEY not found in secrets or environment variables!")
    st.info("💡 [INFO] Please set OPENAI_API_KEY in Streamlit Cloud secrets or environment variables.")
    st.stop()

# Gmail 설정 (Streamlit Secrets 또는 환경 변수에서 가져오기)
try:
    SENDER_EMAIL = st.secrets["GMAIL_USER"]
    SENDER_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]
except:
    # 백업: 환경 변수에서 가져오기 (로컬 개발용)
    SENDER_EMAIL = os.getenv("GMAIL_USER", "yoonwhan0@gmail.com")
    SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "ewiyxncttelrokiw")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    st.session_state.client = openai.OpenAI(api_key=API_KEY)

def add_message(role, content):
    """메시지를 세션 상태에 추가"""
    st.session_state.messages.append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

def send_email(recipient_email, subject, body):
    """Gmail을 통해 이메일 전송"""
    try:
        # SMTP 서버 설정
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # 이메일 메시지 생성
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = f"[NEURAL INTERFACE] {subject}"
        
        # 메시지 본문 추가
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # SMTP 서버 연결 및 이메일 전송
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, recipient_email, text)
        server.quit()
        
        return True, "✅ [SUCCESS] Email transmitted successfully via neural network."
        
    except Exception as e:
        return False, f"❌ [ERROR] Email transmission failed: {str(e)}"

def parse_email_request(user_input):
    """사용자 입력에서 이메일 전송 요청을 파싱"""
    email_keywords = ["메일 보내줘", "메일 보내줄래", "메일", "이메일", "email", "mail", "보내", "send", "전송", "transmit"]
    
    if any(keyword in user_input.lower() for keyword in email_keywords):
        # 간단한 이메일 정보 추출 (정규식 사용)
        import re
        
        # 이메일 주소 추출
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, user_input)
        
        # 이메일 주소가 있으면 해당 주소로, 없으면 기본 주소로
        recipient = emails[0] if emails else "yoonwhan0@gmail.com"
        
        return {
            "action": "send_email",
            "recipient": recipient,
            "subject": "NEURAL INTERFACE Transmission",
            "body": f"AI Generated Message: {user_input}"
        }
    
    return None

def get_chat_response(user_input):
    """OpenAI API를 사용하여 응답 생성"""
    try:
        # 시스템 메시지와 대화 기록 준비
        messages = [
            {"role": "system", "content": "You are an advanced AI neural interface with email transmission capabilities. When users say '메일 보내줘' or '메일 보내줄래?' or similar email requests, you MUST send an email immediately. You have access to Gmail SMTP (yoonwhan0@gmail.com) for secure email transmission. Use professional, technical language with cyberpunk/hacker aesthetic. Always confirm email transmission with technical terminology."}
        ]
        
        # 최근 10개 메시지만 포함
        recent_messages = st.session_state.messages[-10:] if len(st.session_state.messages) > 10 else st.session_state.messages
        for msg in recent_messages:
            messages.append({"role": msg["role"], "content": msg["content"]})
        
        # 사용자 입력 추가
        messages.append({"role": "user", "content": user_input})
        
        # OpenAI API 호출
        response = st.session_state.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

def main():
    """메인 애플리케이션"""
    # 커스텀 헤더
    st.markdown('''
    <div class="main-header">
        <h1>⚡ NEURAL INTERFACE v2.1.3</h1>
        <p class="terminal-text">[SYSTEM] Advanced AI Communication Protocol Active</p>
        <p class="warning-text">[WARNING] Unauthorized access detected. Proceed with caution.</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # 사이드바
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown('<h3 class="terminal-text">[CONTROL PANEL]</h3>', unsafe_allow_html=True)
        
        # 대화 기록 초기화 버튼
        if st.button("💀 PURGE MEMORY", type="secondary"):
            st.session_state.messages = []
            st.markdown('<p class="success-text">[SUCCESS] Memory banks cleared. All traces eliminated.</p>', unsafe_allow_html=True)
            st.rerun()
        
        st.markdown("---")
        st.markdown('<h4 class="terminal-text">[SYSTEM SPECS]</h4>', unsafe_allow_html=True)
        st.markdown("""
        <div class="terminal-text">
        - **NEURAL ENGINE**: GPT-3.5-turbo Core<br>
        - **MEMORY BANK**: Persistent conversation storage<br>
        - **REAL-TIME PROTOCOL**: Live communication interface<br>
        - **EMAIL TRANSMISSION**: Gmail SMTP integration<br>
        - **LANGUAGE SUPPORT**: Multi-lingual neural processing<br>
        - **SECURITY LEVEL**: MAXIMUM
        </div>
        """, unsafe_allow_html=True)
        
        # 대화 통계
        if st.session_state.messages:
            st.markdown("---")
            st.markdown('<h4 class="terminal-text">[NEURAL ACTIVITY]</h4>', unsafe_allow_html=True)
            user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
            bot_messages = len([msg for msg in st.session_state.messages if msg["role"] == "assistant"])
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<div class="metric-card"><h4 class="terminal-text">👤 HUMAN</h4><h2 style="color: #00ff00;">{user_messages}</h2></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-card"><h4 class="terminal-text">⚡ AI</h4><h2 style="color: #ff6b35;">{bot_messages}</h2></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 채팅 인터페이스
    chat_container = st.container()
    
    with chat_container:
        # 이전 메시지들 표시
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                st.caption(f"⏰ {message['timestamp']}")
        
        # 사용자 입력
        if prompt := st.chat_input("[NEURAL INTERFACE] Enter command..."):
            # 사용자 메시지 추가 및 표시
            add_message("user", prompt)
            with st.chat_message("user"):
                st.markdown(prompt)
                st.caption(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
            
            # 이메일 전송 요청 확인
            email_request = parse_email_request(prompt)
            
            # 챗봇 응답 생성
            with st.chat_message("assistant"):
                with st.spinner("⚡ [NEURAL PROCESSING] Analyzing input..."):
                    response = get_chat_response(prompt)
                    
                    # 이메일 전송 요청이 있으면 처리
                    if email_request:
                        st.markdown(response)
                        st.caption(f"⚡ {datetime.now().strftime('%H:%M:%S')} [NEURAL RESPONSE]")
                        
                        # 이메일 전송 실행
                        with st.spinner("📧 [EMAIL TRANSMISSION] Establishing secure connection..."):
                            success, email_result = send_email(
                                email_request["recipient"],
                                email_request["subject"],
                                email_request["body"]
                            )
                            
                            if success:
                                st.success(email_result)
                                response += f"\n\n{email_result}"
                            else:
                                st.error(email_result)
                                response += f"\n\n{email_result}"
                    else:
                        st.markdown(response)
                        st.caption(f"⚡ {datetime.now().strftime('%H:%M:%S')} [NEURAL RESPONSE]")
                
                # 챗봇 응답을 메시지에 추가
                add_message("assistant", response)

if __name__ == "__main__":
    main()
