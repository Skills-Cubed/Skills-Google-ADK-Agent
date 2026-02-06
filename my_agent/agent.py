from google.adk.agents import Agent

root_agent = Agent(
    name="my_agent",
    model="gemini-2.0-flash",
    description="A simple helpful assistant.",
    instruction="You are a helpful assistant. Answer user questions clearly and concisely.",
)
