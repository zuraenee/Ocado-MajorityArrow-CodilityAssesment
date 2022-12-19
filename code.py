def solution(S):
    up_counter = 0
    down_counter = 0
    right_counter = 0
    left_counter = 0
    """ Counting Section """
    for entry in S:
        if entry == "^":
            up_counter += 1
        elif entry == ">":
            right_counter += 1
        elif entry == "<":
            left_counter += 1
        elif entry == "v":
            down_counter += 1
    max_counter = max([up_counter, down_counter, right_counter, left_counter])
    return len(S) - max_counter


if __name__ == '__main__':
    string1 = "^vv<v"
    string2 = "v>>>vv"
    string3 = "<<<"
    sol = solution(string3)
    print(sol)
