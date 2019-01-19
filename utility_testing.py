from MyCFG import MyCFG

from MyUtility import MyUtility

from MyNode import MyNode


def main():
    cfg = MyCFG()
    utility = MyUtility()
    cfg.addNode(MyNode(0))
    cfg.addNode(MyNode(1))
    cfg.addNode(MyNode(2))
    cfg.addNode(MyNode(3))
    cfg.addNode(MyNode(4))
    cfg.connect(0, 1)
    cfg.connect(0, 2)
    cfg.connect(2, 4)
    cfg.connect(4, 2)
    cfg.connect(2, 3)
    cfg.connect(1, 3)
    cfg.printPretty()
    print("Dominator set started ----------->\n\n")
    utility.generateDomSet(cfg)
    print("Dominator set ended----------->\n\n")
    utility.generateSDomSet(cfg)
    print("Strictly Dominator set ended ----------->\n\n")
    utility.generatIDom(cfg)
    print("Immediate Dominator ended ----------->\n\n")
    utility.generateDFSet(cfg)
    print("Dominator Frontier set ended ----------->\n\n")
    for i in cfg.nodes:
        print(i, " --> ", cfg.nodes[i].domSet)
    print("Strictly Dominator set ----------->\n\n")
    for i in cfg.nodes:
        print(i, " --> ", cfg.nodes[i].sDomSet)
    print("Immediate Dominator ----------->\n\n")
    for i in cfg.nodes:
        print(i, " --> ", cfg.nodes[i].iDom)
    print("Dominator Frontier set ----------->\n\n")
    for i in cfg.nodes:
        print(i, " --> ", cfg.nodes[i].DFSet)

if __name__=='__main__':
    main()
