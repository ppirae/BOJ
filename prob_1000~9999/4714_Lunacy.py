while True:
    n = float(input())
    if n == -1.0:
        break
    print("Objects weighing {0:.2f} on Earth will weigh {1:.2f} on the moon.".format(n, 0.167*n))