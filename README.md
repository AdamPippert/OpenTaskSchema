# **JSON Open Task Hierarchy (JOTH) \- v0.1 Proposal**

## **1\. Introduction**

The JSON Open Task Hierarchy (JOTH) standard proposes a simple, consistent JSON structure for representing hierarchical tasks, their dependencies, and associated metadata. Its primary goal is to facilitate interoperability between different software systems, particularly those involving automated task decomposition, execution tracking, project management visualization, and AI agent coordination.  
This standard defines a schema for task objects represented in JSON, focusing on clarity, flexibility, and ease of parsing.

## **2\. Scope**

JOTH defines the structure and semantics of JSON objects used to represent individual tasks and their hierarchical relationships (parent/child) and dependencies (prerequisites).  
It does *not* define:

* Specific communication protocols between systems exchanging JOTH data.  
* The internal logic of systems creating or consuming JOTH data.  
* Specific UI implementations for visualizing JOTH data.

## **3\. Core Concepts**

* **Hierarchy:** Tasks can be nested within other tasks, forming a tree structure. This is primarily represented using the children field.  
* **Dependencies:** Tasks can depend on the completion of other tasks, represented using the dependencies field.  
* **Task Metadata:** Each task carries essential information like its type, status, and description.

## **4\. Data Format**

JOTH utilizes **JSON (JavaScript Object Notation)**. A JOTH dataset typically consists of a JSON array containing one or more top-level JOTH Task Objects.

## **5\. JOTH Task Object Schema Definition (v0.1)**

A JOTH Task Object MUST adhere to the following structure:

| Field Name | Data Type | Requirement | Description |
| :---- | :---- | :---- | :---- |
| id | String | **Mandatory** | A unique identifier for the task within its scope (e.g., project, dataset). |
| description | String | **Mandatory** | A human-readable description of the task's objective. |
| type | String (Enum Recommended) | **Mandatory** | The category or nature of the task. See suggested values below. |
| status | String (Enum Recommended) | **Mandatory** | The current state of the task. See suggested values below. |
| dependencies | Array of Strings | **Mandatory** | An array containing the ids of tasks that MUST be completed before this task can start. Can be empty. |
| children | Array of JOTH Task Objects | **Mandatory** | An array containing nested JOTH Task Objects representing sub-tasks. Can be empty. |
| artifacts | Object | Optional | Key-value pairs containing data or links related to the task's inputs/outputs (e.g., file paths, URLs, logs). |
| priority | Integer / String | Optional | Indicates the relative priority of the task. Interpretation is context-dependent. |
| assigned\_agent\_type | String | Optional | Suggests the type of agent or system suitable for executing the task. |
| creation\_timestamp | String (ISO 8601\) / Integer | Optional | Timestamp indicating when the task was created. |
| completion\_timestamp | String (ISO 8601\) / Integer | Optional | Timestamp indicating when the task was completed (reached a final status like 'done' or 'failed'). |

**Suggested Enum Values (v0.1):**

* **type**: feature, epic, story, task, subtask, code, test, bug, integration, review, debug, documentation, design, deployment, research, milestone (This list is extensible, but these provide a common base).  
* **status**: todo, inprogress, blocked, review, done, failed, cancelled, pending (This list is extensible).

**Note on Hierarchy:** While the primary method for representing hierarchy is the nested children array, systems *may* choose to implement hierarchy using a parent\_id field if nesting is impractical for their storage or processing model. However, for interoperability, generating/parsing the children structure is recommended.

## **6\. Example**

\[  
  {  
    "id": "PROJ-AUTH",  
    "description": "Implement User Authentication Feature",  
    "type": "feature",  
    "status": "inprogress",  
    "dependencies": \[\],  
    "children": \[  
      {  
        "id": "AUTH-10",  
        "description": "Design User Schema",  
        "type": "design",  
        "status": "done",  
        "dependencies": \[\],  
        "children": \[\],  
        "artifacts": { "schema\_diagram": "/docs/auth\_schema\_v1.png" },  
        "creation\_timestamp": "2025-04-08T10:00:00Z",  
        "completion\_timestamp": "2025-04-08T15:30:00Z"  
      },  
      {  
        "id": "AUTH-11",  
        "description": "Implement /register Endpoint",  
        "type": "code",  
        "status": "inprogress",  
        "dependencies": \["AUTH-10"\],  
        "children": \[\],  
        "artifacts": { "branch": "feature/auth-register" },  
        "assigned\_agent\_type": "backend-coder-v2",  
        "creation\_timestamp": "2025-04-09T09:15:00Z"  
      },  
      {  
        "id": "AUTH-12",  
        "description": "Write Unit Tests for /register",  
        "type": "test",  
        "status": "todo",  
        "dependencies": \["AUTH-11"\],  
        "children": \[\],  
        "artifacts": {},  
         "creation\_timestamp": "2025-04-09T09:15:05Z"  
      }  
    \],  
    "artifacts": { "requirements\_doc": "/docs/auth\_feature.md" },  
    "creation\_timestamp": "2025-04-08T09:00:00Z"  
  }  
\]

## **7\. Versioning**

This document describes **JOTH version 0.1**. Future revisions should increment the version number and document changes clearly.

## **8\. Openness and Next Steps**

This proposal is intended as a starting point for an open standard. Further steps could include:

* Publishing this specification in a public repository (e.g., GitHub).  
* Inviting feedback and contributions from the community.  
* Refining the schema based on feedback and real-world usage.  
* Potentially establishing a simple governance model for future updates.