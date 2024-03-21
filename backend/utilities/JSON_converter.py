import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
        def default(self,obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

def convert_to_json(data):
     return json.dumps(data, cls=DateTimeEncoder, indent=5)

