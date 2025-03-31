from bson import ObjectId

def convert_objectid_to_str(data: dict) -> dict:
    
    for key, value in data.items():
        if isinstance(value, ObjectId):
            data[key] = str(value)
        elif isinstance(value, dict):
            data[key] = convert_objectid_to_str(value)
        elif isinstance(value, list):
            data[key] = [str(item) if isinstance(item, ObjectId) else item for item in value]
    return data

def document_to_dict(doc) -> dict:
    return convert_objectid_to_str(doc.to_mongo().to_dict())
