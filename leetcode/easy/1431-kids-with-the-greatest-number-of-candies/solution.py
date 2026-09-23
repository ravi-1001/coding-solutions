class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= maximum:
                result.append(True)

            else:
                result.append(False)

        return result