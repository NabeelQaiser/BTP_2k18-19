class PreProcessor:

    def __init__(self, fileSpec, fileData):
        self.fileSpec = fileSpec
        self.fileData = fileData

    def getSpec(self):
        with open(self.fileSpec, 'r') as f:
            lines = f.readlines()
            tableInfo = dict()      # format : {'tableName': [(attr, nullity), (attr, nullity), ...]}
            constraints = []        # list of strings
            isEnd = False
            for line in lines:
                if not isEnd:
                    line = line.upper()
                    line = line.strip()
                    tokens = line.split('::')
                    tokens[0] = tokens[0].strip()
                    if len(tokens[0]) > 0:
                        if tokens[0] == 'CONSTRAINTS':
                            isEnd = True
                            constraints = tokens[1].strip().split(',')
                            for i in range(len(constraints)):
                                constraints[i] = constraints[i].strip()
                                constraints[i] = constraints[i].strip('(')
                                constraints[i] = constraints[i].strip(')')
                        else:
                            temp = []
                            attr = tokens[1].strip().split(',')
                            for i in range(len(attr)):
                                pair = (attr[i].split(':')[0].strip(), attr[i].split(':')[1].strip())
                                temp.append(pair)
                            tableInfo[tokens[0].strip()] = temp
                else:
                    break
            return tableInfo, constraints



    def start(self):
        tableInfo, constraints = self.getSpec()
        constraintString = ""
        for i in range(len(constraints)-1):
            constraintString = constraintString + constraints[i] + " AND "
        constraintString = constraintString + constraints[len(constraints)-1]
        constraintString = constraintString.strip()

        f = open(self.fileData, "r")
        content = f.read().upper()
        f.close()
        temp = content.strip().split("BEGIN")
        result = ""
        result = result + temp[0] + "BEGIN\n\t" + "ASSUME " + constraintString + " ;\n" + temp[1]
        for i in range(2, len(temp)):
            result = result + "BEGIN" + temp[i]

        temp = result.strip().split("END")
        result = temp[0]
        for i in range(1, len(temp)-1):
            result = result + "END" + temp[i]
        result = result + "ASSERT " + constraintString + " ;\n\t" + "END" + temp[len(temp)-1]
        return tableInfo, constraints, result
