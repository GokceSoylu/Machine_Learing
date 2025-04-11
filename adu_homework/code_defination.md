**CSE 419 - YAPAY ZEKÂ**

**Ödev #1: Çok Etmenli Sezgisel Optimizasyon ile Cutting Stock Problemi Çözümü**

**Öğrenci Adı:** Gökçe Soylu  
**Öğrenci No:** 241805111  
**Tarih:** 15 Nisan 2025

---

### **1. Giriş**

Cutting Stock Problemi (CSP), üretim ve imalat süreçlerinde sıkça karşılaşılan klasik bir optimizasyon problemidir. Amaç, büyük rulolar halinde bulunan malzemenin (örneğin ahşap, kağıt, metal) belirli uzunluklardaki daha küçük parçalara kesilmesidir. Bu işlem sırasında malzeme israfı en aza indirilmek istenir. Bu projede CSP, çok etmenli bir mimari kullanılarak sezgisel optimizasyon algoritmaları ile çözülmektedir.

---

### **2. Problem Tanımı**

Sabit uzunlukta bir stok rulosu ve müşteri taleplerini karşılamak için gerekli olan daha küçük parça uzunlukları verildiğinde, amaç, malzeme israfını en aza indiren en verimli kesim desenini bulmaktır. Örneğin, 100 metrelik bir rulodan 10, 15 ve 20 metrelik parçalar kesilmesi gerekiyorsa, mümkün olduğunca az artık bırakacak şekilde bir kesim stratejisi belirlenmelidir.

---

### **3. Yöntem**

#### 3.1 Çok Etmenli Sistem Tasarımı
İki farklı çok etmenli strateji uygulanmıştır:
- **İşbirlikçi Etmen Tabanlı Optimizasyon**: Her etmen CSP’yi bağımsız olarak çözmeye çalışır ve en iyi çözümlerini paylaşır. Bu çözümler birleştirilerek nihai sonuç iyileştirilir.
- **Hiper Meta-Sezgisel Yaklaşım**: Her etmen farklı bir sezgisel algoritma kullanır. Etmenler tarafından bulunan en iyi çözüm seçilir.

#### 3.2 Kullanılan Sezgisel Algoritmalar
- **Simüle Tavlama (SA)**: Yerel en iyilerden kurtulmak için zamanla soğuyan bir sıcaklık parametresiyle daha kötü çözümleri belirli olasılıkla kabul eder.
- **Tepe Tırmanma (HC)**: Her iterasyonda daha iyi komşu çözümlere geçerek ilerler.
- **Genetik Algoritma (GA)**: Seçim, çaprazlama ve mutasyon işlemleriyle bir çözüm popülasyonunu geliştirir.

---

### **4. Kod Açıklaması**

Bu bölüm Python kodunun ana bileşenlerini açıklar:

**generate_random_solution(...)**: 
Kalan uzunluğa sığabilecek rastgele parçalar seçerek geçerli bir rastgele kesim deseni oluşturur.

**calculate_waste(...)**:
Bir çözümdeki kesilen parçaların toplamı ile stok uzunluğu arasındaki farkı hesaplar (artık).

**simulated_annealing(...)**:
Rastgele bir çözümle başlar ve daha iyi çözümler arar. Bazen daha kötü çözümleri de kabul ederek yerel minimumlardan kaçınır. "Sıcaklık" değeri her adımda azalır.

**hill_climbing(...)**:
Rastgele bir çözümle başlar ve daha iyi komşu çözümlere geçerek ilerler. Yerel minimumda takılabilir ama hızlıdır.

**genetic_algorithm(...)**:
Başlangıçta rastgele çözümlerden oluşan bir popülasyon oluşturur. Çaprazlama ve mutasyon yoluyla yeni nesiller oluşturur ve iyileşme sağlar.

**run_agents(...)**:
Seçilen etmen sayısı kadar etmeni çalıştırır. Her etmen SA, HC veya GA algoritmalarından birini kullanır. Her biri bulduğu en iyi çözüm ve israf değerini döndürür.

**Ana bölüm**:
Kullanıcıdan şu veriler alınır:
- Stok uzunluğu
- İstenen parça uzunlukları (virgülle ayrılmış)
- Etmen sayısı

Sonrasında tüm etmenler çalıştırılır, çözümler toplanır ve kullanıcıya gösterilir.

---

### **5. Deneysel Sonuçlar**

Örnek yapılandırma:
- **Stok Uzunluğu**: 100 metre
- **Parça Uzunlukları**: [10, 15, 20]
- **Etmen Sayısı**: 3 (SA, HC, GA)

| Etmen | Algoritma             | Kesim Deseni              | Artık (metre) |
|-------|------------------------|----------------------------|----------------|
| 1     | Simüle Tavlama        | [20, 20, 20, 20, 15]       | 5              |
| 2     | Tepe Tırmanma         | [15, 15, 20, 20, 15, 10]   | 5              |
| 3     | Genetik Algoritma     | [20, 20, 20, 15, 15, 10]   | 0              |

---

### **6. Sonuç**

Cutting Stock Problem’inin çözümünde çok etmenli sezgisel yaklaşım etkili sonuçlar vermiştir. Yapılan örnek uygulamada, Genetik Algoritma sıfır artık ile en iyi sonucu vermiştir. Bu da farklı optimizasyon stratejilerini paralel çalıştırmanın ve en iyisini seçmenin faydasını göstermektedir.

Gelecekte yapılabilecek geliştirmeler:
- Dinamik etmen koordinasyonu
- Hibrit algoritmalar
- Grafik arayüz geliştirilmesi

---

### **Kaynakça**
[1] https://github.com/nargesbh/Cutting-stock-problem-using-Simulated-Annealing  
[2] https://pypi.org/project/mealpy/