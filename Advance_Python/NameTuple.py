# [1] Name Tuple
# [-] Name tuple is a subclass of tuple
# [-] Tuple + class == Named Tuple
# [-] from collections import namedtuple
# [-] namedtuple(typename,field_names)
# ----------------------------------------
from collections import namedtuple
person = namedtuple('person',['Name','Age'])
new_person = person('Karim',23)
print(new_person)
