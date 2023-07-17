import streamlit as st
from langchain.llms import OpenAI
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

st.title('🦜🔗 Sepana Home Assigment')

with st.sidebar:
    st.title('🤗💬 SepanaChat App')
    add_vertical_space(5)
    st.write('Made with ❤️ by Shahaf Pariente')
    openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Generate empty lists for generated and past.
# generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm SepanaChat, How may I help you?"]
# past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.empty()
# input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()


# User input
# Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if input_text and openai_api_key.startswith('sk-'):
        return input_text


# Applying the user input box
with input_container:
    user_input = get_text()


# Response output
# Function for taking user prompt as input followed by producing AI generated responses
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm(input_text)


# Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        input_container.empty()

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))


