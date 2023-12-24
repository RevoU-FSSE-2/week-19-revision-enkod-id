class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def max_tree_depth(tree):
   if not tree:
       return 0
   else:
       left_depth = max_tree_depth(tree[1])
       right_depth = max_tree_depth(tree[3])
       return max(left_depth, right_depth) + 1

def run_tree_depth(input_tree):
   return max_tree_depth(input_tree)

input_tree = [3, 9, 20, None, None, 15, 7]
result = run_tree_depth(input_tree)
print(result)
