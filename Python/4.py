""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root.left is not None:
        if root.data < root.left.data:
            return "No"
        elif not check_binary_search_tree_(root.left):
            return "No"
    if root.right is not None:
        if root.data > root.right.data:
            return "No"
        elif not check_binary_search_tree_(root.right):
            return "No"
    
    return "Yes"

