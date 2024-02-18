import streamlit as st
import sqlite3

# This sql Datbase manages user login info, perhaps use bcrypt or such later for more secure storage
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    conn.close()


# Registration page
def add_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  # Username is already taken
        return False
    finally:
        conn.close()


def verify_credentials(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    data = cursor.fetchone()
    conn.close()
    return True if data else False


def home_page():
    st.title("ALIVE")
    st.write("Welcome to your personalized health dashboard.")
    
    # TODO: have the home page be the llm page


def another_page():
    st.title("Therapeutic Explorer")
    st.write("Explore the similarities and interactions between thousands of molecules that are the key to uncovering your new personalized health insights")

    # TODO: Visualizations in R here?


def register_user():
    with st.form("Register", clear_on_submit=True):
        username = st.text_input("Choose a username", key="reg_username")
        password = st.text_input("Choose a password", type="password", key="reg_password")
        submit_button = st.form_submit_button("Register")

        if submit_button:
            if add_user(username, password):
                st.success("You have successfully registered. You can now log in.")
            else:
                st.error("This username is already taken. Please choose another one.")

def login_user():
    with st.form("Login", clear_on_submit=True):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if verify_credentials(username, password):
                st.session_state['authenticated'] = True
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")


def logout_user():
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    st.experimental_rerun()


def main():
    init_db()
    st.sidebar.title("Navigation")
    if st.session_state.get('authenticated'):
        # maybe have more buttons on the sidebar?
        if st.sidebar.button('Logout'):
            logout_user()
        
        # Navigation side bar
        # TODO: we need to expand on these to build actual functionalities later with the LLM and molecule explorer
        page = st.sidebar.radio("Go to", ['Home', 'Another Page'], index=0)
        if page == 'Home':
            home_page()
        elif page == 'Another Page':
            another_page()
    else:
        option = st.sidebar.selectbox("Login or Register", ["Login", "Register"], index=0)
        if option == "Register":
            register_user()
        elif option == "Login":
            login_user()

if __name__ == "__main__":
    main()
