class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def decode():

            res = []

            while self.i < len(s) and s[self.i] != ']':
                if s[self.i].isalpha():
                    res.append(s[self.i])
                    self.i += 1

                else:

                    num = 0
                    while self.i < len(s) and s[self.i].isdigit():
                        num = num * 10 + int(s[self.i])
                        self.i += 1

                    self.i += 1

                    decode_part = decode()

                    self.i += 1

                    res.append(decode_part * num)
            return "".join(res)

        return decode()