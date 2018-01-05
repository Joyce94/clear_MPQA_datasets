class Entity():
    def __init__(self, start, end, category):
        self.start = start
        self.end = end
        self.category = category

    def equal(self, entity):
        return self.start == entity.start and self.end == entity.end and self.category == entity.category

    def match(self, entity):
        span = set(range(int(self.start), int(self.end) + 1))
        entity_span = set(range(int(entity.start), int(entity.end) + 1))
        return len(span.intersection(entity_span)) and self.category == entity.category

    def propor_score(self, entity):
        span = set(range(int(self.start), int(self.end) + 1))
        entity_span = set(range(int(entity.start), int(entity.end) + 1))
        return float(len(span.intersection(entity_span))) / float(len(span))

    def toprint(self):
        print(self.category+'['+str(self.start)+','+str(self.end)+']')

def is_continue(e, label, prefix_array):
    if len(label) < 3 or label == '<pad>' or label == '<start>':
        return False
    if label[0] in prefix_array[3]:
        return False
    if label[0] in prefix_array[1] and cleanLabel(label, prefix_array) == cleanLabel(e, prefix_array):
        return True

def cleanLabel(label, prefix_array):
    prefix = [e for ele in prefix_array for e in ele]
    if len(label) > 2 and label[1] == '-':
        if label[0] in prefix:
            return label[2:]

def read_sentence_labeler(path):
    words = []
    labels = []
    sen = ' '
    lab = ' '
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):

            if line.split(' ')[0] != 'rel' and line != '\n':
                if len(line.split(' ')) != 6:
                    print(line.split(' '))
                    print(id)
                if line.split(' ')[0] != 'token':
                    print(line.split(' '))
                    print(id)
                if line.split(' ')[3] != '-1':
                    print(line.split(' '))
                    print(id)
                if line.split(' ')[4] != 'ROOT':
                    print(line.split(' '))
                    print(id)
            if line.split(' ')[0] == 'rel':
                if len(line.split(' ')) != 5:
                    print(line.split(' '))
                    print(id)
            if line == '\n':
                # count += 1
                # if os.path.exists("./data.txt"):
                #     file = open("./data.txt", "a")
                # else:
                #     file = open("./data.txt", "w")
                # file.write('\n第'+str(count)+'个句子：\n')
                # file.write(sen.strip())
                # file.write('\n')
                # file.write(lab.strip())
                # file.write('\n')
                # file.close()
                words.append(sen.strip())
                labels.append(lab.strip())
                sen = ' '
                lab = ' '
            else:
                sentence = line.strip().split(' ')
                # print(sentence)
                if sentence[0] == 'token':
                    sen = sen + sentence[1] + ' '
                    lab = lab + sentence[-1] + ' '
                    # labb.append(sentence[5])

    return words, labels

def read_sentence_labeler_new(path):
    words = []
    labels = []
    sen_orig = []
    sen = ' '
    lab = ' '
    sen_origin = ' '
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line == '\n':
                words.append(sen.strip())
                labels.append(lab.strip())
                sen_orig.append(sen_origin.strip())
                sen = ' '
                lab = ' '
                sen_origin = ' '
            else:
                sentence = line.strip().split('\t')
                # print(sentence)
                sen = sen + sentence[0] + ' '
                sen_origin = sen_origin + sentence[1] + ' '
                lab = lab + sentence[-2] + '-com' + ' '
    # print(len(words))       # 3222
    # print(len(labels))
    # print(len(sen_orig))
    return words, labels


def read_corpus_labeler(corpus_data, corpus_labels):
    data = []
    labels = []
    seq_list = []
    for i in range(len(corpus_data)):
        text = corpus_data[i].strip()
        label = corpus_labels[i].strip()
        labels.append(label.split())
        data.append(text.split())
        # print(text.split())
        # print(len(text.split()))
        seq_list.append(len(text.split()))
    # print(seq_list)
    # print(len(seq_list))
    return data, labels, seq_list

def createAlphabet_labeler(data, label):
    data_num = 0
    for index in range(len(data)):
        data_num += len(data[index])
        if len(data[index]) != len(label[index]):
            # print('error')
            print(index)
    # print(data_num)
    id2label = []
    count = 0
    for index in range(len(label)):
        count += len(label[index])
        for w in label[index]:
            if w not in id2label:
                id2label.append(w)
    id2label = set(id2label)
    id2label = [e for e in id2label]
    # print(count)
    return id2label, count, data_num

