import json
from json import JSONDecodeError

data = {
  "vowels": {
      "a": "අ",
      "A": "අ",
      "aa": "ආ",
      "Aa": "ආ",
      "ae": "ඇ",
      "Ae": "ඇ",
      "aee": "ඈ",
      "Aee": "ඈ",
      "i": "ඉ",
      "I": "ඉ",
      "ii": "ඊ",
      "Ii": "ඊ",
      "u": "උ",
      "U": "උ",
      "uu": "ඌ",
      "Uu": "ඌ",
      "ERU": "ඍ",
      "ERU'": "ඎ",
      "IRU": "ඏ",
      "IRU'": "ඐ",
      "e": "එ",
      "E": "එ",
      "ee": "ඒ",
      "Ee": "ඒ",
      "ai": "ඓ",
      "Ai": "ඓ",
      "o": "ඔ",
      "O": "ඔ",
      "oo": "ඕ",
      "Oo": "ඕ",
      "au": "ඖ",
      "Au": "ඖ",
      "x": "(අං)",
      "X": "(අඃ)"
  },
  "consonants": {
      "k": "ක",
      "c": "ක",
      "K": "ක",
      "kh": "ඛ",
      "Kh": "ඛ",
      "g": "ග",
      "G": "ඝ",
      "gh": "ඝ",
      "Gh": "ඝ",
      "ng": "ඞ",
      "nng": "ඟ",
      "zg": "ඟ",
      "ch": "ච",
      "Ch": "ඡ",
      "j": "ජ",
      "J": "ඣ",
      "jh": "ඣ",
      "ngj": "ඤ",
      "zk": "ඤ",
      "ny": "ඤ",
      "Ngj": "ඥ",
      "jny": "ඥ",
      "nyj": "ඦ",
      "zj": "ඦ",
      "t": "ට",
      "T": "ඨ",
      "d": "ඩ",
      "D": "ඪ",
      "N": "ණ",
      "zd": "ඬ",
      "nd": "ඬ",
      "th": "ත",
      "Th": "ථ",
      "dh": "ද",
      "Dh": "ධ",
      "n": "න",
      "ndh": "ඳ",
      "p": "ප",
      "P": "ඵ",
      "ph": "ඵ",
      "r": "ර",
      "l": "ල",
      "L": "ළ",
      "s": "ස",
      "sh": "ශ",
      "Sh": "ෂ",
      "h": "හ",
      "w": "ව",
      "v": "ව",
      "f": "ෆ",
      "b": "බ",
      "B": "භ",
      "bh": "භ",
      "m": "ම",
      "mb": "ඹ",
      "y": "ය"
  },
  "dependent_vowels": {
      "aa": "ා",
      "ae": "ැ",
      "aae": "ෑ",
      "i": "ි",
      "ii": "ී",
      "u": "ු",
      "uu": "ූ",
      "ERU": "ෘ",
      "e": "ෙ",
      "ee": "ේ",
      "ai": "ෛ",
      "o": "ො",
      "oo": "ෝ",
      "au": "ෞ",
      "x": "ං"
  }
}


