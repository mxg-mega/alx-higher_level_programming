#include "lists.h"
#include <stddef.h>
#include <stdio.h>

int list_len(listint_t *head);

/**
  * is_palindrome - function checks if list is a palindrome
  * @head: head of the linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  * Description: a palindrome is an experession that shows that
  * it can be read forward or reverse
  */
int is_palindrome(listint_t **head)
{
	listint_t *cmp = NULL, *cmp_num = NULL;
	int len = 0, i = 0, stop = 0, j = 0;

	if (*head == NULL)
	{
		return (1);
	}

	len = list_len(*head) + 1;
	if (len == 0)
	{
		perror("A cycle was encountered\n");
		return (1);
	}
	else if (len == 1)
	{
		return (1);
	}
	else
	{
		stop = len / 2;
	}
	j = len - 1;
	cmp_num = *head;
	while (cmp_num->next != NULL && i < stop)
	{
		int l = 0;

		cmp = *head;
		while (l < j)
		{
			cmp = cmp->next;
			l++;
		}
		if (cmp_num->n != cmp->n)
		{
			return (0);
		}
		cmp_num = cmp_num->next;
		i++;
		j--;
	}
	return (1);
}

/**
  * list_len - function counts the lenght of the list
  * @head: head of the linked list
  * Return: 0 or length of list
  */
int list_len(listint_t *head)
{
	listint_t *current = NULL, *fast = NULL;
	int i;

	if (head == NULL)
	{
		return (0);
	}

	i = 0;
	current = head;
	fast = head->next;
	while (current->next != NULL)
	{
		if (current == fast)
		{
			return (0);
		}

		i++;
		current = current->next;
		fast = fast->next;
	}
	return (i);
}
