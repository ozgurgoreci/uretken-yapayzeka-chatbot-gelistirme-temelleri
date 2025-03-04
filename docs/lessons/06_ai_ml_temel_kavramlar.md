# Yapay Zeka (AI) ve Makine Öğrenmesi (ML) – Temel Kavramlar

## Yapay Zeka nedir?
Yapay zeka, bilgisayar sistemlerinin normalde insan aklıyla ilişkilendirilen görevleri öğrenmesini ve gerçekleştirmesini sağlayan bir bilgisayar bilimi dalıdır​. Başka bir deyişle, AI (Artificial Intelligence), insanların zekâ gerektiren işleri makinelerin yapabilmesi demektir. Bu sistemler çevrelerini algılayıp kararlar alabilir ve zamanla performanslarını geliştirebilir. Örneğin bir yapay zeka, insan gibi konuşmayı anlamayı veya görüntülere bakıp tanıdığı nesneleri ayırt etmeyi öğrenebilir.

**Günlük hayattan yapay zeka örnekleri:**

- Akıllı telefonlardaki sesli asistanlar (Siri, Google Asistan gibi) sesimizi anlayıp sorularımıza cevap verebilir. Bu asistanlar, yapay zekanın doğal dil işleme yeteneğine güzel bir örnektir
- **​Öneri sistemleri:** Netflix’in dizi/film önerileri veya Spotify’ın müzik önerileri, bizim geçmiş tercih ve beğenilerimize bakarak tahmin yapar. Bu da yapay zeka sayesinde olur
- **Otomatik sürüş özellikleri:** Modern arabalar, yapay zeka ile şerit takibi yapabilir veya park edebilir. Örneğin, bazı araçlar çevresini algılayıp kendi kendine fren yapabilir​
- **E-posta spam filtreleri:** Gelen kutunuzdaki yapay zeka, hangi e-postanın istenmeyen (spam) olduğunu öğrenip onları otomatik olarak ayırabilir.

Bu örneklerin hepsinde, makineler normalde insanların yaptığı bir değerlendirme veya öğrenme işini üstlenmiş olur.

## Makine Öğrenmesi (ML) Nedir?

Makine öğrenmesi, yapay zekânın bir alt dalıdır ve bilgisayarların verilerden öğrenmesini sağlayan yöntemleri içerir. Klasik programlamada insanlar bilgisayara ne yapacağını adım adım kodlarken, makine öğreniminde bilgisayarlar çok sayıda örnek veriye bakarak kendi kurallarını keşfeder. Bu sayede, açıkça programlanmadan, sadece verilerden çıkarım yaparak yeni durumlarla ilgili tahminler üretebilirler.
Oracle'nin yaptığı resmi bir tanıma göre, makine öğrenimi “tükettikleri verilere göre öğrenen ya da performansı iyileştiren sistemler oluşturmaya odaklanan bir yapay zeka alt kümesidir”​ . Yani ML algoritmaları, veriler üzerinde çalıştıkça daha iyi sonuçlar verecek şekilde kendini adapte eder. Örneğin bir makine öğrenimi algoritmasına birçok kedi ve köpek fotoğrafı gösterirsek, zamanla yeni bir resimde kediyi köpekten ayırmayı **öğrenebilir**.

**Günlük hayattan makine öğrenimi örnekleri:**

- **E-posta filtreleri:** Az önce bahsettiğimiz spam filtreleri, makine öğrenimi kullanarak hangi e-postaların istenmeyen olduğunu öğrenir. Önceden “spam” ve “spam değil” olarak işaretlenmiş binlerce e-postayı eğitim verisi olarak kullanıp yeni gelen bir mesajın spam olup olmadığını tahmin eder.
- **Alışveriş ve film önerileri:** Online alışveriş siteleri veya dijital platformlar, sizin gezdiğiniz ürünlere veya izlediğiniz filmlere bakarak hoşunuza gidebilecek başka ürün/film önerir. Bu öneri motorları makine öğrenimi sayesinde çalışır; çok sayıda kullanıcı verisini analiz ederek benzer ilgi alanlarını öğrenir.
- **Yüz tanıma:** Akıllı telefonlar veya sosyal medya, fotoğraflardaki yüzleri otomatik tanıyabiliyor. Örneğin, telefonunuzun fotoğraf galerisinde biriyle ilgili tüm fotoğrafları tek bir klasörde toplayabildiğini görürsünüz – bu, makine öğrenimi ile gerçekleştirilen bir yüz tanıma algoritması sayesinde olur. 
- **Bankacılıkta dolandırıcılık tespiti:** Bankalar, kredi kartı işlemlerini izleyip olağandışı bir harcama gördüğünde uyarı verebilir. Bu sistem, geçmiş işlemlerden öğrenerek “normal” davranışı bilir ve farklı bir durum olduğunda alarm verir – yine makine öğrenimi uygulamasıdır.

