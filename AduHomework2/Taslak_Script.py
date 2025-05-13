class SmartHomeAgent:
    def __init__(self):
        self.facts = set()
        self.rules = {}

    def tell_fact(self, fact):
        self.facts.add(fact)

    def tell_rule(self, rule):
        condition, action = rule.split("->")
        condition = condition.strip()
        action = action.strip()
        self.rules[condition] = action

    def run(self):
        for condition, action in self.rules.items():
            if condition in self.facts:
                print(f"Aksiyon: {action}")

# Ajanı başlat
agent = SmartHomeAgent()

# Durumlar (Facts)
agent.tell_fact("cold_weather")
agent.tell_fact("dark_room")
agent.tell_fact("someone_home")

# Kurallar (Rules)
agent.tell_rule("cold_weather -> turn_on_heater")
agent.tell_rule("dark_room -> turn_on_lamp")
agent.tell_rule("someone_home -> open_curtains")
agent.tell_rule("movie_time -> turn_on_tv")
agent.tell_rule("going_out -> turn_off_heater")

# Ajanı çalıştır
agent.run()
