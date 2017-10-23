"""
Merge two sorted arrays and return it as a new array.
# NOTE: YOU CAN NOT USE ANY SORTING LIBRARIES
"""

extra_tests = False

def merge_two_list_helper(list1, list2):
    # check some edge cases
    if (type(list1) is not list) or (type(list2) is not list):
        print('Unexpected input; merge_two_list_helper takes two lists. Returning None.')
        return None
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    idx_l1_least = 0
    while (list1[idx_l1_least] <= list2[0]): # find the first place where list1 is greater than list2[0]
        idx_l1_least += 1
        if (idx_l1_least == len(list1)): # all of list1 is less than list2[0]
            return list1 + list2
    idx_l2_least = 0
    while (list2[idx_l2_least] <= list1[idx_l1_least]): # now find the last place where list1[idx] is still greater than list2
        idx_l2_least += 1
        if (idx_l2_least == len(list2)): # all of list2 fits between list1[idx_l1_least-1] and list1[idx_l1_least]
            return list1[0:idx_l1_least] + list2 + list1[idx_l1_least:]
    return merge_two_list_helper(list1[0:idx_l1_least] + list2[0:idx_l2_least] + list1[idx_l1_least:],
                                                   list2[idx_l2_least:]) # recurse with a more sorted list1


# DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1, list2):
	return merge_two_list_helper(list1, list2)


# test cases
def main():
    if (extra_tests == True):
        list1 = 'this is a string'
        list2 = []
        print("Expecting None; your output is {}".format(merge_two_list(list1, list2)))
        list1 = []
        list2 = {dict:'this is a dict'}
        print("Expecting None; your output is {}".format(merge_two_list(list1, list2)))
        list1 = [1,2,3]
        list2 = []
        print("Expecting [1,2,3]; your output is {}".format(merge_two_list(list1, list2)))
        list1 = []
        list2 = [3,5,9]
        print("Expecting [3,5,9]; your output is {}".format(merge_two_list(list1, list2)))

        list1 = [1,2,3]
        list2 = [4,5,6,7]
        print("Expecting [1,2,3,4,5,6,7]; your output is {}".format(merge_two_list(list1, list2)))

        list1 = [1,2,3,99]
        list2 = [4,5,6,7]
        print("Expecting [1,2,3,4,5,6,7,99]; your output is {}".format(merge_two_list(list1, list2)))

        list1 = [1,2,3,16,17,18,22,28,54,61,77,99]
        list2 = [4,5,6,7,12,19,20,21,25,50,51,52,77,77,77,98]
        print("Expecting stuff in order; note four 77s; your output is {}".format(merge_two_list(list1, list2)))



    list1 = [1,3,5]
    list2 = [2,4,6]
    print("merging [1,3,5] and [2,4,6]......")
    print("expected result is [1,2,3,4,5,6]")
    print("your output is {}".format(merge_two_list(list1, list2)))


if __name__ == "__main__":
    main()
