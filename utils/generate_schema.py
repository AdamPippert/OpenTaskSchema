from models.joth import JothTask
import json

schema = JothTask.model_json_schema()

schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
schema["$id"] = "https://github.com/AdamPippert/JOTH"
schema["title"] = "JOTH Task Schema"
schema["version"] = "0.0.1"

with open('joth_schema.json', 'w') as f:
    json.dump(schema, f, indent=2)