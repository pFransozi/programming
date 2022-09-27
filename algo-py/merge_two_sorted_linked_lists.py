'''


'''

def mergeLists(head1, head2):
    #sys.setrecursionlimit(2000)
    return _mergeLists(head1, head2)

def _mergeLists(head1, head2):
    
    if not head1: return head2
    if not head2: return head1
    
    if head1.data < head2.data: 
        merge = head1
        merge.next = _mergeLists(head1.next, head2)
    else:
        merge = head2
        merge.next = _mergeLists(head1, head2.next)

    return merge

