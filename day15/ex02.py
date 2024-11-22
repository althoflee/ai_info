import streamlit as st

prompt = st.chat_input("궁금한것 물어보세요")

editor_text = st.text_area("추가적인 프롬프트",key="editor1",value="default text")


if prompt:
    print(prompt)    
    st.text(f'당신은 방금 {prompt} 말씀했어요.')