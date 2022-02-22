from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
şu_an = datetime.now()

saniye = datetime.timestamp(şu_an)

print(saniye)

şu_an2 = datetime.fromtimestamp(0)

print(şu_an2)