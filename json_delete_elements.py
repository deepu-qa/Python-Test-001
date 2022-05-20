import os
import json

# removing "outParams" and "appdate"
def parse_json(input_file_name):
    service = "ntp"
    with open(input_file_name, 'r') as dataFile:
        data = json.load(dataFile)

    # print(data)
    # if "" in data["watchdog"]["services"]:
    del data["inParams"]["appdate"]
    del data["outParams"]

    # print(data)
    with open("json_output.json", 'w') as outputFile:
        data = json.dump(data, outputFile)

if __name__ == "__main__":
    parse_json("Inputs/test_payload.json")