#BTS Song Analyzer
#This program will get BTS song as input and will use many python fundamental concepts and functions and give various aspects of the song as output.

developer_name = "AIML_Student"
print(f"Hello, I am {developer_name} and I will be your BTS song analyzer today!")
song_name = input("Please enter the name of a BTS song: ").strip()
print()
print(f"--- ANALYZING SONG: '{song_name}' ---")
print(f"Length : {len(song_name)} characters")
print(f"First letter : {song_name[0].upper()}")
print(f"Last letter : {song_name[-1].lower()}")
print(f"First 3 letters: {song_name[0].upper() + song_name[1:3].lower()}")
print(f"Last 3 letters: {song_name[-3:]}")
print(f"Uppercase : {song_name.upper()}")
print(f"Lowercase : {song_name.lower()}")
word_check = 'na' in song_name
print(f"Does the song name contain 'na'?: {word_check}")
print(f"How many 'a' in song name?: {song_name.count('a')}")
print(f"Replace 'a' with '💜': {song_name.replace('a','💜')}")
print(f"Starts with 'D'? : {song_name.startswith('D')}")
print(f"Ends with 'e'? : {song_name.endswith('e')}")
print("=" * 50)
print("Thank you for using BTS Song Analyzer! 💜")
