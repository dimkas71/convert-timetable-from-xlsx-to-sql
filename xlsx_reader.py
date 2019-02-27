import json, argparse
from openpyxl import load_workbook

#TODO: Move the definition of it to a module
class EmployeeInfo:
    def __init__(self, personnelNum, name, position):
        self.personnelNum = personnelNum
        self.name = name
        self.position = position

    def __repr__(self):
        return "EmployeeInfo(personnelNum={}, name={}, position={})".format(self.personnelNum, self.name, self.position)

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Read xlsx files to objects")
    parser.add_argument("-f", "--file", dest = "file", type = str, help = "json file with configuration info")

    args = parser.parse_args()

    config_list = None

    if (args.file):
        with open(args.file, 'r', encoding = "utf-8") as fp:
            config_list = json.load(fp)

    personnel_infos = []

    if (config_list is not None):
        wb = load_workbook(config_list[0]["file"])
        ws = wb[config_list[0]["sheet"]]
        
        for row_num in range(config_list[0]["row_from"], config_list[0]["row_to"]):
            pi = ""
            name = ""
            pos = ""
            cell = ws.cell(row = row_num, column = config_list[0]["col_name"])
            if hasattr(cell, "value"):
                name = str(cell.value)
            
            cell = ws.cell(row = row_num, column = config_list[0]["col_pn"])
            if hasattr(cell, "value"):
                pi = str(cell.value)

            cell = ws.cell(row = row_num, column = config_list[0]["col_position"])
            if hasattr(cell, "value"):
                pos = str(cell.value)

            personnel_infos.append(EmployeeInfo(personnelNum = pi, name = name, position = pos))
    
    print(personnel_infos)