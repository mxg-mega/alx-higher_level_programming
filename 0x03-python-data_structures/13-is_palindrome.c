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
	listint_t *cmp = NULL, *prev = NULL, *next = NULL;
	int len = 0, i = 0, stop = 0;

	if (*head == NULL)
	{
		return (1);
	}

	len = list_len(*head) + 1;
	if (len == 0)
	{
		perror("A cycle was encountered\n");
		return (-1);
	}
	if (len == 1)
	{
		return (1);
	}

	stop = len / 2;
	cmp = *head;
	while (i < stop)
	{
		next = cmp->next;
		cmp->next = prev;
		prev = cmp;
		cmp = next;
		i++;
	}
	if (len % 2 != 0)
	{
		cmp = cmp->next;
	}
	while (prev != NULL && cmp != NULL)
	{
		if (prev->n != cmp->n)
		{
			return (0);
		}
		prev = prev->next;
		cmp = cmp->next;
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
	listint_t *current = NULL, *fast = NULL, *slow = NULL;
	int length;

	slow = head;
	fast = head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (0);
		}
	}
	length = 0;
	current = head;
	while (current->next != NULL)
	{
		length++;
		current = current->next;
	}
	return (length);
}
