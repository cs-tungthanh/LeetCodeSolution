# https://leetcode.com/problems/add-two-numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Sol1:
    def getValueFromList(self, lst: [ListNode]):
        runner = lst
        stack = []
        while (runner != None):
            stack.insert(0, str(runner.val))
            runner = runner.next
        return int("".join(stack))
    
    def convertToStringList(self, string):
        list1 = []
        list1[:0] = string
        return list1
    
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getValueFromList(l1);
        num2 = self.getValueFromList(l2);
        result = self.convertToStringList(str(num1+num2));
        node = None;
        for item in result:
            node = ListNode(int(item), node);
        return node;

class Sol2: #more efficient runtime
    def solve(self, l1, l2):
        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val);
        return res.next;
            
