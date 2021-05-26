items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
data = input().lower().split()
junk_materials = {}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
item_is_obtained = False
all_materials = {}
while not item_is_obtained:
    for index in range(0, len(data), 2):
       key = data[index + 1]
       value = int(data[index])
       if key in key_materials:
           key_materials[key] += value
       else:
           if not key in junk_materials:
               junk_materials[key] = value
           else:
               junk_materials[key] += value
       for this_key, value in key_materials.items():
            if value >= 250:
                item_is_obtained = True
                key_materials[this_key] -= 250
                print(f"{items[this_key]} obtained!")
                break
       if item_is_obtained:
            break
    if item_is_obtained:
            break
    data = input().lower().split()
    all_materials = {}
sorted_key_items = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_junk_items = sorted(junk_materials.items(), key=lambda kvp: kvp[0])


for key, value in sorted_key_items:
    print(f"{key}: {value}")
for key, value in sorted_junk_items:
    print(f"{key}: {value}")
