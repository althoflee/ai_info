# session
import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0

#counter = 0

if st.button("increase") :
    #counter = counter+1
    st.session_state.counter += 1

st.write(f" counter : {st.session_state.counter}" )
    
