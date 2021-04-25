from data_structures.stack import Stack


def daily_temperatures(temperatures_list: list[int]) -> list[int]:
    """The classic problem from leetcode.
    https://leetcode.com/problems/daily-temperatures/
    """

    size = len(temperatures_list)
    answer = [0] * size
    stack = Stack()

    for idx in range(size - 1, -1, -1):
        while not stack.empty and temperatures_list[stack.top] <= temperatures_list[idx]:
            stack.pop()
        answer[idx] = stack.top - idx if not stack.empty else 0
        stack.push(idx)

    return answer


if __name__ == '__main__':
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
