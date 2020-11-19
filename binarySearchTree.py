class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def search(root, key):
    if root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)
    
    return search(root.left, key)

if __name__ == '__main__':
  def question3(): 
     #put question here
     try:
       #put test code here
        r = Node(50)
        r = insert(r, 30)
        r = insert(r, 20)
        r = insert(r, 40)
        r = insert(r, 70)
        r = insert(r, 60)
        r = insert(r, 80)
        inorder(r)
     catch Exception as e:
       print('Question3 test failed with', e)

  def anotherQuestion():
    # blah

  question3()

  anotherQuestion() 


#search(r, 30)
