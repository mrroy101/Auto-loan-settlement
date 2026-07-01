"""
Data Collection Agent

Reads customer data using CustomerService
and returns a complete NegotiationContext.
"""

from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool

from services.customer_service import CustomerService
from llm.azure_openai import AzureOpenAIClient


customer_service = CustomerService()


def load_customer_data(customer_id: str) -> str:
    """
    Loads customer data and converts it into
    a readable string for downstream agents.
    """
    context = customer_service.load_customer(customer_id)
    return f"""
Customer ID : {context.customer.customer_id}

Customer Name : {context.customer.customer_name}

Vehicle :
{context.vehicle.brand}
{context.vehicle.model}
{context.vehicle.variant}

Outstanding :
₹{context.loan.total_outstanding}

Monthly EMI :
₹{context.loan.emi_amount}

Days Past Due :
{context.days_past_due}

LES :
₹{context.settlement.les}

MID :
₹{context.settlement.mid}

HES :
₹{context.settlement.hes}
"""


load_customer_tool = FunctionTool(load_customer_data, description="Load customer information from Excel.")


data_collection_agent = AssistantAgent(
    name="DataCollectionAgent",
    model_client=AzureOpenAIClient.get_client(),
    tools=[load_customer_tool],
    system_message="""
You are the Data Collection Agent.

Responsibilities

• Load customer data.

• Read Excel.

• Build customer context.

Never negotiate.

Never calculate.

Only provide factual information.
""",
)
