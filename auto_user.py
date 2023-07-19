from langchain import ConversationChain
from langchain.memory import ConversationBufferMemory

import utils

auto_user_memory = ConversationBufferMemory()


def get_conversation_chain(llm):
    return ConversationChain(
        llm=llm,
        verbose=False,
        memory=auto_user_memory,
        prompt=utils.prompt_user
    )