**AI ile ML Arasındaki Farklar**

Yapay zeka (AI) ve makine öğrenimi (ML) terimleri sık sık birbiriyle karıştırılır, ancak aralarında bir hiyerarşi vardır. Makine öğrenimi, yapay zekânın bir alt kümesidir​. Yani her makine öğrenimi uygulaması bir yapay zeka örneğidir, fakat her yapay zeka uygulaması makine öğrenmesi kullanmak zorunda değildir​. Örneğin, sabit kurallarla programlanmış bir satranç oynayan yazılım yapay zekâ olarak kabul edilebilir, ancak bu yazılım belirli kurallar dahilinde çalışıyorsa ve veriden öğrenmiyorsa “makine öğrenmesi” değildir.
Basit bir benzetmeyle: Yapay zeka bir şemsiye kavram gibidir, makine öğrenimi ise o şemsiyenin altındaki yöntemlerden biridir. Yapay zekâ, makinelerin zeki davranmasını amaçlarken; makine öğrenimi, bu zekâya ulaşmanın belirli bir yoludur (verilerden örüntü öğrenerek). Örneğin:

- Eğer bir bilgisayar programı satrançta her olası hamleyi önceden programlanmış bir kural kitabıyla değerlendiriyorsa bu bir yapay zekâ yaklaşımıdır, ama makine öğrenmesi değildir (çünkü program yeni hamleleri kendi kendine öğrenmiyor, sadece önceden yazılmış kuralları uyguluyor).
- Öte yandan, bir program binlerce satranç maçının kayıtlarını inceleyip hangi hamlelerin kazanma olasılığını artırdığını kendi çıkarsıyorsa, bu makine öğrenmesidir (veriden öğrenme var). Bu program da bir yapay zekâ uygulamasıdır, ama özellikle makine öğrenmesi yöntemini kullanarak çalışır.

Kısacası AI daha geniş bir kavram, ML ise onun gerçekleştirilme yollarından biridir. Günlük konuşmada iki terim bazen birbiri yerine kullanılıyor olsa da, teknik olarak bu ayrımı bilmek faydalıdır.

## Fine-Tuning (İnce Ayar) Nedir?

Fine-tuning, önceden eğitilmiş bir modeli alıp onu belirli bir görev için biraz daha eğitme sürecidir​. Bir modeli sıfırdan eğitmek yerine, zaten benzer bir problem üzerinde öğrenmiş bir modeli alırız ve yeni problemimizin verileriyle kısa bir “ince ayar” eğitim yaparız. Böylece model, yeni göreve uyum sağlar. Fine-tuning genellikle transfer öğrenimin bir parçası olarak anılır ve modern yapay zeka projelerinde sıkça kullanılır.

**Gerçek hayattan bir benzetme:** Diyelim ki genel olarak araba kullanmayı bilen bir sürücünüz var. Şimdi onu sadece ralli yarışı için eğitmek istiyorsunuz. Baştan araba sürmeyi öğretmenize gerek yok; yerine, mevcut sürüş yeteneklerine ince ayar yaparak ralli pistinde nasıl davranacağını öğretirsiniz. Makine öğreniminde de fine-tuning benzer şekilde işler: Model zaten “temel yeteneklere” sahiptir, biz sadece hedef görevle ilgili ufak düzeltmeler yaparız.

**Teknik bir örnek:** Bir görüntü tanıma modeli düşünün. İnternet üzerindeki milyonlarca genel fotoğraf üzerinde eğitilmiş olsun (mesela kedileri, köpekleri, ev eşyalarını tanıyor). Bu modeli alıp, diyelim ki sadece röntgen filmlerinde hastalık tanıma görevine uyarlamak istiyoruz. Fine-tuning yaparak, modele elimizdeki sınırlı sayıdaki röntgen filmi görüntüsünü gösterir ve ağırlıklarında küçük değişiklikler yaparak onu bu özel işi yapmaya uygun hale getiririz. Bu sayede model, az miktarda veriyle yeni görevi öğrenir, çünkü zaten önceden genel görsel özellikleri öğrenmiş durumdadır.

## Full Training (Tam Eğitim) Nedir?

Full training, bir makine öğrenimi modelini sıfırdan, en baştan eğitmek anlamına gelir. Yani modelin bütün parametreleri rastgele bir başlangıçla alınır ve tamamen sizin veri setiniz üzerinde eğitilir. Bu, modelin “boş bir kafa” ile işe başlaması gibidir; tüm bilgiyi baştan sizin sağladığınız eğitim verisinden edinir.

