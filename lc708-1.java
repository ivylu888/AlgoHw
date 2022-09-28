/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

/*
case 0: only insert node exist, new a node and eturn itself
case 1: find a maximum node(since its next node is the smallest one) （要記得等於，有可能插入值（or整個cycle）值都一樣
1-1 (插入node 需是比最大值還大or最小值的)
1-2 find suitable popsition 
*/

class Solution {
    public Node insert(Node head, int insertVal) {
       Node newNode = new Node(insertVal);
        if(head == null){
            head = newNode;
            newNode.next = head;
            return head;
        }
        
        Node max = head;
        while(max.next != head && max.val <= max.next.val){
            max = max.next;//find max
        }
        
        Node min = max.next, cur = min;
        if(insertVal >= max.val || insertVal <= min.val){
            Node node = new Node(insertVal, min);
            max.next = node;
        }else{
            while(cur.next.val < insertVal){
                cur = cur.next;
            }
            
         //cur == insert || cur < insert ->insertval插在cur跟cur.next中間
            Node node = new Node(insertVal, cur.next);
            cur.next = node;
        }
        
        return head;
    }
}
