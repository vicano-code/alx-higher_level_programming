#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer of the list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[1024];
	int i, a;
	listint_t *current;

	if (*head == NULL)/*empty list*/
		return (1);
	if (*head != NULL && *head->next == NULL)/*single node list*/
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
	while (a <= i)
	{
		if (arr[a] != arr[i])
			return (0);
		a++;
		i--;
	}
	return (1);
}
