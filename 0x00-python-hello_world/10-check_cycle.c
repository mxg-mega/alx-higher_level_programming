#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - function checks if a linked list has a cycle
  * @list: head of the list
  *
  * Return: 0 if no cycle, 1 if cycle found
  */
int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	if (list == NULL)
	{
		return (0);
	}
	current = list;
	while (current->next != NULL)
	{
		if (current->next == list)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
