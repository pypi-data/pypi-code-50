from argument_esa_model.esa import ESA
from conf.configuration import *

esa_model_debatepedia = None
esa_model_strategic_intelligence = None
import pandas as pd



def load_topics(topic_ontology):
    path_topics = get_path_topics(topic_ontology)
    topics_df=pd.read_csv(path_topics)
    return list(topics_df['topic'])
def initialize_models():
    path_esa_model_debatepedia = get_path_topic_model('ontology-debatepedia','esa')
    path_esa_model_strategic_intelligence = get_path_topic_model('ontology-strategic-intelligence','esa')
    esa_model_debatepedia = ESA (path_esa_model_debatepedia)
    esa_model_strategic_intelligence = ESA (path_esa_model_strategic_intelligence)
    return  esa_model_debatepedia,esa_model_strategic_intelligence

def save_topics_for(ontology):
    topics= model(ontology,'Life is hard and expensive')
    path_ontology = get_path_topics(ontology)
    topics_df = pd.DataFrame({'topic':topics})
    topics_df.to_csv(path_ontology,encoding='utf-8')

def model(topic_ontology,text):
    if topic_ontology=='ontology-strategic-intelligence':
        topic_dictionary = esa_model_strategic_intelligence.process(text, False)
    if topic_ontology == 'ontology-debatepedia':
        topic_dictionary = esa_model_debatepedia.process(text, False)
    return sorted(topic_dictionary)


#esa_model_debatepedia,esa_model_strategic_intelligence=initialize_models()
#save_topics_for('ontology-strategic-intelligence')
#save_topics_for('ontology-debatepedia')