#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter

class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return 'User ({})'.format(self.id)

users = [User(i) for i in (23, 3, 99, 11)]
print(sorted(users, key=attrgetter('id')))