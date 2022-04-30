<?php
class Solution {

/**
* @param ListNode $l1
* @param ListNode $l2
* @return ListNode
*/
function addTwoNumbers($l1, $l2) {
$head = $current = new ListNode();
$valNext = 0;

while ($l1 || $l2 || $valNext) {
$val = ($l1->val ?? 0) + ($l2->val ?? 0) + $valNext;
$valNext = $val >= 10 ? 1 : 0;

$current->next = new ListNode($val % 10);
$current = $current->next;

$l1 = $l1->next;
$l2 = $l2->next;
}

return $head->next;

}
}
?>
