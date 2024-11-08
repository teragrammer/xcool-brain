class StudentState:
    def __init__(self, name):
        self.name = name
        self.mastery = {}
        self.current_level = "beginner"

    def update_master(self, topic, score):
        self.mastery[topic] = score

        if score > 80:
            self.current_level = "advanced"
        elif score > 50:
            self.current_level = "intermediate"
        else:
            self.current_level = "beginner"
