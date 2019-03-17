#!/usr/bin/env python
# coding: utf-8
from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.events = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        self.events.append({'user_id': user_id, 'time': time})

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        """
        def _remove_old(event_list: deque):
            return filter(
                lambda x: time - self.FIVE_MIN < x['time'] <= time,
                event_list
            )

        def _count_actions(event_list):
            return Counter(map(
                lambda x: x['user_id'],
                event_list
            )).values()

        def _filter_actions(number_of_actions):
            return True if number_of_actions == count else False

        return sum(map(
            lambda x: 1,
            filter(_filter_actions, _count_actions(_remove_old(self.events)))
        ))
        """
        # :-)
        return sum(map(
            lambda x: 1,
            filter(
                lambda x: True if x == count else False,
                Counter(map(
                    lambda x: x['user_id'],
                    filter(
                        lambda x: time - self.FIVE_MIN < x['time'] <= time,
                        self.events
                    ))).values())
        ))
