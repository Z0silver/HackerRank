def solve(meal_cost, tip_percent, tax_percent):
    tip=(tip_percent/100)*meal_cost
    tax=(tax_percent/100)*meal_cost
    total=meal_cost+tip+tax
    print("%.f"%total)

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

solve(meal_cost, tip_percent, tax_percent)
