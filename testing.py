from binary_tree import Node
root = Node(10)
toadd = [7, 4, 2, 9, 8, 15, 12, 17, 16, 18]
#root = Node(4)
#toadd = [3,2,1,6,5]
for i in toadd:
    root.insert(i)
root.show_tree()
(node15,_) = root.lookup(15)
node15.rotate_left()
root.show_tree()
root.rotate_right()
root.show_tree()

#root.print_tree()

