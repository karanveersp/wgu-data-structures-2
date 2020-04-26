from operator import attrgetter

# can use datetime.time(hour=16) to get the actual datetime object

class Activity:
    def __init__(self, name, start, end):
        self.name = name
        self.start_time = start
        self.end_time = end

    def conflicts_with(self, other_activity):
        if self.end_time <= other_activity.start_time:
            return False
        elif other_activity.end_time <= self.start_time:
            return False
        return True  # all other cases mean conflict
    

def activity_selection(activities):
    num_acts = len(activities)
    # 24h format end time
    sorted_activities = sorted(activities, key=attrgetter("end_time"))
    chosen = [] 
    current = sorted_activities[0]
    chosen.add(current)
    for act in activities:
        if not act.conficts_with(current):
            chosen.append(act)
            current = act
    return chosen


def main():
    activities = [
        Activity("History museum", 9, 10),
        Activity("Morning mountain hike", 9, 12),
        Activity("Boat tour", 11, 14),
        Activity("Day mountain hike", 13, 16),
        Activity("Hang gliding", 14, 16),
        Activity("Snorkeling", 15, 17),
        Activity("Fireworks show", 20, 21),
        Activity("Night movie", 19, 21),
    ]
    chosen = activity_selection(activities)
    for i in chosen:
        print((i.name, i.start, i.end))

if __name__ == "__main__":
    main()