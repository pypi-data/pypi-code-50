from pre_processing.pre_processing import CorpusHandler

def preprocess(text):
    text_process = CorpusHandler.pre_process(
        text,
        disabled=['to_st_named_entities', 'lemmatize', 'tokenize'],
        num_cpus=1
    )

    return text_process
