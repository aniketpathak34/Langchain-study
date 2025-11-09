import random
from abc import ABC, abstractmethod


class Runnables(ABC):
    @abstractmethod
    def invoke(input_method):
        pass


class NakliLLM(Runnables):
    def __init__(self):
        print("LLM Created")

    def invoke(self, prompt):
        response_list = [
            "Mentos Zindagi Mein Kuch Meetha Ho Jaaye!",
            "Mentos: The Freshmaker!",
            "Chew Mentos, Feel the Freshness!",
        ]
        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        response_list = [
            "Mentos Zindagi Mein Kuch Meetha Ho Jaaye!",
            "Mentos: The Freshmaker!",
            "Chew Mentos, Feel the Freshness!",
        ]

        return {"response": random.choice(response_list)}


class NakliPromptTemplate(Runnables):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


class NakliStrOutputParser(Runnables):

    def invoke(self, input_date):
        return input_date.get("response", "")


class RunnableConnector(Runnables):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            print("Running:", runnable.__class__.__name__)
            print("Input Data:", input_data)
            input_data = runnable.invoke(input_data)
        return input_data


# llm = NakliLLM()
# parser = NakliStrOutputParser()

# template = NakliPromptTemplate(
#     template= "what the longitude and latitude of {place}?",
#     input_variables= ["place"]
# )

# chain = RunnableConnector([template, llm, parser])
# output = chain.invoke({"place": "India"})
# print(output)


# example 2 where we gonna create two big chains to connect together

# todo
#    create a one chain which will generate joke on a topic
#     create another chain which will summarize the joke and explain the joke
#     connect both chains together


llm = NakliLLM()
parser = NakliStrOutputParser()

template1 = NakliPromptTemplate(
    template="tell me a funny joke on the topic: {topic}",
    input_variables=["topic"]
)

template2 = NakliPromptTemplate(
    template="Summarize the following joke and explain why it's funny: {response}",
    input_variables=["response"]
)

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])
response = final_chain.invoke({'topic': 'cricket'})

print("Explanation:", response)