import md5
from itertools import count


key = "yzbqklnj"


for i in count(start=1):
    h = md5.new(key + str(i)).hexdigest()
    if h.startswith("000000"):
        print i
        break
