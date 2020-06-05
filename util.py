def split_rule(input):
    tmp = input.replace(" ","").split('->')
    variable = tmp[0]
    production = tmp[1]    
    return [variable, production]
