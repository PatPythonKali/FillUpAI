import random_address as ra

ca = ra.real_random_address()

print(ca)
print(ca["address1"] + " " +
      ca["city"] + " " +
      ca["state"] + " " +
      ca["postalCode"] )