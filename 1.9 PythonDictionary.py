# Provided lists
songs = ["Yesterday", "Respect", "Imagine", "Smells Like Teen Spirit"]
playcounts = [50, 89, 70, 65]

# 1. Create plays dictionary using dict comprehension and zip
plays = {song: playcount for song, playcount in zip(songs, playcounts)}

# 2. Print plays dictionary
print(plays)

# 3. Add a new entry for "Purple Haze" with playcount 1
plays["Purple Haze"] = 1

# 4. Update playcount for "Respect" to 94
plays["Respect"] = 94

# 5. Create library dictionary with two key-value pairs
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# 6. Print library dictionary
print(library)