Tam eğitim yaparken, genellikle daha fazla veri ve daha uzun eğitim süresi gerekebilir çünkü modelin hiçbir ön bilgisi yoktur. Fine-tuning’in aksine, burada bir kısayol yoktur – model öğrenmesi gereken ne varsa o eğitimde öğrenecektir.

**Gerçek hayat benzetmesi:** Hiç bilmediğiniz bir dilde konuşmayı öğrenmek istediğinizi düşünün. Eğer tam eğitim yolundan giderseniz, bu dili doğrudan A’dan Z’ye öğrenmeye başlarsınız: alfabesini, temel kelimelerini, gramerini sıfırdan çalışırsınız. Bu çok zaman ve pratik gerektirir. Diğer yandan, eğer zaten bildiğiniz bir dile benzese bile (örneğin İspanyolca biliyorsunuz ve İtalyanca öğrenmek istiyorsunuz), tamamen sıfırdan başlamadan önce İspanyolca bilginizden faydalanabilirsiniz – bu da bir çeşit fine-tuning olurdu.

Makine öğreniminde tam eğitim tercih edilecekse, genellikle yeterince büyük ve kapsamlı bir veri seti olduğundan ve mevcut hazır modellerin işe yaramayacağından emin olunur. Örneğin, çok özgün bir problem üzerinde çalışıyorsanız ve piyasada buna yakın bir önceden eğitilmiş model yoksa, modeli tam eğitimle kendiniz eğitmeniz gerekebilir.

## Train/Test Split (Eğitim/Test Bölünmesi) Nedir?

Train/test split, elinizdeki veri setini modelinizi eğitmek ve daha sonra doğruluğunu ölçmek amacıyla ayırma işlemine denir. Genel olarak bir veri setini iki ana kısma böleriz:

- **Eğitim seti (training set):** Model bu verilere bakarak öğrenir.
- **Test seti (test set):** Eğitim tamamlandıktan sonra, modeli hiç görmediği bu verilerle deneriz.

Bu ayrımın amacı, modelin yeni verilerde nasıl performans gösterdiğini anlamaktır. Eğer tüm veriyi eğitime kullanıp sonra aynı veride modelin başarısına baksaydık, modelin ezberleyip ezberlemediğini anlayamazdık. Test verisi, modelin gerçekten **genelleyebilme** yeteneğini ölçer.

**Günlük hayattan bir benzetme:** Bir öğrencinin sınava hazırlandığını düşünün. Öğrenci sınav konularını öğrenmek için ders notlarını ve soru bankalarını çalışır – bunlar **eğitim verisi** gibidir. Daha sonra gerçek sınava girer ve sınavda karşısına tamamen yeni sorular gelir – işte bu da **test verisi** gibidir. Öğrencinin sadece çalıştığı soruları ezberleyip ezberlemediğini, yoksa konuyu genellikle anlayıp anlamadığını anlamak için sınav soruları elbette farklı olmalıdır. Eğer öğrenci çalıştığı soruların aynısıyla sınava girerse (ki bu durumda modelin test verisi de eğitim verisiyle aynı olurdu), aldığı not yüksek olsa bile bu onun konuyu anladığını göstermez; sadece ezber yapmış olabilir. Aynı şekilde, bir makine öğrenimi modeli de eğitildiği veride mükemmel sonuç verse bile, test verisinde başarılı olamıyorsa bu modelin pratikte işe yaramadığını gösterir.

Uygulamada genellikle verinin %70-%80’lik kısmı eğitim için, kalan %20-%30’luk kısmı test için ayrılır (oranlar ihtiyaca göre değişebilir). Bu sayede model, gördüğü verilerle öğrenir, görmediği verilerle de sınanır.

(Not: Sıkça, eğitim verisinden ayrı olarak bir de **doğrulama (validation)** seti ayrılır. Bir sonraki bölümde bunu açıklıyoruz. Doğrulama seti, eğitim sırasında modelin ayarlarını denemek için kullanılır ve en sonunda model **test seti** ile değerlendirilir.)

## Training Data (Eğitim Verisi) Nedir?

Eğitim verisi, modelin öğrenmesi için kullandığımız veri kümesidir. Model tüm kalıpları, ilişkileri, “bilgiyi” bu veri üzerinden alır. Bir nevi, modelin **ders kitabı ve alıştırmaları** eğitim verisidir diyebiliriz.

Örneğin, bir yapay zekâya elma ile portakalı ayırt etmeyi öğretmek istiyorsak, eğitim verisi olarak ona birçok **etiketli** resim gösteririz: Hangi resimde elma var, hangisinde portakal var. Model bu örneklerden öğrenerek “elma genelde kırmızıdır yuvarlaktır; portakal turuncudur ve yüzeyi pütürlüdür” gibi çıkarımları kendi kendine yapar. Elbette model bunu bizim gibi cümlelerle düşünmez, ama matematiksel olarak bu ayrımı yapabilmeyi öğrenir.

