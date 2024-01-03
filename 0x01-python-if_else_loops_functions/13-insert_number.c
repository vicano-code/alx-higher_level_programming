#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert into list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *tmp, *new;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;
	current = *head;
	while (current)
	{
		if (current->n == new->n)
			current = current->next;
		else if (current->n < new->n)
		{
			tmp = current;
			current = current->next;
			if (current->n > new->n)
			{
				tmp->next = new;
				new->next = current;
				return (new);
			}
		}
		else
		{
			tmp = current;
			current = current->next;
			if (current->n < new->n)
			{
				tmp->next = new;
				new->next = current;
				return (new);
			}
		}
	}
	return (NULL);
}
