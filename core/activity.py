import csv
from os import path
from shutil import copy
from itertools import cycle


class Activities:
    def __init__(self, file):
        self.file = file
        self.load()

    def load(self):
        self.activity_list = []
        if not path.isfile(self.file):
            # Create activities.csv from the sample if it does not already exist
            copy(
                f"{self.file}.sample",
                self.file,
            )

        with open(self.file, "r") as f:
            # Get activities.csv contents
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                try:
                    activity = row[0]
                    self.activity_list.append(activity)
                except IndexError:
                    pass

        if not self.activity_list:
            self.activity_list = ["with reactions"]

        self.loop = cycle(self.activity_list)

    def get(self):
        return next(self.loop)

    def add(self, activity):
        with open(self.file, "a", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=",", lineterminator="\n")
            w.writerow([activity])

        self.load()

    def remove(self, activity):
        if activity not in self.activity_list:
            return False

        self.activity_list.remove(activity)
        with open(self.file, "w", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=",", lineterminator="\n")
            for row in self.activity_list:
                w.writerow([row])

        self.load()
        return True
