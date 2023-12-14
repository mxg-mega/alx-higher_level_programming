#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  * insert_node - function inserts a node at a certain poistion
  * @head: head of the linked list
  * @number: the position to insert it at
  *
  * Return: the address of the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currentdelay = NULL, *currentlead = NULL;
	listint_t *newNode = NULL;

	if (*head == NULL)
	{
		return (add_nodeint_end(&(*head), number));
	}
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
	{
		return (NULL);
	}
	newNode->n = number;
	newNode->next = NULL;

	if (number < 0)
	{
		newNode->next = *head;
		*head = newNode;
		return (*head);
	}
	currentdelay = *head;
	currentlead = (*head)->next;
	while (currentdelay->next != NULL && currentlead->next != NULL)
	{
		/* check if the number wasnt found so add the new node to the end of the node */
		if (currentdelay == currentlead)
		{
			free(newNode);
			return (NULL);
		}
		if (number >= currentdelay->n && number < currentlead->n)
		{
			newNode->next = currentlead;
			currentdelay->next = NULL;
			currentdelay->next = newNode;
			break;
		}
		currentdelay = currentdelay->next;
		currentlead = currentlead->next;
	}
	if (number > currentlead->n)
	{
		return (add_nodeint_end(&(*head), number));
	}
	return (newNode);
}

