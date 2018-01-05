import os
import re

def read_ILP(path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    sen_list = []
    # sen = ''
    total = []
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line != '\n':
                line = line.strip().split('\t')
                words.append(line[0])
                pos.append(line[1])
                label.append(line[2])
                if len(line) != 3:
                    print(id)
                count += 1
                sen_list.append(line[0])
            elif line == '\n':
                sen_c += 1
                count += 1
                sen = ' '.join(sen_list)
                # print(sen)
                total.append(sen)
                sen_list = []
                # sen = ''
    print(count)
    print(sen_c)
    print(len(total))
    # print(total)
    print(len(set(total)))
    return words, pos, label

def write_ILP(path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    if os.path.exists("./sen.txt"):
        os.remove("./sen.txt")
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            sen = ['token']
            if line != '\n':
                line = line.strip().split('\t')
                # words.append(line[0])
                # pos.append(line[1])
                # label.append(line[2])
                if len(line) != 3:
                    print(id)
                count += 1
                sen.append(line[0])
                sen.append(line[1])
                sen.append('-1')
                sen.append('ROOT')
                sen.append(line[2])
                sen = ' '.join(sen)
                # print(sen)
                # if os.path.exists("./sen.txt"):
                #     os.remove("./sen.txt")
                # if os.path.exists("./sen.txt"):
                #     file = open("./sen.txt", "a", encoding='utf-8')
                # else:
                #     file = open("./sen.txt", "w", encoding='utf-8')
                # file.write(sen)
                # file.write('\n')
                # file.close()
            elif line == '\n':
                sen_c += 1
                count += 1
                # if os.path.exists("./sen.txt"):
                #     file = open("./sen.txt", "a", encoding='utf-8')
                # else:
                #     file = open("./sen.txt", "w", encoding='utf-8')
                # file.write('\n')
                # file.close()
    print(count)
    print(sen_c)
    return words, pos, label

def rewrite_ILP(path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    if os.path.exists("./sen.txt"):
        os.remove("./sen.txt")
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            sen = ['token']
            digit_total = []
            if line != '\n':
                line = line.strip().split('\t')
                # words.append(line[0])
                # pos.append(line[1])
                # label.append(line[2])
                if len(line) != 3:
                    print(id)
                count += 1
                string = line[2]
                digit_list = re.findall(r"\d+\.?\d*", string)


                sen.append(line[0])
                sen.append(line[1])
                sen.append('-1')
                sen.append('ROOT')
                sen.append(line[2])
                sen = ' '.join(sen)
                # print(sen)
                # if os.path.exists("./sen.txt"):
                #     os.remove("./sen.txt")
                # if os.path.exists("./sen.txt"):
                #     file = open("./sen.txt", "a", encoding='utf-8')
                # else:
                #     file = open("./sen.txt", "w", encoding='utf-8')
                # file.write(sen)
                # file.write('\n')
                # file.close()
            elif line == '\n':
                sen_c += 1
                count += 1
                # if os.path.exists("./sen.txt"):
                #     file = open("./sen.txt", "a", encoding='utf-8')
                # else:
                #     file = open("./sen.txt", "w", encoding='utf-8')
                # file.write('\n')
                # file.close()
    print(count)
    print(sen_c)
    return words, pos, label

def read_senid(path):
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            # print(line.split(' '))
            line = line.strip().split(' ')
            if len(line) != 3:
                print(id)

def ILP_bio(path, write_path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    if os.path.exists(write_path):
        os.remove(write_path)
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            sen = ['token']
            if line != '\n':
                line = line.strip().split('\t')
                if len(line) != 3:
                    print('error')
                    print(id)
                    print(line)
                # words.append(line[0])
                # pos.append(line[1])
                # label.append(line[2])
                if len(line) != 3:
                    print(id)
                count += 1
                # 标注rel
                # string = line[2]
                # if len(string) > 1:
                #     digit_list = re.findall(r"\d+\.?\d*", string)
                #     print(digit_list)
                # 标注bio
                if len(line[2]) > 1:
                    label = line[2].split('_')
                    if label[0] == 'B':
                        label[0] = 'b'
                    else:
                        label.insert(0, 'm')
                    label_single = []
                    label_single.append(label[0])
                    label_single.append(label[1])
                    label = '-'.join(label_single)
                    # print(label)
                else:
                    # print('O')
                    label = 'o'
                sen.append(line[0])
                sen.append(line[1])
                sen.append('-1')
                sen.append('ROOT')
                sen.append(label)
                sen = ' '.join(sen)
                if os.path.exists(write_path):
                    file = open(write_path, "a", encoding='utf-8')
                else:
                    file = open(write_path, "w", encoding='utf-8')
                file.write(sen)
                file.write('\n')
                file.close()
                # sen.append(line[0])
                # sen.append(line[1])
                # sen.append('-1')
                # sen.append('ROOT')
                # sen.append(line[2])
                # sen = ' '.join(sen)
                # print(sen)
                # if os.path.exists("./sen.txt"):
                #     os.remove("./sen.txt")
                # if os.path.exists("./sen.txt"):
                #     file = open("./sen.txt", "a", encoding='utf-8')
                # else:
                #     file = open("./sen.txt", "w", encoding='utf-8')
                # file.write(sen)
                # file.write('\n')
                # file.close()
            elif line == '\n':
                sen_c += 1
                count += 1
                if os.path.exists(write_path):
                    file = open(write_path, "a", encoding='utf-8')
                else:
                    file = open(write_path, "w", encoding='utf-8')
                file.write('\n')
                file.close()

    print(count)
    print(sen_c)
    return words, pos, label

ILP_path = './MPQA_processed_dataset_new/all_ILP_modify.txt'
# sen_path = './MPQA_processed_dataset_new/sentenceid.txt'
write_path = "./all_ILP_bio.txt"
words, pos, label = ILP_bio(ILP_path, write_path)
# print(set(label))
# label_set = set(label)
# for e in label_set:
#     e_list = e.split('_')
#     # print(len(e_list))
#     if 'DSE' in e_list:
#         if len(e_list)>3:
#             print(e)
# words2, pos2, label2 = rewrite_ILP(ILP_path)
# print(words)
# print(pos)
# print(label)
# if os.path.exists("./clear.txt"):
#     os.remove("./clear.txt")
# if os.path.exists("./clear.txt"):
#     file = open("./clear.txt", "a", encoding='utf-8')
# else:
#     file = open("./clear.txt", "w", encoding='utf-8')
# file.write(str(label))
# file.close()

# read_senid(sen_path)









