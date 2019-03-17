#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    try:
        p_node = head.next_node
    except AttributeError:
        return head
    new_head = head
    new_head.next_node = None
    while p_node is not None:
        p_node.next_node, new_head, p_node = \
           new_head, p_node,  p_node.next_node
    return new_head