**Gerçek hayattan benzetme:** Bir çocuğa hayvanları öğretirken, ona farklı hayvan resimleri gösterip isimlerini söylersiniz. “Bak bu bir kedi, küçük ve tüylü; bu bir köpek, daha büyük ve havlar.” Bir süre sonra çocuk yeni bir hayvan gördüğünde (daha önce görmediği bir kedi fotoğrafı mesela) “bu bir kedi olmalı” diyebilir. Burada çocuğun öğrendiği tüm örnekler onun eğitim verisiydi.

Özetle, eğitim verisi modelin **hafızasını şekillendirir**. Bu veri ne kadar çeşitli ve kapsamlı olursa modelin öğrenebileceği kapsam da o kadar geniş olur. Ancak sadece eğitim verisine bakarak modelin başarısını değerlendiremeyiz; bu yüzden farklı veri setlerine de ihtiyaç duyarız (doğrulama ve test verileri gibi).

## Validation Data (Doğrulama Verisi) Nedir?

Doğrulama verisi, model eğitilirken kullanılan ve **modelin performansını izlemek/ayarlarını yapmak için** ayrılan veri setidir. Bu veri, eğitim sırasında ara kontrol noktası gibi görev yapar. Model, eğitim sırasında belirli aralıklarla doğrulama seti üzerinde test edilir ki aşırı uyum **(overfitting)** olup olmadığı anlaşılsın ve gerekiyorsa hiperparametre adı verilen model ayarları bu sonuçlara göre ayarlansın​

Doğrulama verisi, eğitim verisinden ayrı tutulur, ancak model bu veriye bakarak kendini güncellemez (yani hatalarından öğrenmez) – sadece performansına bakılır. Amaç, modelin **görmediği veriye karşı** başarısını eğitim sırasında takip etmektir. Eğer model doğrulama verisinde kötüleşmeye başlıyorsa, bu genelde aşırı öğrenmeye başladığının bir işaretidir ve eğitim durdurulabilir veya ayarları değiştirilebilir.

**Gerçek hayattan benzetme:** Yine öğrenci örneğine dönersek, öğrenci sınavdan önce kendi kendine küçük bir deneme sınavı yapabilir veya öğretmeni ona küçük bir **quiz** uygulayabilir. Bu quiz sonuçlarına bakarak öğrenci hangi konularda eksik olduğunu görür ve gerekirse daha fazla çalışır. Quiz sorularının amacı not vermek değil, öğrenciyi sınava daha iyi hazırlamaktır. Doğrulama verisi de model için böyle bir rol oynar – bir nevi **prova sınavı** gibidir.

Önemli nokta, doğrulama seti de hiçbir şekilde eğitim setine dahil edilmez, model bu veriyi “görerek” öğrenmez. Sadece performans ölçümü için kullanılır. En sonunda ise modelin asıl değerlendirmesi test setiyle yapılır (doğrulama seti ile değil)​

## Test Data (Test Verisi) Nedir?

Test verisi, modelin eğitimi tamamlandıktan sonra, gerçek dünyada nasıl performans göstereceğini ölçmek için kullanılan, **tamamen saklanmış** ve model tarafından görülmemiş veri kümesidir. Bu verilerle modelin tahminleri alınır ve sonuçlar değerlendirilir. Test verisinin amacı, modelin genel başarı düzeyini ve hatalarını samimi bir şekilde ortaya koymaktır.

Yine öğrenci benzetmemize bakarsak, test verisi **asıl sınav sorularıdır**. Öğrenci tüm hazırlığını yapmıştır (model eğitilmiştir), belki kendini denemiştir (doğrulama yapılmıştır), artık sınav vakti gelmiştir. Sınavda karşısına çıkan sorular, çalıştığı kaynaklarda birebir görmediği sorulardır. Burada aldığı sonuç, onun o konuları gerçekten öğrenip öğrenmediğinin ölçüsüdür. Model için de test verisindeki performansı, eğitimin gerçekten işe yarayıp yaramadığını gösterir.

Test verisi ile modelin başarımını ölçerken, genellikle **metrikler** hesaplanır: Örneğin yüzde kaç doğrulukla bildi, hataları nelerdi vs. Bu sonuçlar modelin gerçek hayata ne kadar hazır olduğunu gösterir. Eğer test verisinde iyi sonuç veriyorsa, modeli gerçek dünyada (üretimde) kullanmak üzere güvenimiz artar. Yok eğer test verisinde başarısızsa, modeli yeniden gözden geçirmek gerekir (belki daha fazla veri ile yeniden eğitmek veya model yapısını değiştirmek gibi).

