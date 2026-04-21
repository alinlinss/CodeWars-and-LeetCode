def tree_by_levels(node):
    if not node:
        return []

    row = [node]
    final = []
    while row:
        curr = row.pop(0)
        final.append(curr.value)

        if curr.left:
            row.append(curr.left)

        if curr.right:
            row.append(curr.right)

    return final
