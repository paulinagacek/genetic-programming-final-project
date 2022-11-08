from Node import *


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
        else:
            rightchild = node.children[0].value
        return str(leftchild) + "=" + str(rightchild) + ";"

    @staticmethod
    def get_comparison(node: Node) -> str:
        leftchild = Converter.get_arithmetical_op(
            node.children[0]) if node.children[0].type == NodeType.ARITHMETICAL_OP else node.children[0].value
        middlechild = node.value
        rightchild = Converter.get_arithmetical_op(
            node.children[1]) if node.children[1].type == NodeType.ARITHMETICAL_OP else node.children[1].value
        return "(" + str(leftchild) + middlechild + str(rightchild)+")"

    @staticmethod
    def get_arithmetical_op(node: Node) -> str:
        leftchild = Converter.get_arithmetical_op(
            node.children[0]) if node.children[0].type == NodeType.ARITHMETICAL_OP else node.children[0].value
        middlechild = node.value
        rightchild = Converter.get_arithmetical_op(
            node.children[1]) if node.children[1].type == NodeType.ARITHMETICAL_OP else node.children[1].value
        return "(" + str(leftchild) + middlechild+str(rightchild) + ")"

    @staticmethod
    def get_logical_op(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        middlechild = node.value
        right_child = Converter.get_logical_op(
            node.children[1]) if node.children[1].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[1])
        return "(" + str(left_child) + middlechild+str(right_child) + ")"

    @staticmethod
    def get_conditional_statement(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        right_child = Converter.get_proper_node(node.children[1])
        return "IF" + str(left_child) + right_child + ";"

    @staticmethod
    def get_loop(node: Node) -> str:
        left_child = Converter.get_logical_op(
            node.children[0]) if node.children[0].type == NodeType.LOGICAL_OP else Converter.get_comparison(node.children[0])
        right_child = Converter.get_proper_node(node.children[1])
        return "LOOP" + str(left_child) + right_child + ";"

    @staticmethod
    def get_print(node: Node) -> str:
        leftchild = Converter.get_arithmetical_op(
            node.children[0]) if node.children[0].type == NodeType.ARITHMETICAL_OP else node.children[0].value
        return "print" + str(leftchild) + ";"

    @staticmethod
    def get_proper_node(node: Node) -> str:
        if node.type == NodeType.SEQUENCE:
            output = ""
            for child in node.children:
                output += Converter.get_proper_node(child)
            return output
        elif node.type == NodeType.ASSIGNMENT:
            return Converter.get_assignment(node)
        elif node.type == NodeType.LOOP:
            return Converter.get_loop(node)
        elif node.type == NodeType.CONDITIONAL_STATEMENT:
            return Converter.get_conditional_statement(node)
        elif node.type == NodeType.PRINT:
            return Converter.get_print(node)
