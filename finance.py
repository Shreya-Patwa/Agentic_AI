from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

def Build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(),DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
        # debug_mode=True
    )

agent=Build_agent()

agent.print_response("Use given Tools whenever possible.Share the NVDA stock price and analyst recommendations")
