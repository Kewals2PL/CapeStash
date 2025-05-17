import json

with open("capes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("data.js", "w", encoding="utf-8") as f:
    f.write("const data = ")
    json.dump(data, f, indent=4)
    f.write(";")