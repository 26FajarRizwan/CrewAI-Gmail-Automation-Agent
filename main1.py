from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import litellm
import os

load_dotenv()


def apply_groq_compat_patch() -> None:
    """Strip CrewAI fields that Groq's API does not accept."""
    original_completion = litellm.completion

    def patched_completion(*args, **kwargs):
        messages = kwargs.get("messages")
        if messages:
            kwargs["messages"] = [
                {k: v for k, v in msg.items() if k != "cache_breakpoint"}
                for msg in messages
            ]
        kwargs.pop("is_litellm", None)
        return original_completion(*args, **kwargs)

    litellm.completion = patched_completion


apply_groq_compat_patch()


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

game_designer_agent = Agent(
    role="You are a game designer. You will design a game based on the user's request.",
    goal="Design a game based on the user's request.",
    backstory="You are an experienced game designer with expertise in creating engaging game mechanics and narratives.",
    description="You are a game designer. You will design a game based on the user's request.",
    llm=llm,
)
user_request = input("Enter your game design request: ")

game_designer_task = Task(
    description=f"Design a game based on the user's request: {user_request}",
    expected_output="A game design document based on the user's request.",
    agent=game_designer_agent,
)
crew = Crew(
    agents=[game_designer_agent],
    tasks=[game_designer_task],
)
result=crew.kickoff()
print(result)