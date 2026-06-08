import json
import urllib.parse

new_json = {}

with open("static/legacy_index.json", "r") as f:
    data = json.load(f)
    

    for signal in data:
        url = urllib.parse.unquote(data[signal]['url'])
        url = urllib.parse.quote(url, safe=":/")
        new_json[url] = {
            'dir': data[signal]['dir'],
            'name': signal
        }
json_str = json.dumps(new_json, indent=4)    
with open("static/index.json", "w") as f:
    f.write(json_str)