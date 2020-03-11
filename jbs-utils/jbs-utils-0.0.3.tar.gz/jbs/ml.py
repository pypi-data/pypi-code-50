from jbs import ir
import pandas as pd


def default_sentence_tokenizer(text: str, delimiter='.'):
    """
    Splits sentence according to the given delimiter while striping each sentence
    and removing zero length sentences.
    :param text:
    :param delimiter:
    :return:
    """
    sentences = text.split(delimiter)
    return [sentence.strip() for sentence in sentences if len(sentence.strip()) > 0]


def init(book_name: str, sentence_tokenizer=default_sentence_tokenizer) -> (pd.DataFrame, pd.DataFrame, pd.DataFrame):
    """
    Get from jbs.ir the provided book and then build and return 3 dataframes:
    doc_df, sentence_df, word_df
    :param book_name:
    :return:
    """
    doc_df = ir.get_book(book_name)
    doc_df.rename(columns={'position': 'pos_doc'}, inplace=True)

    return doc_df


