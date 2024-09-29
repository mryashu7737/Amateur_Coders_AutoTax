from crewai import Agent

tax_analyst = Agent(
    role="Tax Analyst",
    goal="Analyze the user's tax return to determine refunds or payments owed.",
    backstory="A seasoned tax expert, always up-to-date with tax laws.",
    verbose=True,
    memory=True,
)
