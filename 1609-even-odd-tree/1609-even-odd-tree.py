# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        # all even nodes are odd, so checking starts at root node
        if root.val % 2 != 1:
            return False

        q = deque()
        q.append( root )
        level = -1
        isOddEven = True

        while q and isOddEven:
            width = len(q)
            level += 1
            temp = []

            for i in range(width):
                if q[0].left:
                    q.append(q[0].left)

                if q[0].right:
                    q.append( q[0].right )
                
                temp.append( q[0].val )
                q.popleft()

            # for odd level, even integer in striclty decreasing order
            if level % 2 == 1: 
                
                # when the level only have a single element check wheather the element is odd or not
                if len(temp) == 1 and temp[0]%2 != 0:
                    return False

                for i in range( len(temp) - 1):
                    if not (temp[i] > temp[i + 1] and temp[i]%2 == 0 and temp[i + 1]%2 == 0):
                        return False
            
            # for even level, odd integers in strictly increasing odrder
            elif level > 0 and level % 2 == 0:

                # when the level only have single element chech weather the element is even or not
                if len(temp) == 1 and temp[0]%2 != 1:
                    return False

                for i in range( len(temp) - 1):
                    if not (temp[i] < temp[i + 1] and temp[i]%2 == 1 and temp[i + 1]%2 == 1):
                        return False

        return isOddEven