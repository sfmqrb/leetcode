package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	Tree := TreeNode{
		Val:   40,
		Left:  &TreeNode{Left: &TreeNode{
			Val: 60,
			Left: nil,
			Right: nil,
		}, Right: &TreeNode{
			Val: 55,
			Left: nil,
			Right: nil,
		}, Val: 50},
		Right: &TreeNode{Left: nil, Right: nil, Val: 30},
	}
	fmt.Println(invertTree(&Tree))
}

func invertTree(root *TreeNode) *TreeNode {
	return invertTreeSrcNode(root)
}

func invertTreeSrcNode(srcNode *TreeNode) *TreeNode {
	if srcNode == nil {
		return nil
	}
	srcNode.printTreeNode()
	tmpNode := TreeNode{
		Left:  invertTreeSrcNode(srcNode.Right),
		Right: invertTreeSrcNode(srcNode.Left),
		Val:   srcNode.Val,
	}
	return &tmpNode
}

func (T *TreeNode) printTreeNode() {
	if T == nil {
		fmt.Println("NIL")
	}
	fmt.Println("val: ", T.Val, "left_val: ", T.Left, "right_val: ", T.Right)
}
