# Google Kick Start 2020 Round A, Allocation problem

######Adam Rör#############


test_cases = int(input().strip())
sum = 0
counter = 0
for i in range(test_cases):
    house_and_budget = input().strip().split()
    house_and_budget = list(map(int, house_and_budget))
    house_cost = input().strip().split()
    house_cost = list(map(int, house_cost))
    house_cost.sort()
    for k in house_cost:
        sum = sum + k
        if sum <= house_and_budget[1]:
            counter = counter + 1

    print("Case #%d: " % (i+1), end='')
    print(counter)
    sum = 0
    counter = 0
