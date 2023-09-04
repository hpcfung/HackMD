from PyPDF2 import PdfReader

def is_near(x,y):
    margins = 5
    return abs(x-y) < margins

def visitor_body(text, cm, tm, fontDict, fontSize):
    global is_even
    y = tm[5]
    if text == '  ':
        text = ' '
    x = tm[4]
    if text != '\n' and len(parts) > 3 and 'Chapter' not in parts[-4]:
        if is_even:
            one_tab_x_pos = 158.4
            two_tab_x_pos = 175
        else:
            one_tab_x_pos = 236.4
            two_tab_x_pos = 253
        if is_near(x,one_tab_x_pos):
            text = '_TAB'+ text
        if is_near(x,two_tab_x_pos):
            text = '_TAB_TAB' + text

    parts.append(text)
    print(tm, repr(text)) # debug info

    # if y > 50 and y < 720:
    #     parts.append(text)


def scan_page(page_num):
    page = reader.pages[page_num-1]  # zero based, so page num - 1;
    # print(page.extract_text())

    # print('ORIGINAL EXTRACT')
    # print(page.extract_text(visitor_text=visitor_body))
    global is_even
    if page_num % 2 == 0:
        is_even = True
    else:
        is_even = False
    page.extract_text(visitor_text=visitor_body)

if __name__ == "__main__":
    output_filename = 'per'
    min_page = 12 # actual page num # 12,22
    max_page = 22

    reader = PdfReader("per.pdf")

    parts = []
    is_even = None
    for page_num in range(min_page,max_page+1):
        scan_page(page_num)
    text_body = "".join(parts)

    print('PROCESSED TEXT')
    print(text_body)

    file1 = open(output_filename+'.txt', 'w')
    file1.writelines(text_body)
    file1.close()

# https://pypdf2.readthedocs.io/en/3.0.0/user/extract-text.html

# import PyPDF2
# print(PyPDF2.__version__)
