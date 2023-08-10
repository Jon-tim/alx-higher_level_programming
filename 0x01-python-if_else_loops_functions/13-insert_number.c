#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new, *previous, *current;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	previous = current = *head;

	if (current == NULL || new->n < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current)
	{
		if (new->n > current->n)
		{
			previous = current;
			current = current->next;
		}
		else if (new->n < current->n)
		{
			previous->next = new;
			new->next = current;
			break;
		}
	}
	return (new);
}
