import streamlit as st
import google.generativeai as genai
from PIL import Image

# 웹페이지 설정
st.set_page_config(page_title="통계 AI")
st.title("📊 통계 빈칸 채우기 챗봇")

# 사이드바 API 설정
api_key = st.sidebar.text_input("Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 이미지 업로드
    uploaded_file = st.file_uploader("통계 표 이미지 업로드", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드된 이미지", use_container_width=True)
        
        if st.button("📈 빈칸 채우기 실행"):
            with st.spinner("AI 분석 중..."):
                try:
                    prompt = "이미지의 표 구조를 분석해서 빈칸을 채운 마크다운 표를 출력하고 계산 근거를 알려줘."
                    response = model.generate_content([prompt, image])
                    st.success("완료!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"오류: {e}")
else:
    st.info("💡 왼쪽 사이드바에 구글 API 키를 입력해주세요.")
