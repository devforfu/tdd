from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_and_empty_list_items(self):
        self.fail("Write me!")
