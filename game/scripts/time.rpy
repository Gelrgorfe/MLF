init python:
    class day_time:
        def __init__(self):
            self.day = 1
            self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.times_of_day = ["morning", "afternoon", "evening", "night"]
            self.current_time_index = 0

        @property
        def weekday(self):
            return self.weekdays[(self.day - 1) % 7]

        @property
        def time(self):
            return self.times_of_day[self.current_time_index]

        def advance(self, increment=1, days=0):
            total_increment = increment + days * len(self.times_of_day)

            for i in range(total_increment):
                self.current_time_index += 1
                if self.current_time_index == len(self.times_of_day):
                    self.current_time_index = 0
                    self.day += 1
default clock = day_time()