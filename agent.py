from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()

def Build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        instructions="You are helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent=Build_agent()

agent.print_response("Is it safe to travel UAE today?")
