
# # pylint: disable=all
# import unittest
# from unittest.mock import patch
# from translate import Translator
# import sys
# sys.path.append('C:/Users/37064/repos/PTUA3_CodeAcademy_course/202306/20230627-Docker_app_launch/source/')
# from translator import translaitor



# class TranslatorTestCase(unittest.TestCase):

#     @patch('builtins.input', return_value="Me")
#     def test_translator(self, mock_input):
#         expected_output = [
#             "de: Ich" "fr: Moi" "it: Io" "be: Мне" "pl: Ja" "sv: Jag" "uz: Men" "zh: 我" "lt: Aš" "so: idheh"
#         ]

#         with patch('sys.stdout') as mock_stdout:
#             translaitor()

#         output = mock_stdout.getvalue().strip().split()
#         self.assertEqual(output, expected_output)


# if __name__ == '__main__':
#     unittest.main()



import unittest
from unittest.mock import patch
from io import StringIO
from translate import Translator
# import sys
# sys.path.append('C:/Users/37064/repos/PTUA3_CodeAcademy_course/202306/20230627-Docker_app_launch/source/')
from main import translaitor



class TranslatorTestCase(unittest.TestCase):

    # @patch('builtins.input', return_value="Hello, my name is Paulius and i like Python")
    def test_translator_with_valid_sentence(self):
        expected_output = [
            "de: Hallo, mein Name ist Paulius und ich mag Python",
            "fr: Bonjour, je m'appelle Paulius et j'aime Python",
            "it: Ciao, mi chiamo Paulius e mi piace Python",
            "be: Добры дзень, мяне завуць Павел, і я люблю Python.",
            "pl: Cześć, mam na imię Paulius i lubię Pythona",
            "sv: Hej, jag heter Paulius och jag gillar Python",
            "uz: Salom, mening ismim Paulius va menga Python yoqadi",
            "zh: 你好，我叫Paulius ，我喜欢Python",
            "lt: Sveiki, mano vardas Paulius ir man patinka Python",
            "so: Hi, magacaygu waa Paulius oo waxaan jeclahay Python"
        ]

        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="Hello, my name is Paulius and i like Python"):
                translaitor()

        output = fake_output.getvalue().strip().split('\n')

        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main()


    # def test_translation_english_to_spanish(self):
    #        with patch('builtins.input', new=StringIO()):
    #         result = translaitor()
    #         self.assertEqual(result, "Hola")