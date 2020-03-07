import torch
import numpy as np
from scipy.stats import rankdata
from rdflib.term import Literal, URIRef
from tqdm import tqdm
from multimodal.batching import BatchLoader
from multimodal.builddata import Utils
from sklearn import utils
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from multiprocessing import cpu_count
from torch.nn.init import xavier_normal_, xavier_uniform_
from torch.autograd import Variable
from multimodal.gating import Gate, SingleGate, MultiGate
from multimodal.distMult import DistMult

class TransE(torch.nn.Module):

    def __init__(self, entity_total, relation_total,
                 numerical_embeddings, textual_embeddings,
                 numerical_literals, textual_literals,
                 textliteral2id, numliteral2id,
                 relation2id,
                 embedding_size=100, margin=1.0,
                 L1_flag=True, literalE=False, enhancement=False):

        super(TransE, self).__init__()

        self.textliteral2id = textliteral2id
        self.numliteral2id = numliteral2id
        self.relation2id = relation2id
        self.embedding_size = embedding_size

        self.margin = margin
        self.L1_flag = L1_flag
        self.literalE = literalE
        self.enhancement = enhancement

        self.num_gate = Gate(embedding_size + embedding_size, embedding_size)
        self.txt_gate = Gate(embedding_size + embedding_size, embedding_size)

        # Num. Literal
        # num_ent x n_num_lit
        self.numerical_literals = None
        self.n_num_lit = numerical_literals.shape[1]
        if self.n_num_lit > 0: self.numerical_literals = Variable(torch.from_numpy(numerical_literals))

        # Txt. Literal
        # num_ent x n_txt_lit
        self.textual_literals = None
        self.n_txt_lit = textual_literals.shape[1]
        if self.n_txt_lit > 0: self.textual_literals = Variable(torch.from_numpy(textual_literals))

        if self.n_num_lit > 0 and self.n_txt_lit > 0:
            print("using multi gate: both numerical and textual literals found!")
            self.rel_gate = MultiGate(embedding_size, self.n_num_lit, self.n_txt_lit)
        elif self.n_num_lit > 0 and self.n_txt_lit == 0:
            print("using single gate: only numerical literals found!")
            self.rel_gate = SingleGate(embedding_size, self.n_num_lit)
        elif self.n_num_lit == 0 and self.n_txt_lit > 0:
            print("using single gate: only textual literals found!")
            self.rel_gate = SingleGate(embedding_size, self.n_txt_lit)

        self.numerical_embeddings = torch.nn.Embedding.from_pretrained(torch.Tensor(numerical_embeddings), freeze=False,
                                                                       padding_idx=0)
        self.textual_embeddings = torch.nn.Embedding.from_pretrained(torch.Tensor(textual_embeddings), freeze=False,
                                                                     padding_idx=0)
        self.embeddings = torch.nn.Embedding(num_embeddings=entity_total + relation_total,
                                             embedding_dim=embedding_size, padding_idx=0)

        self.final_embeddings = dict()

    def init(self):
        xavier_normal_(self.embeddings.weight.data)

    def forward(self, pos_h, pos_t, pos_r, neg_h, neg_t, neg_r, update=True):

        if self.literalE or self.enhancement:
            pos_h_e = self.__enhance(pos_h, update=True)
            pos_t_e = self.__enhance(pos_t, update=True)
            pos_r_e = self.embeddings(torch.LongTensor(pos_r))
            neg_h_e = self.__enhance(neg_h, update=False)
            neg_t_e = self.__enhance(neg_t, update=False)
            neg_r_e = self.embeddings(torch.LongTensor(neg_r))
        else:
            pos_h_e = self.embeddings(torch.LongTensor(pos_h))
            pos_t_e = self.embeddings(torch.LongTensor(pos_t))
            pos_r_e = self.embeddings(torch.LongTensor(pos_r))

            for i, e in enumerate(pos_h): self.final_embeddings[e] = pos_h_e[i]
            for i, e in enumerate(pos_t): self.final_embeddings[e] = pos_t_e[i]

            neg_h_e = self.embeddings(torch.LongTensor(neg_h))
            neg_t_e = self.embeddings(torch.LongTensor(neg_t))
            neg_r_e = self.embeddings(torch.LongTensor(neg_r))

        for i, r in enumerate(pos_r): self.final_embeddings[r] = pos_r_e[i]

        if self.L1_flag:
            pos = torch.sum(abs(pos_h_e + pos_r_e - pos_t_e), 1, keepdim=True)
            neg = torch.sum(abs(neg_h_e + neg_r_e - neg_t_e), 1, keepdim=True)
            predict = pos
        else:
            pos = torch.sum((pos_h_e + pos_r_e - pos_t_e) ** 2, 1, keepdim=True)
            neg = torch.sum((neg_h_e + neg_r_e - neg_t_e) ** 2, 1, keepdim=True)
            predict = pos

        loss = torch.Tensor(0)
        if neg.shape[0] > pos.shape[0]:
            neg = neg.view(-1, pos.shape[0]).permute(1, 0)
        if pos.shape[0] == neg.shape[0]:
            loss = torch.sum(torch.max(pos - neg + self.margin, torch.zeros(pos.shape)))

        return loss, predict

    def __enhance(self, e, update=False):
        if self.enhancement:
            e_num = [i for i, ex in enumerate(e) if ex in self.numliteral2id]
            e_txt = [i for i, ex in enumerate(e) if ex in self.textliteral2id]
            e_rel = [i for i in range(len(e)) if i not in e_num and i not in e_txt]

            rel_ind = [e[i] for i in e_rel]
            num_ind = [e[i] for i in e_num]
            txt_ind = [e[i] for i in e_txt]

            rel_emb = self.embeddings(torch.LongTensor(rel_ind))

            if self.literalE:
                if self.numerical_literals is not None and self.textual_literals is not None:
                    num_lit = self.numerical_literals[rel_ind]
                    txt_lit = self.textual_literals[rel_ind]
                    rel_emb = self.rel_gate(rel_emb, num_lit, txt_lit)
                elif self.numerical_literals is not None and self.textual_literals is None:
                    num_lit = self.numerical_literals[rel_ind]
                    rel_emb = self.rel_gate(rel_emb, num_lit)
                elif self.numerical_literals is None and self.textual_literals is not None:
                    txt_lit = self.textual_literals[rel_ind]
                    rel_emb = self.rel_gate(rel_emb, txt_lit)

            emb = self.embeddings(torch.LongTensor(num_ind))
            if len(num_ind) > 0:
                num_emb = self.num_gate(emb, self.numerical_embeddings(torch.LongTensor([self.numliteral2id[i] for i in num_ind])))
            else:
                num_emb = emb

            emb = self.embeddings(torch.LongTensor(txt_ind))
            if len(txt_ind) > 0:
                txt_emb = self.txt_gate(emb, self.textual_embeddings(torch.LongTensor([self.textliteral2id[i] for i in txt_ind])))
            else:
                txt_emb = emb

            e_emb = torch.zeros((e.shape[0], self.embedding_size))

            for i, ind in enumerate(e_num):
                e_emb[ind] = num_emb[i]
                if update: self.final_embeddings[e[ind]] = e_emb[ind]
            for i, ind in enumerate(e_txt):
                e_emb[ind] = txt_emb[i]
                if update: self.final_embeddings[e[ind]] = e_emb[ind]
            for i, ind in enumerate(e_rel):
                e_emb[ind] = rel_emb[i]
                if update: self.final_embeddings[e[ind]] = e_emb[ind]
        else:
            e_emb = self.embeddings(torch.LongTensor(e))
            if self.numerical_literals is not None and self.textual_literals is not None:
                num_lit = self.numerical_literals[e]
                txt_lit = self.textual_literals[e]
                e_emb = self.rel_gate(e_emb, num_lit, txt_lit)
            elif self.numerical_literals is not None and self.textual_literals is None:
                num_lit = self.numerical_literals[e]
                e_emb = self.rel_gate(e_emb, num_lit)
            elif self.numerical_literals is None and self.textual_literals is not None:
                txt_lit = self.textual_literals[e]
                e_emb = self.rel_gate(e_emb, txt_lit)

            if update:
                for i, _ in enumerate(e):
                    self.final_embeddings[e[i]] = e_emb[i]

        return e_emb


