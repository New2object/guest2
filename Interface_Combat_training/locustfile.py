# coding=utf-8
from locust import HttpLocust, TaskSet, task


# 定义用户的行为

class UserBehavior(TaskSet):
    @task
    def baidu_page(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
