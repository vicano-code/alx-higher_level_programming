#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer of the list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[10240];
	int i, a;
	listint_t *current;

	if (head == NULL)/*no list*/
		return (0);
	if (*head == NULL)/*empty list*/
		return (1);

	current = *head;
	arr[0] = current->n;
	i = 0;
	while (current->next != NULL)
	{
		current = current->next;
		i++;
		arr[i] = current->n;
	}
	a = 0;
	if (i == 1)/*single node list*/
		return (1);
	while (a <= i) /*save node values into array & check palindrome*/
	{
		if (arr[a] != arr[i])
			return (0);
		a++;
		i--;
	}
	return (1);
}
