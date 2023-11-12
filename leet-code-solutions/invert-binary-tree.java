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
    // see these videos
    // - https://www.youtube.com/watch?v=OnSn2XEQ4MY&t=36s
    // -https://www.youtube.com/watch?v=fKgZiCXb6zs
    public TreeNode invertTree(TreeNode root) {
        if( root == null)
            return null;
        else{
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;

            invertTree(root.left);
            invertTree(root.right);
        }
        
        return root;
    }
}