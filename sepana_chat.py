import streamlit as st
from langchain import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
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

if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []

# Layout of input/response containers
# input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

if openai_api_key.startswith('sk-'):
    # Create an OpenAI instance
    llm = OpenAI(temperature=0,
                 openai_api_key=openai_api_key,
                 model_name='gpt-3.5-turbo',
                 verbose=False)

    # Create a ConversationEntityMemory object if not already created
    if 'entity_memory' not in st.session_state:
        st.session_state.entity_memory = ConversationEntityMemory(llm=llm, k=5)

    # Create the ConversationChain object with the specified configuration
    Conversation = ConversationChain(
        llm=llm,
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        memory=st.session_state.entity_memory
    )
else:
    st.markdown(''' 
        ```
        - 1. Enter API Key + Hit enter 🔐 

        - 2. Ask anything via the text input widget

        Your API-key is not stored in any form by this app. However, for transparency ensure to delete your API once used.
        ```

        ''')
    st.sidebar.warning('API key required to try this app.The API key is not stored in any form.')


# Function for taking user provided prompt as input
def get_text():
    # input_text = st.text_input("You: ", "", key="input")
    input_text = st.chat_input()
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if input_text and openai_api_key.startswith('sk-'):
        return input_text


# Applying the user input box
with st.container():
    user_input = get_text()


# Response output
# Function for taking user prompt as input followed by producing AI generated responses
def generate_response(input_text):
    return Conversation.run(input=input_text)


# Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

if openai_api_key:
    # Allow to download as well
    download_str = []
    # Display the conversation history using an expander, and allow the user to download it
    with st.expander("Conversation", expanded=True):
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            st.info(st.session_state["past"][i], icon="🧐")
            st.success(st.session_state["generated"][i], icon="🤖")
            download_str.extend(st.session_state["past"][i])
            download_str.extend(st.session_state["generated"][i])

        # Can throw error - requires fix
        download_str = '\n'.join(download_str)
        if download_str:
            st.download_button('Download', Conversation.memory.dict())
