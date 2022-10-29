import json


# To transform serializers.data to manipulable json
def to_json(obj):
    dumped = json.dumps(obj)
    return json.loads(dumped)
