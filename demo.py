from pyfaq import FAQModel
import json
import jieba


jieba.setLogLevel(20)


def main():
    querys = [
        'nihao',
        '你好！',
        '“银联二维码活动”是什么',
        '怎么领文具',
        '如何查奖金',
        '如何查年假',
        '去哪吸烟',
        '吸烟',
        "我爱背景天安门",
        'woaibeijing'
    ]
    #querys = ['怎么领用文具ne', "怎么领文具"]
    #querys = ["去哪抽烟呢文具", '怎么领用文具ne', "怎么领文具"]

    querys = ["请假", "抽烟请假", "如何报销", "报销补充医疗保险", "你好"]
    querys = ['打印机', '子女报销范围/材料']

    model = FAQModel("knowledge")

    for index, query in enumerate(querys):
        print(index, query)
        result = model.get_answer(query)
        print("dict", (result))
        # print("json", json.dumps(result))

    # print(model.get_std_query(14)["answer"])



if __name__ == '__main__':
    main()
