import streamlit as st

def main():
    st.header("Learning Streamlit")
    name = st.text_input('enter your name')

    col1,col2 = st.columns(2,gap = 'small')

    with col1:
        if st.button('Display my name',type='primary',key='btn1',width = 'stretch'):
            print('hi ',name)
    with col2:
        if st.button('Display my name',type='secondary',key='btn2',width=300):
            print('bye',name)
    st.markdown("""
    HI
    """)
    st.markdown("""
        <style>
            button{
                background:orange !important;
            }
            </style>
    """,unsafe_allow_html=True)

main()
