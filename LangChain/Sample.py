import numpy as np
import os

from langchain.llms import OpenAI

from langchain.agents import AgentType, initialize_agent, load_tools


os.environ['OPENAI_API_KEY']=''

llm=OpenAI(temperature=0.6)

text = "Which cricket team won IPL?"
print(llm(text))

tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

resultr=agent.run("when was Elon musk born? What is his age right now in 2023?")

print(resultr)   


#msg = "Roll a dice"
#print(msg)

#print(np.random.randint(1,9))
