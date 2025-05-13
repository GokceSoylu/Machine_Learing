**CSE 419 - Artificial Intelligence**
**Assignment #2 Report**

---

### 1. Projenin Amacı / Purpose of the Project

## Bu projenin amacı, mantıksal düşünme (Logic-of-Thought) yaklaşımı ile çalışan bir akıllı ev ajanı gelistirmektir. Kullanıcının verdiği doğal dil komutlarını, mantıksal önermelere dönüştürerek evdeki cihazları kontrol eden bir sistem tasarlanmıştır.

The goal of this project is to develop a smart home agent that works based on the Logic-of-Thought approach. The system interprets natural language commands from the user and converts them into logical propositions to control smart home devices.

---

### 2. Sistem Mimarisi / System Architecture

Sistem şu parçalardan oluşmaktadır:

* `SmartHomeAgent` sınıfı: Olguları ve kuralları tutar.
* `tell_fact(fact)`: Yeni olgu ekler.
* `tell_rule(rule)`: Yeni mantıksal kural tanımlar.
* `update_facts_from_input(user_input)`: Kullanıcıdan gelen komutu yorumlayarak olgulara çevirir.
* `run()`: Kuralları kontrol ederek şartlar sağlandığında aksiyon tetikler.

---

The system consists of the following components:

* `SmartHomeAgent` class: Stores facts and rules.
* `tell_fact(fact)`: Adds a new fact.
* `tell_rule(rule)`: Defines a logical rule.
* `update_facts_from_input(user_input)`: Translates user input into facts.
* `run()`: Evaluates rules and triggers corresponding actions.

---

### 3. Olgular ve Kurallar / Facts and Rules

Tanımlanan 5 temel kural:

1. `cold_weather -> turn_on_heater`
2. `dark_room -> turn_on_lamp`
3. `someone_home -> open_curtains`
4. `movie_time -> turn_on_tv`
5. `going_out -> turn_off_heater`

---

Defined 5 core rules:

1. `cold_weather -> turn_on_heater`
2. `dark_room -> turn_on_lamp`
3. `someone_home -> open_curtains`
4. `movie_time -> turn_on_tv`
5. `going_out -> turn_off_heater`

---

### 4. Doğal Dil ve Aksiyon Eşleştirme / Natural Language to Action Mapping

| Komut (TR)           | Olgu          | Aksiyon           |
| -------------------- | ------------- | ----------------- |
| Üşüyorum             | cold\_weather | turn\_on\_heater  |
| Çok karanlık burası. | dark\_room    | turn\_on\_lamp    |
| Evdeyim              | someone\_home | open\_curtains    |
| Film zamanı          | movie\_time   | turn\_on\_tv      |
| Dışarı çıkıyorum     | going\_out    | turn\_off\_heater |

---

| Command (EN)    | Fact          | Action            |
| --------------- | ------------- | ----------------- |
| I am cold       | cold\_weather | turn\_on\_heater  |
| It is dark here | dark\_room    | turn\_on\_lamp    |
| I am at home    | someone\_home | open\_curtains    |
| It's movie time | movie\_time   | turn\_on\_tv      |
| I am going out  | going\_out    | turn\_off\_heater |

---

### 5. Çalışma Senaryosu / Sample Execution

**Girdi (Input):** "Evdeyim ve üşüyorum."

**Ajan Çıktısı (Agent Output):**

```
Aksiyon tetiklendi: open_curtains
Aksiyon tetiklendi: turn_on_heater
```

---

### 6. Sonuç / Conclusion

## Bu çalışma, mantıksal kurallar ve basit çıkarım yöntemleriyle akıllı ev cihazlarını kontrol eden bir sistemin başarıyla geliştirilebileceğini göstermiştir.

This study demonstrates that a smart home system can be successfully developed using logical rules and simple inference mechanisms.
