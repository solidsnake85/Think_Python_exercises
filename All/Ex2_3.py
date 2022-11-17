# 1. The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5?
radius = 5
pi = 3.14159

print ((4/3) * (pi * radius**3))

# 2. Cover price of book is $24.95, bookstores get 40% discount.  Shipping is $3 for first copy, 75 cents for each
# additional.  Total wholesale cost for 60 copies?
discount = .6
total_Copies = 60
addit_Copies = total_Copies - 1
extra_Cost = .75 * addit_Copies

print ((24.95 * discount) * total_Copies + 3 + (extra_Cost))

# 3. Leave house at 6:52am and run 1 mile at easy pace (8:15/mile) then 3 miles at tempo (7:12/mile), and 1 mile at
# easy pace again, what time do I get home for breakfast?
easy = 8.25
tempo = 7.2

print (easy + (3 * tempo) + easy) # 7:30am (and 6 seconds)