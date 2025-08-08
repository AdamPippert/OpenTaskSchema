from models.ots import OtsTask
import json

schema = OtsTask.model_json_schema()

schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
schema["$id"] = "https://github.com/AdamPippert/OpenTaskSchema"
schema["title"] = "Open Task Schema"
schema["version"] = "0.2.0"

with open('ots.json', 'w') as f:
    json.dump(schema, f, indent=2)