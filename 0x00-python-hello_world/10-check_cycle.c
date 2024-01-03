#include "lists.h"

/**
 * listint_len - number of elements in a linked listint_t list
 * @h: the listint_t list
 * Return: the number of elements
 */

size_t listint_len(const listint_t *h)
{
	size_t elem_count = 0;

	while (h)
	{
		if (h->n)
			elem_count++;

		h = h->next;
	}

	return (elem_count);
}

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *current, *tmp;

	if (list == NULL)
		return (0);
	current = list;
	tmp = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == tmp)
			return (1);
	}
	return (0);
}
