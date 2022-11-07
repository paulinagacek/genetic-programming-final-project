from Node import *

class Converter:

    @staticmethod
    def get_assignment(node: Node) -> str:
        if node.type != NodeType.ASSIGNMENT:
            raise Exception("Not assignment!")
        
        leftchild = node.children[0].value
        rightchild = node.children[1].value
        return str(leftchild) + "=" + str(rightchild) + ";"
    
    @staticmethod
    def get_condition(node: Node) -> str:
        if len(node.children) == 1:
            return str(node.children[0].type)
        else:
            leftchild = Converter.get_arithmetical_expr(node.children[0])
            middlechild = Converter.get_comparison(node.children[1])
            rightchild = Converter.get_arithmetical_expr(node.children[2])
            return "("+ leftchild + middlechild + rightchild+")"
    
    @staticmethod
    def get_arithmetical_expr(node: Node) -> str:
        if len(node.children) == 0:
            return str(node.value)
        elif len(node.children) == 1:
            return str(node.children[0].value)
        else:
            leftchild = Converter.get_arithmetical_expr(node.children[0])
            middlechild = Converter.get_operator(node.children[1])
            rightchild = Converter.get_arithmetical_expr(node.children[2])
            return "(" + leftchild + middlechild+rightchild + ")"
    
    @staticmethod
    def get_comparison(node: Node) -> str:
        if node.type == NodeType.EQ:
            return "=="
        elif node.type == NodeType.NOT_EQ:
            return "!="
        elif node.type == NodeType.LESS_THAN:
            return "<"
        elif node.type == NodeType.GREATER_THAN:
            return ">"
    
    @staticmethod
    def get_operator(node: Node) -> str:
        if node.type == NodeType.ADD:
            return "+"
        elif node.type == NodeType.DIV:
            return "/"
        elif node.type == NodeType.MUL:
            return "*"
        elif node.type == NodeType.SUB:
            return "-"