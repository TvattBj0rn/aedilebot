from src.utils import load_json_to_dict

th_relics_dict=load_json_to_dict("data\\th_relic_types.json")

result = {}

for name,type in th_relics_dict.items():
    if type in result:
        result[type].append(name)
    else:
        result[type]= []

for type,names in result.items():
    print(type)
    for name in names:
        print(name, end=";")
    print("\n")
