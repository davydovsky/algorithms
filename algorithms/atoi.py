class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        n = len(s)

        result = 0
        sign = 1
        place = 0

        for i in range(n):
            if i == 0 and s[i] in ('-', '+'):
                if s[i] == '-':
                    sign = -1
                continue
            try:
                num = int(s[i])
                if place:
                    result_1 = result * place
                    result = result_1 + num
                else:
                    result = num
                    place = 10
            except ValueError:
                break

        return result * sign


if __name__ == '__main__':
    s = Solution()
    s.myAtoi("4193 with words")
