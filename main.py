import json
import re


rules = []
expressions = []

def read_grammars():
    with open('input.json') as input_file:
        data = json.load(input_file)

        # fill the rules list
        for g in data['grammars']:
            for i in range(0, len(data['grammars'][g])): 
                new_rule = re.findall(r"[\w']+", data['grammars'][g][i]) # turn "A-> aB,R" to "[A,aB,R]"
                if new_rule not in rules:
                    rules.append(new_rule)

def get_inputs():
    input_chars = input("Enter the expression: ").split(" ")
    for char in input_chars:
        expressions.append(char)
    

read_grammars()
get_inputs()

print("##########")

print(rules)
print(expressions)

