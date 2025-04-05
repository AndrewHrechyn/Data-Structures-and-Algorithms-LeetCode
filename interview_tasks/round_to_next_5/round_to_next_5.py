class Solution:

    def __init__(self):
        pass

    def round_to_next_5_v1(self, n):
        if n % 5 == 0:
            return n
        else:
            return (n - (n % 5)) + 5

    def round_to_next_5_v2(self, n):
        if n % 5 == 0:
            return n
        else:
            temp = n // 5
            return 5 * temp + 5

if __name__ == '__main__':

    solution = Solution()

    print(solution.round_to_next_5_v1(6))
    print(solution.round_to_next_5_v2(10))
    #6 % 5 == 1
    #7 // 5 == 1
    #2 // 5 == 0
