/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int sum = 0;
    int low = 0;
    int high = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        this.low = low;
        this.high = high;
        inorder(root);
        return sum;   
    }


    public void inorder(TreeNode root){
        if(root != null){
            inorder(root.left);
            
            if(root.val >= low && root.val <= high)
                sum += root.val;

            inorder(root.right);
        }
    }
}