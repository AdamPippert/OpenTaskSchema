from models.joth import JothTask
import json

schema = JothTask.model_json_schema()

with open('joth_task_schema.json', 'w') as f:
    json.dump(schema, f, indent=2)