import string as st
import random
import time
all = st.printable
length = 16
password = ''.join(random.sample (all,length))
print(password)


