class Solution:

    def count_anagrams(self, list_1) -> int:

        list_1 = [i.lower() for i in list_1]

        print(list_1)

        for letter in list_1:
            temp = letter.split(' ')
            temp_1 = sorted(temp)
            print(temp_1)


if __name__ == '__main__':
    solution = Solution()

    strs = ['aBc', 'bcA', 'Cba', 'aB', 'Ba', 'BA']

    print(solution.count_anagrams(strs))