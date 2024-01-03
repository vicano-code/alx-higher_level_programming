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

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL) /*empty list*/
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	if ((*head)->next == NULL)/*single value list*/
	{
		if ((*head)->n <= new->n)
			(*head)->next = new;
		else
		{
			new->next = *head;
			*head = new;
		}
		return (new);
	}
	if ((*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	while (current->next != NULL)
	{
		if (current->n == new->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
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
	current->next = new;
	return (new);
}
