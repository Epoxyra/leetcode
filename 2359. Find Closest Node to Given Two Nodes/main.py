class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def get_distances(start: int) -> dict:
            dist = {}
            current = start
            d = 0
            while current != -1 and current not in dist:
                dist[current] = d
                current = edges[current]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_distance = float('inf')
        result_node = -1

        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_distance:
                    min_distance = max_dist
                    result_node = i
                elif max_dist == min_distance and i < result_node:
                    result_node = i

        return result_node