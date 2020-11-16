lnode *mergeSortedLists(lnode *head1, lnode *head2)
{
	lnode *headS = NULL;
	if(!head1)
		return head2;
	
	if(!head2)
		return head1;
	
	if(head1->data > head2->data)
	{
		headS = head2;
		headS->next = mergerSortedLists(head1, head2->next);
	}
	else
	{
		headS = head1;
		headS->next = mergeSortedLists(head1->next, head2);
	}
	
	return headS;
}
