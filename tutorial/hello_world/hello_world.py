import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Load environment variables from .env file
load_dotenv()

async def main() -> None:
    """Simple example demonstrating an AI assistant saying 'Hello World!'."""
    
    # Initialize the OpenAI client with configuration
    client = AzureOpenAIChatCompletionClient(
        model=os.getenv("MODEL_NAME"),
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version=os.getenv("API_VERSION"),
        api_key=os.getenv("AZURE_API_KEY")
    )

    # Create and run the assistant agent
    agent = AssistantAgent("assistant", client)
    response = await agent.run(task="Say 'Hello World! And solve 2+3'")
    await asyncio.sleep(0.0005)  # Wait for 0.5ms
    print(response)


if __name__ == "__main__":
    asyncio.run(main())