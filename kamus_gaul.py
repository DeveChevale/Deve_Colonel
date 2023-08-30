meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidak setujuan",
            "CREEPY": "menakutkan,tidak menyenangkan",
            "AGGRO": "untuk menjadi gelisah/marah",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print(meme_dict[word])

else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("saya tidak menemukan minimal Kapital/lainnya")
