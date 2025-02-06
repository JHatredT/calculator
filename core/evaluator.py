from core.parser import ParseTree
from core.dlm import Delimiter


class Evaluator:
    def evaluate(self, tree: ParseTree) -> float:
        output = []
        for node in tree.nodes:
            if type(node) == float:
                output.append(node)
                continue

            if len(output) < node.arity:
                raise ValueError
            
            output.append(node(output.pop(-i-1) for i in range(node.arity)[::-1]))

        return output[0]