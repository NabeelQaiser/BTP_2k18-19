
# test strings...

# s1 = "( ( ! ( ( x - 1 ) > ( ! ( x + 5 ) ) ) ) v ( y < 2 ) )"      # properly bracketed
# s2 = " y ==> 2 "    # this isn't properly bracketed
# s3 = "( y ==> 2 )"    # this isn't properly bracketed, proper is: "( ( y ) ==> ( 2 ) )"
# s4 = "( ! ( y ) ==> ( 2 ) )"    # '!' isn't properly bracketed, proper is: "( ( ! ( y ) ) ==> ( 2 ) )"
# s5 = "( ( ! ( ( ! ( y ) ) >= 5 ) ) ==> ( 2 ) )"      # properly bracketed
# s6 = "( ( ! ( x > 5 ) ) > ( ! ( 9 ) ) )"      # properly bracketed


class WpcStringConverter():

    def __init__(self, wpcString):
        self.wpcString = wpcString
        self.tokens = []
        self.convertedWpc = ""
        self.implies_p = []
        self.implies_p_q = []


    def execute(self):
        self.wpcString = self.wpcString.replace("   ", " ")
        self.wpcString = self.wpcString.replace("  ", " ")
        self.wpcString = self.wpcString.strip()
        self.tokens = self.wpcString.split(" ")
        self.convertedWpc = self.convert(0, len(self.tokens)-1)

    def convert(self, start, end):
        length = end-start+1
        if length < 1:
            return ""
        else:
            needProcessing = False
            tempCounter = start
            while tempCounter <= end:
                if self.tokens[tempCounter] in ['^', 'v', '!', '==>']:
                    needProcessing = True
                    break
                tempCounter = tempCounter + 1
            if not needProcessing:
                if self.tokens[start] == '(':      # for strings like "( ( -- ) <= ( -- ) )"
                    bracketMatchingIndex = self.bracketMatcher(start, end)
                    if bracketMatchingIndex == end:
                        return self.convert(start+1, end-1)
                    else:
                        return self.getStringFromTokens(start, end)
                else:      # for strings like "xx >= zz", although these comes under ill-bracketed strings
                    return self.getStringFromTokens(start, end)
            else:
                if self.tokens[start] == '(':      # for strings like "( ( ! ( -- ) ) ==> ( -- ) )"
                    bracketMatchingIndex = self.bracketMatcher(start, end)
                    if bracketMatchingIndex == end:
                        return self.convert(start+1, end-1)
                    else:
                        if self.tokens[bracketMatchingIndex+1] == '^':      # for strings like "( ! ( -- ) ) ^ ( -- )"
                            return "And( " + self.convert(start, bracketMatchingIndex) + ", " + self.convert(bracketMatchingIndex+2, end) + " )"
                        elif self.tokens[bracketMatchingIndex+1] == 'v':
                            return "Or( " + self.convert(start, bracketMatchingIndex) + ", " + self.convert(bracketMatchingIndex + 2, end) + " )"
                        elif self.tokens[bracketMatchingIndex+1] == '==>':
                            p = self.convert(start, bracketMatchingIndex)
                            q = self.convert(bracketMatchingIndex + 2, end)
                            p_implies_q = "Implies( " + p + ", " + q + " )"
                            self.implies_p.append(p)
                            self.implies_p_q.append(p_implies_q)
                            return p_implies_q
                        else:      # for strings like "( ! ( -- ) ) <= ( -- )"
                            return "( " + self.convert(start, bracketMatchingIndex) + " ) " + self.tokens[bracketMatchingIndex + 1] + " ( " + self.convert(
                                bracketMatchingIndex + 2, end) + " )"
                elif self.tokens[start] == '!':      # for strings like "! ( -- )"
                    return "Not( " + self.convert(start+1, end) + " )"



    def bracketMatcher(self, start, end):
        count = 0
        while start <= end:
            if self.tokens[start] == '(':
                count = count+1
            elif self.tokens[start] == ')':
                count = count-1
            if count == 0:
                return start
            start = start+1

    def getStringFromTokens(self, start, end):
        tempCounter = start
        tempString = ""
        while tempCounter <= end:
            tempString = tempString + self.tokens[tempCounter] + " "
            tempCounter = tempCounter + 1
        return tempString.strip()