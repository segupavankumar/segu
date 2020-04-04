class Tree:
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
     def tree(self):
         return self.data
root=Tree('A')
root.left=Tree('B')
root.right=Tree('C')
root.left.left=Tree('d')
root.left.right=Tree('e')
root.right.left=Tree('f')
root.right.right=Tree('g')
def Postorder():
     print('Tree in Preorder is ',root.left.left.tree(),root.left.right.tree(),root.left.tree(),' ',root.right.left.tree(),root.right.right.tree(),root.right.tree(),' ',root.tree())
def Preorder():
    print('Tree in Preorder is ',root.tree(),' ',root.left.tree(),root.left.left.tree(),root.left.right.tree(),' ',root.right.tree(),root.right.left.tree(),root.right.right.tree())
Postorder()
Preorder()


#out put
# Tree in Preorder is  d e B   f g C   A
# Tree in Preorder is  A   B d e   C f g
