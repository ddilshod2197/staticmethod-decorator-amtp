class Arxitektor:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def ismni_chiqar(self):
        return f"Arxitektorning ismi: {self.ism} {self.familiya}"

    @staticmethod
    def ismni_chiqar_static(ism, familiya):
        return f"Arxitektorning ismi: {ism} {familiya}"

arxitektor = Arxitektor("Ali", "Vali")
print(arxitektor.ismni_chiqar())
print(Arxitektor.ismni_chiqar_static("Ali", "Vali"))
```

Kodda `@staticmethod` qachon ishlatiladi degan savolga javob berish uchun quyidagilar ko'rsatilgan:

- `@staticmethod` metodlar klassga tegishli bo'lib, ular klassning obyektlari orasida farq qilmaydi.
- `@staticmethod` metodlar klassga tegishli bo'lib, ular klassning obyektlari orasida farq qilmaydi. Ular klassga tegishli bo'lib, ular klassning obyektlari orasida farq qilmaydi.
- `@staticmethod` metodlar klassga tegishli bo'lib, ular klassning obyektlari orasida farq qilmaydi. Ular klassga tegishli bo'lib, ular klassning obyektlari orasida farq qilmaydi.
