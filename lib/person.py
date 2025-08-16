#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Lewis", job="Sales"):
        self._name = "Lewis"
        self.name=name

        self._job = "Sales"
        self.job=job


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, person_name):
        if isinstance(person_name,str) and 1<= len(person_name) <=25:
            self._name = person_name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter

    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")