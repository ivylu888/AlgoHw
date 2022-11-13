"""
public class Node <T> {
    public T data;
    public Node<T> left;
    public Node<T> right;

    public Node<T> parent;

    public Node(T data){
        this.data = data;
    }
}
"""
def printParent(node:Node, val:int, parent:int):
    if not node:
        return
    if node.data == val:
        print(parent)
    else:
        printParent(node.left, val, node.data)
        printParent(node.right, val, node.data)
