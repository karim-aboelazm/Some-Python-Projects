# ---------------------------------------+
# Auther : Karim Mohammed Aboelazm       |
# Date   : 5-2-2022                      | 
# ---------------------------------------+
from prettytable import PrettyTable
from faker import Faker
table = PrettyTable()
fake = Faker()

table.field_names=['ID', 'Name','Email']
for i in range(1,21):
    table.add_row([i,fake.name(),fake.email()])
print(table)


