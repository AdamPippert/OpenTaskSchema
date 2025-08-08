
# **Open Task Schema (OTS) - v0.2 Proposal**

## Overview

The Open Task Schema (OTS) is a flexible schema for representing task hierarchies, supporting diverse 
use cases across industries and projects. OTS enables interoperability by providing a common language for 
describing tasks, their dependencies, and associated metadata. This document outlines the proposed structure of 
OTS v0.1, along with examples and guidelines for implementation.

### Key Features

- **Flexible Schema**: Accommodate various task types, including software development (e.g., user stories), 
project management (e.g., milestones), and scientific research (e.g., experiments).
- **Dependency Management**: Support hierarchical relationships between tasks, allowing for clear visualization 
of dependencies and impact on overall progress.
- **Metadata Enrichment**: Incorporate rich metadata such as descriptions, assigned agents, priority levels, 
timestamps, and artifact attachments to enhance task representation.
- **Interoperability**: Define a standardized JSON format that can be easily consumed and produced by different 
systems and platforms.

## OTS Schema Structure

### Core Elements

1. **id** (string, required): Unique identifier for the task.
2. **description** (string, optional): A brief explanation of the task's purpose or objective.
3. **type** (string, optional): Task classification (e.g., story, bug, epic).
4. **status** (string, optional): Current state of the task (e.g., todo, inprogress, done).
5. **dependencies** (array of strings, optional): IDs of tasks that must be completed before this task can 
start.
6. **children** (array of objects, optional): Hierarchical array of subtasks or related tasks.
7. **artifacts** (object, optional): Key-value pairs representing attachments, links, or references relevant to 
the task.
8. **priority** (integer, optional): Numeric representation of task importance or urgency.
9. **assigned_agent_type** (string, optional): Type of resource assigned to the task (e.g., developer, 
researcher).
10. **creation_timestamp** (string, ISO 8601 format, optional): Date and time when the task was created.
11. **completion_timestamp** (string, ISO 8601 format, optional): Date and time when the task was marked as 
completed.

### Extended Elements (conditional based on parent or metadata)

- **due_date** (string, ISO 8601 format, optional): Target completion date for the task.
- **estimate** (object, optional): Estimated effort required to complete the task (e.g., story points, hours).
- **labels** (array of strings, optional): Custom tags or categories associated with the task.

## Example Usage with Interoperability Testing

In addition to demonstrating the structure and flexibility of OTS, it's essential to showcase how to perform 
interoperable operations like updating task statuses. Below is a step-by-step example using Python, leveraging 
the `pydantic` library for data modeling and `requests` for HTTP interactions. This example assumes you have an 
API endpoint that accepts JSON payloads conforming to the OTS schema for updating tasks.

### Prerequisites

1. Install required libraries:

   ```bash
   pip install pydantic requests
   ```

2. Ensure you have access to a server with the following endpoints (replace placeholders with actual URLs and 
tokens):
   - `PUT /tasks/{task_id}`: Update a task's status, expected in JSON format conforming to OTS.
   - `GET /tasks/{task_id}`: Retrieve a task by ID, useful for fetching current states before updating.

### Example Code: Updating Task Status


The following Python script demonstrates how to update the status of a task from "inprogress" to "done":

```python
from pydantic import BaseModel
import requests


# Define OTS Task Model
class OtsTask(BaseModel):
    id: str
    description: str
    type: str = None  # Optional, as per OTS schema
    status: str
    dependencies: list = []
    children: list = []
    artifacts: dict = {}
    priority: int = None
    assigned_agent_type: str = None
    creation_timestamp: str = None
    completion_timestamp: str = None


# Example task data
task = OtsTask(
    id="12345",
    description="Implement user authentication",
    type="story",
    status="inprogress",
    dependencies=["67890"],  # Dependency on another task
    children=[
        OtsTask(id="54321", description="Set up database schema")
    ],
    artifacts={"documentation_link": "https://example.com/docs"}
)


def update_task_status(api_url, task):
    headers = {"Content-Type": "application/json"}
    response = requests.put(f"{api_url}/tasks/{task.id}", json=task.dict(), headers=headers)

    if response.status_code == 200:
        print("Task status updated successfully")
    else:
        print(f"Failed to update task status: {response.text}")


# Replace with your API endpoint URL and token for authentication (if required)
api_url = "https://your-task-management-api.com"
token = "your_api_token"  # Include in headers if token-based authentication is used

if token:
    headers["Authorization"] = f"Bearer {token}"

update_task_status(api_url, task)
```


### Notes

1. **Error Handling**: Implement robust error handling to manage API response codes and messages appropriately.
2. **Authentication**: Ensure that your API endpoint supports the required authentication method (e.g., 
token-based, basic auth).
3. **Rate Limiting**: Be mindful of potential rate limits imposed by the API to avoid service disruptions.

## Contributing & License

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please submit an 
issue or pull request. This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for 
details.

