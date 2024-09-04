from art import logo
import random

# Blackjack oyununda kullanılan kartlar. 11, As kartını temsil eder.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Oyuncu ve bilgisayarın kartlarını saklamak için listeler oluşturulur.
user_cards = []
computer_cards = []

def calculate_score(cards):
    """Bu fonksiyon, verilen kart listesinin toplam puanını hesaplar.
    As kartı (11) durumu göz önüne alınarak eğer toplam puan 21'i geçerse, As kartı 1 olarak değerlendirilir."""

    score = sum(cards)
    # As kartlarının sayısını kontrol et
    num_aces = cards.count(11)

    # Toplam puan 21'i geçiyorsa ve As kartı varsa, As kartını 11'den 1'e çevir
    while score > 21 and num_aces > 0:
        score -= 10  # As kartını 11'den 1'e çevir
        num_aces -= 1

    return score

def blackjack():
    """Bu fonksiyon, bir Blackjack oyunu başlatır ve kullanıcı ile bilgisayarın kartlarını yönetir."""

    # Yeni oyun için önceki kartları temizle
    user_cards.clear()
    computer_cards.clear()

    # Oyuncu ve bilgisayara iki kart dağıtılır
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    # Bilgisayarın toplam puanı 17'den azsa, bilgisayar kart çeker
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    # Oyunun logosunu ve ilk kartların durumu gösterilir
    print(logo)
    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    # Eğer oyuncunun ilk iki kartının toplamı 21 ise, Blackjack yapmış demektir
    if calculate_score(user_cards) == 21:
        print("Blackjack! You win!")
        return

    game_over = False
    while not game_over:
        # Oyuncuya bir kart daha almak isteyip istemediği sorulur
        hit_or_stay = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if hit_or_stay == "y":
            # Oyuncu bir kart daha çekmeyi seçerse, kart listesine eklenir
            user_cards.append(random.choice(cards))
            print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"\tComputer's first card: {computer_cards[0]}")

            # Eğer oyuncunun toplam puanı 21'i geçerse, oyuncu kaybeder
            if calculate_score(user_cards) > 21:
                print("You have lost!")
                game_over = True
        else:
            # Oyuncu kart çekmeyi durdurmayı seçerse, oyun sona erer
            game_over = True
            print(f"Your final hand is: {user_cards}, final score: {calculate_score(user_cards)}")
            print(f"Computer's final hand is: {computer_cards}, final score: {calculate_score(computer_cards)}")

            # Oyun sonucuna göre kazanan belirlenir
            if calculate_score(computer_cards) > 21:
                print("You win!")
            elif calculate_score(computer_cards) > calculate_score(user_cards):
                print("You lose! :(")
            elif calculate_score(computer_cards) == calculate_score(user_cards):
                print("Draw! :|")
            else:
                print("You win! :D")

if __name__ == "__main__":
    # Oyunun başında kullanıcıya oyunu oynayıp oynamak istemediği sorulur
    yes_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if yes_or_no == "y":
        blackjack()
    else:
        print("Maybe next time!")
