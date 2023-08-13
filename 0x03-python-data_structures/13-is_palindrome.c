#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: head node of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t list_length, i, j, middle, *array;
	listint_t *current;

	if (!*head)
		return (1);
	list_length = linked_list_length(head);
	middle = list_length / 2, i = 0;
	array = malloc(sizeof(int) * list_length);

	current = *head;
	for (i = 0; i < list_length; i++)
	{
		array[i] = current->n;
		current = current->next;
	}
	if (list_length % 2 == 0)
	{
		for (i = 0, j = list_length - 1; i < middle && j >= middle; i++, j--)
		{
			if (array[i] != array[j])
			{
				free(array);
				return (0);
			}
		}
	}
	else
	{
		for (i = 0, j = list_length - 1; i <= middle && j >= middle; i++, j--)
		{
			if (array[i] != array[j])
			{
				free(array);
				return (0);
			}
		}
	}
	free(array);
	return (1);
}

/**
 * linked_list_length - function that gets the length of a linked list
 * @head: pointer to the head node
 * Return: length of the linked list
 */
size_t linked_list_length(listint_t **head)
{
	listint_t *current;
	size_t length = 0;

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		length++;
	}
	return (length);
}
