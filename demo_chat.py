# import re
#
# from langchain import ConversationChain
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
#
# import utils
#
# llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo-0613', openai_api_key='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')
# llm_user = ChatOpenAI(temperature=0.7, model='gpt-3.5-turbo-0613', openai_api_key='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')
#
# memory = ConversationBufferMemory()
#
# memory.chat_memory.add_user_message(utils.SCENARIO_EXAMPLE)
# memory.chat_memory.add_ai_message(utils.FIRST_OPTIONS)
# memory.chat_memory.add_user_message(utils.USER_FIRST_CHOICE)
# memory.chat_memory.add_ai_message(utils.SECOND_OPTIONS)
# memory.chat_memory.add_user_message(utils.USER_SECOND_CHOICE)
# memory.chat_memory.add_ai_message(utils.FINAL_OPTIONS)
# memory.chat_memory.add_user_message(utils.USER_THIRD_CHOICE)
#
# memory_2 = ConversationBufferMemory()
#
# conversation = ConversationChain(
#     llm=llm,
#     prompt=utils.prompt,
#     verbose=True,
#     memory=memory
# )
#
# conversation_2 = ConversationChain(
#     llm=llm_user,
#     verbose=True,
#     memory=memory_2,
#     prompt=utils.prompt_user
# )
#
# scenario = ""
# for scen in [utils.SCENARIO_2, utils.SCENARIO_3]:
#     while True:
#         user_input = input('Enter you message ')
#         if user_input == 'start':
#             user_input = scen
#         memory_2.chat_memory.add_user_message(user_input)
#         if re.search(r"\bend\b", user_input, re.IGNORECASE):
#             break
#         pred = conversation.predict(input=user_input)
#         memory_2.chat_memory.add_ai_message(pred)
#         print(pred)
#     print("New Scenario")
#
# ai_input = scen
# memory_2.chat_memory.add_user_message("This is the end of the Human examples, "
#                                       "pay attention when the Human ended the chats, now it is your time to shine and answer like you are the Human")
#
# while True:
#     ai_input = conversation.predict(input=ai_input)
#
#     ai_input = conversation_2.predict(input=ai_input)
#
#     if re.search(r"\bend\b", ai_input, re.IGNORECASE):
#         print('finish', ai_input)
#         break
#     print(ai_input)
