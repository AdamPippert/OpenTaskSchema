from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class JothTask(BaseModel):
    id: str = Field(
        ..., 
        description="Unique task identifier"
    )
    description: Optional[str] = Field(
        ..., 
        description="Task description"
    )
    type: Optional[str] = Field(
        default=None, 
        description="Task type (story, epic, bug, etc.)"
    )
    status: Optional[str] = Field(
        default=None, 
        description="Current status"
    )
    dependencies: Optional[List[str]] = Field(
        default=None,
        description="Tasks this task depends on"
    )
    children: Optional[List["JothTask"]] = Field(
        default=None,
        description="Nested subtasks"
    )
    artifacts: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Task-related artifacts and attachments"
    )
    priority: Optional[int] = Field(
        default=None, 
        description="Priority level"
    )
    assigned_agent_type: Optional[str] = Field(
        default=None, 
        description="Agent type assigned"
    )
    creation_timestamp: Optional[datetime] = Field(
        default=None, 
        description="When created"
    )
    completion_timestamp: Optional[datetime] = Field(
        default=None, 
        description="When completed"
    )
    due_date: Optional[datetime] = Field(
        default=None, 
        description="Target completion date"
    )
    estimate: Optional[object] = Field(
        default=None,
        description="Estimated time to complete"
    )
    labels: Optional[List[str]] = Field(
        default=None,
        description="Labels for categorization"
    )
    