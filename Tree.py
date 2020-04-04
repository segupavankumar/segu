class Tree:
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
     def tree(self):
         return self.data
t='\t'
root=Tree('A')
root.left=Tree('B')
root.right=Tree('C')
root.left.left=Tree('d')
root.left.right=Tree('e')
root.right.left=Tree('f')
root.right.right=Tree('g')
def Inorder():
    print('Tree in Inorder is  ',root.left.left.tree(),root.left.tree(),root.left.right.tree(),' ',root.tree(),' ',root.right.left.tree(),root.right.tree(),root.right.right.tree())
def Preorder():
    print('Tree in Preorder is ',root.tree(),' ',root.left.tree(),root.left.left.tree(),root.left.right.tree(),' ',root.right.tree(),root.right.left.tree(),root.right.right.tree())
def Postorder():
     print('Tree in Preorder is ',root.left.left.tree(),root.left.right.tree(),root.left.tree(),' ',root.right.left.tree(),root.right.right.tree(),root.right.tree(),' ',root.tree())
Inorder()
Preorder()
Postorder()


#OUT PUT
# Tree in Inorder is   d B e   A   f C g
# Tree in Preorder is  A   B d e   C f g
# Tree in Preorder is  d e B   f g C   A
