# 1. The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5?
radius = 5
pi = 3.14159

print ((4/3) * (pi * radius**3))

# 2. Cover price of book is $24.95, bookstores get 40% discount.  Shipping is $3 for first copy, 75 cents for each
# additional.  Total wholesale cost for 60 copies?
discount = .6

print ((24.95 * 60) * discount + 3 + (.75 * 59))

# 3. Leave house at 6:52am and run 1 mile at easy pace (8:15/mile) then 3 miles at tempo (7:12/mile), and 1 mile at
# easy pace again, what time do I get home for breakfast?
easy = 8.25
tempo = 7.2

print (easy + (3 * tempo) + easy) # 7:30am (and 6 seconds)