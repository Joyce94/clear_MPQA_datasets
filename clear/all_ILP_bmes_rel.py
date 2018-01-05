import os
import re
import operator

def read_ILP(path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    sen_list = []

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

def ILP_bmes(path, write_path):
    count = 0
    sen_c = 0
    words = []
    pos = []
    label = []
    if os.path.exists(write_path):
        os.remove(write_path)
    with open(path, 'r', encoding='utf-8') as fin:
        entity_count = -1
        line_old = '\n'
        for id, line in enumerate(fin.readlines()):
            sen = ['token']
            label_old = ''
            if line != '\n':
                line = line.strip().split('\t')
                if len(line) != 3:
                    print(id)
                count += 1

                # 标注bmes
                if len(line[2]) > 1:
                    if line[2].split('_')[0] == 'B':
                        if entity_count == 0:
                            # print(label)
                            label_old = label
                        elif entity_count == 1:
                            label[0] = 's'
                            # label = '_'.join(label)
                            # print(label)
                            # print(label)
                            label_single = []
                            label_single.append(label[0])
                            label_single.append(label[1])
                            label_single.extend(label[2:])
                            label = '-'.join(label_single)
                            # print(label)
                            label_old = label
                        elif entity_count != 0 and entity_count != -1 and entity_count != 1:
                            label[0] = 'e'
                            # label = '_'.join(label)
                            label_single = []
                            label_single.append(label[0])
                            label_single.append(label[1])
                            label_single.extend(label[2:])
                            label = '-'.join(label_single)
                            # print(label)
                            label_old = label
                        label = line[2].split('_')
                        label[0] = 'b'
                        entity_count = 1
                    elif line[2].split('_')[0] != 'B':
                        # label = '_'.join(label)
                        # print(label)
                        # print(line)
                        label_single = []
                        label_single.append(label[0])
                        label_single.append(label[1])
                        label_single.extend(label[2:])
                        label = '-'.join(label_single)
                        # print(label)
                        label_old = label
                        label = line[2].split('_')
                        label.insert(0, 'm')
                        entity_count += 1
                    # 标注rel
                    # string = line[2]
                    # if len(string) > 1:
                    #     digit_list = re.findall(r"\d+\.?\d*", string)
                    #     print(digit_list)
                else:
                    if entity_count == 0:
                        # print(label)
                        label_old = label
                    elif entity_count == 1:
                        label[0] = 's'
                        # label = '_'.join(label)
                        label_single = []
                        label_single.append(label[0])
                        label_single.append(label[1])
                        label_single.extend(label[2:])
                        label = '-'.join(label_single)
                        # print(label)
                        label_old = label
                    elif entity_count != 0 and entity_count != -1 and entity_count != -1:
                        label[0] = 'e'
                        # label = '_'.join(label)
                        label_single = []
                        label_single.append(label[0])
                        label_single.append(label[1])
                        label_single.extend(label[2:])
                        label = '-'.join(label_single)
                        # print(label)
                        label_old = label
                    label = 'o'
                    entity_count = 0

                if line_old != '\n':
                    sen.append(line_old[0])
                    sen.append(line_old[1])
                    sen.append('-1')
                    sen.append('ROOT')
                    sen.append(label_old)
                    sen = ' '.join(sen)
                    # print(sen)
                    if os.path.exists(write_path):
                        file = open(write_path, "a", encoding='utf-8')
                    else:
                        file = open(write_path, "w", encoding='utf-8')
                    file.write(sen)
                    file.write('\n')
                    file.close()
                    line_old = line

            elif line == '\n':
                if entity_count == 0:
                    # print(label)
                    label_old = label
                elif entity_count == 1:
                    label[0] = 's'
                    # label = '_'.join(label)
                    label_single = []
                    label_single.append(label[0])
                    label_single.append(label[1])
                    label_single.extend(label[2:])
                    label = '-'.join(label_single)
                    # print(label)
                    label_old = label
                elif entity_count != 0 and entity_count != -1 and entity_count != -1:
                    label[0] = 'e'
                    # label = '_'.join(label)
                    label_single = []
                    label_single.append(label[0])
                    label_single.append(label[1])
                    label_single.extend(label[2:])
                    label = '-'.join(label_single)
                    # print(label)
                    label_old = label

                sen.append(line_old[0])
                sen.append(line_old[1])
                sen.append('-1')
                sen.append('ROOT')
                sen.append(label_old)
                sen = ' '.join(sen)

                # print('\n')
                entity_count = -1
                sen_c += 1
                count += 1
                # print(sen)
                if os.path.exists(write_path):
                    file = open(write_path, "a", encoding='utf-8')
                else:
                    file = open(write_path, "w", encoding='utf-8')
                file.write(sen)
                file.write('\n')
                file.write('\n')
                file.close()
            line_old = line

    print(count)
    print(sen_c)

def ILP_bmes_rel(path):
    count = 0
    sen_c = 0
    # if os.path.exists("./all_ILP_bmes_rel.txt"):
    #     os.remove("./all_ILP_bmes_rel.txt")
    rel_list = []
    total_digit = []
    start = 0
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line != '\n':
                line = line.strip().split(' ')
                if len(line) != 6:
                    print(id)
                count += 1
                # 标注bmes
                if len(line[5]) > 1:
                    # 标注rel
                    if line[5].split('-')[0] == 'e':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        # print(digit_list)
                        total_digit.extend(digit_list)
                        for e in digit_list:
                            s = e + '-' + category + '-' + str(id-start)
                            # print(s)
                            rel_list.append(s)
                    elif line[5].split('-')[0] == 's':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        # print(digit_list)
                        for e in digit_list:
                            s = e + '-' + category + '-' + str(id-start)
                            # print(s)
                            rel_list.append(s)
            elif line == '\n':
                start = id + 1
                # print(rel_list)
                # print(total_digit)
                total_digit = list(set(total_digit))
                total_digit.sort()
                # print(total_digit)
                digit_num = len(total_digit)
                index_digit = list(range(digit_num))
                total_digit = dict(zip(total_digit, index_digit))
                category_dict = {'AGENT': 0, 'DSE': 1, 'TARGET': 2}
                # print(total_digit)
                B = []
                b = list(range(3))
                for i in range(digit_num):
                    bb = [0 for e in b]
                    B.append(bb)
                # cheak
                cheak = []
                for i in range(digit_num):
                    cheak.append([])
                for e in rel_list:
                    print(e)
                    print(id)
                    cheak[total_digit[e.split('-')[0]]].append(e.split('-')[1:])
                # print(cheak)
                for e in cheak:
                    if len(e) > 3:
                        print(e)
                        print('error')

                for e in rel_list:
                    B[total_digit[e.split('-')[0]]][category_dict[e.split('-')[1]]] = e.split('-')[2]
                # print(B)
                # B = [['6', '8', '0'], ['6', '12', 0], ['6', '15', '25'], ['32', '34', '31'], ['6', '39', '82']]
                # print(B)
                rel = ['rel']
                for i in range(len(B)):
                    if B[i][0] != 0 and B[i][1] != 0:
                        if int(B[i][0]) < int(B[i][1]):
                            rel.append(B[i][0])
                            rel.append(B[i][1])
                            rel.append('1')
                            rel.append('AGENT-DSE')
                        else:
                            rel.append(B[i][1])
                            rel.append(B[i][0])
                            rel.append('-1')
                            rel.append('AGENT-DSE')
                        rel_a = ' '.join(rel)
                        print(rel_a)
                        rel = ['rel']
                    if B[i][1] != 0 and B[i][2] != 0:
                        if int(B[i][1]) < int(B[i][2]):
                            rel.append(B[i][1])
                            rel.append(B[i][2])
                            rel.append('-1')
                            rel.append('TARGET-DSE')
                        else:
                            rel.append(B[i][2])
                            rel.append(B[i][1])
                            rel.append('1')
                            rel.append('TARGET-DSE')
                        rel_t = ' '.join(rel)
                        print(rel_t)
                        rel = ['rel']
                rel_list = []
                total_digit = []

    print(count)
    print(sen_c)

def ILP_bmes_rel_old(path):
    count = 0
    sen_c = 0
    if os.path.exists("./all_ILP_bmes_rel.txt"):
        os.remove("./all_ILP_bmes_rel.txt")
    rel_list = []
    total_digit = []
    start = 0
    entity_error = 0
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line != '\n':
                line = line.strip().split(' ')
                if len(line) != 6:
                    print(id)
                count += 1
                # 标注bmes
                if len(line[5]) > 1:
                    # 标注rel
                    if line[5].split('-')[0] == 'e':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        digit_list = [int(e) for e in digit_list]
                        # print(digit_list)
                        total_digit.extend(digit_list)
                        for e in digit_list:
                            s = str(e) + '-' + category + '-' + str(id-start)
                            # print(s)
                            rel_list.append(s)
                    elif line[5].split('-')[0] == 's':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        digit_list = [int(e) for e in digit_list]
                        # print(digit_list)
                        total_digit.extend(digit_list)
                        for e in digit_list:
                            s = str(e) + '-' + category + '-' + str(id-start)
                            # print(s)
                            rel_list.append(s)
            elif line == '\n':
                start = id + 1
                # print(rel_list)
                # print(total_digit)
                total_digit = list(set(total_digit))
                # print(total_digit)
                total_digit.sort()
                # print(total_digit)
                digit_num = len(total_digit)
                index_digit = list(range(digit_num))
                total_digit = dict(zip(total_digit, index_digit))
                # category_dict = {'AGENT': 0, 'DSE': 1, 'TARGET': 2}
                # print(total_digit)
                B = []
                b = list(range(2))
                for i in range(digit_num):
                    bb = [[] for e in b]
                    B.append(bb)
                # print(B)
                for e in rel_list:
                    category = e.split('-')[1]
                    ent_digit = int(e.split('-')[0])
                    if category == 'DSE':
                        B[total_digit[ent_digit]][0] = e.split('-')[2]
                    else:
                        B[total_digit[ent_digit]][1].append(e.split('-')[1:])
                # print(B)
                # [['8', [['AGENT', '6']]], ['12', [['AGENT', '6']]], ['15', [['AGENT', '6'], ['TARGET', '25']]], ['34', [['TARGET', '31'], ['AGENT', '32']]], ['39', [['AGENT', '6'], ['TARGET', '82']]]]
                # B = [['6', '8', '0'], ['6', '12', 0], ['6', '15', '25'], ['32', '34', '31'], ['6', '39', '82']]
                # print(B)
                rel = ['rel']
                for i in range(len(B)):
                    if B[i][0] == [] or B[i][1] == []:
                        # print(id)
                        # print(B)
                        # print('error')
                        entity_error += 1
                    for j in range(len(B[i][1])):
                        if B[i][1][j][0] == 'AGENT':
                            if int(B[i][1][j][1]) < int(B[i][0]):
                                rel.append(B[i][1][j][1])
                                rel.append(B[i][0])
                                rel.append('1')
                                rel.append('AGENT-DSE')
                            else:
                                rel.append(B[i][0])
                                rel.append(B[i][1][j][1])
                                rel.append('-1')
                                rel.append('AGENT-DSE')
                            rel_a = ' '.join(rel)
                            print(rel_a)
                            rel = ['rel']
                        elif B[i][1][j][0] == 'TARGET':
                            if int(B[i][1][j][1]) < int(B[i][0]):
                                rel.append(B[i][1][j][1])
                                rel.append(B[i][0])
                                rel.append('1')
                                rel.append('TARGET-DSE')
                            else:
                                rel.append(B[i][0])
                                rel.append(B[i][1][j][1])
                                rel.append('-1')
                                rel.append('TARGET-DSE')
                            rel_t = ' '.join(rel)
                            print(rel_t)
                            rel = ['rel']
                rel_list = []
                total_digit = []
    print(entity_error)
    print(count)
    print(sen_c)

def ILP_bmes_rel2(path, write_path):
    count = 0
    sen_c = 0
    if os.path.exists(write_path):
        os.remove(write_path)
    rel_list = []
    total_digit = []
    start = 0
    entity_error = 0
    more_dse = 0
    rel_count = 0
    A_seq = []
    T_seq = []
    D_seq = []
    ss = 0
    category_dict = {'AGENT': 0, 'DSE': 1, 'TARGET': 2}
    entity_rel_count = [[],[],[]]
    a_rel_count = []
    t_rel_count = []
    with open(path, 'r', encoding='utf-8') as fin:
        for id, line in enumerate(fin.readlines()):
            if line != '\n':
                line = line.strip().split(' ')
                if len(line) != 6:
                    print(id)
                    print(line)
                count += 1
                # 标注bmes
                if len(line[5]) > 1:
                    # 标注rel
                    if line[5].split('-')[0] == 'b':
                        ss = id
                    if line[5].split('-')[0] == 'e':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        digit_list = [int(e) for e in digit_list]

                        # print(digit_list)
                        entity_rel_count[category_dict[category]].append(len(digit_list))
                        # print(entity_rel_count)
                        total_digit.extend(digit_list)
                        for e in digit_list:
                            s = str(e) + '-' + category + '-' + str(id-start)
                            # print(id-start)
                            rel_list.append(s)
                        if category == 'AGENT':
                            A_seq.append(id - ss + 1)
                        elif category == 'DSE':
                            D_seq.append(id - ss + 1)
                        elif category == 'TARGET':
                            T_seq.append(id - ss + 1)
                    elif line[5].split('-')[0] == 's':
                        category = line[5].split('-')[1]
                        string = line[5]
                        digit_list = re.findall(r"\d+\.?\d*", string)
                        digit_list = [int(e) for e in digit_list]
                        # print(digit_list)
                        entity_rel_count[category_dict[category]].append(len(digit_list))
                        # print(entity_rel_count)
                        total_digit.extend(digit_list)
                        for e in digit_list:
                            s = str(e) + '-' + category + '-' + str(id-start)
                            # print(s)
                            rel_list.append(s)
                        if category == 'AGENT':
                            A_seq.append(1)
                        elif category == 'DSE':
                            D_seq.append(1)
                        elif category == 'TARGET':
                            T_seq.append(1)
                    label = line[5].split('-')
                    label = '-'.join(label[0:2])
                    s = []
                    s.extend(line[0:5])
                    s.append(label)
                    s = ' '.join(s)
                    if os.path.exists(write_path):
                        file = open(write_path, "a", encoding='utf-8')
                    else:
                        file = open(write_path, "w", encoding='utf-8')
                    file.write(s)
                    file.write('\n')
                    file.close()
                else:
                    line = ' '.join(line)
                    if os.path.exists(write_path):
                        file = open(write_path, "a", encoding='utf-8')
                    else:
                        file = open(write_path, "w", encoding='utf-8')
                    file.write(line)
                    file.write('\n')
                    file.close()
            elif line == '\n':
                start = id + 1
                # print(rel_list)
                # print(total_digit)
                total_digit = list(set(total_digit))
                # print(total_digit)
                total_digit.sort()
                # print(total_digit)
                digit_num = len(total_digit)
                index_digit = list(range(digit_num))
                total_digit = dict(zip(total_digit, index_digit))
                # category_dict = {'AGENT': 0, 'DSE': 1, 'TARGET': 2}
                # print(total_digit)
                B = []
                b = list(range(2))
                for i in range(digit_num):
                    bb = [[] for e in b]
                    B.append(bb)
                # print(B)
                for e in rel_list:
                    category = e.split('-')[1]
                    ent_digit = int(e.split('-')[0])
                    if category == 'DSE':
                        if B[total_digit[ent_digit]][0] != []:
                            # print('error')
                            # print(id)
                            # print(e)
                            more_dse += 1
                        else:
                            B[total_digit[ent_digit]][0] = int(e.split('-')[2])
                    else:
                        B[total_digit[ent_digit]][1].append(e.split('-')[1:])
                # print(B)
                rel = ['rel']
                # print(B)
                B.sort(key=operator.itemgetter(0))
                # print(B)
                for i in range(len(B)):
                    rel_count += len(B[i][1])
                    line_rel_count = len(B[i][1])
                    a_line_rel_count = 0
                    t_line_rel_count = 0
                    if B[i][0] == []:
                        print('no dse')
                    if B[i][1] == []:
                        entity_error += 1
                        # print('error')
                    for j in range(len(B[i][1])):
                        if B[i][1][j][0] == 'AGENT':
                            a_line_rel_count += 1
                            if int(B[i][1][j][1]) < int(B[i][0]):
                                rel.append(B[i][1][j][1])
                                rel.append(str(B[i][0]))
                                rel.append('1')
                                rel.append('AGENT-DSE')
                            else:
                                rel.append(str(B[i][0]))
                                rel.append(B[i][1][j][1])
                                rel.append('-1')
                                rel.append('AGENT-DSE')
                            rel_a = ' '.join(rel)
                            # print(rel_a)
                            if os.path.exists(write_path):
                                file = open(write_path, "a", encoding='utf-8')
                            else:
                                file = open(write_path, "w", encoding='utf-8')
                            file.write(rel_a)
                            file.write('\n')
                            file.close()
                            rel = ['rel']
                        elif B[i][1][j][0] == 'TARGET':
                            t_line_rel_count += 1
                            # print(rel_list)
                            # print(id)
                            # print(B[i][1][j][1])
                            # print(B[i][0])
                            if int(B[i][1][j][1]) < int(B[i][0]):
                                rel.append(B[i][1][j][1])
                                rel.append(str(B[i][0]))
                                rel.append('1')
                                rel.append('TARGET-DSE')
                            else:
                                rel.append(str(B[i][0]))
                                rel.append(B[i][1][j][1])
                                rel.append('-1')
                                rel.append('TARGET-DSE')
                            rel_t = ' '.join(rel)
                            # print(rel_t)
                            if os.path.exists(write_path):
                                file = open(write_path, "a", encoding='utf-8')
                            else:
                                file = open(write_path, "w", encoding='utf-8')
                            file.write(rel_t)
                            file.write('\n')
                            file.close()
                            rel = ['rel']
                    if line_rel_count != (a_line_rel_count + t_line_rel_count):
                        print('there are errors in line rel count')
                    else:
                        # print(a_line_rel_count)
                        # print(t_line_rel_count)
                        a_rel_count.append(a_line_rel_count)
                        t_rel_count.append(t_line_rel_count)
                rel_list = []
                total_digit = []
                if os.path.exists(write_path):
                    file = open(write_path, "a", encoding='utf-8')
                else:
                    file = open(write_path, "w", encoding='utf-8')
                file.write('\n')
                file.close()
    print(rel_count)
    print(more_dse)
    print(entity_error)
    print(count)
    print(sen_c)
    print(entity_rel_count)
    print(a_rel_count)
    print(t_rel_count)

    # print(A_seq)
    # print(D_seq)
    # print(T_seq)
    return A_seq, D_seq, T_seq

ILP_path = './MPQA_processed_dataset_new/all_ILP_modify.txt'
# sen_path = './MPQA_processed_dataset_new/sentenceid.txt'
rel_path = './all_ILP_bmes_token_rel2.txt'
# words, pos, label = ILP_bmes(ILP_path)

write_path = "./all_ILP_bmes_rel2-test.txt"
write_path2 = "./all_ILP_bmes_token_rel2.txt"
# ILP_bmes(ILP_path, write_path2)
A_seq, D_seq, T_seq = ILP_bmes_rel2(rel_path, write_path)

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









