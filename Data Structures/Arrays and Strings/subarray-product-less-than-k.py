class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest_key = [keysPressed[0], releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > slowest_key[1]:
                slowest_key = [keysPressed[i], duration]
            elif duration == slowest_key[1]:
                alphabetical_order = max(slowest_key[0], keysPressed[i])
                slowest_key = [alphabetical_order, duration]
        return slowest_key[0]