Özetle, **eğitim verisi öğrenme içindir, doğrulama verisi ayar ve izleme içindir, test verisi ise nihai değerlendirme içindir**. ​Bu ayrım, makine öğrenimi modelinin adil ve genel performansını ölçebilmek için kritik öneme sahiptir.

## Overfitting (Aşırı Uyum) Nedir?

Overfitting, bir makine öğrenimi modelinin **eğitim verisine aşırı derecede uyum sağlaması**, ama yeni verilere genelleyememesi durumudur​.Aşırı uydurmuş bir model, adeta eğitim verisini **ezberlemiştir** – bu yüzden eğitim verisinde hatasız sonuç verebilir; fakat eğitimde görmediği yeni bir veriyle karşılaştığında beklenmedik hatalar yapar. Bu istenmeyen bir durumdur, çünkü modelin amacı sadece ezberlemek değil, öğrendiklerini genelleştirip her türlü veriye uygulanabilir hale getirmektir.

**Gerçek hayattan basit bir örnek:** Bir öğrenci düşünün, matematik sınavına çalışırken elindeki çözümlü soruları ve cevaplarını ezberliyor. Sınavda karşısına benzer sorular gelirse çok iyi yapıyor; ancak soru biraz farklılaşırsa (örneğin sayılar değişir veya farklı bir formül sorulur) bocalıyor ve soruyu çözemiyor. Bu öğrenci aslında konuyu tam anlamamış, sadece gördüğü soruların cevaplarını ezberlemiş. Modelde overfitting de aynen böyledir. Model eğitim verisindeki örnekleri ezberlerse, o örneklerde mükemmel sonuç verir ama küçük bir değişiklik olduğunda ne yapacağını bilemez.

Teknik olarak, aşırı uyum çoğunlukla model çok karmaşık olduğunda veya eğitim verisi göreceli olarak az ve sınırlı olduğunda ortaya çıkar. Model, verideki gürültü veya rastlantısal ayrıntıları dahi öğrenir. Örneğin, kedi fotoğraflarını öğrenen bir model düşünelim: Eğitimdeki bir kedi fotoğrafında arka planda hep bir belirli renk duvar olsun. Model kediye dair özelliklerle birlikte belki o duvarın rengini de “kedi özelliği” olarak öğrenmiş olabilir. Sonra farklı renkte arka planı olan bir kedi fotoğrafı gösterildiğinde tanıyamayabilir, çünkü **yanlış bir detayı** öğrenmiştir

Kaynaklarda bu durum şöyle özetlenir: _“Aşırı öğrenme durumunda modelimiz eğitim kümesinde çok iyi bir performans verirken, test kümesinde daha başarısız bir performans gösterir. Eğitim kümesinden elde ettiği bilgileri genelleyemez. Bu duruma örnek olarak bir öğrencinin sınava girmeden önce bilgileri çok iyi bir şekilde ezberleyip, sınava girince farklı türde sorular ile karşılaşıp başarısız olması verilebilir.”​_

**Overfitting’i önlemek için** çeşitli yöntemler kullanılır (örneğin daha fazla veri toplamak, modeli basitleştirmek, düzenlileştirme/regularization teknikleri uygulamak, **doğrulama verisi** ile erken durdurma yapmak gibi). Ama bu konular ileri düzey konular olup, temelde bilinmesi gereken: aşırı uydurma, modelin **yeni durumlarda başarısız olması** demektir.

## Epoch (Dönem) Nedir?

Epoch (Türkçesiyle “dönem”), makine öğrenimi eğitim sürecinde, modelin tüm eğitim veri kümesini baştan sona bir kez görmesi anlamına gelir. Bir eğitim süreci genellikle birden fazla epoch içerir. Örneğin 5 epoch boyunca eğitim yapıyoruz demek, model eğitimdeki tüm verileri 5 kez gözden geçirecek demektir.

Bunu şöyle düşünebiliriz: 1000 resimden oluşan bir eğitim veri setimiz varsa, 1 epoch’ta bu 1000 resmin her biri model tarafından işlenip öğrenmeye katkı yapar. 10 epoch eğitirsek, model toplamda verisetini 10 kez taramış olur. Epoch sayısı bir hiperparametredir, yani eğitim başlamadan önce belirlediğimiz bir ayardır; genellikle eğitim yeterince öğrenene veya doğrulama başarımı durmaya başlayana kadar birkaç, birkaç yüz hatta binlerce epoch denenebilir​

