import copy, re, json
from util import *


rules = {}
expressions = []
stack = []
grammar_no = 0
actions = []

def read_grammars(grammar_no):
    with open('input.json') as input_file:
        data = json.load(input_file)
        # fill the rules list
        for g in data['grammars']:
            if g == grammar_no:
                for i in range(0, len(data['grammars'][g])): 
                    new_rule=split_rule(data['grammars'][g][i])
                    if new_rule[0] not in rules:
                        rules[new_rule[0]]=[new_rule[1]]
                    else:
                        rules[new_rule[0]].append(new_rule[1])

def input_expression():
    input_chars = input("\nEnter the expression: ")
    for char in input_chars.split(" "):
        expressions.append(char)
    return input_chars

def input_grammar_number():
    print("Which grammar would you like to check your expression with (from 1-4): ")
    print("(Note that my code is PDA, it doesn't support the 5th grammar which is unrestricted)\n")
    return input("")
    
    
def check_expression(stack, expression):
    
    # no go situations
    if len(stack) > len(expression) or \
        (len(stack) == 0 and len(expression) > 0):
        actions.pop() # remove the action done from the list of valid actions if it didn't work
        return False
    
    stack_pointer = stack.pop()
    print("STACK:")
    print("top:", stack_pointer)
    print("others:", stack)
    
    # if we reached the last character of the input string
    if stack_pointer == expression[-1]:
        expression.pop()
        if len(stack) == 0 and len(expression) == 0:
            print("\n$$$$$$$$$$$$$$$$$$$$$$")
            print(  "$$$     ACCEPT     $$$")
            print(  "$$$$$$$$$$$$$$$$$$$$$$\n")
            print_actions(actions)
            exit()
        check_expression(copy.deepcopy(stack), copy.deepcopy(expression))
    
    # check if we have a symbol that's not in the grammar
    if stack_pointer not in rules:
        return False

    # save the productions for the current variable
    for rule in rules:
        if rule==stack_pointer:
            stack_prods = rules[rule]
            break
    
    # call this function recursively for each production that stack pointer variable has
    for production in stack_prods:
        tmp_stack = copy.deepcopy(stack)
        for inner_item in production.split(" "):
            tmp_stack.append(inner_item)
        actions.append((stack_pointer,"->", production)) # add every action that we do (the ones that don't work will be poped.)
        check_expression(tmp_stack, copy.deepcopy(expression))

grammar_no = input_grammar_number()
read_grammars(grammar_no)
input_str = input_expression()
stack.append(next(iter(rules)))

print_grammar(rules)
print_input(input_str)

if not check_expression(stack, expressions):
    print("\n$$$$$$$$$$$$$$$$$$$$$$")
    print(  "$$$      FAIL      $$$")
    print(  "$$$$$$$$$$$$$$$$$$$$$$\n")
