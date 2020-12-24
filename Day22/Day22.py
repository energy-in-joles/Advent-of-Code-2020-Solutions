def main():
  with open("cards.txt", 'r') as File:
    cards = ''.join(card for card in File).strip().split('\n\n')
    p1_cards = [int(card) for card in cards[0].split('\n')[1:]] # get list of p1 and 2 cards
    p2_cards = [int(card) for card in cards[-1].split('\n')[1:]]
    print(f"Part 1: {Combat(p1_cards.copy(), p2_cards.copy())}")
    print(f"Part 2: {Part2(p1_cards, p2_cards)}")

def Combat(p1_cards, p2_cards):
  while len(p1_cards) > 0 and len(p2_cards)> 0: # while both players still have cards
    p1_top = p1_cards.pop(0) # get val of top and remove from lst
    p2_top = p2_cards.pop(0)
    if p1_top > p2_top: # append according to who wins
      p1_cards += [p1_top, p2_top]
    elif p1_top < p2_top:
      p2_cards += [p2_top, p1_top]
    # ignore if p1_top == p2_top

  if p1_cards: # if list has items (ie winner because loser has none)
    win_deck = p1_cards
  else:
    win_deck = p2_cards
  return calc_winner_score(win_deck)

# Part 2: throw in recursion
def Part2(p1_cards, p2_cards):
  return calc_winner_score(recursiveCombat(p1_cards, p2_cards)[1])

def recursiveCombat(p1_cards, p2_cards):
  p1_archive = []
  p2_archive = []
  while len(p1_cards) > 0 and len(p2_cards)> 0: # while both players still have cards
    if p1_cards in p1_archive and p2_cards in p2_archive:
      return 0, p1_cards
    p1_archive.append(p1_cards.copy()) # archive decks in each game to detect repetition ie infinite loop.
    p2_archive.append(p2_cards.copy())
    p1_top = p1_cards.pop(0) # get val of top and remove from lst
    p2_top = p2_cards.pop(0)
    if p1_top <= len(p1_cards) and p2_top <= len(p2_cards): # recursion to determine winner if size(rest of deck) >= current_val
      p1_cards_copy = p1_cards[:p1_top].copy()
      p2_cards_copy = p2_cards[:p2_top].copy()
      winner = recursiveCombat(p1_cards_copy, p2_cards_copy)[0]
    elif p1_top > p2_top: # assign winner based on larger number
      winner = 0
    elif p1_top < p2_top:
      winner = 1

    if winner == 0: # append according to the winner
      p1_cards += [p1_top, p2_top]
    else:
      p2_cards += [p2_top, p1_top]

  if p1_cards:
    win_deck = p1_cards
  else:
    win_deck = p2_cards
  return winner, win_deck

def calc_winner_score(winning_deck):
  sum = 0
  for i, n in enumerate(winning_deck): # scoring is sum of reversed postion * val (ie last card is 1 * last_card_val)
    sum += (len(winning_deck) - i) * n
  return sum

if __name__ == "__main__":
  main()
