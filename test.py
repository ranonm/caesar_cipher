import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_postive_key_should_right_shift(self):
        """
        Test that characters are right shifted when key is a positive integer.
        """
        self.assertEqual(caesar_cipher("What a string!", 5), "Bmfy f xywnsl!")

    def test_negative_key_should_left_shift(self):
        """
        Test that characters are left shifted when key is a negative integer.
        """
        self.assertEqual(caesar_cipher("code", -2), "ambc")

    def test_key_of_zero_should_not_change_encrypt_text(self):
        """
        Test that string is unchanged when key is zero.
        """
        self.assertEqual(caesar_cipher("code", 0), "code")

    def test_spaces_are_preserved(self):
        """
        Test that whitespace in plain text are preserved.
        """
        self.assertEqual(caesar_cipher("write code", 3), "zulwh frgh")

    def test_special_characters_are_preserved(self):
        """
        Test that special characters in plain text are preserved.
        """
        self.assertEqual(caesar_cipher("code!#@$", 3), "frgh!#@$")

    def test_character_case_are_preserved(self):
        """
        Test that character case in plain text are preserved.
        """
        self.assertEqual(caesar_cipher("Code", 2), "Eqfg")

    def test_wraps_from_z_to_a_when_right_shifting(self):
        """
        Test that shifting occurs from z to a when right shifting.
        """
        self.assertEqual(caesar_cipher("zoo", 5), "ett")

    def test_wraps_from_a_to_z_when_left_shifting(self):
        """
        Test that shifting wraps from a to z when left shifting"
        """
        self.assertEqual(caesar_cipher("abacus", -5), "vwvxpn")


if __name__ == "__main__":
    unittest.main()
