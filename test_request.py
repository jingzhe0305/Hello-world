from pyfaq import FAQModel
import jieba
import pytest


jieba.setLogLevel(20)

@pytest.mark.api
def test_get_answer():
    querys = ['打印机', '子女报销范围/材料']

    model = FAQModel("knowledge")

    for index, query in enumerate(querys):
        print(index, query)
        result = model.get_answer(query)
        print("dict", (result))