def Extract_category(label2id, prefix_array):
    prefix = [e for ele in prefix_array for e in ele]
    category_list = []
    for key in label2id:
        if '-' in key:
            category_list.append(cleanLabel(key, prefix))
    # print(set(category_list))    # {'AGENT', 'TARGET', 'DSE'}
    category_set = set(category_list)
    return category_set


class Count():
    def __init__(self, category_set, dataset_num):
        self.total_num = 0
        self.total_num_bio = 0
        self.category_set = category_set
        self.dataset_num = dataset_num

    def set_eval_var(self):
        category_num = len(self.category_set)
        self.B = []
        self.C = []
        for i in range(category_num):
            self.B.append(0)
            self.C.append(0)

    def count_num(self, train_label, prefix_array, prefix_array_bio):
        for index in range(dataset_num):
            gold_set, gold_entity_group = Extract_entity(train_label[index], self.category_set, prefix_array)
            gold_set_bio, gold_entity_group_bio = Extract_entity_bio(train_label[index], self.category_set, prefix_array_bio)
            # gold_set, gold_entity_group = Extract_entity(train_label[index], self.category_set, prefix_array)
            # gold_set_bio, gold_entity_group_bio = Extract_entity(train_label[index], self.category_set, prefix_array)

            self.total_num += len(gold_set)
            self.total_num_bio += len(gold_set_bio)
            for id in range(len(gold_entity_group)):
                self.B[id] += len(gold_entity_group[id])
                self.C[id] += len(gold_entity_group_bio[id])
                if len(gold_entity_group[id]) != len(gold_entity_group_bio[id]):
                    # print(gold_entity_group[id])
                    # print(gold_entity_group_bio[id])
                    print(index)
                else:
                    for i, e in enumerate(gold_entity_group_bio[id]):
                        if not e.equal(gold_entity_group[id][i]):
                            e.toprint()
                            gold_entity_group[id][i].toprint()
                            print("equal", index)
        # return self.total_num, self.B

    def print(self):
        category_list = [e for e in self.category_set]
        print("The total num is ", self.total_num, self.total_num_bio)
        for i in range(len(self.category_set)):
            print("Category: ", category_list[i], " , num : ", self.B[i], self.C[i])

def Extract_entity(labels, category_set, prefix_array):
    prefix = [e for ele in prefix_array for e in ele]
    ent = []
    id = 0
    while (id < len(labels)):
        if labels[id][0] in prefix_array[0] and len(labels[id]) > 2:
            j = id + 1
            end = -1
            while (j < len(labels)):
                if labels[j][0] in prefix_array[2] and len(labels[j]) > 2:
                    end = j
                    category = cleanLabel(labels[j], prefix)
                    entity = Entity(id, end, category)
                    ent.append(entity)
                    # entity.toprint()
                    break
                if not is_continue(labels[id], labels[j], prefix_array):
                    end = j - 1
                    break
                end = j
                j += 1
            id = end
        elif labels[id][0] in prefix_array[3] and len(labels[id]) > 2:
            category = cleanLabel(labels[id], prefix)
            entity = Entity(id, id, category)
            ent.append(entity)
            # entity.toprint()
        id += 1
    category_num = len(category_set)
    category_list = [e for e in category_set]
    entity_group = []

    for i in range(category_num):
        entity_group.append([])
    # print(entity_group)
    for id, c in enumerate(category_list):
        for entity in ent:
            if entity.category == c:
                entity_group[id].append(entity)
                # if c == 'DSE':
                #     entity.toprint()
    return set(ent), entity_group

