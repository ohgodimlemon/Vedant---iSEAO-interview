
def boundary_summariser(list):
    if not list:
        return []

    boundary_summarised = []
    current_boundary = [list[0]] #start with first element, trivial

    for idx in range(len(list) - 1):     

        if (list[idx] + 1 != list[idx + 1]):
            current_boundary.append(list[idx])
            boundary_summarised.append(current_boundary)
            current_boundary = [list[idx + 1]] # new starting boundary
        
    current_boundary.append(list[-1]) # add last element because we never reached there
    boundary_summarised.append(current_boundary)
        
    return boundary_summarised

def tester(test_list, summarised_list, ground_truth):
    print("Input was: ", test_list)
    print("Output was: ", summarised_list)
    print("Output should be (ground truth): ", ground_truth)
    if ground_truth == summarised_list:
        print("test passed!")
        print("----------------------------")
    else:
        print("test failed")
        print("----------------------------")

def main ():
    #test 1
    test_1 = [1,3,4,5,7]
    summarised_list = boundary_summariser(test_1)
    tester(test_1, summarised_list, [[1,1],[3,5],[7,7]])

    #test 2
    test_2 = [1, 2, 3, 5, 6, 8]
    summarised_list = boundary_summariser(test_2)
    tester(test_2, summarised_list, [[1, 3], [5, 6], [8, 8]])

    #test 3 EDGE CASE
    test_3 = [4]
    summarised_list = boundary_summariser(test_3)
    tester(test_3, summarised_list, [[4,4]])

    #test 4 EDGE CASE
    test_4 = []
    summarised_list = boundary_summariser(test_4)
    tester(test_4, summarised_list, [])
    

if __name__ == "__main__":
    main()