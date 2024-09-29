struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {

    ListNode sentinel = ListNode(0);
    ListNode *head = &sentinel;
    ListNode *temp;

    while ((list1 != nullptr) || (list2 != nullptr)) {
      if (list1 == nullptr) {
        head->next = list2;
        break;
      }

      if (list2 == nullptr) {
        head->next = list1;
        break;
      }

      if (list1->val <= list2->val) {
        temp = list1->next;
        list1->next = nullptr;
        head->next = list1;
        head = head->next;
        list1 = temp;
      } else {
        temp = list2->next;
        list2->next = nullptr;
        head->next = list2;
        head = head->next;
        list2 = temp;
      }
    }

    return sentinel.next;
  }
};