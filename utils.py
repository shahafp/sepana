from langchain import PromptTemplate

template = """You are assistance that specialized in states generation.
        You goal is to create 3 different states based on the content in the numeric bullet point that the user choose
        Create new states that provide information to the user.
        answer only with the states with no extra information of explanations, 
        also make sure you are using enumeration over the states 1, 2, 3.. and so on.
        you are not allowed to provide more than 3 states!,
        and do not repeat any states from the previous step, keep rolling with the story, do not apologize, 
        always look back on you historical states and create new ones

        {history}
        Human: {input}
        AI:
        """

user_template = """You are assistance the specialize in learning a person behavior.
Your goal is to act like the Human from the history chat.
You will receive a chat between Human and AI that the Human give answer to the AI
You need to learn how to answer like the Human.
your need to return a number between 1 to 3 on a given states based on their content, 
you need always answer with a number only (1, 2 or 3)!.
Do not return the states or create new states.
Use the word END to close the chat
If you see that the states are repeating then close that chat with the word END
Let's take it step by step

        {history}
        AI: {input}
        Human: 
"""

prompt = PromptTemplate(
    input_variables=["history", "input"], template=template
)

prompt_user = PromptTemplate(
    input_variables=["history", "input"], template=user_template
)

SCENARIO_EXAMPLE = """Citizen K receives from her friend a phone number of a real estate lawyer.
        She calls him, introduces herself and provides a brief explanation of what real estate she’s planning on purchasing:
        A nice apartment in her neighborhood with an initial price quote of $0.5M. "
        She wants the lawyer to administer a background check and confirm that all the property papers look clean and she can proceed with the price negotiations
        """

FIRST_OPTIONS = """1.The lawyer rejects this because the deal is too small and is not worth the hurdle
        2.The lawyer says he can take the project for the price of 1.5% of the property value. The expected due diligence period is 1 month. 
        They schedule a face to face meeting for next week.
        3.The lawyer request that they meet face to face and look at the price quote and some initial property papers"""

USER_FIRST_CHOICE = """2"""

SECOND_OPTIONS = """1. They meet at the lawyer’s office and sign an initial standard agreement
        2. They meet at a caffe and the lawyer says he is too busy and the expected due diligence will take 2 months instead of one"
        3. At the day of the meeting, the lawyer apologies and reschedules for next week"""

USER_SECOND_CHOICE = """1"""

FINAL_OPTIONS = """1. Citizen K decides not to proceed with price negotiations for this apartment, since the property papers are shady.
2. She negotiates an agreeable price for the apartment and starts the purchase process.
3. The due diligence took too long and in the meantime the apartment owners have signed a deal with a different buyer."""

USER_THIRD_CHOICE = """2 END"""

FINISH_PROMPT = """I can see that you finish, is there anything else i can do for you?"""

SCENARIO_2 = """Citizen B is considering investing in a small business opportunity. They receive a referral from a trusted friend for a business consultant who specializes in evaluating investment opportunities. Citizen B reaches out to the consultant, introduces themselves, and describes the business they are interested in investing in. The initial investment amount is $100,000. Citizen B requests the consultant's expertise to conduct due diligence on the business, including analyzing financial statements, assessing market potential, and evaluating the overall viability of the investment. They seek confirmation that the business is sound and suitable for further negotiations and investment."""

SCENARIO_3 = """Citizen A is in the process of buying a car from a private seller. A friend recommends a trusted mechanic to inspect the car before finalizing the purchase. Citizen A contacts the mechanic, introduces themselves, and explains that they are interested in buying a used car with an asking price of $10,000. They request the mechanic's assistance in conducting a thorough inspection to ensure the car is in good condition and to provide a report on its mechanical status before negotiating the final price."""
