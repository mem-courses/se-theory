TRANSLATE_PROMPT = """
这是一道《软件工程》课程的题目，以json的形式给出.
请你将其topic和options翻译成中文，并注意符合json的格式要求.
请直接输出json格式，以{"chapter":为开头,以}为结尾.下面是题目内容:
%s
"""

EXPLAIN_PROMPT = """
我是正在修读《软件工程》课程的学生，这是一道我遇到的客观题，你是我的软件工程专业课老师，熟悉软件工程领域知识，请帮我简单的讲解一下这道题目。
要求：
1.直接开始你的讲解，在解答清晰明了的情况下尽可能简短
2.不需要使用markdown语法添加额外样式
%s
"""

SIMPLIFY_EXPLAIN_PROMPT = """
我是正在修读《软件工程》课程的学生，这是一道我遇到的客观题，你是我的软件工程专业课老师，熟悉软件工程领域知识，已经帮我针对这道题目进行了解析。
请帮我稍微简化解析的表达，但不能修改原解析中提供的任何信息，保留其完整性，只是删除一些无意义的表述。
要求：
1.不需要使用markdown语法添加额外样式
2.因为我已经知道了答案，你不再需要再解析中强调答案是是什么，比如“这个说法是正确的”“这道题选C”“C是正确答案”
3.请直接输出解析内容，不要输出任何额外的前缀后缀，比如“这道题考察的是……”，“本题中……”
4.在意思不变的情况下简化文字表达，但不能删去原解析中的信息，如名词的英文、对概念的解释、对题目的分析，一些举例等等。
<problem>
%s
</problem>
<explanation>
%s
</explanation>
"""