**Anlaması kolay bir örnekle açıklayalım:** Diyelim ki ezberlemeniz gereken 50 tane kelime var. Bu 50 kelimeyi bir kez baştan sona çalışmanız bir epoch olsun. Eğer 5 epoch çalışırsanız, bu listeyi 5 defa tekrar etmiş olursunuz. Genelde listeyi ne kadar çok tekrar ederseniz o kadar iyi akılda kalır; fakat bir yerden sonra verim azalmaya başlayabilir veya gereğinden fazla tekrar yapıp zaman kaybedebilirsiniz. Model eğitimi de buna benzer: Veriyi birkaç kez göstermek genelde modelin öğrenmesini artırır, ancak çok fazla epoch yaparsak model **aşırı öğrenme** riskiyle karşılaşabilir. Bu yüzden uygun epoch sayısını bulmak önemlidir.

Özetle, epoch sayısı modelin **eğitim turu** sayısıdır. “1 epoch = tüm veri bir kere gösterildi”. Bu kavram, eğitim sürecini adımlara bölmek ve her adımda modeli değerlendirmek için kullanılır. Örneğin her epoch sonunda doğrulama setiyle modele bakılıp performansı ölçülür, böylece kaç epoch’un ideal olduğuna karar verilebilir.

## Transfer Learning (Transfer Öğrenimi) Nedir?

Transfer öğrenimi, bir makine öğrenimi modelinin bir görevde öğrendiği bilgiyi başka bir benzer göreve aktarması yaklaşımıdır​. Normalde, her yeni görev için modeli sıfırdan eğitmemiz gerekebilir; ancak transfer öğrenimi sayesinde, modelin halihazırda öğrendiği becerileri yeniden kullanabiliriz ve böylece **daha az veriyle**, **daha hızlı eğitim** mümkün olur.

Bunu bir örnekle somutlaştıralım: Diyelim ki İngilizce biliyorsunuz ve şimdi İspanyolca öğrenmek istiyorsunuz. İngilizce bilginiz size İspanyolca öğrenirken avantaj sağlar – pek çok kelime benzer, alfabe aynı, dil yapıları benzerlik gösteriyor. Yani İngilizce bilgisi, İspanyolca öğrenimine transfer oluyor (aktarılıyor). Tam tersi, eğer İngilizce bilmeseydiniz ve Çince öğrenmeye kalksaydınız, elinizde işe yarar pek bir bilgi olmayacaktı, sıfırdan öğrenmeniz gerekecekti. İşte yapay zekâ modelleri de benzer şekilde, bir alanda öğrendiklerini diğer alanda kullanabilir.

**Teknik açıdan bir örnek:** “Resim tanıma” için eğitilmiş büyük bir model düşünün (milyonlarca görüntü üzerinde eğitilmiş ve binlerce nesneyi tanıyabilen bir model olsun). Şimdi elimizde çok özel bir görev var: Diyelim sadece kedilerin belirli bir cinsini tespit etmek istiyoruz ya da tıbbi bir alanda röntgen görüntülerinden bir hastalığı saptayacağız. Sıfırdan model eğitmek yerine, genel resim tanıma modelini alıp, son katmanlarını veya bazı ayarlarını bu yeni veriyle **yeniden eğitmek (yani fine-tune etmek)** transfer öğrenimidir. Modelin önceki görevde öğrendiği temel görsel özellikler (kenarlar, şekiller, renkler gibi) yeni göreve taşınır ve sadece spesifik kısım öğretilir. Sonuç olarak, çok daha az veriyle iyi bir performans elde edilebilir.

Günlük hayatta transfer öğrenimine bir diğer örnek de eğitim hayatımızdan olabilir: Lisede matematik öğrendiğimiz için üniversitede fizik derslerini daha kolay anlayabiliriz. Çünkü matematik bilgisini fiziğe transfer ediyoruz. Aynı şekilde, bir şirkette müşteri hizmetleri konusunda eğitilmiş bir yapay zekâ modelini alıp başka bir şirkette benzer müşteri sorularını yanıtlamak için uyarlamak da transfer öğrenimidir (temel dil becerilerini ve soru-cevap yapılarını zaten biliyordur, sadece yeni şirketin ürün bilgilerini öğrenmesi yeterli olur).


## Encoder Nedir?

Encoder kelime anlamıyla “**kodlayıcı**” demektir. Yapay zeka ve veri işleme bağlamında encoder, **veriyi bir formattan başka bir formata dönüştüren** veya daha kullanışlı bir temsilini çıkaran sistemdir. Veriyi ham halinden alıp, modelin daha kolay işleyebileceği bir biçime şifreler diyebiliriz. Bu şifrelemeden kastımız genellikle veriyi sayısal bir özelliğe dönüştürmek veya boyutunu/karmaşıklığını azaltmaktır.

