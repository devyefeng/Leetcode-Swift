//
//  94.swift
//  Leetcode-Swift
//
//  Created by devyc on 2021/7/19.
//

import Foundation

/*
 94. 二叉树的中序遍历 (简单)
 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
 */

/*
 思路：
 方法一：递归
 方法二：迭代
 */

class Solution_94 {
    /// 方法一：递归
    func inorderTraversal_1(_ root: TreeNode?) -> [Int] {
        if root == nil {
            return []
        }
        var ans = [Int]()
        ans += inorderTraversal(root?.left)
        ans += [root!.val]
        ans += inorderTraversal(root?.right)
        return ans
    }
    
    /// 方法二：迭代
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        var stack = [TreeNode]()
        var node = root
        while node != nil || !stack.isEmpty {
            while node != nil {
                stack.append(node!)
                node = node?.left
            }
            node = stack.popLast()
            ans.append(node!.val)
            node = node?.right
        }
        return ans
    }
    
    func test() {
        print(inorderTraversal(createTreeNode([1,2,3,4,5,6,7])))
    }
}