class RuleBasedTransliterator:
    def __init__(self):
        """
        Initialize the SinhalaTransliterator object with the configuration file.
        """
        self.vowels = {}
        self.consonants = {}
        self.dependent_vowels = {}
        self.vowels = data.get('vowels', {})
        self.consonants = data.get('consonants', {})
        self.dependent_vowels = data.get('dependent_vowels', {})

    def __split_into_logical_groups(self, word: str) -> list:
        """
        Split a word into logical groups based on provided dictionaries of dependent vowels, consonants, and vowels.

        This function takes a word as input and splits it into logical groups according to the rules defined in the dictionaries
        of dependent vowels, consonants, and vowels. It returns a list of logical groups.

        Parameters:
        -----------
        word : str
            The word to be split into logical groups.

        Returns:
        --------
        list
            A list of logical groups obtained by splitting the word.

        Raises:
        -------
        None

        Examples:
        ---------
        word = "අර්බුදය"
        dependent_vowels = {'aa': 'ා', 'i': 'ි', 'u': 'ු'}
        consonants = {'r': 'ර', 'b': 'බ', 'd': 'ද', 'y': 'ය'}
        vowels = {'a': 'අ', 'e': 'එ', 'o': 'ඔ'}
        split_into_logical_groups(word, dependent_vowels, consonants, vowels)
        ['අ', 'ර්', 'බු', 'ද', 'ය']

        Notes:
        ------
        - The word should be a valid string without any special characters or spaces.
        - The dictionaries should be properly defined with valid mappings.
        - The function assumes that the dictionaries cover all possible characters in the word.
        """
        logical_groups = []
        current_group = ''
        i = 0
        while i < len(word):
            try:
                # Check for consonants
                for length in range(4, 0, -1):
                    if i + length <= len(word):
                        group = word[i:i + length]
                        if group in self.consonants:
                            logical_groups.append(current_group)
                            current_group = self.consonants[group]
                            i += length

                            if i >= len(word):
                                current_group = current_group + "්"
                                break
                            else:
                                for next_length in range(3, 0, -1):
                                    if i + next_length <= len(word):
                                        group = word[i:i + next_length]
                                        if group in self.dependent_vowels:
                                            logical_groups.append(current_group)
                                            current_group = self.dependent_vowels[group]
                                            i += next_length
                                            break
                                else:
                                    if i < len(word) and word[i] == "a":
                                        i += 1
                                    elif (word[i:i + 1] or word[i:i + 2] or word[i:i + 3] or word[i:i + 4]) in (self.consonants or self.vowels):
                                        current_group = current_group + "්"
                                        break
                                    else:
                                        # Handle unknown characters
                                        current_group += word[i]
                                        i += 1
                            break
                else:
                    # Handle unknown characters
                    current_group += word[i]
                    i += 1

                # Check for vowels
                for length in range(3, 0, -1):
                    if i + length < len(word):
                        group = word[i:i + length]
                        if group in self.vowels:
                            logical_groups.append(current_group)
                            current_group = self.vowels[word[i:i + 3]]
                            i += 3
                            break

                # # Check for dependent vowel signs
                # for length in range(3, 0, -1):
                #     print("Dependent Vowels")
                #     if i + length < len(word):
                #         group = word[i:i + length]
                #         if group in self.dependent_vowels:
                #             logical_groups.append(current_group)
                #             current_group = self.dependent_vowels[word[i:i + 3]]
                #             i += 3
                #             break

            except Exception as e:
                # Handle exceptions
                print(f"An error occurred: {str(e)}")
                return []

        if current_group:
            logical_groups.append(current_group)

        return logical_groups

    def transliterator(self, text: str) -> str:
        """
        Transliterate English text into the Sinhala script.

        This method takes English text as input and transliterates it into the Sinhala script.
        It separates the text into paragraphs and words, and transliterates each word individually.
        The transliterated text maintains the original paragraph structure.

        Parameters:
        -----------
        text : str
            The English text to be transliterated.

        Returns:
        --------
        str
            The transliterated text in the Sinhala script.

        Examples:
        ---------
        transliterator('Hello, how are you?\nI am fine, thank you.')
        'හෙලෝ, හොවේ ඔයාටම කොහොමද?\nමම හොඳින් ස්තුතියි, ස්තුතියි.'

        transliterator('This is a test.\nTesting transliteration.')
        'මෙය පරීක්ෂාවක්ය.\nපරීක්ෂකරුගේ අර්ථය.'

        Notes:
        ------
        - The method relies on the 'vowels', 'consonants', and 'dependent_vowels' dictionaries
          to perform the transliteration. Make sure these dictionaries are defined correctly
          in the configuration file before calling this method.
        - The method uses the 'split_into_logical_groups' helper function to split each word
          into logical groups based on the rules of Sinhala transliteration.
        """

        try:
            paragraphs = text.split('\n')
            transliterated_paragraphs = []

            for paragraph in paragraphs:
                words = paragraph.split()
                transliterated_words = []

                for word in words:
                    logical_groups = self.__split_into_logical_groups(word)

                    output = ''
                    for group in logical_groups:
                        if group in self.vowels:
                            output += self.vowels[group]
                        elif group in self.dependent_vowels:
                            output += self.dependent_vowels[group]
                        else:
                            output += group

                    transliterated_word = output
                    transliterated_words.append(transliterated_word)

                transliterated_paragraph = ' '.join(transliterated_words)
                transliterated_paragraphs.append(transliterated_paragraph)

            output_text = '\n'.join(transliterated_paragraphs)
            return output_text

        except Exception as e:
            print(f"Error in transliterator method: {e}")


if __name__ == "__main__":
    transliterator = RuleBasedTransliterator()
    input_word = "ammaa kohomadha oyaata. \n mamanam hondhin"

    out = transliterator.transliterator(input_word)
    print(out)
