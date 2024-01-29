from bson import ObjectId

def convert_to_json(data):
    if(isinstance(data, ObjectId)):
        return str(data)
    if isinstance(data, dict):
        return {k: convert_to_json(v) for k, v in data.items()}
    if isinstance(data, list):
        return [convert_to_json(v) for v in data]
    return data