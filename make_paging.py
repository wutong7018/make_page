"""
要求：运行程序，先将内容读到内存中，用列表储存
    接收用户输入的页码，每页5条，仅输出当页的内容
    最多只能输入3次
"""
with open(file='test_file', mode='r', encoding='utf-8') as f:
    li = f.readlines()
count = 0
while count < 3:
    count += 1
    page = int(input('请输入页码：').strip())
    page_num, remainder = divmod(len(li), 5)
    if page > page_num+1:
        print('页码超过实际页码')
    elif page <= 0:
        print('页码不为能为o或负数')
    elif 0 < page <= page_num:
        for i in range(5):
            print(li[(page-1)*5+i].strip())
    elif page == page_num+1 and remainder != 0:
        for i in range(remainder):
            print(li[(page-1)*5+i], end='')

