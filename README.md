# Machine_Learing

here we are :))

![image1](https://user-images.githubusercontent.com/92854954/222135572-c22f1c12-5b4b-4451-9fc6-28560861021b.png)


# Supervised Learning

## Regression

### Linear Regression 

* Simple Linear Regression

* Multiple Linear Regression

* PCR

* PLS 

* Ridge Regression

* Lasso Regression

* ENET

### Non-Linear Regression

* KNN

* SVR

* ANN

* CART

* Bagged Trees

* RF

* GBM

* XBoost

* LightGBM

* CatBoost

## Classification 

* Logistic Regression 

* and others(KNN, SVC, ANN, CART, RF, GBM, XBoost, LightGBM, CatBoost)



# Unsupervised Learning

## Clustering

* K means





**Ufak notlarım:**

supervised learning temelde iki kısma ayırlıyor. regresyon problemelri ve classification problemeleri. genellikle algorştmalar her ikisi 
içind ekullanılıyor. Bu yüzden aşşağıda regression yada classification demeden algorştmaların genel mantıklarını özetledim 

- **simle linear reg:** ax+b
- **multtiple linear reg:** b0+b1X1+b2X2...  tune için cross_val_score kkullanlır
- **princaple componenet regression:** Hocam bağımsız değişknler arasında ilişki(koralasyon) olması durumunda kullanılır. Önce boyut 
indirgenmesi yapılarak koralsyondan kurtulunur daha sonra regresyon kurulur.
Bu indirgenme işlemş sadece bağımsız değişkenle riçinyapılır. Tuned kısmında ise değişken sayısı seçem yapılır. Burada mücadele ettiğimiz başka bir unsur ise fazal değişken olmasıyldı işte bu sorunla da model tune işeleminde mücadeel ederiz. optimum değişken sayısınıbulmak için brut force yöntemi kullanılır.(döngü ile olası tüm değişken sayıları denenir ve rmse değerleri bir dizide kaydedilir daha sonra bu dizi görselleştirilerek optimum değer gözlenir :))
- **partial least squared regression:** pcr'da indirgenme yapılırken bağımlı değişkenden alakasız olarak yapılır. burada ise indirgenme 
değişkenlerin bağımlı değişknele ilişkisi max olacak şekilde yapılır. ve pcr'da değişken atm ayapıyorduk burada değişkenler s
atılmaz. n_components sayısı tuned edilir. yine brut force ile.
- **ridge regression:** rmse'yi küçük tutmak için katsayılara ceza uygular. regresyon sonucu eldeettiğimiz b0 ve b1 değerlerinin biliyoruz işet 
rmse nin en küçük olacaği b değerlerini bulmaya çalışırz. bunu yaparkende katsayıalırı sıfıra yaklaştırız. Ceza terimi dediğimiz şey lambda
(alpha)dır bunu optimim değeri cross validation kullanılır(RidgeCV)(L2)kullanılır(b^2)
- **lasso regression:** ridge ile aynı mantığa sahip. tek fark ridge katsayıları sıfır yapmaz lasso yapar. bu yüzden değişkenler arasında seçme 
işlemi yapmıl olur. (L1 kullanınlır.(|b|)) kare almak yerine mutlak alıondığı için - değerler gider direkt bir feature selection yapılmış 
olunur.
- **elastic net regression:** L1 ve L2 birleştirilir. hem seçme hem ceza uygulama yapılmış olur.




