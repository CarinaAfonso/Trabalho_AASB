
import sys

class BinaryTree:

    def __init__(self, val, dist=0, left = None, right = None):
        self.value = val
        self.distance = dist
        self.left = left
        self.right = right
        
    def getCluster(self):
        res = []
        if self.value >= 0:
            res.append(self.value)
        else:
            if (self.left!= None):
                res.extend(self.left.getCluster())
            if (self.right!= None):
                res.extend(self.right.getCluster())
        return res    

    def printtree(self):
        self.printtreerec(0, "Root")
        
    def printtree2(self):
        self.printtreerec(0, "Root")
        
    def printtreerec (self, level, side):
        for i in range(level): sys.stdout.write("\t")
        al = self.getCluster();
        sys.stdout.write(side + ":" + str(al)+ " Dist.: " + str(self.distance) + "\n")
        if self.value < 0:
            if (self.left != None): 
                self.left.printtreerec(level+1, "Left")
            else: 
                sys.stdout.write("Null")
            if (self.right != None): 
                self.right.printtreerec(level+1, "Right")
            else: 
                sys.stdout.write("Null\n")
    
    def printtree_rec2(self, level, side):
        tabs = ""
        for i in range(level): 
            tabs += "\t"
        if self.value >= 0:
            print(tabs, side, " -value:", self.value)
        else:
            print(tabs, side, "-Dist.: ", self.distance)
            if self.left != None:
                self.left.printtree_rec(level+1, "Left")
            if self.right != None:
                self.right.printtree_rec(level+1, "Right")


def test():              
    a = BinaryTree(1)
    b = BinaryTree(2)
    c = BinaryTree(3)
    d = BinaryTree(4)
    e = BinaryTree(-1, 2.0, a, b)
    f = BinaryTree(-1, 3.0, c, d)
    g = BinaryTree(-1, 4.0, e, f)
    g.printtree()
    g.printtree2()
    

if __name__ == '__main__':
    test()
    
# Result for test
# Root:[1, 2, 3, 4] Dist.: 4.0
#     Left:[1, 2] Dist.: 2.0
#         Left:[1] Dist.: 0
#         Right:[2] Dist.: 0
#     Right:[3, 4] Dist.: 3.0
#         Left:[3] Dist.: 0
#         Right:[4] Dist.: 0

