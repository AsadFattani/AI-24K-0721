# ---------------------- TASK 1 ---------------------- #

import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]

#1 Probability of drawing a red card (Hearts or Diamonds)
red_cards = [card for card in deck if card[1] in ['Hearts', 'Diamonds']]
prob_red_theoratical = len(red_cards) / len(deck)

#2 Given red card, probability of it being a Heart
hearts = [card for card in red_cards if card[1] == 'Hearts']
prob_heart_given_red_theoratical = len(hearts) / len(red_cards)


#3 Given face card, probability of it being a Diamond
face_cards = [card for card in deck if card[0] in ['Jack', 'Queen', 'King']]
diamond_face = [card for card in face_cards if card[1] == 'Diamonds']
prob_diamond_given_face_theoratical = len(diamond_face) / len(face_cards)

#4 Given face card, probability of it's a spade or a queen
spade_face = [card for card in face_cards if card[1] == 'Spades']
queens = [card for card in face_cards if card[0] == 'Queen']
spade_or_queen = set(spade_face) | set(queens)
prob_spade_or_queen_given_face_theoratical = len(spade_or_queen) / len(face_cards)



trials = 100000
red_count = 0
heart_given_red_count = 0
face_count = 0
diamond_given_face_count = 0
spade_or_queen_given_face_count = 0

for _ in range(trials):
    card = random.choice(deck)
    # Red card
    if card in red_cards:
        red_count += 1
        if card in hearts:
            heart_given_red_count += 1
    # Face card
    if card in face_cards:
        face_count += 1
        if card in diamond_face:
            diamond_given_face_count += 1
        if card in spade_or_queen:
            spade_or_queen_given_face_count += 1

prob_red = red_count / trials
prob_heart_given_red = heart_given_red_count / red_count if red_count > 0 else 0
prob_diamond_given_face = diamond_given_face_count / face_count if face_count > 0 else 0
prob_spade_or_queen_given_face = spade_or_queen_given_face_count / face_count if face_count > 0 else 0

print(f"Theoretical P(Red) = {prob_red_theoratical:.4f}, Simulated P(Red) = {prob_red:.3f}")
print(f"Theoretical P(Heart|Red) = {prob_heart_given_red_theoratical:.3f}, Simulated P(Heart|Red) = {prob_heart_given_red:.3f}")
print(f"Theoretical P(Diamond|Face) = {prob_diamond_given_face_theoratical:.3f}, Simulated P(Diamond|Face) = {prob_diamond_given_face:.3f}")
print(f"Theoretical P(Spade or Queen|Face) = {prob_spade_or_queen_given_face_theoratical:.3f}, Simulated P(Spade or Queen|Face) = {prob_spade_or_queen_given_face:.4f}")




