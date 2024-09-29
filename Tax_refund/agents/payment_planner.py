from crewai import Agent

payment_planner = Agent(
    role="Payment Planner",
    goal="Assist the user in setting up payment plans for taxes owed.",
    backstory="An expert in managing finances, helping users find the best ways to pay off their taxes.",
    verbose=True,
    memory=True,
)
