/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    TreeNode target, answer;
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        this.target = target;
        inorder(original, cloned);
        
        return answer;
    }

    public void inorder(TreeNode orig, TreeNode cloned) {

        if (orig != null) {

            inorder(orig.left, cloned.left);

            if (orig == target)
                answer = cloned;

            inorder(orig.right, cloned.right);
        }

    }
}