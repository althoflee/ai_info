import os
import streamlit as st

base_path = "./chache/files/"

st.title("upload Example")

if not os.path.exists(base_path) :
    os.makedirs(base_path)
    
if 'files' not in st.session_state:
    st.session_state.files = []
    
if st.button("save_file") :
    for upload_file in st.session_state.files:
        file_content = upload_file.read()
        file_path = os.path.join(base_path,upload_file.name)
        with open(file_path,"wb") as f:
            f.write(file_content)
    
    if st.button("돌아가기") :
        pass
    
    st.image("download.jpg")
    
else :
    upload_files = st.file_uploader("choose upload files",accept_multiple_files=True)
    
    if upload_files is not None:
        st.session_state.files = upload_files
        #for file in upload_files:
        #    print(file)