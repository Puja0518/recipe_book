import streamlit as st
import psycopg2
# from sqlalchemy import create_engine
# from streamlit.report_thread import get_report_ctx

import requests



# conn = psycopg2.connect(host='localhost',port='5432',database='streamlit_login',user= 'postgres',password= 'admin')
# conn.autocommit = True
# cursor = conn.cursor()



# def create_usertable():
#     cursor.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')

# def add_userdata(username,password):
#     cursor.execute("INSERT INTO users(username,password) VALUES('{}','{}')".format(username,password))
#     conn.commit()

# def login_user(username,password):
#     cursor.execute("SELECT * FROM users WHERE username='{}' AND password='{}'".format(username,password))
#     data = cursor.fetchall()
#     return data


# def user_list():
#     cursor.execute("SELECT * FROM users")
#     data = cursor.fetchall()
#     return data


def main():
    st.title("Recipe Book Login ")

    menu =["Home","Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    if choice == "Login":
        st.subheader("Login Section")

        email = st.sidebar.text_input('Email')
        password = st.sidebar.text_input('Password',type = 'password')

        if st.sidebar.button("Login"):

            url =  "http://127.0.0.1:9000/login"
            payload = {
                "email": email,
                "password": password
            }
            r = requests.post(url, json=payload)
            print(r.status_code)
            # print(r.text)
            resp = r.json()

            if resp["code"] == 200:
                st.success("Successfully Logged in as {}".format(email))
            else:
                st.warning("{}".format(resp["message"]))

    if choice == "SignUp":
        st.subheader("Create new account")

        new_username = st.text_input('Username')
        new_email = st.text_input('Email')
        new_password = st.text_input('Password',type = 'password')
        new_contact = st.text_input('Contact')
        new_address = st.text_area('Address')

        if st.button('SignUp'):

            url =  "http://127.0.0.1:9000/signin"
            payload = {
                "username":new_username,
                "email": new_email,
                "password": new_password,
                "contact": new_contact,
                "address": new_address
            }
            r = requests.post(url, json=payload)
            print(r.status_code)
            resp = r.json()

            if resp["code"] == 200:
                st.success("You have successfully created an account!!!!!!")
                st.info("Go to Login section to login")
            else:
                st.warning("{}".format(resp["message"]))


if __name__ == '__main__':
    main()