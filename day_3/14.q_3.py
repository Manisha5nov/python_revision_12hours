# take the user age as input and check whether the user is eligible to vote or not. 
# (age>=18) and whether they are a senior citizen or not. (age>=60) 

age =int(input("enter your age ="))
can_vote = age >= 18
is_senior_citizen = age >= 60
print(f"Can vote: {can_vote}")
print(f"Is senior citizen: {is_senior_citizen}")