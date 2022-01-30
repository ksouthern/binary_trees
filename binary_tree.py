"""
Based on the code provided at: https://github.com/laurentluce/python-algorithms/blob/master/algorithms/binary_tree.py
Extended to AVL trees by Karl Southern
"""
from tkinter import *
import copy


class Node:
    """
    Tree node: left and right child + data which can be any object
    """

    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data
        self.parent = None



    def lookup(self, data, parent=None):
        """
        Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def refresh_parents(self):
        if self.left:
            self.left.parent = self
            self.left.refresh_parents()
        if self.right:
            self.right.parent = self
            self.right.refresh_parents()

    def children_count(self):
        """
        Returns the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def count_levels(self):
        """
        Count the number of levels in the tree
        """
        lcount = 0
        rcount = 0
        if self.left:
            lcount = self.left.count_levels()
        if self.right:
            rcount = self.right.count_levels()
        return 1 + max(lcount, rcount)

    def get_coords(self, x, y, sw, sh):
        tosend = [[x, y, self.data]]
        if self.left:
            tosend = tosend + (self.left.get_coords(x - sw / 2, y + sh, sw / 2, sh))
        if self.right:
            tosend = tosend + (self.right.get_coords(x + sw / 2, y + sh, sw / 2, sh))
        return tosend

    def get_lines(self, x, y, sw, sh):
        tosend = []
        if self.left:
            l = self.left.get_coords(x - sw / 2, y + sh, sw / 2, sh)
            tosend = tosend + [[x, y, l[0][0], l[0][1]]]
            tosend = tosend + self.left.get_lines(x - sw / 2, y + sh, sw / 2, sh)
        if self.right:
            r = self.right.get_coords(x + sw / 2, y + sh, sw / 2, sh)
            tosend = tosend + [[x, y, r[0][0], r[0][1]]]
            tosend = tosend + self.right.get_lines(x + sw / 2, y + sh, sw / 2, sh)
        return tosend

    def show_tree(self):
        h = self.count_levels()
        w = 2 ** (h - 1)
        sh = 512 * 1.25
        sw = 512 * 1.5
        r = sw / w / 2
        if r >=10:
            r = 10
        window = Tk()
        window.title("Binary Tree")  # Set a title
        canvas = Canvas(window, width=sw + 100, height=sh + 100, bg="white")
        canvas.pack()
        sh = int((sh - 2 * h * r) / (h))
        toshow = self.get_lines(50 + sw / 2, 50 + r, sw / 2, sh)
        for i in toshow:
            x1 = i[0]
            y1 = i[1]
            x2 = i[2]
            y2 = i[3]
            canvas.create_line(x1, y1, x2, y2)
        toshow = self.get_coords(50 + sw / 2, 50 + r, sw / 2, sh)
        for i in toshow:
            x = i[0]
            y = i[1]
            text = i[2]
            if r == 10:
                canvas.create_oval(x - r, y - r, x + r, y + r, fill="white")
            canvas.create_text(x, y, text=text)

        window.mainloop()

    ########################################################################################################################
    #                                                                                                                      #
    #                                          EDIT THE CODE BELOW                                                         #
    #                                                                                                                      #
    ########################################################################################################################
    """
    1)Extend insert to add parents
    2)Implement rotate_right and rotate_left

    """
    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert

        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def delete(self, data):
        """
        Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node with its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent's child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right


    def rotate_right(self):
        """
        rotate the tree to the right such that this node becomes the right child of the new root
        N.B you can't do self = new_root, so you will need to do:
        self.data = new_root.data
        self.left = new_root.left
        self.right = new_root.right
        self.parent = new_root.parent
        """

    def rotate_left(self):
        """
        rotate the tree to the left such that this node becomes the left child of the new root
        N.B you can't do self = new_root, so you will need to do:
        self.data = new_root.data
        self.left = new_root.left
        self.right = new_root.right
        self.parent = new_root.parent
        """
