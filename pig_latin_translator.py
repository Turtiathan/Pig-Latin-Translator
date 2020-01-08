class PigLatin():
	def __init__(self, word):
		self.word = word

	def translate(self):
		"""
		Takes a word and translates it to Pig Latin.
		"""
		vowels = "aeiou"

		if (self.word[0] not in vowels) and (self.word[1] in vowels):
			new_word = self.word[1:] + self.word[0] + "ay"
		elif self.word[0] in vowels:
			new_word = self.word + "way"
		else:
			new_word = self.word[2:] + self.word[:2] + "ay"

		print(new_word)

while(True):
	print("Hello. This program converts English words to the Pig Latin version.")
	word = input("Please enter a word you want to translate.")

	pig_latin = PigLatin(word)
	pig_latin.translate()

	print("Do you want to translate another word?")
	choice = input("Press 'n' or 'N' if you want to quit. Otherwise hit any key.")

	if choice == 'n' or 'N':
		break
