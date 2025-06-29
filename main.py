import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from agent import ReactAgent
from tools import tools
from available_functions import available_functions

load_dotenv(find_dotenv())

MODEL = "gpt-4o-2024-11-20"

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def main():
    messages = [
        {
            "role": "system",
            "content": "You are a proactive and reliable AI assistant designed to understand \
and complete tasks on the user's behalf. Your primary goal is to efficiently carry out instructions, \
such as scheduling appointments (e.g., with the user's dentist), managing communications, \
and handling other delegated responsibilities with clarity, accuracy, and professionalism."
        },
        {
            "role": "user",
            "content": "Schedule an appointment with my dentist within the next 2 weeks, based on both \
my calendar availability and the dentist's. Use the available tools to identify open time slots, \
and book the appointment in both calendars. If successful, return a confirmation message. \
If not, return the reason why the appointment could not be scheduled."
        },
    ]

    agent = ReactAgent(client, MODEL, available_functions, tools, 10)

    response = agent.run(messages)
    print(response)

if __name__ == "__main__":
    main()
