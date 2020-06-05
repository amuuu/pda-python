def split_rule(input):
    tmp = input.split(' -> ')
    variable = tmp[0]
    production = tmp[1]    
    return [variable, production]
