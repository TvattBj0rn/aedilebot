import csv
import json

file_names = ["Damage", "Vehicles_Tripods_Emplacements", "Weapons", "Structures", "Multitier_Structures"]

def csv_to_json(csv_file_path, json_file_path):
    # Read both CSV and JSON files
    with open(csv_file_path, encoding="utf-8") as csvf, open(json_file_path, "w", encoding="utf-8") as jsonf:
        # convert python each csv row into python dict and then to JSON String and write to file
        jsonf.write(json.dumps(list(csv.DictReader(csvf)), indent=4))


def json_to_js(json_file_path, js_file_path, object_name):
    with open(json_file_path, encoding="utf-8") as jsonf, open(js_file_path, "w", encoding="utf-8") as jsf:
        jsf.write(f"export const {object_name} = ")
        for row in jsonf.readlines():
            if ":" in row:
                splited = row.split(":")
                without = splited[0]
                if "(" in without:
                    without = without.split("(")[0] + '"'
                without = without.replace(" ", "")
                if without == '"Name"':
                    jsf.write(f'"ObjectType":"{object_name}",\n')
                final = ":".join([without, *splited[1:]])
            else:
                final = row
            jsf.write(final)

#MAIN
for file_name in file_names:
    csv_file, json_file, js_file = file_name + ".csv", file_name + ".json", file_name + ".js"
    csv_to_json(csv_file, json_file)
    json_to_js(json_file, js_file, file_name)
