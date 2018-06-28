import random


fname = "datos.csv"


with open(fname,"wt") as f:
    f.write("x,y\n")
    for i in range(150):
        a = random.randint(1,200)
        b = random.randint(1,200)
        # f.write("[{},{}],\n".format(a,b))
        f.write("{},{}\n".format(a,b))


