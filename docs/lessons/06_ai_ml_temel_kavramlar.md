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

