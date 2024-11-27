import streamlit as st

testval = "hello "

testval = testval + "python"

print(testval)

st.title("UI Test")
st.text("it is plain text")

if st.button("test Click") :
    st.text("u click button")
    
agree = st.checkbox("I agree?")

if agree : 
    st.write("Agree")
else :
    st.write("not agree")
    
onoff = st.toggle("toggle me")

if onoff:
    st.write("Toggle on")
else :
    st.write("Toggle off")

_radio = st.radio("radio",("A button","B button","C button"))

st.divider()
check1 = st.checkbox("check btn1")
check2 = st.checkbox("check btn2")
st.divider()

age = st.slider("how old are u",0,130,25)
st.write(f"i am {age} years old")

if st.button("ok") :
    print(f"check box value : {check1} , {check2}")
    print(f"radio value {_radio}")
    print(f"toggle {onoff}")
