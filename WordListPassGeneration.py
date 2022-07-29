import random
import string

length = int(input('\nEnter the length of password: '))
numpss = int(input('\nEnter number of password you want create: '))

i = 0
while i < numpss:
    i += 1
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits

    all = lower + upper + num

    temp = random.sample(all, length)
    password = "".join(temp)

    all = string.ascii_letters + string.digits
    password = "".join(random.sample(all, length))

    print(password)
