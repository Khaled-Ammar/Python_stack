# ------------------(1)----------------------
for x in range(0, 151, 1):
    print(x)
# ------------------(2)--------------------
for x in range(5, 501, 5):
    print(x)
# ------------------(3)--------------------
for x in range(1, 101, 1):
    if x % 5 == 0:
        print("coding")
    if x % 10==0:
        print("coding dojo")
    else:
        print(x)
# ------------------(4)--------------------
x=0
for i in range(1, 500000, 1):
    if i % 2 == 1:
        x += i
print(x) 
# ------------------(5)--------------------   
for x in range(2018,1,-4):
    print(x)
# ------------------(6)--------------------   
lowNum = 3
mult = 6
highNum = 9
print(f"lowNum= {lowNum} mult= {mult} highNum={highNum}.")

