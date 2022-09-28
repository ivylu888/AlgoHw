/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode begin = head;
        ListNode end = head;
        for(int i = 1; i < k; i++){
            begin = begin.next;
        }
        
        //找到第k點 附值給fast、slow從頭開始
        ListNode slow = head;
        ListNode fast = begin;
        
        //同時前進
        while(fast.next != null){
            slow = slow.next;
            fast = fast.next;
        }
        
        end = slow;
        
        //swap
        int temp = end.val;
        end.val = begin.val;
        begin.val = temp;
        
        return head;
    }
}
