import os
class Doc():
    def __init__(self, name, doc_id, start_sen_id, sen_sum):
        self.name = name
        self.doc_id = doc_id
        self.start_sen_id = start_sen_id
        self.sen_sum = sen_sum


def read_file_senid(path, train0_doc):
    doc_id = -1
    doc_name = ''
    count = 0
    doc_count = -1
    start_id = -1
    doc_list = []
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line != '\n':
                line = line.strip().split(' ')
                # print(line)
                if id == 0:
                    doc_id = int(line[0])
                    doc_name = line[2]
                    doc_count = int(line[1])
                    count += 1
                    start_id = id
                elif int(line[0]) == doc_id:
                    count += 1
                    doc_count = int(line[1])
                else:
                    # print(doc_name)
                    # print(doc_id)
                    # print(start_id)
                    # # print(count-1)
                    # print(doc_count+1)
                    doc = Doc(doc_name, doc_id, start_id, doc_count+1)
                    # print(doc.name)
                    if doc.name in train0_doc:
                        # print(doc.doc_id)
                        doc_list.append(doc)
                    doc_id = int(line[0])
                    doc_name = line[2]
                    count += 1
                    start_id = id
            else:
                doc = Doc(doc_name, doc_id, start_id, count - 1)
                doc_list.append(doc)
    # print(len(train0_doc))
    # print(len(doc_list))
    return doc_list

def read_filelist(path):
    doc_list = []
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            # print(line)
            doc_list.append(line.strip())
    # print(len(doc_list))
    # print(doc_list[0])
    return doc_list

# path = './MPQA_processed_dataset_new/all_ILP_bmes_rel-2.txt'
path = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\doclist.mpqaOriginalSubset'
filelist_path = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\filelist_train8'
filelist_path_test = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\filelist_test8_modify'
filelist_path2 = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\filelist_train9'
filelist_path_test2 = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\filelist_test9'
dev_path = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\dev.txt'
write_path = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\split\test8.txt'
train8_doc = read_filelist(filelist_path)
test8_doc = read_filelist(filelist_path_test)
train0_doc = read_filelist(filelist_path2)
test0_doc = read_filelist(filelist_path_test2)
# dev_doc = read_filelist(dev_path)
# all_doc = read_filelist(path)
all_8 = []
all_8.extend(train8_doc)
all_8.extend(test8_doc)
all_0 = []
all_0.extend(train0_doc)
all_0.extend(test0_doc)
# print(all_doc)
# print(train0_doc)
# print(test0_doc)
# print(len(train0_doc))    # 315
# print(len(test0_doc))     # 35
# print(len(all_doc))       # 482

# train0_doc_list = read_file_senid(path, train0_doc)
# print(len(train0_doc_list))
# print(len(train0_doc_list))
# all_doc_list = read_file_senid(path, train0_doc)
# print(len(all_doc_list))      # 481
# print(train0_doc)
# check
count = 0
check = []
s = 0
for e in all_0:
    if e not in all_8:
        s += 1
        print(e)
    else:
        # if os.path.exists(write_path):
        #     file = open(write_path, "a", encoding='utf-8')
        # else:
        #     file = open(write_path, "w", encoding='utf-8')
        # file.write('\n')
        # file.write(e)
        # file.close()
        check.append(e)
        count += 1
#     # if e.name == 'xbank/wsj_1073':
#     #     print('true')
print(s)
print(count)
print(len(check))
# c = []
# for e in check:
#     if e not in test8_doc:
#         c.append(e)
# print(c)
# line_path = r'C:\Users\user\PycharmProjects\script\MPQA_processed_dataset_new\all_ILP_bmes_rel-2.txt'
# Extract_lines(line_path, train0_doc_list)






