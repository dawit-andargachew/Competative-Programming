class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # at each time decrease the processessing time by one
        for i in range( len(tasks) ):
            tasks[i].append(i)

        heapify(tasks)
        processQueue, order = [], []
        time = 0 # initial time

        while tasks or processQueue:
            curr_task = []

            if not processQueue:
                curr_task = heappop(tasks)
                time =curr_task[0] +  curr_task[1] # increase the global time by current task ending
                curr_task = [curr_task[1], curr_task[2]] # just take [endTime, index], arriving time is not needed
            else:
                curr_task = heappop(processQueue)
                time += curr_task[0] # icreaset the global time

            order.append( curr_task[1] ) # grap the order

            # take every task which arrives while curr_task is excecuting
            while tasks and time >= tasks[0][0]:
                a = heappop(tasks)
                heapq.heappush(processQueue, [ a[1], a[2]])

        return order