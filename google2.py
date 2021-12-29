# Google Kick Start 2020 Round A, plating problem

######Adam Rör#############


# return the maximum beuty value
def getMax(sum, plates, stack_size, n_of_stacks, curr_stack, visisted, result):
    maxResult = 0

    if curr_stack >= n_of_stacks and plates > 0:
        return 0

    # base case for recursion
    if plates <= 0 or curr_stack >= n_of_stacks:
        return 0

    # DP
    if visisted[curr_stack][plates] == 1:
        return result[curr_stack][plates]

    # So every stack will get counted
    maxResult = getMax(sum, plates, stack_size, n_of_stacks,
                       curr_stack+1, visisted, result)

    for j in range(1, min(plates, stack_size)+1):
        maxResult = max(sum[curr_stack][j-1] + getMax(sum, plates-j,
                                                      stack_size, n_of_stacks, curr_stack+1, visisted, result), maxResult)

    result[curr_stack][plates] = maxResult
    visisted[curr_stack][plates] = 1
    return maxResult

# Changing the lists so its the added value eg, [1,2,3,4,5] -> [1,3,6,10,15]


def calc(arr, plates, stack_size, n_of_stacks, p, visisted, result):
    sum = []
    temp_list = []
    temp = 0

    for j in range(n_of_stacks):
        for i in range(stack_size):

            temp = arr[j][i] + temp

            temp_list.append(temp)
        sum.append(temp_list)
        temp_list = []
        temp = 0
    # print(sum)

    result = getMax(sum, plates, stack_size, n_of_stacks, 0, visisted, result)

    print("Case #%d:" % p, end=' ')
    print(result)


def main():

    test_cases = int(input().strip())

    counter = 0
    all_beuty_values = []
    for i in range(test_cases):
        # Using this to make it dynamically programmed
        visisted = [[0]*2000 for i in range(50)]
        result = [[0]*2000 for i in range(50)]
        first_line = input().strip().split()
        first_line = list(map(int, first_line))
        number_of_stacks = first_line[0]
        size_of_stack = first_line[1]
        using_plates = first_line[2]
        for k in range(number_of_stacks):
            beuty_values = input().strip().split()
            beuty_values = list(map(int, beuty_values))
            all_beuty_values.append(beuty_values)
        calc(all_beuty_values, using_plates,
             size_of_stack, number_of_stacks, i+1, visisted, result)
        all_beuty_values = []


if __name__ == "__main__":
    main()
