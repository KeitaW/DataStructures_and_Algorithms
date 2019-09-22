import json

rf = {"id": "1", "left": {"id": "2", "left": {"id": "3", "left": None, "next": None, "right": None, "val": 4}, "next": None, "right": {"id": "4", "left": None, "next": None, "right": None, "val": 5}, "val": 2},
      "next": None, "right": {"id": "5", "left": {"id": "6", "left": None, "next": None, "right": None, "val": 6}, "next": None, "right": {"id": "7", "left": None, "next": None, "right": None, "val": 7}, "val": 3}, "val": 1}
val = json.dumps(rf)
print(val)
