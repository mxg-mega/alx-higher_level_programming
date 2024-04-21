#!/usr/bin/python3
""" add_item function """
sys = __import__('sys')
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""  script adds all arguments to a Python list, and then save them to a file
 """
args = sys.argv
filename = "add_item.json"
data = []

try:
    loadInfo = load_from_json_file(filename)
except:
    save_to_json_file(data, filename)

if len(args) != 1:
    data = loadInfo[:]
    for i in range(1, len(args)):
        data.append(args[i])
    save_to_json_file(data, filename)
