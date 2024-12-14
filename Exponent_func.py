print(2**3)

def power_func(base,pow):
    result=1
    for count in range(pow):
        result = result*base
    return result

print(power_func(4,3))
