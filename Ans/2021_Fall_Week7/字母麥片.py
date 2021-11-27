input_arr = [str(i) for i in input().split(",")]
seen = {}
new_list = [seen.setdefault(x, x) for x in input_arr if x not in seen]
duplicate_element = []
for i in seen:
    if input_arr.count(i) > 1:
        duplicate_element.append(i)
for i in duplicate_element:
    del seen[i]
print(",".join(seen.values()))
