import streamlit as st

from database import (
    add_user,
    login_user,
    user_exists
)


# ---------------- LOGIN ---------------- #

def login_page():

    st.title("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    login_btn = st.button("Login")

    if login_btn:

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.authenticated = True

            st.session_state.username = username

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )


# ---------------- SIGNUP ---------------- #

def signup_page():

    st.title("📝 Signup")

    username = st.text_input(
        "Create Username"
    )

    password = st.text_input(
        "Create Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    signup_btn = st.button("Signup")

    if signup_btn:

        if user_exists(username):

            st.error(
                "Username already exists"
            )

        elif password != confirm_password:

            st.error(
                "Passwords do not match"
            )

        elif len(password) < 4:

            st.error(
                "Password must be at least 4 characters"
            )

        else:

            success = add_user(
                username,
                password
            )

            if success:

                st.success(
                    "Account Created Successfully"
                )

                st.info(
                    "Go to Login Page"
                )

            else:

                st.error(
                    "Signup Failed"
                )


# ---------------- LOGOUT ---------------- #

def logout():

    st.session_state.authenticated = False

    st.session_state.username = ""

    st.rerun()