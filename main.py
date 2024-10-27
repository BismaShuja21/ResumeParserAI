# main.py
import streamlit as st
from modules.users import process_user_mode
from modules.recruiters import process_recruiters_mode

def main():
    st.set_page_config(page_title="Resume Parser", page_icon="✅")

    # Sidebar
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose an option", ["Users", "Recruiters"])

    if app_mode == "Users":
        process_user_mode()

    elif app_mode == "Recruiters":
        process_recruiters_mode()

if __name__ == "__main__":
    main()
