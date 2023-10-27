import streamlit as st
from TodoDAO2 import TodoDAO2
# streamlit run main_streamlit.py

def main():
    dao = TodoDAO2("todos_db.db")
    st.set_page_config(layout='wide')
    st.title('Test Streamlit')
    st.write("Hello **world** !")
    st.write("``` a =2 ```")
    title = st.text_input('Movie title', 'Life of Brian')
    if st.button('Show movie'):
        st.write('The current movie title is', title)    
    st.table(dao.find_all())

if __name__ == '__main__':
    main()
