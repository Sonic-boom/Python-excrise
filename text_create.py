ef invest(amount, rate, time):
    print("principal amount:{}".format(amount))
    for i in range(1, time + 1):
        amount = amount * (1 + rate)
        print('year {} : ${}'.format(i, amount))


invest(100, 0.05, 14600)
