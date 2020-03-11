# -*- coding: utf-8 -*-
import spacy, json
nlp = spacy.load("en_core_web_sm")

def postag(doc):
    doc = nlp(doc)
    return ' '.join([t.text+'_'+t.tag_ for t in doc])
    for token in doc:
        attrs.append({
            'i' : token.i,    #int    start 0
            'text' : token.text,
            'whitespace_' : token.whitespace_,
            'orth_' : token.orth_,
            'ent_type_' : token.ent_type_,
            'ent_iob_' : token.ent_iob_,
            'ent_id_' : token.ent_id_,
            'norm_' : token.norm_,
            'lemma_' : token.lemma_,
            'lower_' : token.lower_,
            'shape_' : token.shape_,
            'prefix_' : token.prefix_,
            'suffix_' : token.suffix_,
            'is_alpha' : token.is_alpha,
            'is_ascii' : token.is_ascii,
            'is_digit' : token.is_digit,
            'is_lower' : token.is_lower,
            'is_upper' : token.is_upper,
            'is_title' : token.is_title,
            'is_punct' : token.is_punct,
            'is_left_punct' : token.is_left_punct,
            'is_right_punct' : token.is_right_punct,
            'is_space' : token.is_space,
            'is_bracket' : token.is_bracket,
            'is_quote' : token.is_quote,
            'is_currency' : token.is_currency,
            'like_url' : token.like_url,
            'like_num' : token.like_num,
            'like_email' : token.like_email,
            'is_oov' : token.is_oov,
            'is_stop' : token.is_stop,
            'pos_' : token.pos_,
            'tag_' : token.tag_,
            'dep_' : token.dep_,
            'lang_' : token.lang_,
            'prob' : token.prob,
            'idx' : token.idx,
            'sentiment' : token.sentiment,
            'lex_id' : token.lex_id,
            'rank' : token.rank,
            'cluster' : token.cluster,
        })

if __name__ == '__main__':
    print(postag("This is you book."))