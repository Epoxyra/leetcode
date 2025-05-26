import math
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        point_distance_queue = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(point_distance_queue, ((distance, point)))
        k_closest = []
        while len(k_closest) < k:
            closest_point = heapq.heappop(point_distance_queue)[1]
            k_closest.append(closest_point)
        return k_closest
