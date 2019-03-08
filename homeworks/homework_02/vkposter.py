#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts = {}
        self.subscriptions = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.posts.keys():
            self.posts[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.posts.keys():
            self.user_posted_post(-1, post_id)
        if user_id not in self.posts.get(post_id)[1]:
            self.posts.get(post_id)[1].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.subscriptions.keys():
            self.subscriptions[follower_user_id] = [followee_user_id]
        else:
            self.subscriptions.get(follower_user_id).append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        posts = list(self.posts.keys())
        posts.sort(reverse=True)
        relevant_posts = [post_id for post_id in posts
                          if self.posts.get(post_id)[0] in
                          self.subscriptions.get(user_id)]
        return relevant_posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        posts = list(self.posts.keys())
        posts.sort(key=lambda post_id: (len(self.posts.get(post_id)[1]),
                                        post_id), reverse=True)
        posts = posts[:k]
        return posts
