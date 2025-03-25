import phi
from phi.playground import Playground, serve_playground_app
from phi.agent import Agent   
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv  

# Set up Groq API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# web search agent
web_search_agent = Agent(
    name="web Search Agent",
    role="Search the web for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions= ["Always include sources"],
    show_tool_calls=True,
    markdown=True
    )

# finacial agent
finance_agent = Agent(
    name="Finance AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True,
                      analyst_recommendations=True,
                      stock_fundamentals=True,
                      company_news=True)],
    instructions=["USe tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

app = Playground(agents=[web_search_agent,finance_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)