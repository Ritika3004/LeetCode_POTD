class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        #time 0 => person 0
        #time 0 => 0, 1
        #time 1 => 2, 3
        #time 2 => 4
        #[0, 1, 2, 3, 4]
        q=[]    #heapq
        heapq.heappush(q, (0, 0))   #time, person
        heapq.heappush(q, (0, firstPerson))

        graph = collections.defaultdict(list)
        for person_i, person_ii, time in meetings:
            graph[person_i].append((person_ii, time))
            graph[person_ii].append((person_i, time))

        answer = set()
        while q:
            time, person_i = heapq.heappop(q)
            if person_i in answer:
                continue
            answer.add(person_i)
            for person_ii, meeting_time in graph[person_i]:
                if meeting_time >= time:
                    heapq.heappush(q, (meeting_time, person_ii))
        return list(answer)
