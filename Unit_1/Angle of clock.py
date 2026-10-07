h = int(input("Enter hours passed : "))
m = int(input("Enter minutes passed : "))
s = int(input("Enter seconds passed : "))


H = h*30
M = m*0.5
S = s*(1/120)

T = H + M + S

print(f"Total angle passed since midnight is {T}")