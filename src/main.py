import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain import (
    OpenAI,
    PromptTemplate,
)
from langchain.utilities import SQLDatabase
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentType
from langchain.agents.tools import Tool
from langchain.chains import LLMChain
from langchain.agents import initialize_agent

# from langchain.tools import ShellTool
from tools import tools
from prompt_templates import web_prompts
load_dotenv()

class DotEnv(TypedDict):
    OPENAI_API_KEY: str

settings: DotEnv = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
}
OPENAI_API_KEY = settings["OPENAI_API_KEY"]


if __name__ == "__main__":
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, model="text-davinci-003")

    # shell_tool = ShellTool()
    # tools = [
    #     Tool(
    #         name="Shell",
    #         func=shell_tool,
    #         description="run shell commands"
    #     ),
    # ]

    agent_chain = initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent_chain.run(input=web_prompts, chat_history={"chat_history"})

    # prompt = PromptTemplate(template=template)
    # db = SQLDatabase.from_uri("sqlite:///todos.db")
    # db_chain = SQLDatabaseChain(llm=llm, database=db, prompt=prompt)
    # db_chain.run("Develop a webpage that shows the total number of page views. Make sure to store this value because we need to show the total number of views when a new person joins")

    # agent_executor = create_sql_agent(llm=OpenAI(temperature=0, model="text-davinci-003"), db=db, verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    # agent_executor.run()
