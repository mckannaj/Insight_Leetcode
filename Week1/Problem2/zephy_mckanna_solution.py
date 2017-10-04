"""
Given a string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

extra_tests = False

def is_substring_helper (data):
    # test an edge condition
    if len(data) <= 1:
        return True # string is short enough that it must be substrings (although... zero could be False/Error... no substrings?)

    currentLetter = 1 # we'll start checking substrings with the second letter
    global_substring = []
    substring_guess = []
    goodSubstring = True # assume we have a good substring (in case it's all the same letter)
    testingSubstring = False # at the start, we're just building the substring
    for idx, letter in enumerate(data):
        if testingSubstring == False: # we still need to check against the original
            if (len(global_substring) > (len(data) / 2)):
                return False  # didn't find it in the first half, not gonna find it
            if (letter != data[0]): # this letter is different from the first; can't check a substring yet
                goodSubstring = False # without more info, this can't be a string of substrings
            else: # this letter is the same as the first one; let's check to see if they're identical strings
                if (idx > 0): # don't want to do this on the first letter
                    substring_guess = global_substring
                    testingSubstring = True # let's see if it just repeats until the end
        else: # we're testing the substring now
            if (substring_guess[currentLetter] == letter): # still seems good
                currentLetter = currentLetter + 1
                if (currentLetter > len(substring_guess)):
                    currentLetter = 0
                goodSubstring = True # if we stay in this loop, we've got a string of substrings
            else: # found a difference; this can't be the substring
                currentLetter = 1 # will be starting with the second letter next time
                substring_guess = []
                testingSubstring = False
                goodSubstring = False # if it's a string of substrings, it ain't this substring

        global_substring.append(letter)  # add the letter to the potential substring
    return goodSubstring


#DON NOT CHANGE THIS FUNCTION
def is_substring (string_input):
    return is_substring_helper(string_input)


#test case
def main():
    if (extra_tests == True):
        zTest0 = ""
        zTest1 = "aaaaaaaaaaaa"
        zTest2 = "ababdabab"
        print ("Testing your code with zTest0, the expected output is True, your output is {}".format(is_substring(zTest0)))
        print ("Testing your code with zTest1, the expected output is True, your output is {}".format(is_substring(zTest1)))
        print ("Testing your code with zTest2, the expected output is False, your output is {}".format(is_substring(zTest2)))

    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

if __name__ == "__main__":
    main()