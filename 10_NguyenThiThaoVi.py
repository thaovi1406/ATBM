#Cho k= STT , và Plaintext = TenCuaBan. Hãy mã hóa theo thuật toán Ceasar
def caesar_index(plaintext, k):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for ch in plaintext:
        if ch in alphabet_upper:  # chữ in hoa
            pos = alphabet_upper.index(ch)          # vị trí 0-25
            new_pos = (pos + k) % 26                # dịch k bước
            ciphertext += alphabet_upper[new_pos]   #lấy kí tự ở vị trí new_pos
        elif ch in alphabet_lower:  # chữ thường
            pos = alphabet_lower.index(ch)
            new_pos = (pos + k) % 26
            ciphertext += alphabet_lower[new_pos]
        else:
            ciphertext += ch  # ký tự khác thì giữ nguyên
    return ciphertext

plaintext = "NguyenThiThaoVi"
k = 10

print("Plaintext  :", plaintext)
print("Ma hoa Ceasar:", caesar_index(plaintext, k))




