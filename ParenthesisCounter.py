# last date modified 3/23/2024 - 1403/01/04
# unnecessary code lines were not removed yet.
import numpy
from copy import deepcopy


class ParenthesisCounter:
    """
    Description:
        > counts the total number of pairs of characters
            that given to it and this is not exclusive to
            parenthesis, brackets and curly brackets.
    Details :
        > This class defines 3 methods and a constructor.
        > Class methods are :
            [1] indexer -> gets indexes of pair chars then sets it to the self.indexes
            [2] isPaired -> checks if all pair chars are paired properly
            [3] PIPA (Parenthesis Indexes Pairing Algorithm) -> pairs the indexes given from self.indexer method

    """

    # def __init__(
    #     self,
    #     phrase: str,
    #     searchingCharactersList: tuple = (
    #         ("(", ")"),
    #         ("[", "]"),
    #         ("{", "}"),
    #     ),
    # ) -> None:

    def __init__(
        self,
        phrase: str,
        searchingCharactersList: tuple = (
            ("(", ")"),
            ("[", "]"),
            ("{", "}"),
        ),
    ) -> None:
        """Initializing the global variables"""
        self.phrase = phrase  # the input to be processed
        self.indexes: dict = {}  # the index of paired characters
        self.searching_characters_list: tuple = (
            searchingCharactersList  # characters check list to be paired
        )

    def indexer(self) -> None:
        """_summary_
        The indexer method breaks down the self.phrase string into a list of characters then
        using self.searching_characters_list gets the index of the wanted characters,
        appends them into a dictionary then sets the self.indexes variable value.

        Note:
            The output of this method will be used by 2 class methods:
                isPaired method: To check if all wanted characters either paired or not.
                PIPA (Parenthesis Indexes Pairing Algorithm) : To pair the wanted characters in
                self.phrase using the self.indexes.


        Sets: self.indexes
            dict: a dictionary of all wanted characters' indexes.
        """
        phrase_characters_list: list = list(self.phrase)
        phrase_len: int = len(phrase_characters_list)
        searching_characters_list: tuple = self.searching_characters_list
        chars_index_list: list = []
        chars_index_dict: dict = {}
        for char_pair in searching_characters_list:
            for char in char_pair:
                if char in phrase_characters_list:
                    for index in range(0, phrase_len):
                        if phrase_characters_list[index] == char:
                            chars_index_list.append(index)
                chars_index_dict[char] = chars_index_list
                chars_index_list = []
        self.indexes = chars_index_dict

    # def isPaired(self) -> bool:
    #     """_summary_
    #         This method checks if each pair characters either paired or not.

    #         First checks if one of the pair chars are missing or not :
    #             e.g. (((( and ]]]] -> returns False, () and {} -> passes the first condition
    #         Second checks if total number of pair chars are equal or not:
    #             e.g. (), {{{{}}}} and ()[][][][[[]]][] -> passes the condition and returns True
    #             ()) and []] -> fails the condition and returns False.

    #     Returns:
    #         bool: True, if all opening and closing characters are paired
    #             False, if not.
    #     """
    #     phrase: str = self.phrase
    #     indexes: dict = self.indexes
    #     searching_characters_list: tuple = self.searching_characters_list
    #     for pair_char in searching_characters_list:
    #         if (pair_char[0] in phrase) is not (pair_char[1] in phrase):
    #             print(
    #                 f"Syntax error : Check '{pair_char[0]}' and '{pair_char[1]}' were paired"
    #             )
    #             return False
    #         for pair_char in searching_characters_list:
    #             if indexes[pair_char[0]].__len__() != indexes[pair_char[1]].__len__():
    #                 print(
    #                     f"Syntax error : Check '{pair_char[0]}' and '{pair_char[1]}' were paired \n Missing open or close parenthesis or bracket"
    #                 )
    #                 return False
    #     return True
    def isPaired(self) -> bool:
        stack = []
        pair_dict = {")": "(", "]": "[", "}": "{"}
        for char in self.phrase:
            if char in pair_dict.values():
                stack.append(char)
            elif char in pair_dict.keys():
                if stack == [] or pair_dict[char] != stack.pop():
                    return False
        return stack == []

    def PIPA(self) -> dict:  # PPA stands for Parenthesizes Index Pairing Algorithm
        """_summary_
            Using the output of indexer method this method pairs the pair chars then returns the paired indexes.
        Returns:
            dict: _description_
        """
        indexes: dict = self.indexes
        searching_characters_list: tuple = self.searching_characters_list
        open_index_list: list = []
        close_index_list: list = []
        possible_pairs_list: list = []
        pairs_dict: dict = {}
        chars_pair_dict: dict = {}
        pair: int = 0
        for char_pair in searching_characters_list:
            open_index_list = deepcopy(indexes[char_pair[0]])
            close_index_list = deepcopy(indexes[char_pair[1]])
            open_index_list.reverse()
            close_index_list.reverse()
            for open_index in open_index_list:
                for close_index in close_index_list:
                    if close_index > open_index:
                        possible_pairs_list.append(close_index - open_index)
                    try:  # BUG : this part fails when the phrase is ()()() and similar. find and fix it.
                        pair = numpy.min(possible_pairs_list) + open_index
                        pairs_dict[open_index] = pair
                        close_index_list.pop(close_index_list.index(pair))
                        possible_pairs_list = []
                    except:
                        # print ("Error caused on : ", possible_pairs_list, open_index)
                        pass
            chars_pair_dict[char_pair] = pairs_dict
            pairs_dict = {}
        return chars_pair_dict

    def inputSimplifier(self):
        pass

    def driver(self):
        # Just a simple driver to implement in other parts.
        self.indexer()
        if self.isPaired():
            return self.PIPA()


if __name__ == "__main__":
    counter: object = ParenthesisCounter(phrase=input("Enter the phrase: "))
    print(counter.driver())
