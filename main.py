import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    
    print("1-100 arası sayı tahmin oyunu!")
    
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