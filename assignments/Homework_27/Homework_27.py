#Вставка дерева в существующее дерево
def insert_tree(root: Node, subtree: Node, parent_value: int) -> Node:
    """
    Вставляет subtree как поддерево к узлу с value == parent_value
    """

    if root is None:
        return subtree

    if root.value == parent_value:
        # вставка в свободное место
        if root.left is None:
            root.left = subtree
        elif root.right is None:
            root.right = subtree
        else:
            raise ValueError("У вузла вже зайняті обидві гілки")
        return root

    if root.left:
        insert_tree(root.left, subtree, parent_value)

    if root.right:
        insert_tree(root.right, subtree, parent_value)

    return root

# Удаление поддерева
def delete_subtree(root: Node, parent_value: int, side: str) -> Node:
    """
    side: 'left' або 'right'
    """

    if root is None:
        return None

    if root.value == parent_value:
        if side == "left":
            root.left = None
        elif side == "right":
            root.right = None
        else:
            raise ValueError("side має бути 'left' або 'right'")
        return root

    if root.left:
        delete_subtree(root.left, parent_value, side)

    if root.right:
        delete_subtree(root.right, parent_value, side)

    return root
