"""
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
is decoded back to the original list of strings.
Please implement encode and decode

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


class Solution:
    def __init__(self, delimiter):
        self.delimiter = delimiter

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        output = ""
        for word in strs:
            output += f'{len(word)}{self.delimiter}{word}'
        return output

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string):
        start_idx = 0
        end_idx = 0
        result = []
        while end_idx < len(string):
            if string[end_idx] == self.delimiter:
                lenght = int(string[start_idx:end_idx])
                word = string[end_idx + 1:end_idx + lenght + 1]
                result.append(word)
                start_idx = end_idx + lenght + 1
                end_idx = start_idx
            else:
                end_idx += 1
        return result


s = Solution("!")
encoded = s.encode(["lint", "code", "love", "you"])
print(encoded)
decoded = s.decode(encoded)
print(decoded)

encoded = s.encode(["we", "say", ":", "yes"])
print(encoded)
decoded = s.decode(encoded)
print(decoded)
