# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        out = [0]
        maximum = 0
        for i in range(len(gain)):
            out.append(out[i] + gain[i])
            if out[i+1] > maximum:
                maximum = out[i+1]

        return maximum
        