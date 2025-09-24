# Provided tarot dictionary
tarot = {1:  "The Magician", 2:  "The High Priestess", 3:  "The Empress", 4: "The Emperor",
         5: "The Hierophant", 6:  "The Lovers", 7:  "The Chariot", 8: "Strength", 9:  "The Hermit",
         10: "Wheel of Fortune", 11: "Justice", 12:  "The Hanged Man", 13: "Death", 14:  "Temperance",
         15: "The Devil", 16:  "The Tower", 17:  "The Star", 18: "The Moon", 19: "The Sun",
         20:  "Judgement", 21:  "The World", 22: "The Fool"}

# 1. Create empty spread dictionary
spread = {}

# 2. Pop card 13 and assign to 'past'
spread['past'] = tarot.pop(13)

# 3. Pop card 22 and assign to 'present'
spread['present'] = tarot.pop(22)

# 4. Pop card 10 and assign to 'future'
spread['future'] = tarot.pop(10)

# 5. Print each key and value in spread
for time, card in spread.items():
    print(f"Your {time} is the {card} card.")
