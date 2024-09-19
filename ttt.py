from PIL import Image
import os
import json

last_list = []

with open('fff.json', 'r') as f:
    json_data = f.read()

list_thump = json.loads(json_data)

print(len(list_thump))
if "4dvpj5jbka" in list_thump:
    print("YESS")

# for li in list_thump:
#     xx = li.split('_')
#     print(xx[0])
#     last_list.append(xx[0])

# updated_json_data = json.dumps(last_list)
# with open('fff.json', 'w') as f:
#     f.write(updated_json_data)