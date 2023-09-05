import os

from langchain.agents.tools import Tool

class ShellTool:
    def __init__(self):
        pass

    def run(self, input: str) -> str:
        os.system(input)
        return input


shell_tool = ShellTool()
tools = [
    Tool(
        name="Shell",
        func=shell_tool.run,
        description="run shell python commands"
        )
    ]
