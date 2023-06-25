import streamlit as st
import pandas as pd
import numpy as np

from calc import matcal

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
}
.title{
margin-top:-100px;
}
</style>""",
unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.header('Assignment Problem')
st.markdown("""---""")
col1,col2=st.columns(2)

with col1:
    rows = st.slider('Enter number of Rows:', min_value=1, max_value=10, value=0, step=1)
with col2:
    cols = st.slider('Enter number of Columns:', min_value=1, max_value=10, value=0, step=1)

st.markdown("""
<style>
    button.step-up {display: none;}
    button.step-down {display: none;}
    div[data-baseweb] {border-radius: 4px;}
    }
</style>""",
unsafe_allow_html=True)

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows,gap="medium")
    return grid


try:
    if (rows==0 and cols==0):
        st.write("Enter columns and rows to create a matrix.")
    elif (rows==0):
        st.write("Enter rows to create a matrix.")
    elif (cols==0):
        st.write("Enter columns to create a matrix.")
    else:
        mygrid = make_grid(rows,cols)
except:
  pass


l=[]
l1=[]
for i in range(rows):
    for j in range(cols):
        a=mygrid[i][j].number_input(":",key=(i*10+j),label_visibility="collapsed",value=0,step=0)
        l.append(a)
    l1.append(l)   
    l=[]

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.markdown("""---""")  
maxmin = st.radio(
    "Select",
    ('Maximum', 'Minimum'),label_visibility="collapsed")
    
if maxmin == 'Maximum':
    x=1
else:
    x=0

st.markdown(
    """
<style>
body{
    text-align:center;
}
div.stButton > button:first-child { 
height: 3em;
width: 42em; 
}</style>
""",
    unsafe_allow_html=True,
)

submit=st.button("Submit")

al=[]
if submit:
    try:
        ans=matcal(l1,x,int(rows),int(cols))
        st.write("Allocations")
        for i in ans:
            al.append(i[0])
        st.table(al)
        col=ans[2][0][0]
        row=ans[2][0][1]
        tc=0
        for i in range(len(ans)):
            col=ans[i][0][0]
            row=ans[i][0][1]
            tc=tc+l1[col-1][row-1]
        st.write("Total Cost:",tc)


    except:
        pass
    


