# 1. Create paintings list
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# 2. Create dates list
dates = [1939, 1933, 1946, 1940]

# 3. Zip paintings and dates and convert to list
paintings = list(zip(paintings, dates))
print(paintings)

# 4. Append new paintings with dates as tuples
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

# 5. Find length of paintings list
length = len(paintings)

# 6. Generate audio tour numbers starting from 1
audio_tour_number = list(range(1, length + 1))
print(audio_tour_number)

# 7. Zip audio tour numbers with paintings to create master_list
master_list = list(zip(audio_tour_number, paintings))

# 8. Print master_list
print(master_list)
