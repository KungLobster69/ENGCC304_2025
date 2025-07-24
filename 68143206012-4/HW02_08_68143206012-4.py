#โปรแกรมวิเคราะห์ประโยค
sentence = input("ป้อนประโยค: ")
char_count = len(sentence)
word = sentence.split()
word_count = len(word)
print("ประโยคของคุณ: ", sentence)
print("มีจำนวนอักขระทั้งหมด: ", char_count, "ตัว")
print("มีจำนวนคำทั้งหมด: ", word_count, "คำ")