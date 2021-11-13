import json

import requests

if __name__ == "__main__":
    with requests.Session() as s:
        s.post("http://localhost:3141/send_message", data={"payload": json.dumps({"to": "#general", "text": "asdas"})})
