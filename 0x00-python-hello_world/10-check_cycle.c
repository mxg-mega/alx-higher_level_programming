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
	listint_t *delay = NULL;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	current = list;
	delay = list->next;
	while (delay != NULL && delay->next != NULL)
	{
		if (current == delay)
		{
			return (1);
		}

		current = current->next;
		delay = delay->next->next;
	}
	return (0);
}
