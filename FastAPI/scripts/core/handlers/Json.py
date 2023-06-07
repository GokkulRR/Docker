import json
with open("sample_data.json","r") as file:

    data = json.load(file)
    print(type(data))
    for i in data:
        print(i)

    store_list = []
    parameters = data["parametersList"]
    print(parameters)
    for each_item in parameters:
        store_dict = {
            "parameterName": each_item["parameterName"],
            "min_value": each_item["min"],
            "max_value": each_item["max"],
            "avg_value": each_item["avg"]
        }
        store_list.append(store_dict)
    print(store_list)

    json_store = json.dumps(store_list, indent=3)
    print(json_store)

with open("sample_out.json", "w") as file1:
    file1.write(json_store)

