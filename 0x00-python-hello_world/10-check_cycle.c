#include "lists.h"

/**
 * check_cycle - cihecks if a singly linked list has a cycle in it
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
	while (1)
	{
		if (current->next != NULL)
		{
			current = current->next;
			if (current == tmp)
				return (1);
		}
		else
			return (0);
	}
}
