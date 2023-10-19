class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions *=4
        face = 'N'
        pos = {'x':0,'y':0}
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                match face:
                    case 'N':
                        pos['y']+=1
                    case 'S':
                        pos['y']-=1
                    case 'E':
                        pos['x']+=1
                    case 'W':
                        pos['x']-=1
            elif instructions[i] == 'L':
                match face:
                    case 'N':
                        face = 'W'
                    case 'S':
                        face = 'E'
                    case 'E':
                        face = 'N'
                    case 'W':
                        face = 'S'
            else:
                match face:
                    case 'N':
                        face = 'E'
                    case 'E':
                        face = 'S'
                    case 'S':
                        face='W'
                    case 'W':
                        face = 'N'
            
        if pos['x']==pos['y'] and pos['x'] == 0:
            return True
        return False