def Extract_entity_bio(labels, category_set, prefix_array):
    idx = 0
    ent = []
    while (idx < len(labels)):
        if (is_start_label(labels[idx], prefix_array)):
            idy = idx
            endpos = -1
            while (idy < len(labels)):
                if not is_continue2(labels[idy], labels[idx], prefix_array, idy - idx):
                    endpos = idy - 1
                    break
                endpos = idy
                idy += 1
            category = cleanLabel2(labels[idx], prefix_array)
            entity = Entity(idx, endpos, category)
            ent.append(entity)
            idx = endpos
        idx += 1
    category_num = len(category_set)
    category_list = [e for e in category_set]
    # print(category_list)
    entity_group = []
    for i in range(category_num):
        entity_group.append([])
    # print(entity_group)
    for id, c in enumerate(category_list):
        for entity in ent:
            if entity.category == c:
                entity_group[id].append(entity)
                # if c == 'DSE':
                #     entity.toprint()
    return set(ent), entity_group

def is_start_label(label, prefix_array):
    if len(label) < 3:
        return False
    return (label[0] in prefix_array[0]) and (label[1] == '-')

def is_continue2(label, startLabel, prefix_array, distance):
    if distance == 0:
        return True
    if len(label) < 3 or label == '<pad>' or label == '<start>':
        return False
    if distance != 0 and is_start_label(label, prefix_array):
        return False
    if (startLabel[0] == 's' or startLabel[0] == 'S') and startLabel[1] == '-':
        return False
    if cleanLabel2(label, prefix_array) != cleanLabel2(startLabel, prefix_array):
        return False
    return True

def cleanLabel2(label, prefix_array):
    prefix = [e for ele in prefix_array for e in ele]
    if len(label) > 2 and label[1] == '-':
        if label[0] in prefix:
            return label[2:]
    return label

def count_seq(seq_list):
    b = list(range(12))
    B = [[] for e in b]
    # print(B)
    for i in range(len(seq_list)):
        B[seq_list[i]//10].append(seq_list[i])
    # print(B)
    count = [len(e) for e in B]
    print(count)
    

# path = './data/my_data_8/train_8.txt'
# path = './all_ILP_bio.txt'
# path = './all_ILP_bmes.txt'
path = './sentence.dat'
# path = r"C:\Users\user\PycharmProjects\script\dev.txt"
# path = r"C:\Users\user\PycharmProjects\script\MPQA\test9.txt"
# path = r"C:\Users\user\PycharmProjects\script\MPQA\train0.txt"
train_data, train_label = read_sentence_labeler(path)
# import os
# if os.path.exists("./train_data0.txt"):
#     file = open("./train_data0.txt", "a", encoding='utf-8')
# else:
#     file = open("./train_data0.txt", "w", encoding='utf-8')
# file.write(str(train_data))
# file.close()
# if os.path.exists("./train_data0.txt"):
#     file = open("./train_data0.txt", "a", encoding='utf-8')
# else:
#     file = open("./train_data0.txt", "w", encoding='utf-8')
# file.write(str(train_label))
# file.close()
# print(len(train_data))
# print(len(train_label))
train_data, train_label, seq_list = read_corpus_labeler(train_data, train_label)

label_list, label_num, data_num = createAlphabet_labeler(train_data, train_label)
# print(label_list)     # ['m-AGENT', 'b-DSE', 'm-DSE', 'm-TARGET', 'b-TARGET', 'o', 'b-AGENT']
# ['e-DSE', 'b-DSE', 'm-AGENT', 'e-AGENT', 's-AGENT', 'm-DSE', 'b-AGENT', 'm-TARGET', 's-TARGET', 's-DSE', 'o', 'b-TARGET', 'e-TARGET']

seq_set = set(seq_list)
# print(seq_set)
# count_seq(seq_list)

if label_num == data_num:
    print("After testing, the number of data is equal to the number of labels.")
else:
    print("After testing, the number of data is not equal to the number of labels.")
prefix_array = [['b', 'B'], ['m', 'M'], ['e', 'E'], ['s', 'S']]
prefix_array_bio = [['b', 'B', 's', 'S'], ['m', 'M', 'e', 'E']]

# prefix_array_bio = [['b', 'B'], ['m', 'M']]
category_set = Extract_category(label_list, prefix_array)
# print(category_set)
# cheak label
if len(label_list) != len(prefix_array)*len(category_set)+1:
    print("Maybe there are some errors in labelset, you need to check.")
dataset_num = len(train_label)
print(dataset_num)

count = Count(category_set, dataset_num)
count.set_eval_var()
count.count_num(train_label, prefix_array, prefix_array_bio)
count.print()







