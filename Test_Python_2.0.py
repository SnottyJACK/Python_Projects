import time
from progress.bar import IncrementalBar

mylist = []
for i in range(1000):
     mylist.append(i)

bar = IncrementalBar('Countdown', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(0.005)

bar.finish()
print("\t\t\tВСЁ ПИЗДЕЦ ")
