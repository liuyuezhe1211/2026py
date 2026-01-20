# 作者: 刘悦喆
# 2026年01月20日11时00分34秒
# liuyuezhe1211@163.com

class BNode(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Btree:
    def __init__(self):
        self.root=None
        self.help_queue=[]

    def level_build_tree(self,node:BNode):
        if self.root is None:
            self.root=node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild=node
            else:
                self.help_queue[0].rchild=node
                self.help_queue.pop(0) #对每个队头元素操作，在将其左孩子，右孩子都放入后，就出辅助队列，对下一个元素操作

    def pre_order(self,current_node:BNode): #前序遍历
        if current_node:
            print(current_node.elem,end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def mid_order(self,current_node:BNode):
        if current_node:
            self.mid_order(current_node.lchild)
            print(current_node.elem,end=' ')
            self.mid_order(current_node.rchild)

    def last_order(self,current_node:BNode):
        if current_node:
            self.last_order(current_node.lchild)
            self.last_order(current_node.rchild)
            print(current_node.elem,end=' ')

    def level_order(self):
        help_queue=[]
        help_queue.append(self.root)
        while help_queue:
            out_node=help_queue.pop(0)
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)
            print(out_node.elem,end=' ')

if __name__ == '__main__':
    tree=Btree()
    for i in range(1,11):
        new_node=BNode(i)
        tree.level_build_tree(new_node)
    tree.pre_order(tree.root)
    print(' ')
    tree.mid_order(tree.root)
    print(' ')
    tree.last_order(tree.root)
    print(' ')
    tree.level_order()