class TransETransformer:

    def __init__(self, types_per_entity=None, entities_per_type=None,
                 ontology=None, literalE=False, enhancement=False, mult=False):

        self.neg_ratio = 1.0
        self.batch_size = 128
        self.embedding_size = 100
        self.num_epochs = 100
        self.learning_rate = 0.001

        self.types_per_entity = types_per_entity
        self.entities_per_type = entities_per_type
        self.ontology = ontology

        self.literalE = literalE
        self.enhancement = enhancement
        self.mult = mult

        self.ent_embeddings = dict()
        self.rel_embeddings = dict()

        self.num_fc = None


    def fit(self, train_data=None, test_data=None, valid_data=None):
        print("Getting TransE embeddings...")
        print("Preparing data...")
        self.train_triples = train_data
        self.valid_triples = valid_data
        self.test_triples = test_data
        self.train, self.test, self.valid, self.word2index, self.index2word, \
        self.head_tail_selector, self.entity2id, self.id2entity, \
        self.relation2id, self.id2relation = Utils.build_data(train_data, test_data, valid_data)

        print(len(self.word2index), len(self.entity2id), len(self.relation2id))
        # cannot assert this: in RDF KGs relations might feature as nodes
        # assert len(self.word2index) % (len(self.entity2id) + len(self.relation2id)) == 0

        batch = BatchLoader(self.train, self.test,
                            self.word2index, self.index2word,
                            self.head_tail_selector,
                            self.entity2id, self.id2entity, self.relation2id, self.id2relation,
                            types_per_entity=self.types_per_entity, entities_per_type=self.entities_per_type,
                            ontology=self.ontology,
                            batch_size=self.batch_size, neg_ratio=self.neg_ratio)
        self.__start(batch)

    def __start(self, batch, is_predict=False):
        n_entities = len(self.entity2id)
        n_relations = len(self.relation2id)
        train_num_embeddings, train_num_literals = self.__get_numerical_embeddings(self.train, literals=True)
        valid_num_embeddings = self.__get_numerical_embeddings(self.valid)
        test_num_embeddings = self.__get_numerical_embeddings(self.test)
        train_txt_embeddings, tags, docs, train_txt_literals = self.__get_textual_embeddings(self.train, literals=True)
        valid_txt_embeddings, _, _ = self.__get_textual_embeddings(self.valid, tags, docs)
        test_txt_embeddings, _, _ = self.__get_textual_embeddings(self.test, tags, docs)
        numerical_embeddings = {**train_num_embeddings, **test_num_embeddings, **valid_num_embeddings}
        textual_embeddings = {**train_txt_embeddings, **test_txt_embeddings, **valid_txt_embeddings}

        textliteral2id = dict()
        numliteral2id = dict()
        num_embeddings = list()
        for i, literal in enumerate(list(numerical_embeddings.keys())):
            numliteral2id[literal] = i
            num_embeddings.append(numerical_embeddings[literal])
        txt_embeddings = list()
        for i, literal in enumerate(list(textual_embeddings.keys())):
            textliteral2id[literal] = i
            txt_embeddings.append(textual_embeddings[literal])

        if len(num_embeddings) == 0: num_embeddings = [[]]
        if len(txt_embeddings) == 0: txt_embeddings = [[]]

        if not self.mult:
            model = TransE(n_entities, n_relations,
                    numerical_embeddings=num_embeddings, textual_embeddings=txt_embeddings,
                    numerical_literals=train_num_literals, textual_literals=train_txt_literals,
                    textliteral2id=textliteral2id, numliteral2id=numliteral2id,
                    relation2id=self.relation2id,
                    embedding_size=self.embedding_size,
                    literalE=self.literalE, enhancement=self.enhancement)
        else:
            model = DistMult(n_entities, n_relations,
                    numerical_embeddings=num_embeddings, textual_embeddings=txt_embeddings,
                    numerical_literals=train_num_literals, textual_literals=train_txt_literals,
                    textliteral2id=textliteral2id, numliteral2id=numliteral2id,
                    relation2id=self.relation2id,
                    embedding_size=self.embedding_size,
                    literalE=self.literalE, enhancement=self.enhancement)

        model_path = '{0}.model'.format('transE')

        model.init()
        opt = torch.optim.Adam(model.parameters(), lr=self.learning_rate)

        if not is_predict:
            num_batches_per_epoch = int((len(self.train) - 1) / self.batch_size) + 1
            for epoch in tqdm(range(self.num_epochs)):
                batch.reset()
                for batch_num in range(num_batches_per_epoch):
                    x_batch, y_batch = batch()

                    if not self.mult:
                        ph = x_batch[:self.batch_size, 0]
                        pr = x_batch[:self.batch_size, 1]
                        pt = x_batch[:self.batch_size, 2]
                        nh = x_batch[self.batch_size:, 0]
                        nr = x_batch[self.batch_size:, 1]
                        nt = x_batch[self.batch_size:, 2]
                        loss, pred = model.forward(ph, pt, pr, nh, nt, nr)
                        h = ph
                        r = pr
                        t = pt
                    else:
                        h = x_batch[:, 0]
                        r = x_batch[:, 1]
                        t = x_batch[:, 2]
                        loss, pred = model.forward(h, t, r, y_batch)

                    opt.zero_grad()
                    loss.backward()
                    opt.step()

                    # print("batch", batch_num, ":", loss)
                    if epoch == self.num_epochs - 1:
                        for i, _ in enumerate(h):
                            self.ent_embeddings[self.entity2id[self.index2word[h[i]]]] = model.final_embeddings[h[i]].tolist()
                            self.rel_embeddings[self.relation2id[self.index2word[r[i]]]] = model.final_embeddings[r[i]].tolist()
                            self.ent_embeddings[self.entity2id[self.index2word[t[i]]]] = model.final_embeddings[t[i]].tolist()
                # if epoch % 10 == 0: batch.update_distances(self.id2entity.keys(), model.final_embeddings, self.embedding_size)
                # if (epoch + 1) % 5 == 0:
                #     self.__eval(model, str(epoch), is_valid=False)
                #     model.train()
            # evaluate with test set...
            self.__eval(model, model_path)
        else:
            with torch.no_grad():
                h = batch[:, 0]
                r = batch[:, 1]
                t = batch[:, 2]

                if not self.mult:
                    nh = torch.LongTensor(0)
                    nt = torch.LongTensor(0)
                    nr = torch.LongTensor(0)
                    loss, pred = model.forward(h, t, r, nh, nt, nr)
                else:
                    loss, pred = model.forward(h, t, r, torch.LongTensor(0))
            new_ent_emb = dict()
            new_rel_emb = dict()
            for i, _ in enumerate(h):
                new_ent_emb[self.index2word[h[i]]] = model.final_embeddings[h[i]].tolist()
                new_rel_emb[self.index2word[r[i]]] = model.final_embeddings[r[i]].tolist()
                new_ent_emb[self.index2word[t[i]]] = model.final_embeddings[t[i]].tolist()
            return new_ent_emb, new_rel_emb


    def __eval(self, model, model_path, is_valid=False):
        print("Start evaluation...")
        model.eval()
        num_splits = 8
        if is_valid:
            x_test = np.array(list(self.valid.keys())).astype(np.int32)
            y_test = np.array(list(self.valid.values())).astype(np.float32)
        else:
            x_test = np.array(list(self.test.keys())).astype(np.int32)
            y_test = np.array(list(self.test.values())).astype(np.float32)
        len_test = len(x_test)
        batch_test = int(len_test / (num_splits - 1))
        entity_array = np.array(list(self.entity2id.values()))
        # entity_array = np.array(list(batch.indexes_ents.keys()))

        print(len_test, "evaluation triples,", batch_test, "evaluation batches")

        def predict(ph, pt, pr):
            with torch.no_grad():
                if not self.mult:
                    nh = torch.LongTensor(0)
                    nt = torch.LongTensor(0)
                    nr = torch.LongTensor(0)
                    loss, pred = model.forward(ph, pt, pr, nh, nt, nr)
                else:
                    loss, pred = model.forward(ph, pt, pr, torch.LongTensor(0))
            return pred

        def test_prediction(x_batch, y_batch, head_or_tail='head'):

            hits10 = 0.0
            mrr = 0.0
            mr = 0.0

            for i in range(len(x_batch)):
                # we repeat the triple at index i in x_batch as many times as there are entities
                new_x_batch = np.tile(x_batch[i], (len(self.entity2id), 1))
                # should be all ones, as all triples in x_batch are real
                new_y_batch = np.tile(y_batch[i], (len(self.entity2id), 1))
                if head_or_tail == 'head':
                    new_x_batch[:, 0] = entity_array
                else:  # 'tail'
                    new_x_batch[:, 2] = entity_array

                lstIdx = []
                for tmpIdxTriple in range(len(new_x_batch)):
                    # create a temporary corrupted triple
                    tmpTriple = (new_x_batch[tmpIdxTriple][0],
                                 new_x_batch[tmpIdxTriple][1],
                                 new_x_batch[tmpIdxTriple][2])
                    if (tmpTriple in self.train) or (tmpTriple in self.valid) or (tmpTriple in self.test):
                        lstIdx.append(tmpIdxTriple)
                new_x_batch = np.delete(new_x_batch, lstIdx, axis=0)
                new_y_batch = np.delete(new_y_batch, lstIdx, axis=0)

                # thus, insert the valid test triple again, to the beginning of the array
                new_x_batch = np.insert(new_x_batch, 0, x_batch[i], axis=0)
                # thus, the index of the valid test triple is equal to 0
                new_y_batch = np.insert(new_y_batch, 0, y_batch[i], axis=0)

                results = []
                listIndexes = range(0, len(new_x_batch), (int(self.neg_ratio) + 1) * self.batch_size)
                for tmpIndex in range(len(listIndexes) - 1):
                    h_batch = new_x_batch[listIndexes[tmpIndex]:listIndexes[tmpIndex + 1], 0]
                    t_batch = new_x_batch[listIndexes[tmpIndex]:listIndexes[tmpIndex + 1], 2]
                    r_batch = new_x_batch[listIndexes[tmpIndex]:listIndexes[tmpIndex + 1], 1]
                    results = np.append(results, predict(h_batch, t_batch, r_batch))
                h_batch = new_x_batch[listIndexes[-1]:, 0]
                t_batch = new_x_batch[listIndexes[-1]:, 2]
                r_batch = new_x_batch[listIndexes[-1]:, 1]
                results = np.append(results, predict(h_batch, t_batch, r_batch))

                results = np.reshape(results, -1)
                # print(results)

                results_with_id = rankdata(results, method='ordinal')
                _filter = results_with_id[0]

                # print("predicted ranking:", results_with_id)

                mr += _filter
                mrr += (1.0 / _filter)
                if _filter <= 10:
                    hits10 += 1

                # print("mr, mrr, hits@10:", mr, mr / (i + 1), mrr, mrr / (i + 1), hits10, hits10 / (i + 1))

            num = len(x_batch)
            if num == 0:
                num = 1
            return np.array([mr / num, mrr / num, hits10 / num])

        total_head_results = []
        total_tail_results = []
        for testIdx in tqdm(range(0, num_splits - 1)):
            head_results = test_prediction(
                x_test[batch_test * testIdx: batch_test * (testIdx + 1)],
                y_test[batch_test * testIdx: batch_test * (testIdx + 1)],
                head_or_tail='head')
            tail_results = test_prediction(
                x_test[batch_test * testIdx: batch_test * (testIdx + 1)],
                y_test[batch_test * testIdx: batch_test * (testIdx + 1)],
                head_or_tail='tail')
            total_head_results.append(head_results)
            total_tail_results.append(tail_results)
        head_results = test_prediction(x_test[batch_test * (num_splits - 1): len_test],
                                       y_test[batch_test * (num_splits - 1): len_test],
                                       head_or_tail='head')
        tail_results = test_prediction(x_test[batch_test * (num_splits - 1): len_test],
                                       y_test[batch_test * (num_splits - 1): len_test],
                                       head_or_tail='tail')
        total_head_results.append(head_results)
        total_tail_results.append(tail_results)

        agg_head_results = [0.0] * 3
        agg_tail_results = [0.0] * 3
        for h, t in zip(total_head_results, total_tail_results):
            agg_head_results = [x + y for x, y in zip(agg_head_results, h)]
            agg_tail_results = [x + y for x, y in zip(agg_tail_results, t)]
        total_head_results = [x / num_splits for x in agg_head_results]
        total_tail_results = [x / num_splits for x in agg_tail_results]

        print("head results:", total_head_results)
        print("tail results:", total_tail_results)

        wri = open('TransE.eval.txt', 'w')

        for _val in total_head_results:
            wri.write(str(_val) + ' ')
        wri.write('\n')
        for _val in total_tail_results:
            wri.write(str(_val) + ' ')
        wri.write('\n')

        wri.close()

    def __get_textual_embeddings(self, triples, tags=list(), documents=list(), literals=False):
        if len(tags) > 0:
            tags = list(tags)
        if len(documents) > 0:
            documents = list(documents)
        new_tags = list()

        relations = np.zeros((len(self.word2index.keys()), len(self.id2relation.keys())), dtype=object)
        for triple in triples:
            obj = self.index2word[triple[2]]
            if type(obj) is Literal:
                # also check for empty datatype as this is syntactic sugar for a simple string
                if obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#string') \
                    or obj.datatype is None:
                    text = str(obj.toPython())
                    tags.append(triple[2])
                    new_tags.append(tags[-1])
                    documents.append(TaggedDocument(text, [tags[-1]]))
                    relations[triple[0], self.relation2id[self.index2word[triple[1]]]] = triple[2]

        textual_embeddings = dict()
        if len(documents) > 0:
            # train the doc2vec model to get text embeddings for each literal entity
            model = Doc2Vec(vector_size=self.embedding_size, window=5, workers=cpu_count())
            model.build_vocab([doc for doc in tqdm(documents)])
            for _ in tqdm(range(1)):
                model.train(utils.shuffle([doc for doc in documents]),
                            total_examples=model.corpus_count, epochs=1)
                model.alpha -= 0.002
                model.min_alpha = model.alpha
            # model.train(documents, total_examples=model.corpus_count, epochs=model.iter)
            for doc in new_tags:
                textual_embeddings[doc] = model.docvecs[doc]

        if literals:
            useful_dimensions = relations.shape[1]
            redundant_dimensions = []
            for i, col in enumerate(relations.T):
                if np.isin(col, [0]).all():
                    redundant_dimensions.append(i)

            # if len(redundant_dimensions) == useful_dimensions:
            #     print("No useful dimensions found!")
            #     redundant_dimensions = redundant_dimensions[1:]
            relations = np.delete(relations, redundant_dimensions, axis=1)
            useful_dimensions -= len(redundant_dimensions)
            print(useful_dimensions, "useful dimensions found!")

            textual_literals = np.zeros((len(self.index2word.keys()),
                                         useful_dimensions, self.embedding_size))
            for i, _ in enumerate(textual_literals):
                for j, __ in enumerate(textual_literals[i]):
                    if relations[i, j] in textual_embeddings:
                        textual_literals[i, j] = textual_embeddings[relations[i, j]]
            return textual_embeddings, tags, documents, textual_literals
        return textual_embeddings, tags, documents

    def __get_numerical_embeddings(self, triples, literals=False):
        numerical_embeddings = dict()
        if not self.num_fc:
            self.num_fc = torch.nn.Linear(1, self.embedding_size)

        relations = np.zeros((len(self.word2index.keys()), len(self.id2relation.keys())), dtype=object)
        for triple in triples:
            obj = self.index2word[triple[2]]
            if type(obj) is Literal:
                if obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#decimal') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#integer') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#double') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#float') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#decimal') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#short') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#int') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#long') \
                        or obj.datatype == URIRef('http://www.w3.org/2001/XMLSchema#string'):
                    number = obj.toPython()
                    if type(number) is not str:
                        with torch.no_grad():
                            numerical_embedding = self.num_fc(torch.Tensor([number]))
                            numerical_embeddings[triple[2]] = numerical_embedding.tolist()
                            relations[triple[0], self.relation2id[self.index2word[triple[1]]]] = triple[2]


        if len(numerical_embeddings) > 0:
            # axis 0 indicates that we are normalising per feature: this is what we want!
            max_lit, min_lit = np.max(list(numerical_embeddings.values()), axis=0), np.min(list(numerical_embeddings.values()), axis=0)
            numerical_embeddings = {k: (v - min_lit) / (max_lit - min_lit + 1e-8) for k, v in numerical_embeddings.items()}

        if literals:
            useful_dimensions = relations.shape[1]
            redundant_dimensions = []
            for i, col in enumerate(relations.T):
                if np.isin(col, [0]).all():
                    redundant_dimensions.append(i)

            # if len(redundant_dimensions) == useful_dimensions:
            #     print("No useful dimensions found!")
            #     redundant_dimensions = redundant_dimensions[1:]
            relations = np.delete(relations, redundant_dimensions, axis=1)
            useful_dimensions -= len(redundant_dimensions)
            print(useful_dimensions, "useful dimensions found!")

            numerical_literals = np.zeros((len(self.word2index.keys()),
                                           useful_dimensions, self.embedding_size))
            for i, _ in enumerate(numerical_literals):
                for j, __ in enumerate(numerical_literals[i]):
                    if relations[i, j] in numerical_embeddings:
                        numerical_literals[i, j] = numerical_embeddings[relations[i, j]]
            return numerical_embeddings, numerical_literals

        return numerical_embeddings

    def transform(self, new_data=None):
        super_batch = np.zeros((len(new_data), 3), dtype=np.int32)
        for i, triple in enumerate(new_data):
            head, rel, tail = triple[0], triple[1], triple[2]
            head_ind = self.word2index[head]
            rel_ind = self.word2index[rel]
            tail_ind = self.word2index[tail]

            super_batch[i, :] = [head_ind, rel_ind, tail_ind]

        return self.__start(super_batch, is_predict=True)

    def transform_fitted(self):
        new_ent_embeddings = dict()
        for key in self.ent_embeddings.keys():
            entity = self.id2entity[key]
            new_ent_embeddings[entity] = self.ent_embeddings[key]

        new_rel_embeddings = dict()
        for key in self.rel_embeddings.keys():
            relation = self.id2relation[key]
            new_rel_embeddings[relation] = self.rel_embeddings[key]

        return new_ent_embeddings, new_rel_embeddings

    def fit_transform(self, train_data):
        self.fit(train_data)
        return self.transform_fitted()