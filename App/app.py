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
    st.markdown("""
    ## Welcome to ALIVE Health Dashboard
    Welcome to your personalized health dashboard. Here's where we start our journey towards better health together.
    """, unsafe_allow_html=True)
    
    with st.form("patient_info", clear_on_submit=False):
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])
        feet = st.slider("Height (feet)", min_value=0, max_value=7, step=1)
        inches = st.slider("Height (inches)", min_value=0, max_value=11, step=1)
        total_inches = feet * 12 + inches
        height_cm = round(total_inches * 2.54, 2)
        weight_lbs = st.number_input("Weight (in pounds)", min_value=0.0, format="%.2f")
        weight_kg = round(weight_lbs / 2.205, 2)
        pre_existing_conditions = st.text_area("Pre-existing health conditions")
        current_medications = st.text_area("Current medications")
        submit_button = st.form_submit_button("Submit")
        
        # if we click the button, let's construct the prompt for the LLM.
        if submit_button:
            prompt = f"Given the patient’s demographic information and relevant medical history, please suggest a supplement regimen that could be used to increase the health longevity of the patient.\n\n" \
                     f"Age: {age}\n" \
                     f"Sex: {sex}\n" \
                     f"Height: {feet}'{inches}\" (or {height_cm} cm)\n" \
                     f"Weight: {weight_lbs} lbs (or {weight_kg} kg)\n" \
                     f"Pre-existing conditions: {pre_existing_conditions}\n" \
                     f"Current medications: {current_medications}"
            
            st.write("Constructed Prompt for LLM:")
            st.write(prompt)

            # TODO: actually pass this into the LLM API to query the LLM

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

    st.set_page_config(
        page_title="ALIVE Health Dashboard",
        page_icon=":heart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


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
