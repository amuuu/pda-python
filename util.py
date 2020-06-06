def split_rule(input):
    tmp = input.split(' -> ')
    variable = tmp[0]
    production = tmp[1]    
    return [variable, production]


def print_actions(actions):
    print("ACTIONS DONE:")
    counter = 1
    for item in actions:
        print(counter, ".", item[0], item[1], item[2])
        counter += 1
