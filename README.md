**⚡ MSI Fan Kontrol Merkezi**  
Linux (CachyOS/Arch) tabanlı işletim sistemlerinde çalışan MSI laptoplar için geliştirilmiş, hafif, güvenli ve modern bir fan performans yönetim uygulamasıdır. **Python** ve  **PySide6 (Qt6)** mimarisiyle geliştirilmiştir.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OYQ1AABSAwc8mi5wvkwZyCKCAACr4Z7a7BLfMzFYdAQDwF+da3dX+9QQAgNeuB6feBdUJcyS2AAAAAElFTkSuQmCC)  
**✨ Özellikler**  
- 🔇 **Sessiz Mod (Silent):** Günlük işlerde laptopun tamamen sessiz çalışmasını sağlar.  
- 🔄 **Otomatik Akıllı Mod (Auto):** Sistem sıcaklığına göre fan hızını otomatik dengeler.  
- 🚀 **Cool Boost (Uçuşa Geçiyoruz):** Ağır yük altında ve oyunlarda fanları maksimum hıza zorlar.  
- 🔒 **Güvenli Mimari:** Herhangi bir bulut/API anahtarı içermez, tamamen yerel (local) çalışır ve sistem güvenliğini tehlikeye atmaz.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANElEQVR4nO3OUQmAABBAsSdYxKbXxlpGEAOIFfwTYUuwZWa2ag8AgL841uquzq8nAAC8dj05VAYO3phhoQAAAABJRU5ErkJggg==)  
**🛠️ Gereksinimler**  
Uygulamanın fan profillerini donanım çipine (EC) iletebilmesi için sisteminizde isw aracının kurulu olması gerekir:  
sudo pacman -S isw  
   
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANElEQVR4nO3OQQ2AQBAAsSE5G6B1ReAQGzywwI+QtAq6zcxRnQEA8BfXqla1fz0BAOC1+wEbGgQ4wwvoRwAAAABJRU5ErkJggg==)  
**🚀 Kurulum ve Çalıştırma**  
Projenin yerel bilgisayarınızda (CachyOS/Arch) çalıştırılması için aşağıdaki adımları sırasıyla uygulayabilirsiniz:  
1. Depoyu Bilgisayarınıza İndirin  
git clone https://github.com  
 cd msi-control-center  
   
1. Bağımlılıkları Yükleyin  
   
 Sanal ortam oluşturup gerekli olan PySide6 arayüz kütüphanesini kurun:  
python -m venv .venv  
 source .venv/bin/activate.fish   (Fish Shell kullananlar için)  
 pip install PySide6  
   
1. Uygulamayı Başlatın  
python src/main.py  
   
Bu işe yaramazsa  
   
 "cd msi-control-center" yazarak klasörün içine girip önceki komutu bir daha deneyin  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSNBCkLfE07YGfHAiAU2QtIq6DIzW7UHAMBfnGt1V8fXEwAAXrse4eQF6VhvmPsAAAAASUVORK5CYII=)  
**📄 Lisans (License)**  
Bu proje tamamen **Açık Kaynak (Open Source)** olarak geliştirilmiştir. Dilediğiniz gibi geliştirebilir, değiştirebilir ve kendi reponuzda paylaşabilirsiniz.  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚡ **MSI Fan Control Center** ** | English ** **  
 **A lightweight, secure, and modern fan performance management application developed for MSI laptops running on Linux (CachyOS/Arch) based operating systems. It is built using Python and PySide6 (Qt6) architecture.  
✨ **Features**  
- **Silent Mode:** Ensures the laptop runs completely silent during daily tasks.  
- **Auto Smart Mode:** Automatically balances fan speed based on system temperature.  
- **Cool Boost (Full Speed):** Forces fans to maximum speed under heavy workloads and gaming.  
- **Secure Architecture:** Contains no cloud/API keys, runs completely locally, and does not compromise system security.  
🛠️ **Requirements  
 **For the application to communicate fan profiles to the hardware chip (EC), the isw tool must be installed on your system:  
**bash**  
sudo pacman -S isw  
   
🚀 **Installation and Execution  
 **You can follow these steps in order to run the project on your local machine (CachyOS/Arch):  
1. **Clone the Repository**  
**bash**  
git clone https://github.com  
cd msi-control-center  
   
  
2. **Install Dependencies  
 **Create a virtual environment and install the required PySide6 interface library:  
**bash**  
python -m venv .venv  
source .venv/bin/activate.fish   # For Fish Shell users  
pip install PySide6  
   
 
3. **Launch the Application**  
**bash**  
python src/main.py  
   
 
If this doesn't work, navigate into the folder by typing cd msi-control-center and try the previous command again.  
📄 **License  
 **This project is developed completely as Open Source. You are free to improve, modify, and share it in your own repository as you wish.  
   
