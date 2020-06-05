def split_rule(input):
    tmp = input.split('->')
    variable = tmp[0]
    tmp2 = tmp[1].split(',')
    production = tmp2[0]    
    direction = tmp2[1]

    return [variable, production, direction]
