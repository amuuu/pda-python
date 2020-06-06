def split_rule(input):
    tmp = input.split(' -> ')
    variable = tmp[0]
    production = tmp[1]    
    print(variable)
    print(production)
    return [variable, production]
