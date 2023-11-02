class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def check_ipv4(string):
            array = queryIP.split(".")
            if len(array) != 4:
                return False
            
            for num in array:
                if len(num) <=0 or (len(num) > 1 and len(num) != len(num.lstrip("0"))):
                    return False
                
                for c in num:
                    if not c.isnumeric():
                        return False
                if not (0<=int(num) <= 255):
                    return False
            return True

        def check_ipv6(string):
            
            valid = {"a","b","c","d","e",'f',"A","B","C","D","E","F"}
            array = queryIP.split(":")   
            if len(array) != 8:
                return False

            for num in array:
                if not(1<=len(num) <= 4):
                    return False

                for c in num:
                    if not c.isnumeric() and not c in valid:
                        return False
            return True

        if check_ipv4(queryIP):
            return "IPv4"
        elif check_ipv6(queryIP):
            return "IPv6"
        
        return "Neither"