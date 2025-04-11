import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key


def get_subtasks(prompt):
    """Generates sub-tasks for a given task prompt using the OpenAI API."""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,  # Adjust this value based on desired subtask detail level
        n=5,  # Number of subtasks to generate
        temperature=0.7,  # Control randomness for diverse subtasks
    )

    return response.choices[0].text.strip().split("\n")


def dspy2joth(dspy_file):
    """Converts a .dspy file into JOTH format."""

    tasks = []

    with open(dspy_file, "r") as f:
        for line in f:
            if line.startswith("Task"):
                task_id, title = line[4:].strip().split(":")
                subtasks = get_subtasks(f"Decompose the '{title}' task into a list of sub-tasks.")

                tasks.append({
                    "id": int(task_id),
                    "title": title,
                    "subTasks": subtasks
                })

    return {"tasks": tasks}


if __name__ == "__main__":
    dspy_file = "reasoning_questions.dspy"  # Update this with your .dspy file path
    joth_data = dspy2joth(dspy_file)

    with open("reasoning_questions_joth.json", "w") as f:
        json.dump(joth_data, f, indent=4)

    print(f"Converted {dspy_file} to JOTH format and saved as reasoning_questions_joth.json")
