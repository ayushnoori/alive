import streamlit as st
import sqlite3
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelWithHeads
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from dotenv import load_dotenv
from monsterapi import client as mclient
import json

# get monster api key
load_dotenv()
api_key = os.getenv('API_KEY')
# print(api_key)

deploy_client = mclient(api_key = api_key)
status_ret = deploy_client.get_deployment_status("ac86ae4b-be46-4b46-9227-98a40c3fe006")
print(status_ret)


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
        weight_lbs = st.number_input("Weight (pounds)", min_value=0.0, format="%.2f")
        weight_kg = round(weight_lbs / 2.205, 2)
        pre_existing_conditions = st.text_area("Pre-existing health conditions")
        current_medications = st.text_area("Current medications")
        submit_button = st.form_submit_button("Submit")
        
        # if we click the button, let's construct the prompt for the LLM.
        if submit_button:

            system_prompt = "You are an expert drug development scientist and biomedical researcher studying drugs that can promote longevity and extend healthspan. You must answer an important question. Generate a response that answers this question."

            prompt = f"###Question: I am a {age} year old {sex.lower()} with a height of {feet}'{inches}\" ({height_cm} cm) and a weight of {weight_lbs} lbs ({weight_kg} kg). I have the following pre-existing health conditions: {pre_existing_conditions}. I am currently taking the following medications: {current_medications}. Given my demographic information and relevant medical history, please suggest the 5 most promising small molecule drugs that could be used to improve my longevity and increase my healthspan.\n\n###Response:"
            
            st.write("Constructed prompt for LLM:")
            st.write(prompt)

            assert status_ret.get("status") == "live", "Please wait until status is live!"

            service_client = mclient(api_key = status_ret.get("api_auth_token"), base_url = status_ret.get("URL"))

            payload = {
                "input_variables": {"system": system_prompt,
                    "prompt": prompt},
                "stream": False,
                "temperature": 0.6,
                "max_tokens": 512
            }

            output = service_client.generate(model = "deploy-llm", data = payload)

            if payload.get("stream"):
                for i in output:
                    print(i[0])
            else:
                print(json.loads(output)['text'][0])

            # # TODO: actually pass this into the LLM API to query the LLM
            # tokenizer = AutoTokenizer.from_pretrained("ayushnoori/alive")
            # model = AutoModelWithHeads.from_pretrained("ayushnoori/alive")
            # # model = AutoModelForSeq2SeqLM.from_pretrained("ayushnoori/alive")
            
            # st.write("LLM Response:")
            # for i, output in enumerate(outputs):
            #     line = tokenizer.decode(output, skip_special_tokens=True)
            #     st.write(f"Option {i+1}: {line}")

            # model_name = "ayushnoori/alive"
            # tokenizer = AutoTokenizer.from_pretrained(model_name)
            # model = AutoModelForCausalLM.from_pretrained(model_name)

            # input_ids = tokenizer(prompt, return_tensors="pt").input_ids
            # output_sequences = model.generate(input_ids, max_length=250, num_return_sequences=5, temperature=0.7)

            # # Decode and display the generated sequences
            # for i, generated_sequence in enumerate(output_sequences):
            #     text = tokenizer.decode(generated_sequence, skip_special_tokens=True)
            #     st.write(f"## Suggestion {i+1}")
            #     st.write(text)


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
