import sys


def add_prefix(line):
    global skip_all
    if skip_after_word:
        if skip_word in line:
            skip_all = True
        if skip_all:
            return line

    if with_parts:
        if line[0:4] == 'Part':
            return line
    if line[0:7] == 'Chapter': # line[0:3] == 'Ch.'
        if with_parts:
            return '\t' + line
        else:
            return line
    # modify this depending on doc
    tab_list = [] # 'References','Exercises'
    for check_word in tab_list:
        # if check_word in line:
        #     return '\t' + line

        # if starts with check_word
        if line[0:len(check_word)] == check_word:
            return '\t' + line

    # if line[0:6] == 'Design' or line[0:3] == 'The':
    #     return '\t\t' + line

    prefix = line.partition(" ")[0]
    depth = prefix.count('.') - depth_offset
    # if no '.' in first "word", then returns line
    # eg Index
    # this also works for appendices, eg A.1
    for i in range(depth):
        line = '\t'+line
    if with_parts:
        return '\t' + line
    else:
        return line

def add_suffix(line):
    global last_page_num

    partition = line.rpartition("p.")
    title = partition[0]
    # remove spacebar before p.
    title = title[:-1]

    page_num = partition[2]
    if page_num == '':
        print('\nERROR: no \'p.\' found in line')
        file1.close()
        sys.exit()
    # int: removes spacebar (if any) and \n
    page_num = int(page_num)
    if last_page_num > page_num:
        print(f'WARNING: last page number {last_page_num} > current page number {page_num}')
        file1.close()
        sys.exit()
    last_page_num = page_num
    # +offset: page num on book to page num in pdf
    page_num = str(page_num+offset)

    return title+'/'+page_num+',Black,notBold,notItalic,closed,FitPage\n'

if __name__ == "__main__":
    """
    Before use:
    0. Change Ch. (actually, Ch itself is not necessary?)
    
    1. Change input_filename
    2. Change with_parts (eg if there is Part 1, Part 2, ...)
       - Style: Part or PART at the beginning of add_prefix
    3. Change offset and possibly offset_list
       - eg ('10 Self-Assembly',32): if '10 Self-Assembly' in line, change offset from initial value to 32
       - if not necessary, leave offset_list = []
    4. Change tab_list in add_prefix() to deal with exceptions (under '# modify this depending on doc')
       - eg Exercises in each chapter should be tabbed but does not by default
       - compare eg A.1 is tabbed once by default
       - eg Index is not tabbed by default because it has no dots
       - if not necessary, check that tab_list is empty
       - if necessary: add if blocks
    5. Change depth_offset (for default behavior: 0; if chapter: XV., depth_offset = 1)
       - note: if depth_offset = 1, then eg Bibliography, depth = -1, but still works (no tabs)
    6. Toggle skip_after_word, and if true, change skip_word
       - Stops tabbing after skip_word (return line as is)
       
    Default behavior: not dots = no tab
    Gives warning if page number decreases from entry to entry
    
    Copy and edit for special cases
    
    """

    input_filename = 'nmr'
    file1 = open(input_filename+'_prepos.txt', 'r', encoding="utf8")
    Lines = file1.readlines()
    Lines_write = []

    with_parts = False

    # actual page in pdf - printed page number
    offset = 26
    offset_list = []
    # offset_list = [('10 Self-Assembly',32),
    #                ('12 Biological Mimics and',31),
    #                ('13 Interfaces and Liquid',30),
    #                ('14 Supramolecular Polymers, Gels',29),
    #                ('15 Nanochemistry',28)]

    depth_offset = 1

    skip_after_word = True
    skip_word = 'Preface'

    # Settings over
    skip_all = False
    last_page_num = -1
    for i, line in enumerate(Lines):
        print(repr(line))
        if line == '\n':
            print('NO LINE')
        else:
            for (switch_prompt,new_offset) in offset_list:
                if switch_prompt in line:
                    offset = new_offset

            newline = add_prefix(line=line)
            newline = add_suffix(line=newline)
            print(repr(newline))
            Lines_write.append(newline)

    file1.close()

    file2 = open(input_filename+'_prepos_FORMATTED.txt', 'w', encoding="utf8")
    file2.writelines(Lines_write)
    file2.close()

    sys.exit()




# cases: can go up any level, but can only go down one level
# ch to next ch
# ch to next sec
# sec to next ch
# sec to next sec
# sec to next subsec
# subsec to next ch
# subsec to next sec
# subsec to next subsec

# as far as structure of prefix is concerned, only depth2 matters
# ch to next ch
# sec to next ch
# subsec to next ch
# ch to next sec
# sec to next sec
# subsec to next sec
# sec to next subsec
# subsec to next subsec




# for i,line in enumerate(Lines):
#     old_depth = depth
#     print(line,line[0])
#     if line[0] == '\t':
#         if line[1] == '\t':
#             print('2 tabs')
#         else:
#             print('1 tab')
#     else:
#         depth = 1
#
#     Lines2[i] = '\t'+Lines2[i]
#
# print(type(Lines))

# if i == 21:
#     print(line)
#     print(line == '\tBibliographical and Historical Notes')
#     sys.exit()
