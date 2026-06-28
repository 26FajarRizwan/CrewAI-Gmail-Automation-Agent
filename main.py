import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
load_dotenv()

llm = LLM(model="gemini/gemini-2.5-flash",
          api_key=os.environ.get("GEMINI_API_KEY"),
          )

game_designer = Agent(
    role="Game Designer Developer",
    goal="Create a text-based game that is engaging and fun to play using python that will use the pygame library.",
    backstory="The Game Designer is responsible for creating the concept, rules, and structure of the game.They will design the gameplay mechanics, challenges, and overall experience for the player."
)

game_developer = Task(
    description="The Game Developer is responsible for implementing the game design created by the Game Designer. They will write the code, create the graphics, and ensure that the game functions properly.",
    expected_output="A fully functional text-based game implemented in Python using the Pygame library.",
    agent=game_designer

)

crew = Crew(
    agents=[game_designer],
    tasks=[game_developer],
    llm=llm

)

result = crew.kickoff()
print(result)
