import random

def guess_number():
    print("Zorluk seviyesi seçin:")
    print("1: Kolay (1-50)")
    print("2: Orta (1-100)")
    print("3: Zor (1-200)")
    
    difficulty = int(input("Seçiminiz (1-3): "))
    max_number = {1: 50, 2: 100, 3: 200}[difficulty]
    
    number = random.randint(1, max_number)
    attempts = 0
    
    print(f"1-{max_number} arası sayı tahmin oyunu!")
    
    while True:
        guess = int(input("Tahmininiz: "))
        attempts += 1
        
        if guess == number:
            print(f"Tebrikler! {attempts} denemede buldunuz!")
            break
        elif guess < number:
            print("Daha yüksek!")
        else:
            print("Daha düşük!")

if __name__ == "__main__":
    guess_number()