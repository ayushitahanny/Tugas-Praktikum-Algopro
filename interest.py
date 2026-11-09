def compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

def simple_interest(principal, rate, time):
    return principal + (principal * rate * time)