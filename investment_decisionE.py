expected_return = float(input("Enter expected return(%): "))
risk_level = int(input("Enter risk level: "))
time = int(input("Enter time in years: "))
current_savings = float(input("Enter current savings: "))

def risk_status():
    if risk_level >= 7 and time < 5:
        return "Bad investment"
    return "OK"

def return_quality():
    if expected_return >= 10 and risk_level <= 5:
        return "Good return"
    elif expected_return >= 5 and risk_level <= 7:
        return "Average return"
    else:
        return "Poor return"

def capital_protection():
    if current_savings >= 1000 and risk_level >= 6:
        return "Capital protection needed"

def risk_class():
    if risk_level >= 8:
        return "High risk"
    elif risk_level >= 5:
        return "Medium risk"
    else:
        return "Low risk"

def time_advantage():
    if time >= 5:
        return "Positive signal"
    
def investment_decision():
    if risk_status() == "Bad investment":
        return "Investment not recommended"
    elif return_quality() == "Good return" and risk_class() != "High risk":
        return "Investment recommended"
    elif capital_protection() == "Capital protection needed":
        return "Consider safer options"
    elif time_advantage() == "Positive signal" and risk_class() == "Medium risk":
        return "Investment may be suitable"
    else:
        return "Investment decision requires further analysis"

print("\n--- Investment Analysis ---")
print("Risk Status:", risk_status())
print("Return Quality:", return_quality())
print("Capital Protection:", capital_protection())
print("Risk Class:", risk_class())
print("Time Advantage:", time_advantage())
print("Final Decision:", investment_decision())