- **K nearest neighbors:** Aslında sınıflandır problemleri için ortaya çımış daha sonr aregresyın problemine de uyarlanmıştır.
bağımsız değişkenleri değerleri verlien bir gözlem bağımlı değişkenin tahmin edilmesini istiyor. model tüm bağımsız değişkenlerle 
uzaklıklarının ölçüp bu gözleme en yakın k gözlemi buluyor. ve  bunların ortalamasına göre de bağımlı değişken tahmin ediliyor. k sayısı 
gridsearchcv ile bulunuyor. paremetre olarak k sayıları veriliyor.
- **Support vector regression:** değerleri belli bir aralığın içinde tutma çabası. optimum c değeri gridsearch ile bulunur. yine paremtre olarak 
olası c değerler verilir.
- **Artificial neural network:** Hocam bağımsız değişkenlerş ağılılarla(katsayılarla yani bilyorsun artık bu meseleyi) çarpıyoruz işte bu giirş kısmı. Sonra bu girdileri belirli algoritmalara(metematikse formullere) tabi tutup model hazır oluyro. son hali çıktı olut-yor bu fonksiyona tabi tutalan kısım hidden gizli katman oluyor birden fazla basamakta olabilir bu kısm(çok katmanlı)
- **Classifications and regression treees(CART):** belirli değere göre vrei setini alt ağaçalra bölme işlemşdir. heterojen veri setlerinde başarılıdır. Ama genellenebilirliği pek iyi değildir. overfitting problemi vardır. özellikle çok dallanmada overfitting görülür bu yüzden düğüm sayısı kontrol altına alınır bunun optimum değeri yine cross validation(gridsearcv) ile bulunur. paremetre olarak mean_sample_split ve max_leaf_nodes verilir. anlasın zaten bölünme için en az örnek sayısı ve kaç node olacağı.
- **Baggad trees:** Hoxa burada bagging kullanılır. bagging=pakaetlemek burada birden fazla karar ağacı oluşturup sonra bunların oluşturdukkları tahminin ortalaması bizim sonucummuz olur. overfitting problemi cart kadar değildir. eee sorun ne? n_estimators ağaç sayıs kaç olacak? onu da tabiki cross validation(gridsearcv) ile buluruz :)
- **Random forest:** hocam ağaç oluşturduk iyisi var kötüsü var bunların her birini tahminine aynı değeri verdik mantıklı mı? değil!
işte random forest da bu sorunun çözüyör ağaçalrın tahminin final tahmine etkisi başarısı kadar oluyor :)Ayrıca bir artısı daha her düğümde sample(örnek) seçimini rastgele yapıyor bu sayede rasallığı bozmammış oluyor teşekkürler rf :)
- **Gradient boosting model:** geldi iki gözmün çiçeği. bir basit ağaç oluşturulur sonra  bunun hataları üzerine(hatalrın ağırlıkları arttrılırak önemi arttırılarak) yeni bir ağaç kurulur. bu şekşilde ağaçalr silsilesi oluşturulur. Burad aöbüneli bir ağacın çıktısı diğer ağacın girdisidir. bir ağacın hatası bir sonraki için önem ifade eder ve hesaplama her adımda yapılır. bagginde ise hesaplama parele olarak sonda toplu yapılır. burada ise ardışık hesaplama yapılır :)
tuning sırasında 4 paremetre ile çalıştırk learning_rate bunun 0-1 arasında olması gerekir, küçük olması iyidir. max_depth, kurulacak ağacık max derinliği, n_estimators ağaç sayısı, subsaple ağaç için alınan örnek(satır) sayısı.
- **Exrtreme gradient boosting:** gbm'in gelişmiş versiyonu. daha hızlı ve boş değerlerle de çalışabiliyor. yine hatalar üzerine bir sürü ağaç oluşturuyor sonra bunalr arasından daha kaazançlı olanı kullanılyor sonra ise budama yapıypr bunuda verilen gamma değerine göre ypıyor. kazanç değeri gamma değerinden küçük olan dallar budanıyor. gbm ile ynı paremeetre sadece subsample yerine colsample_bytree ağaç başına alınacakk örnek kullanılır.
- **LİghtGBM:** iki tür büyüme vardır. Level-wise ve eaf-wise. Level wise'da aüaç büyüren denge korunur, level wiswe'da ise daha az hataya sahip olan yapraktan büyünür denge gözetilmez. lightgbm bu sayede diiğer boosting algoritmalarından daha az hata oranına sahiptir. ancak bu yönyem az veri sayılı setlerde kullanıldığında overfitting e sebep olmaktadır.
- **categoric boosting:** kategoric değişkenlerin olduğu veri setlerinde başarılıdır. simetric ağaç kurar bu sayede ovetfitting ile mücadele eder.
- **Logistic regression:** sınflandırma problemi için kullanılır. Sınıflandırma problemi dediğimiz şey bağımlı değişkneşmşzşn kategoric 
olması. Bu durumda tahmin edilen sonuc yani bağımlı değişken 0 yada 1 olacak. Hocam işte logistic regresyon aslında numaric tahmin yapıyor 
yani adı üstünde regresyon ancak bulduğu sonuc kullanılan fonksiyon sayinde 0-1 aralığının dışına çıkmaz. ez cümle sınıflanadırma problemini 
regresyon problemi çözer.

Gözetimsiz Öğrenme(unsupervised learning)

Nedir bu gözetimsiz öğrenme?

Bilmiyom! şaka şaka anlatcam :))

Bu saate kadar belirli sınıflar yeri yurdu sınıfı belli olan verileri verdik. Sonra dedik ki ben sana yeni bir veri vericem onun hangi 
sınıftan olduğunu yada hangi değere sahip olacağını bul. Ama burada verdiğimiz verinin  değerlerin nereye ait olduğu bellli değil. Diyoruz 
ki al veri sen bunu önce sınıflandır bak bakalım bunları nadıl gruplandırabilirsin sonra yeni gönderdiğimimmnde yerini bulursun. 
Artık sınınflandırma işide sende sevgili makine:)

Not: Şu farka dikkat edelim sınıflandırma probleminde zaten birbirinden farklı olna sınıfların birbirinden net olarak ayıran doğru/düzlem 
çizeriz. Kümelemede ise verilen veriler arasında herhangi bir sınıf farkı sınıflama yoktur. Biz kendi belirlediğimz sayıda yine tamamen 
kendimiz sınıflar oluştururuz

ee niye bunun adı gözetimsiz öğrenme(unsupervised learning)? Çünkü ilkinde makine insanın gözlemleyip sınıflandırdığı veriyi işliyor. ancak 
burada ise makine tamamen kendisi kendi bildiği gibi sınıflandırıyor. bu sınıflandurma(kümeleme) işine insan gözlemi karışmıyor

gözetimsiz öğrenme iki kısımda incelenir. Clustering, Temel bileşen analizi.

***Kümeleme***
Disjoint: Birbirlerinden tamamne farklı net sınırlarla ayrılı kümeler 

Overlapping: Venn şemesı gibi kesişimleri bulunabilen kümeler

Probabilistic: Net olarak şu gruba ait diyemiyeceğimiz. yüzdelik oranlarla aitlik bildirilebilinen kümeler. 
bir kişi %80 a grubunda %7b %13 c grubu gibi

Hierarchial: Ağaç yapısını andıran dallandırılan kümeler.