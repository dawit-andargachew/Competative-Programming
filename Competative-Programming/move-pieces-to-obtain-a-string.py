class Solution:
    def canChange(self, start: str, target: str) -> bool:

        n = len(start) - 1
        begin = [0, n]
        goal = [0, n]

        while begin[0] < begin[1] and goal[0] < goal[1]:

            # search for the first L or R in start from the beginning
            while begin[0] < begin[1] and start[begin[0]] == "_":
                begin[0] += 1
            # search for L or R in target 
            while goal[0] < goal[1] and target[goal[0]] == "_":
                goal[0] += 1
            
            # print("left")
            # print(begin[0], " -> ", start[begin[0]], " and ", goal[0], target[goal[0]])
            # case-1: if target is L and R
            if target[goal[0]] == "L":
                if goal[0] > begin[0] or start[begin[0]] == "R":
                    return False
            elif target[goal[0]] == "R":
                if goal[0] < begin[0] or start[begin[0]] == "L":
                    return False
            
            # ------------------- searching for L and R from end
            while goal[1] > goal[0] and target[goal[1]] == "_":
                goal[1] -= 1
            while begin[1] > begin[0] and start[ begin[1] ] == "_":
                begin[1] -= 1
            
            # check
            # print("\n for right")
            # print(begin[1], " -> ", start[begin[1]], " and ", goal[1], target[goal[1]])
            if target[ goal[1] ] == "L":
                if goal[1] > begin[1] or start[begin[1]] == 'R':
                    return False
            elif target[goal[1]] == 'R':
                if goal[1] < begin[1] or start[begin[1]] == "L":
                    return False
            
            begin[0] += 1
            begin[1] -= 1
            
            goal[0] += 1
            goal[1] -= 1
        
        # check the number of L and R
        one = defaultdict(int)
        two = defaultdict(int)

        for i in start:
            one[i] += 1
        for i in target:
            two[i] += 1

        if one['L'] != two["L"] or one["R"] != two["R"]:
            return False

        return True