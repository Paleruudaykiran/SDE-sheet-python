"""
    Time complexity: O(N)
    Space complexity: O(N)
    
    Where N is length of the string.    
"""


# Function for calculating lps array
def calculateLPSArray(str):

    m = len(str)
    lps = [0] * m

    length = 0

    # As, lps[0] is always 0
    lps[0] = 0

    # The loop calculates lps[i] for i = 1 to M-1.
    i = 1
    while i < m:

        # We get new prefix and new suffix, so increase length of  current lps by 1 and go to next iteration.
        if str[i] == str[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            # Don't increment i here
            if length != 0:
                length = lps[length - 1]
            else:
                # There isn't any lps ends with pat[i], so set lps[i] = 0 and go to next iteration.
                lps[i] = 0
                i += 1

    return lps


def minCharsforPalindrome(str):

    revStr = str[::-1]

    # Concatenate string with $ symbol and reverse string.
    concat = str + "$" + revStr

    # Get LPS array of this concatenated string
    lps = calculateLPSArray(concat)

    return len(str) - lps[-1]
