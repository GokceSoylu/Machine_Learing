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

    def update_facts_from_input(self, user_input):
        # Sabit eşleşmeler: doğal dil → olgu
        natural_language_to_fact = {
            "üşüyorum": "cold_weather",
            "karanlık": "dark_room",
            "evdeyim": "someone_home",
            "film zamanı": "movie_time",
            "dışarı çıkıyorum": "going_out"
        }

        for phrase, fact in natural_language_to_fact.items():
            if phrase in user_input.lower():
                self.tell_fact(fact)

    def run(self):
        actions_triggered = []
        for condition, action in self.rules.items():
            if condition in self.facts:
                actions_triggered.append(action)
                print(f"Aksiyon tetiklendi: {action}")
        if not actions_triggered:
            print("Eşleşen bir durum bulunamadı.")

# Ajan oluştur
agent = SmartHomeAgent()

# Kuralları tanımla
agent.tell_rule("cold_weather -> turn_on_heater")
agent.tell_rule("dark_room -> turn_on_lamp")
agent.tell_rule("someone_home -> open_curtains")
agent.tell_rule("movie_time -> turn_on_tv")
agent.tell_rule("going_out -> turn_off_heater")

# Kullanıcıdan komut al
print("Akıllı ev sistemine komut giriniz (örnek: Üşüyorum, Evdeyim, Film zamanı):")
user_input = input("Komut: ")

# Komutu işle ve ajanı çalıştır
agent.update_facts_from_input(user_input)
agent.run()
