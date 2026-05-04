import streamlit as st

def footer_home():
    

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; items-align:center; justify-content:center">
        <p style="font-weight:bold; color:white"> Created with 💖 by </p>
        <p style="font-weight:bold; color:#8B0000"> Ritik kumar chhitrolia </p>        
        </div>
                
                """,unsafe_allow_html=True)
    

def footer_dashboard():
    

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; items-align:center; justify-content:center">
        <p style="font-weight:bold; color:black"> Created with 💖 by </p>
        <p style="font-weight:bold; color:#8B0000"> Ritik kumar chhitrolia </p>        
        </div>
                
                """,unsafe_allow_html=True)