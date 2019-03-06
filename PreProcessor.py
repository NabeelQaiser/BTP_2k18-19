class PreProcessor:

    def __init__(self, fileSpec, fileData):
        self.fileSpec = fileSpec
        self.fileData = fileData

    def getSpec(self):
        with open(self.fileSpec, 'r') as f:
            lines = f.readlines()
            tableInfo = dict()      # format : {'tableName': [(attr, nullity), (attr, nullity), ...]}
            assumeConstraint = []        # list of strings
            assertConstraint = []        # list of strings
            isEnd = False
            for line in lines:
                if not isEnd:
                    line = line.upper()
                    line = line.strip()
                    tokens = line.split('::')
                    tokens[0] = tokens[0].strip()
                    if len(tokens[0]) > 0:
                        if tokens[0] == 'ASSUME':
                            assumeConstraint = tokens[1].strip().split(',')
                            for i in range(len(assumeConstraint)):
                                assumeConstraint[i] = assumeConstraint[i].strip()
                                assumeConstraint[i] = assumeConstraint[i].strip('(')
                                assumeConstraint[i] = assumeConstraint[i].strip(')')
                        elif tokens[0] == 'ASSERT':
                            isEnd = True
                            assertConstraint = tokens[1].strip().split(',')
                            for i in range(len(assertConstraint)):
                                assertConstraint[i] = assertConstraint[i].strip()
                                assertConstraint[i] = assertConstraint[i].strip('(')
                                assertConstraint[i] = assertConstraint[i].strip(')')
                        else:
                            temp = []
                            attr = tokens[1].strip().split(',')
                            for i in range(len(attr)):
                                pair = (attr[i].split(':')[0].strip(), attr[i].split(':')[1].strip())
                                temp.append(pair)
                            tableInfo[tokens[0].strip()] = temp
                else:
                    break
            return tableInfo, assumeConstraint, assertConstraint



    def start(self):
        tableInfo, assumeConstraint, assertConstraint = self.getSpec()
        assumeConstraintString = ""
        for i in range(len(assumeConstraint)-1):
            assumeConstraintString = assumeConstraintString + assumeConstraint[i] + " AND "
        assumeConstraintString = assumeConstraintString + assumeConstraint[len(assumeConstraint)-1]
        assumeConstraintString = assumeConstraintString.strip()

        assertConstraintString = ""
        for i in range(len(assertConstraint)-1):
            assertConstraintString = assertConstraintString + assertConstraint[i] + " AND "
        assertConstraintString = assertConstraintString + assertConstraint[len(assertConstraint)-1]
        assertConstraintString = assertConstraintString.strip()

        f = open(self.fileData, "r")
        content = f.read().upper()
        f.close()
        temp = content.strip().split("BEGIN")
        result = ""
        result = result + temp[0] + "BEGIN\n\t" + "ASSUME " + assumeConstraintString + " ;\n" + temp[1]
        for i in range(2, len(temp)):
            result = result + "BEGIN" + temp[i]

        temp = result.strip().split("END")
        result = temp[0]
        for i in range(1, len(temp)-1):
            result = result + "END" + temp[i]
        result = result + "ASSERT " + assertConstraintString + " ;\n\t" + "END" + temp[len(temp)-1]
        return tableInfo, assumeConstraint, assertConstraint, result
