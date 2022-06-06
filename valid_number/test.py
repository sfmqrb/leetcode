import re
class Solution:
    def isNumber(self, s: str) -> bool:
        
        ls = re.split('[eE]', s)
        if len(ls) > 2 or len(ls) == 0:
            return False
        
        decimalOrInteger, *integer = ls
        
        if len(integer) > 1:
            return False
        elif not integer:
            integer = '0'
        else:
            integer = integer[0]
        
        decimal_match = self.is_decimal(decimalOrInteger) or self.is_integer(decimalOrInteger)
        
        integer_match = self.is_integer(integer)
        
        return decimal_match and integer_match

    def is_decimal(self, decimal):
        if decimal == '':
            return False
        if not re.search('[0-9]', decimal):
            return False 
        return False if not re.match('^[+-]?[0-9]*\.[0-9]*$', decimal) else True

    def is_integer(self, integer):
        return False if not re.match('^[+-]?[0-9]+$', integer) else True
        
s = Solution()

for x in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    try:
        assert s.isNumber(x) == True
    except AssertionError:
        print("Failed on True input: " + x)
for x in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "3-1", ".", "0e", "e", "e+", "e+-1", "1e1.5", "1e1.5e1.5", "1e1.5e1.5e1.5", "1e1.5e1.5e1.5e1.5"]:
    try:
        assert s.isNumber(x) == False
    except:
        print("Failed on False input: " + x)
    