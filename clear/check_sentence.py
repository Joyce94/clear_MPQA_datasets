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

path1 = './alltest.txt'
# path2 = './data/my_data_8/train_8.txt'
path2 = './MPQA_old/data8/train8.txt'
path3 = './alldata0.txt'
test_data, test_label = read_sentence_labeler(path1)
data, label = read_sentence_labeler(path3)
train_data8, train_label8 = read_sentence_labeler(path2)
print(len(test_data))
print(len(train_data8))
print(len(data))
index_all = list(range(0, 7173))
dict_all = dict(zip(data, index_all))
index_8 = list(range(0, 6269))
dict_8 = dict(zip(train_data8, index_8))

add = []
add_ind = []
e_list = []
for id, e in enumerate(train_data8):
    if e in dict_all.keys():
        # if train_label8[id] == label[dict_all[e]]:
        add.append(dict_all[e])
        # else:
        #     print(e)
    # else:
    #     print(e)
print(len(add))

# print(len(dict_all))
# for e in dict_all.keys():
#     e_list.append(e)
# print(len(e_list))
# e_set = set(e_list)
# print(len(e_set))
# print(add)
# add_set = set(add)
# print(len(add_set))
# index_all_set = set(index_all)
# print(len(add_set.intersection(index_all_set)))

# sen = []
# ind = []
# for id, e in enumerate(data):
#     if e in dict_8.keys():
#         sen.append(dict_all[e])
#         ind.append(id)
# print(len(sen))
# for i in range(len(sen)):
#     if train_label[sen[i]] != test_label8[ind[i]]:
#         print(test_data8[ind[i]])
#         print("\n")
#         print(test_label8[ind[i]])
#         print('\n')
#         print(train_data[sen[i]])
#         print(train_label[sen[i]])
# second
# sen2 = []
# ind = []
# for id, e in enumerate(train_data8):
#     if e in dict_0.keys():
#         # print(dict_0[e])
#         sen2.append(dict_0[e])
#         ind.append(id)
# print(len(sen2))
# for i in range(len(sen2)):
#     if train_label[sen2[i]] != train_label8[ind[i]]:
#         print(train_data8[ind[i]])
#         print("\n")
#         print(train_label8[ind[i]])
#         print('\n')
#         print(train_data[sen2[i]])
#         print(train_label[sen2[i]])
# third

# sen3 = []
# ind = []
# for id, e in enumerate(test_data8):
#     if e in dict_8.keys():
#         # print(dict_0[e])
#         sen3.append(dict_8[e])
#         ind.append(id)
# print(len(sen3))
# for i in range(len(sen3)):
#     if train_label8[sen3[i]] != test_label8[ind[i]]:
#         print(test_data8[ind[i]])
#         print("\n")
#         print(test_label8[ind[i]])
#         print('\n')
#         print(train_data8[sen3[i]])
#         print(train_label8[sen3[i]])
