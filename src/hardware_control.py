import subprocess

class HardwareController:
  
    def __init__(self):
        pass

    def set_fan_profile(self, profile_name):
      
        
        if profile_name == "coolerboost":
            command = ["pkexec", "isw", "-b", "on"]
        elif profile_name == "auto":
           
            subprocess.run(["pkexec", "isw", "-b", "off"], stdout=subprocess.DEVNULL)
            command = ["pkexec", "isw", "-p", "auto"]
        elif profile_name == "silent":
            subprocess.run(["pkexec", "isw", "-b", "off"], stdout=subprocess.DEVNULL)
            command = ["pkexec", "isw", "-p", "silent"]
        else:
            print(f"[FAN Hata] Geçersiz profil ismi: {profile_name}")
            return

        try:
            # Bunu Okuyan Piç
            subprocess.run(command, check=True)
            print(f"[FAN] Profil başarıyla uygulandı: {profile_name}")
        except Exception as e:
            print(f"[FAN Hata] Fan ayarı uygulanamadı: {e}")
