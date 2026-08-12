# Nested if -elif -else statement

age=int(input("enter your age :"))
has_deggree =input("enter 'you have degree or not' True / Flase = ")
if age>=18:
    print("age requirement met")
    if has_deggree=="True":
        print("you are eligibal for this job")
    else:
        print("yor are not eligibal for this job")
else:
    print("you are too young to apply")