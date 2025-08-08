""" Intial code was generated using a local model on an airplane, this will be
updated with a more recent model"""

import json
from dotenv import load_dotenv
import openai
import os


load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key


def get_subtasks(prompt):
    """Generates sub-tasks for a given task prompt using the OpenAI API."""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,  # Adjust this value based on desired subtask detail level
        n=5,  # Number of subtasks to generate
        temperature=0.7,  # Control randomness for diverse subtasks
    )

    return response.choices[0].text.strip().split("\n")


def task_to_ots(task_description):
    """Converts a natural language description into OTS format."""

    title = "Task Description"

    subtasks = get_subtasks(f"Decompose the following task into a list of sub-tasks:\n\n{task_description}")

    return {
        "id": 1,
        "title": title,
        "subTasks": subtasks
    }


if __name__ == "__main__":
    task_description = input("Enter a natural language description of the complex task: ")
    ots_data = task_to_ots(task_description)

    with open("task_ots.json", "w") as f:
        json.dump(ots_data, f, indent=4)

    print(f"Converted task description to OTS format and saved as task_ots.json")
