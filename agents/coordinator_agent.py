"""
Coordinator Agent

Responsible for orchestrating the complete
loan settlement workflow.
"""

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage

from llm.azure_openai import AzureOpenAIClient
from config.prompts import COORDINATOR_PROMPT
from agents.data_collection_agent import data_collection_agent


class CoordinatorAgent:

    def __init__(self):
        self.model_client = AzureOpenAIClient.get_client()
        self.agent = AssistantAgent(
            name="CoordinatorAgent",
            model_client=self.model_client,
            system_message=COORDINATOR_PROMPT,
        )

    async def load_customer(self, customer_id: str):
        message = TextMessage(content=f"Load customer {customer_id}", source="Coordinator")
        response = await data_collection_agent.on_messages([message], cancellation_token=None)
        return response.chat_message.content

    async def start(self, customer_id: str):
        customer_context = await self.load_customer(customer_id)
        return customer_context
