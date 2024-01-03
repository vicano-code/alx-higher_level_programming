#include "lists.h"

/**
 * check_cycle - cihecks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *ahead, *behind;

	if (list == NULL)
		return (0);
	ahead = list;
	behind = list;
	while (1)
	{
		if (ahead->next != NULL && ahead->next->next != NULL)
		{
			ahead = ahead->next->next;
			behind = behind->next;
			if (ahead == behind)
				return (1);
		}
		else
			return (0);
	}
}
