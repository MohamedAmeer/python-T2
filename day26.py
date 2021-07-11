# 1. enumerate a list.

l1 = ["car", "bike", "bicycle", "helicopter", "boat"]
t1 = ("london", "paris", "new york", "los angels")

for a, b in list(enumerate(l1)):
    print(a, b)

# 2. enumerate a tuple

for t in tuple(enumerate(t1)):
    print(t)