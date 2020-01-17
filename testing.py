from binary_tree import Node
root = Node(10)
toadd = [7, 8, 2, 6, 9, 4,11, 1,13,3,15,16,14, 5,12]
#root = Node(4)
#toadd = [3,2,1,6,5]
for i in toadd:
    root.insert(i)
root.show_tree()

#root.print_tree()

