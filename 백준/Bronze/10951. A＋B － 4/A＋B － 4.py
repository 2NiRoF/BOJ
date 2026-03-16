while True:
    try:
        summation = sum(
            [int(i) for i in input().split()]
        )
        print(summation)
    except: break