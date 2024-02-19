class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")
        self.file.seek(0)

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:
            for book in books:
                title, author, release_year, num_pages = book.split(',')
                print(f"Kitap: {title}, Yazar: {author}, Yayim Yili : {release_year}, Sayfa Sayisi: {num_pages}")
        else:
            print("Kütüphanede kitap bulunmamaktadır.")

    def add_book(self):
        title = input("Kitap başlığını girin: ")
        author = input("Kitabın yazarını girin: ")
        release_year = input("Kitabın yayın yılını girin: ")
        num_pages = input("Kitabın sayfa sayısını girin: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Kitap başarıyla eklendi.")

    def remove_book(self):
        title = input("Silmek istediğiniz kitabın başlığını girin: ").lower()
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            updated_books = [book for book in books if title not in book.lower()]
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines(updated_books)
            print(f"'{title}' başlıklı kitap başarıyla silindi.")
        else:
            print("Kütüphanede kitap bulunmamaktadır.")

    def __del__(self):
        if self.file:
            self.file.close()

# Kütüphane nesnesini oluşturalım
lib = Library("books.txt")

# Menü etkileşimi
while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")

    choice = input("Lütfen seçiminizi yapın (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")
