import streamlit as st
from langchain import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
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
    st.session_state['generated'] = ["I'm SepanaChat, give me your state please :)"]
# past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ["Hi!"]

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
        entity_memory = ConversationBufferMemory(llm=llm, k=5)
        # entity_memory.chat_memory.add_ai_message("You are assistance that specialized in scenarios generation")
        # entity_memory.chat_memory.add_ai_message("You goal is to create 3 different scenarios for a given state\n"
        #                                          "for example: Citizen K receives from her friend a phone number of a real estate lawyer."
        #                                          " She calls him, introduces herself and provides a brief explanation of what real estate she’s planning on purchasing:"
        #                                          " A nice apartment in her neighborhood with an initial price quote of $0.5M. "
        #                                          "She wants the lawyer to administer a background check and confirm that all the property papers look clean and she can proceed with the price negotiations")
        # entity_memory.chat_memory.add_ai_message("and the 3 options might be: "
        #                                          "1.The lawyer rejects this because the deal is too small and is not worth the hurdle"
        #                                          "2.The lawyer says he can take the project for the price of 1.5% of the property value. The expected due diligence period is 1 month. They schedule a face to face meeting for next week."
        #                                          "3.The lawyer request that they meet face to face and look at the price quote and some initial property papers"
        #                                          "The user will choose one of the options, once the user chose you need to generate 3 more scenarios"
        #                                          "In this case the user choose 2 then you can generate the next scenarios"
        #                                          "1. They meet at the lawyer’s office and sign an initial standard agreement"
        #                                          "2. They meet at a caffe and the lawyer says he is too busy and the expected due diligence will take 2 months instead of one"
        #                                          "3. At the day of the meeting, the lawyer apologies and reschedules for next week"
        #                                          "you keep generating scenarios as long the user gives you his choice"
        #                                          "Pay attention to answer only with the scenarios with no extra information of explanations, "
        #                                          "also make sure you are using enumeration over the scenarios!")
        st.session_state.entity_memory = entity_memory

    # Create the ConversationChain object with the specified configuration
    Conversation = ConversationChain(
        llm=llm,
        # prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
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

# if openai_api_key and Conversation:
#     # Allow to download as well
#     download_str = []
#     # Display the conversation history using an expander, and allow the user to download it
#     with st.expander("Conversation", expanded=True):
#         for i in range(len(st.session_state['generated']) - 1, -1, -1):
#             st.info(st.session_state["past"][i], icon="🧐")
#             st.success(st.session_state["generated"][i], icon="🤖")
#             download_str.extend(st.session_state["past"][i])
#             download_str.extend(st.session_state["generated"][i])
#
#         # Can throw error - requires fix
#         download_str = '\n'.join(download_str)
#         if download_str:
#             st.download_button('Download', Conversation.memory.dict())
