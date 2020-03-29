
name = input ("What is your name?")
times_str = input ("How many times, should I print your name," + name + " ? " )
count = int(times_str)
for x in range (count):
    print ( x,name, end = " rules ! " )