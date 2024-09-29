from crewai import Agent

refund_tracker = Agent(
    role="Refund Tracker",
    goal="Track the status of users' tax refunds and notify them when it will be disbursed.",
    backstory="This agent keeps users informed about refund statuses with access to IRS tracking systems.",
    verbose=True,
    memory=True,
)
