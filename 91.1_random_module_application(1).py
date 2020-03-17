from random import*

fake_name = ["ram", 'rahul', 'rakesh', 'ana', 'riya', 'pily', 'rishika']
fake_last = ["malhotra", "khurana", "khanna", "arora","khandelwal", "gupta"]

fake_city = ["Alwar", "Kota", "udaipur", "delhi", "mumbai", "ahmbdabad"]

fake_street = ["main", "sideone", "local"]


# name
# address - plot number, street, city, pincode
# email_address
# phone number

for i in range(100):
    first = choice(fake_name)
    last = choice(fake_last)

    name = f"{first}{last}"

    phone = randint(6000000000,9999999999)

    address = f'Plot-{randint(1,100)}, {choice(fake_street)} street, {choice(fake_city)}, {randint(10000,99999)}'

    email = f"{first}{last}{randint(1,100)}@gmail.com"

    print(f'{name} \n{address} \n{phone}\n{email}')

