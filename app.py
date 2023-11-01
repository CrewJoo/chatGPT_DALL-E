import streamlit as st
import openai

# openai.api_key = "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"

# streamlit 시크릿 키 활용
openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

# user_input = st.text_input("Prompt")
# st.write(user_input)

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")
   
if submit and user_input:  
    # st.write(user_input)
    
    # gpt에게 시스템 역할을 주고, 인풋에 입력된 것을 구체적으로 상상하고, 대답은 간단히 하라고 지시함
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appereance of the input. Response it shortly around 20 words."
    }]
    
    # gpt 프롬프트에 추가해줌, 역할은 사용자, 
    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })
    
    # 스피너 넣기
    with st.spinner("Waiting for ChatGPT..."):
    
    
    
        # gpt 사용버전
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt 
        )
    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
    
    # st.write(prompt)

    # 스피너 넣기
    with st.spinner("Waiting for DALL-E..."):
        
    # dall-e 호출
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )
        
    # 오픈ai api 다큐멘테이션 참조
    # dalle_response["data"][0]["url"]
    
    st.image(dalle_response["data"][0]["url"])
    