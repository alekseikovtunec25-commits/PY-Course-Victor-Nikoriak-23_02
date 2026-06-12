import unittest
import tempfile
import json
import os
from unittest.mock import patch

from phonebook import (
    load_phonebook,
    save_phonebook,
    add_record,
    delete_record,
    update_record
)


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = [
            {
                "first_name": "Alex",
                "last_name": "Smith",
                "phone": "123",
                "city": "Kyiv"
            }
        ]

    def test_save_and_load_phonebook(self):

        with tempfile.NamedTemporaryFile(
                mode="w+",
                delete=False,
                suffix=".json"
        ) as temp_file:

            save_phonebook(temp_file.name, self.phonebook)

            loaded = load_phonebook(temp_file.name)

            self.assertEqual(loaded, self.phonebook)

        os.remove(temp_file.name)

    @patch(
        "builtins.input",
        side_effect=["John", "Doe", "555", "Lviv"]
    )
    def test_add_record(self, mock_input):

        add_record(self.phonebook)

        self.assertEqual(len(self.phonebook), 2)

        self.assertEqual(
            self.phonebook[-1]["first_name"],
            "John"
        )

    @patch("builtins.input", side_effect=["123"])
    def test_delete_record(self, mock_input):

        delete_record(self.phonebook)

        self.assertEqual(len(self.phonebook), 0)

    @patch(
        "builtins.input",
        side_effect=[
            "123",
            "NewName",
            "NewSurname",
            "Odessa"
        ]
    )
    def test_update_record(self, mock_input):

        update_record(self.phonebook)

        self.assertEqual(
            self.phonebook[0]["first_name"],
            "NewName"
        )

        self.assertEqual(
            self.phonebook[0]["last_name"],
            "NewSurname"
        )

        self.assertEqual(
            self.phonebook[0]["city"],
            "Odessa"
        )


if __name__ == "__main__":
    unittest.main()