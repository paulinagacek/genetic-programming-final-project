from src.Node import *


class Converter:

    @staticmethod
    def get_assignment(node: Node) -> str:
        if node.type != NodeType.ASSIGNMENT:
            raise Exception("Not assignment!")

        leftchild = node.children[0].value
        rightchild = None
        if node.children[1].type == NodeType.ARITHMETICAL_OP:
            rightchild = Converter.get_arithmetical_op(
                node.children[1])
        elif node.children[1].type == NodeType.INPUT:
            rightchild = "input"
        elif node.children[1].type == NodeType.READ:
            rightchild = Converter.get_read(node.children[1])
        else:
            rightchild = node.children[1].value
        return str(leftchild) + "=" + str(rightchild) + ";"

    @staticmethod
    def get_comparison(node: Node) -> str:
        leftchild = Converter.get_arithmetical_op(
            node.children[0]) if node.children[0].type == NodeType.ARITHMETICAL_OP else node.children[0].value
        middlechild = node.value
        rightchild = Converter.get_arithmetical_op(
            node.children[1]) if node.children[1].type == NodeType.ARITHMETICAL_OP else node.children[1].value
        return str(leftchild) + middlechild + str(rightchild)

    @staticmethod
    def get_arithmetical_op(node: Node) -> str:
        leftchild = None
        if node.children[0].type == NodeType.ARITHMETICAL_OP:
            leftchild = str(Converter.get_arithmetical_op(node.children[0]))
        elif node.children[0].type == NodeType.READ:
            leftchild = Converter.get_read(node.children[0])
        else:
            leftchild = str(node.children[0].value)
        middlechild = node.value
        rightchild = None
        if node.children[1].type == NodeType.ARITHMETICAL_OP:
            rightchild = str(Converter.get_arithmetical_op(node.children[1]))
        elif node.children[1].type == NodeType.READ:
            rightchild = Converter.get_read(node.children[1])
        else:
            rightchild = str(node.children[1].value)
        return leftchild + middlechild+ rightchild

    @staticmethod
    def get_logical_op(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        middlechild = node.value
        right_child = Converter.get_logical_op(
            node.children[1]) if node.children[1].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[1])
        return "(" + str(left_child) + ")" + middlechild+"("+str(right_child) + ")"

    @staticmethod
    def get_conditional_statement(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        right_child = Converter.get_proper_node(node.children[1])
        return "IF(" + str(left_child) + ")" + right_child + ";"

    @staticmethod
    def get_loop(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        right_child = Converter.get_proper_node(node.children[1])
        return "LOOP(" + str(left_child) + ")" + right_child + ";"

    @staticmethod
    def get_print(node: Node) -> str:
        # print("node:", node.type, node.children)
        child = Converter.get_arithmetical_op(
            node.children[0]) if node.children[0].type == NodeType.ARITHMETICAL_OP else node.children[0].value
        return "print(" + str(child) + ");"
    
    @staticmethod
    def get_read(node: Node) -> str:
        child =  node.children[0].value
        return "read(" + str(child) + ");"

    @staticmethod
    def get_proper_node(node: Node) -> str:
        if node.type == NodeType.SEQUENCE:
            output = ""
            for child in node.children:
                output += Converter.get_proper_node(child)
            return output
        elif node.type == NodeType.INSTRUCTION:
            return Converter.get_proper_node(node.children[0])
        elif node.type == NodeType.ASSIGNMENT:
            return Converter.get_assignment(node)
        elif node.type == NodeType.LOOP:
            return Converter.get_loop(node)
        elif node.type == NodeType.CONDITIONAL_STATEMENT:
            return Converter.get_conditional_statement(node)
        elif node.type == NodeType.PRINT:
            return Converter.get_print(node)
        elif node.type == NodeType.READ:
            print("-----------read------------")
            return Converter.get_read(node)
