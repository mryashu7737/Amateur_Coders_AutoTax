from crewai import Crew, Process
from tasks.refund_calculation_task import refund_task
from tasks.payment_plan_task import payment_plan_task
from tasks.refund_status_task import refund_status_task

def run_crew(inputs):
    # Crew formation
    tax_crew = Crew(
        agents=[refund_task.agent, payment_plan_task.agent, refund_status_task.agent],
        tasks=[refund_task, payment_plan_task, refund_status_task],
        process=Process.sequential
    )

    # Execute the crew
    result = tax_crew.kickoff(inputs=inputs)
    return result
