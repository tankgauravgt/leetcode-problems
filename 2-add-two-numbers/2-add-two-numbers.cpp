/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* hx;
        ListNode* tx;
        hx = tx = new ListNode();
        
        int s = 0;
        int c = 0;
        while (l1 != nullptr and l2 != nullptr) {
            
            // calculation:
            s = l1->val + l2->val + c;
            c = s / 10;
            
            // filling the values and appending the list:
            tx->next = new ListNode(s % 10);
            
            // updating pointers:
            tx = tx->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        
        while (l1 != nullptr) {
            
            // calculation:
            s = l1->val + c;
            c = s / 10;
            
            // filling the values and appending the list:
            tx->next = new ListNode(s % 10);
            
            // updating pointers:
            tx = tx->next;
            l1 = l1->next;
        }
        
        while (l2 != nullptr) {
            
            // calculation:
            s = l2->val + c;
            c = s / 10;
            
            // filling the values and appending the list:
            tx->next = new ListNode(s % 10);
            
            // updating pointers: 
            tx = tx->next;
            l2 = l2->next;
        }

        if (c != 0) {
            tx->next = new ListNode(c);
        }
        
        return hx->next;
    }
};
