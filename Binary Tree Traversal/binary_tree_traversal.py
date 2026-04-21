def pre_order(node):
    if node is None:
        return []
    result = [node.data]
    result += pre_order(node.left)
    result += pre_order(node.right)
    return result

def in_order(node):
    if node is None:
        return []
    result = in_order(node.left)
    result += [node.data]
    result += in_order(node.right)
    return result

def post_order(node):
    if node is None:
        return []
    result = post_order(node.left)
    result += post_order(node.right)
    result += [node.data]
    return result
