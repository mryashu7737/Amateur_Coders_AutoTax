from crewai import Crew, Process
from tasks.tax_analysis_task import tax_analysis_task

# Create the crew with both agents
tax_advice_crew = Crew(
    agents=tax_analysis_task.agents,  # Tax Reduction Advisor and Tax Optimization Specialist
    tasks=[tax_analysis_task],
    process=Process.sequential
)

# Function to run tax analysis based on user inputs
def run_tax_analysis(user_data):
    result = tax_advice_crew.kickoff(inputs=user_data)
    return result
