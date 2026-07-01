"""
Azure OpenAI Model Client for AutoGen
"""

import os

from dotenv import load_dotenv
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient


load_dotenv()


class AzureOpenAIClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = AzureOpenAIChatCompletionClient(
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                model=os.getenv("AZURE_OPENAI_MODEL"),
            )
        return cls._client
