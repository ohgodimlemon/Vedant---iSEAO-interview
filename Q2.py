# Q: how do you find max left height and max right height for each index?
# Input/ruin bloc                          [4, 2, 1, 0, 5, 4, 1, 0, 2, 1, 0, 1]
# Max left                                 [0, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
# Max right                                [5, 5, 5, 5 ,4 ,2 ,2 ,2 ,1 ,1 ,1 ,0] 
# Min(Max left, Max right)                 [0, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 0] => max sand height
# Min(Max left, Max right) - ruin blocks  [-4, 2, 3, 4,-1,-2, 1, 2,-1, 0, 1,-1]
# sum the positive answers                 = 13 water blocks             
#
# NOTE: for max right, start from right: because if you start from left youll have to find the
# max in right split of array everytimel. starting from right gives you chance to 
# update your max as you iterate
#
# However, this would take alot of space, maybe we can find max left and max right on the go?
#

def sand_trapped_in_ruins(list):
    l_idx = 0
    r_idx = len(list) - 1
    left_max = list[l_idx]
    right_max = list[r_idx]
    sand_trapped = 0

    while l_idx < r_idx:
        if left_max < right_max:
            l_idx += 1
            left_max = max(left_max, list[l_idx])
            sand_trapped += max(left_max - list[l_idx], 0)
        else:
            r_idx -= 1
            right_max = max(right_max, list[r_idx])
            sand_trapped += max(right_max - list[r_idx], 0)
    
    return sand_trapped

def main():
    test_1 = [4,2,1,0,5,4,1,0,2,1,0,1]
    sand_trapped = sand_trapped_in_ruins(test_1)
    print("Input: ", test_1)
    print("Your output: ", sand_trapped)
    print("Actual output: ", 13)
    if (sand_trapped == 13):
        print("test passed!")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()
        