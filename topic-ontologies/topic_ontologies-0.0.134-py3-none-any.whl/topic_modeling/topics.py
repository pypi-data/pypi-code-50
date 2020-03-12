from argument_esa_model.esa import ESA
from conf.configuration import *

esa_model_debatepedia = None
esa_model_strategic_intelligence = None
import pandas as pd
from topic_modeling import *
import argument_esa_model.esa_all_terms


def load_topics(topic_ontology):
    path_topics = get_path_topics(topic_ontology)
    topics_df=pd.read_csv(path_topics)
    return list(topics_df['topic'])

def model_text(topic_ontology,text):
    path_topic_model = get_path_topic_model(topic_ontology,'esa')
    path_word2vec_model = get_path_topic_model('word2vec','word2vec')
    path_word2vec_vocab = get_path_vocab('word2vec')
    topic_dict = argument_esa_model.esa_all_terms.model_topic(path_topic_model,path_word2vec_model,path_word2vec_vocab,'cos',text)

    sorted_topic_dict = sorted(topic_dict )
    return  sorted_topic_dict



def save_topics_for(ontology):
    print(ontology)
    topics= model_text(ontology,'Life is hard and expensive')
    path_ontology_topics = get_path_topics(ontology)
    print(topics)
    print(path_ontology_topics)
    topics_df = pd.DataFrame({'topic':topics})
    topics_df.to_csv(path_ontology_topics,encoding='utf-8')



save_topics_for('ontology-strategic-intelligence')
save_topics_for('ontology-debatepedia')
save_topics_for('ontology-wikipedia')
#save_topics_for('ontology-strategic-intelligence-sub-topics')

#topics=load_topics('ontology-wikipedia')
#print(topics)
#esa_model_debatepedia,esa_model_strategic_intelligence=initialize_models()
#save_topics_for('ontology-strategic-intelligence')
#save_topics_for('ontology-debatepedia')