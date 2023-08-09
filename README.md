# Sinhala Transliteration Library

The **Sinhala Transliteration Library** is a Python library that provides a rule-based transliteration system to convert English text into the Sinhala script. It's designed to help users convert English words and sentences into their Sinhala equivalents following predefined transliteration rules.

## Features

- Transliterate English text into Sinhala script.
- Follows logical splitting of words based on provided dictionaries of vowels, consonants, and dependent vowels.
- Customizable configuration through dictionaries for vowels, consonants, and dependent vowels.

## Installation

You can install the library using pip:

```bash
pip install singlish-translator
```

## Usage

Here's an example of how to use the library to transliterate English text into Sinhala script:

```python
from singlish-translator import RuleBasedTransliterator

transliterator = RuleBasedTransliterator()

input_text = "ammaa kohomadha oyaata. \n mamanam hondhin"
transliterated_text = transliterator.transliterator(input_text)

print(transliterated_text)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*This project is maintained by Supun Sameera. Feel free to contact me at supunsameeran@gmail.com for any questions or inquiries.*
```

Remember to save this content in a file named `README.md` in your project repository's root directory. You can edit the name and email address in the "maintained by" section as needed.