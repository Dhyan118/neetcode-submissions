class Solution:
    def calculate(self, s: str) -> int:
        operators = ["+", "-", "/", "*"]
        stack = []

        curr_num = 0

        pre_operator = "+"

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

                if pre_operator == "+":
                    stack.append(curr_num)
                elif pre_operator == "-":
                    stack.append(-curr_num)
                elif pre_operator == "*":
                    last_val = stack.pop()
                    stack.append(last_val * curr_num)
                elif pre_operator == "/":
                    last_val = stack.pop()
                    stack.append(int(last_val / curr_num))

                pre_operator = ch
                curr_num = 0

        return sum(stack)

        # s = "3+2*2"
# Step by step:

# read 3 → num = 3
# hit +:
# previous sign = +
# push 3
# stack = [3]
# sign = +
# read 2 → num = 2
# hit *:
# previous sign = +
# push 2
# stack = [3, 2]
# sign = *
# read 2 and end:
# previous sign = *
# pop 2, compute 2*2=4
# stack = [3, 4]
# Final:

# sum(stack) = 7operators = ["+", "-", "/", "*"]
        stack = []

        curr_num = 0

        pre_operator = "+"

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

                if pre_operator == "+":
                    stack.append(curr_num)
                elif pre_operator == "-":
                    stack.append(-curr_num)
                elif pre_operator == "*":
                    last_val = stack.pop()
                    stack.append(last_val * curr_num)
                elif pre_operator == "/":
                    last_val = stack.pop()
                    stack.append(int(last_val / curr_num))

                pre_operator = ch
                curr_num = 0

        return sum(stack)

        # s = "3+2*2"
# Step by step:

# read 3 → num = 3
# hit +:
# previous sign = +
# push 3
# stack = [3]
# sign = +
# read 2 → num = 2
# hit *:
# previous sign = +
# push 2
# stack = [3, 2]
# sign = *
# read 2 and end:
# previous sign = *
# pop 2, compute 2*2=4
# stack = [3, 4]
# Final:

# sum(stack) = 7