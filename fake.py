from faker import Faker

myfake = Faker()

myfake.seed(1)

print(myfake.name()) 
print(myfake.address())
print(myfake.text()) 
print(myfake.sentence())
print(myfake.random_number())