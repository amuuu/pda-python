import copy, re, json
from util import *


rules = {}
expressions = []
stack = []

def read_grammars():
    with open('input.json') as input_file:
        data = json.load(input_file)

        # fill the rules list
        for g in data['grammars']:
            for i in range(0, len(data['grammars'][g])): 
                new_rule=split_rule(data['grammars'][g][i])
                if new_rule[0] not in rules:
                    rules[new_rule[0]]=[new_rule[1]]
                else:
                    rules[new_rule[0]].append(new_rule[1])

def get_expression_input():
    input_chars = input("Enter the expression: ").split(" ")
    for char in input_chars:
        expressions.append(char)
    
def check_expression(stack, expression):
    # no go situations
    if len(stack) > len(expression) or \
        (len(stack) == 0 and len(expression) > 0):
        return False

    stack_pointer = stack.pop()
    
    # if we reached the last character of the input string
    if stack_pointer == expression[-1]:
        expression.pop()
        if len(stack) == 0 and len(expression) == 0:
            print("ACCEPT YAY")
            exit()
        check_expression(copy.deepcopy(stack), copy.deepcopy(expression))
    
    # check if we have a symbol that's not in the grammar
    if stack_pointer not in rules:
        return False
    
    # save the productions for 
    for rule in rules:
        if rule==stack_pointer:
            stack_prods = rules[rule]
            break
    
    for production in stack_prods:
        tmp_stack = copy.deepcopy(stack)
        for inner_item in production.split(" "):
            tmp_stack.append(inner_item)
        check_expression(tmp_stack, copy.deepcopy(expression))

read_grammars()
get_expression_input()
stack.append(next(iter(rules)))

print("\n#####################\n")
print("RULES:", rules)
print("INPUT:", expressions)
print("\n#####################\n")

if not check_expression(stack, expressions):
    print("FAIL")



