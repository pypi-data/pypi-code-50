import torch
from torch import Tensor
from torch import nn
from typing import Union, Tuple, List, Iterable, Dict
import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

class Dissection(nn.Module):
    """
    Based on the paper: "SBERT-WK: A Sentence Embedding Method ByDissecting BERT-based Word Models"
    https://arxiv.org/pdf/2002.06652.pdf
    """
    def __init__(self, word_embedding_dimension, layer_start: int = 4, context_window_size: int = 2):
        super(Dissection, self).__init__()
        self.config_keys = ['word_embedding_dimension']
        self.word_embedding_dimension = word_embedding_dimension
        self.pooling_output_dimension = word_embedding_dimension
        self.layer_start = layer_start
        self.context_window_size = context_window_size

    def forward(self, features: Dict[str, Tensor]):
        all_layer_embedding = features['all_layer_embeddings']

        unmask_num = np.array([sum(mask) for mask in self.masks]) - 1  # Not considering the last item
        all_layer_embedding = np.array(all_layer_embedding)[:, self.layer_start:, :, :]  # Start from 4th layers output

        embedding = []
        # One sentence at a time
        for sent_index in range(len(unmask_num)):
            sentence_feature = all_layer_embedding[sent_index, :, :unmask_num[sent_index], :]
            one_sentence_embedding = []
            # Process each token
            for token_index in range(sentence_feature.shape[1]):
                token_feature = sentence_feature[:, token_index, :]
                # 'Unified Word Representation'
                token_embedding = self.unify_token(token_feature)
                one_sentence_embedding.append(token_embedding)

            one_sentence_embedding = np.array(one_sentence_embedding)
            sentence_embedding = self.unify_sentence(sentence_feature, one_sentence_embedding)
            embedding.append(sentence_embedding)

        output_vector = np.array(embedding)

        features.update({'sentence_embedding': output_vector})
        return features

    def unify_token(self, token_feature):
        """
            Unify Token Representation
        """
        window_size = self.context_window_size

        alpha_alignment = np.zeros(token_feature.shape[0])
        alpha_novelty = np.zeros(token_feature.shape[0])

        for k in range(token_feature.shape[0]):
            left_window = token_feature[k - window_size:k, :]
            right_window = token_feature[k + 1:k + window_size + 1, :]
            window_matrix = np.vstack([left_window, right_window, token_feature[k, :][None, :]])

            Q, R = np.linalg.qr(window_matrix.T)  # This gives negative weights

            q = Q[:, -1]
            r = R[:, -1]
            alpha_alignment[k] = np.mean(normalize(R[:-1, :-1], axis=0), axis=1).dot(R[:-1, -1]) / (np.linalg.norm(r[:-1]))
            alpha_alignment[k] = 1 / (alpha_alignment[k] * window_matrix.shape[0] * 2)
            alpha_novelty[k] = abs(r[-1]) / (np.linalg.norm(r))

        # Sum Norm
        alpha_alignment = alpha_alignment / np.sum(alpha_alignment)  # Normalization Choice
        alpha_novelty = alpha_novelty / np.sum(alpha_novelty)

        alpha = alpha_novelty + alpha_alignment

        alpha = alpha / np.sum(alpha)  # Normalize

        out_embedding = token_feature.T.dot(alpha)

        return out_embedding

    def unify_sentence(self, sentence_feature, one_sentence_embedding):
        """
            Unify Sentence By Token Importance
        """
        sent_len = one_sentence_embedding.shape[0]

        var_token = np.zeros(sent_len)
        for token_index in range(sent_len):
            token_feature = sentence_feature[:, token_index, :]
            sim_map = cosine_similarity(token_feature)
            var_token[token_index] = np.var(sim_map.diagonal(-1))

        var_token = var_token / np.sum(var_token)

        sentence_embedding = one_sentence_embedding.T.dot(var_token)

        return sentence_embedding

    def get_sentence_embedding_dimension(self):
        return self.pooling_output_dimension

    def get_config_dict(self):
        return {key: self.__dict__[key] for key in self.config_keys}

    def save(self, output_path):
        with open(os.path.join(output_path, 'config.json'), 'w') as fOut:
            json.dump(self.get_config_dict(), fOut, indent=2)

    @staticmethod
    def load(input_path):
        with open(os.path.join(input_path, 'config.json')) as fIn:
            config = json.load(fIn)

        return Dissection(**config)