Örneğin, metin verisini ele alalım: Bir encoder, metindeki kelimeleri alıp her birini belirli boyutta bir sayı vektörüne çevirebilir (bu işleme embedding de denir). Model bu sayısal temsil üzerinden işlem yapar, çünkü matematiksel olarak anlam çıkarabilmesi için metnin sayılara çevrilmesi gerekir. Burada encoder görev yapmış olur. Benzer şekilde, bir görüntü işleme modelinde encoder, resmi alıp önemli özelliklerini çıkarabilir (köşeler, renk dağılımları, şekiller gibi) ve bu özellikleri bir vektör halinde temsil edebilir.

**Günlük hayattan örneklerle:**

- **Dosya sıkıştırma:** Bir ZIP programı, büyük bir dosyayı daha küçük bir sıkıştırılmış dosyaya çevirir. Aslında bu bir çeşit encoder işlemidir – orijinal veriyi alır, farklı bir formatta (daha küçük boyutlu) kodlar.
- **Mors alfabesi:** Normal harflerle yazılmış bir mesajı mors koduna çevirmek de bir kodlama işlemidir. Burada encoder rolünü mesajı nokta ve çizgi dizisine çeviren kişi ya da cihaz üstlenir. Örneğin “SOS” kelimesini “... --- ...” şeklinde mors koduna encoder (kodlayıcı) çevirir.
- **MP3 oluşturma:** Bir müzik CD’sindeki ham ses verisini alıp MP3 formatına dönüştüren yazılım bir encoderdır. Bu yazılım, sesi sıkıştırır ve daha küçük hale getirir​

Encoder’ların amacı çoğunlukla veriyi standart hale getirmek, sıkıştırmak veya gizlemek olabilir​. Önemli bir nokta: Bir encoder ile veriyi dönüştürdükten sonra, orijinal haline geri çevirebilmek için bir decoder (kod çözücü) gerekir​
. Zaten genellikle encoder ve decoder ikilisi beraber anılır (özellikle yapay zeka mimarilerinde, örneğin “encoder–decoder ağları”).Özetle, encoder veriyi alır şifreler/kodar, modelin anlayacağı dile çevirir diyebiliriz.

## Decoder nedir?

Decoder, encoder’ın tersine çalışan sistemdir; yani kodlanmış veriyi alıp orijinal veya istenen formata geri çeviren bileşendir. Türkçesiyle “çözümleyici” veya “kod çözücü” de diyebiliriz. Encoder nasıl veriyi şifrelediyse, decoder da o şifreyi çözer.

Örneğin, biraz önceki örnekleri devam edelim:

- ZIP ile sıkıştırılmış bir dosyayı açmak (unzip yapmak) decoder işidir. Decoder programı, sıkışmış veriyi alır ve orijinal dosyayı geri elde eder.
- Mors koduyla “... --- ...” şeklinde alınan sinyali tekrar “SOS” harflerine çevirmek decoder’ın görevidir – mors kodunu çözer. Bu işi yapan kişi veya cihaz decoder rolünü üstlenir.
- MP3 çalar bir decoder’dır; MP3 formatındaki sıkıştırılmış müzik dosyasını alır ve hoparlörden dinlediğimiz analog ses dalgalarına dönüştürür.

Yapay zeka modellerinde de decoder önemli bir kavramdır. Özellikle **encoder–decoder** mimarileri adı verilen model tasarımlarında (örneğin makine çevirisi yapan sinir ağları, özetleme yapan modeller veya Görüntüden metin üreten modeller gibi), encoder gelen veriyi iç temsil olarak kodlar, decoder ise istenen çıktıyı üretir.

Örneğin bir **çeviri modelinde**: İngilizce bir cümle encoder tarafından “anlam vektörüne” dönüştürülür; ardından decoder bu vektörü alıp diyelim ki Türkçe cümleye dönüştürür. Yani encoder metni anlar, decoder yeni dilde anlatır.

Başka bir kullanım alanı olarak, GPT gibi dil modellerinde de aslında jeneratif kısım bir decoder gibidir (aşağıda GPT’yi açıklayacağız). Verilen bir başlangıç metnine dayanarak devamını üretmek, bir anlamda kodlanmış dili gerçek cümlelere çözümlemek demektir.

Özetle, **decoder = kod çözme.** Encoder ile elde ettiğimiz ara temsili, insanın veya hedef uygulamanın kullanacağı forma decoder geri çevirir. Birçok sistemde encoder ve decoder birlikte çalışır: Biri bilgiyi paketler, diğeri açar.

## GPT (Generative Pre-trained Transformer) Nedir?

