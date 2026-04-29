/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }
private:
    bool validate(TreeNode* node, long minVal, long maxVal){
        if (!node) return true;

        // current node must be in intervaal(minVal, maxVal)

        if (node -> val <= minVal || node -> val >= maxVal)
            return false;
        // Check left subtree with updated max bound
        // Check right subtree with updated min bound

        return validate(node -> left, minVal, node->val) && validate(node -> right, node->val, maxVal);

    }
};
