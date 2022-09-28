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
    public ListNode[] splitListToParts(ListNode root, int k) {
        ListNode[] ans = new ListNode[k];
        int len = 0;
        for(ListNode head = root; head != null; head = head.next){
            len++;
        }
        
        int l = len / k;
        int r = len % k;
        ListNode head = root;
        ListNode pre = null;
        for(int i = 0; i < k; ++i, r--){
            ans[i] = head;
            int part_len = l + ((r > 0) ? 1 : 0);
            for(int j = 0; j < part_len; j++){
                pre = head;
                head = head.next;
            }
            if(pre != null) pre.next = null;
        }
        return ans;
    }
}