GPT, İngilizce “Generative Pre-trained Transformer” ifadesinin kısaltmasıdır (Türkçesi: Üretici, Ön-Eğitimli Dönüştürücü anlamına gelir)​ . Bu, OpenAI tarafından geliştirilmiş bir yapay zeka model türüdür. GPT modelleri, özellikle **metin üretmek** (yeni cümleler, paragraflar oluşturmak) üzere tasarlanmıştır ve dil işleme alanında çığır açmışlardır.

Tanımdaki kelimeleri parçalayarak anlayalım:

- **Pre-trained (Ön-eğitimli):** GPT modeli, devasa miktarda metin veri üzerinde önceden eğitilmiştir. Örneğin kitaplar, makaleler, web sayfaları gibi çok geniş bir yazılı veri kütüphanesini okumuş ve genel dil yapısını, bilgisini öğrenmiştir. Bu ön eğitim sayesindedir ki GPT, dilin gramerini, kelime anlamlarını, hatta dünya ile ilgili genel bilgileri istatistiksel olarak bünyesinde barındırır.
- **Generative (Üretici):** GPT, yeni ve orijinal metin üretir. Yani ona bir başlangıç cümlesi verdiğinizde, sonrasını kendi yazar; soru sorarsanız mantıklı bir yanıt üretir; bir konu verirsiniz o konuda makale bile taslaklayabilir. “Üretici” olması, sadece var olanı sınıflandırmak veya analiz etmek değil, yeni içerik oluşturmak olduğu anlamına gelir.
- **Transformer:** Bu, GPT’nin mimari yapısının adıdır. Transformer, 2017 yılında ortaya çıkan ve dil işleme görevlerinde çok başarılı olan bir sinir ağı mimarisidir. Transformers, dikkat mekanizmaları kullanarak dildeki kelimeler arasındaki ilişkileri öğrenir. GPT de bir transformer mimarisi üzerine kuruludur ve bu sayede uzun metin ilişkilerini bile başarıyla yakalayabilir.


GPT modelinin çalışma prensibini basitçe şöyle özetleyebiliriz: İstatistiksel dil tamamlama. Yani çok okuduğu için, bir cümlede bir kelimeden sonra hangi kelimenin gelebileceğini olasılıksal olarak çok iyi tahmin edebilir. Bu tahminleri ard arda zincirleyerek bir paragraf üretebilir. Örneğin, “Bugün hava çok...” diye başlayan bir cümleyi gördüğünde, devamına “**sıcak**” veya “**güzel**” gibi bir kelime gelme olasılığının yüksek olduğunu “**bilir**”. Elbette olay sadece kelime tahmini değil, daha karmaşık cümle yapıları ve tutarlılık da gözetiliyor; ama temel mantık, metni parça parça oluşturmak ve her adımda en uygun kelimeyi (veya ifadeyi) seçmek.

En bilinen örnek ChatGPT’dir. ChatGPT, GPT mimarisini kullanan bir sohbet robotudur ve insanlarla doğal bir dilde diyalog kurabilir. Siz bir şey sorarsınız veya talep edersiniz, o da size anlaşılır ve bağlama uygun bir yanıt verir. Örneğin ChatGPT’den bir hikaye anlatmasını isteyebilirsiniz, size özgün bir hikaye yazabilir. Ya da bir makale hakkında özet isteyebilirsiniz, o metni okuyup özetleyebilir. Ayrıca GPT tabanlı modeller, e-posta taslakları yazma, çeviri yapma, kod üretme, soruları yanıtlama, hatta şiir yazma gibi pek çok amaçla kullanılabiliyor.

Önemli bir nokta: GPT bir bilgiyi araştırmaz, daha çok öğrendiği geniş bilgi havuzundan yola çıkarak yanıt üretir. Yani verdiği cevaplar dilbilgisel ve bağlamsal olarak genellikle doğru ve mantıklıdır, fakat bu cevapların doğruluğu modelin eğitim aldığı veriye dayanır. Bu nedenle, ChatGPT gibi modeller bazen inandırıcı görünen hatalar yapabilir; çünkü gerçekleri değil, olasılıkları dillendirir.

Özetle GPT, çok büyük bir beyinle eğitilmiş bir yazar gibidir. Ne hakkında yazmasını isterseniz, eğitiminde gördüğü bilgileri kullanarak o konuda size akıcı bir metin oluşturabilir. Günümüzde yapay zekâ alanında GPT ve benzeri büyük dil modelleri, insan-dil etkileşiminde devrim yaratmış durumda. Artık müşteri hizmetlerinde otomatik yanıt veren botlar, akıllı asistanlar, içerik üretimine yardımcı araçlar gibi pek çok alanda GPT benzeri AI modelleri kullanılmaktadır.
