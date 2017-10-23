"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Source: https://leetcode.com/problems/decode-string/#/description
"""


# DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) < 2):
            return s # if we wanted to repeat, we'd need at least two chars for the brackets; must just be an unencoded string
        final_string = ''
        consuming_numbers = False
        # if the string is well-formed, we can only get one of two things at the start: a number or a non-number
        number_string = ''
        for index, c in enumerate(s):
            if (consuming_numbers == True): # we're consuming numbers; can only be a number or a '['
                if (c.isdigit()): # this char is a number; we're still consuming numbers
                    number_string += c
                elif (c == '['): # we're into the repeat-string; find the end of it and repeat
                    consuming_numbers = False
                    string_to_repeat = self.find_bracketed_string(s[index+1:]) # repeat this, then decode the rest
                    final_string += self.decodeString(self.repeat_this(int(number_string), string_to_repeat))
                    number_string = '' # reset this
                else:
                    print('Error; decodeString was guaranteed a well-formed string. Returning None.')
                    return None
            else: # not consuming numbers yet
                if (c.isdigit()): # this char is a number; now we are consuming numbers
                    consuming_numbers = True
                    number_string += c
                elif (c == '['):  # edge condition: can we have a bracketed string with no number in front of it?
                    string_to_add = self.find_bracketed_string(s[index + 1:])  # find the corresponding close-bracket
                    final_string += self.decodeString(self.repeat_this(1, string_to_add)) # and add it in
                elif (c != ']'): # it's not a number, not a close bracket... must just be a non-encoded string
                    final_string += c # just add it to the final output
        return final_string

    def repeat_this(self, times, str):
        if len(str) < 1: # empty string, stays empty no matter how many repeats
            return str
        else:
            ret_str = ''
            for x in range(1,times,1):
                ret_str += str
            return ret_str

    def find_bracketed_string(self, str):
        ret_str = ''
        bracket_stack = ['['] # we already came on with this
        for x in str:
            ret_str += x
            if (x == '['):
                bracket_stack.append(x)
            elif (x == ']'):
                bracket_stack.pop()
                if len(bracket_stack) == 0: # this was the last part of the string
                    return ret_str[0:len(ret_str)-1] # last character is a ']' that we don't need
        print('Error: somehow we had unequal numbers of [ and ]!!! Returning None.')
        return None



# Please add your test cases below:

def main():
    s = Solution()
    decoded_string = s.decodeString('[][]')
    print("Expected return None or empty string; received {}.".format(decoded_string))

    decoded_string = s.decodeString('45[]111[]')
    print("Expected return None or empty string; received {}.".format(decoded_string))

    decoded_string = s.decodeString('1[a]2[b]3[c]')
    print("Expected return 'abbccc'; received {}.".format(decoded_string))

    decoded_string = s.decodeString('3[a]2[bc]')
    print("Expected return 'aaabcbc'; received {}.".format(decoded_string))

    decoded_string = s.decodeString('3[a2[c]]')
    print("Expected return 'accaccacc'; received {}.".format(decoded_string))

    decoded_string = s.decodeString('2[abc]3[cd]ef')
    print("Expected return 'abcabccdcdcdef'; received {}.".format(decoded_string))

if __name__ == "__main__":
    main()

