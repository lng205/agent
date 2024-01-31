# 记录

使用Chromadb 调用 OpenAI 24年1月25的embedding-3 API 搭建了向量数据库，用于存储和检索向量。Chromadb这类专用的向量数据库提供了用于向量检索的API，可以大大简化向量检索的过程。

- embedding-3提供了small和large两个API，small主打性价比，价格是之前的ada-002的1/5，同时性能还有小幅提升。large则追求最佳性能，数据维数更大，价格为small的10倍左右。

## 测试

让ChatGPT4设计了一些桌面机器人可能拥有的记忆内容，然后调用embedding-3的API进行存储和检索。设计的检索语句刻意避开了原文中的文本。

- 数据：

    ```python
    documents=[
        "The master mentioned preferring coffee over tea in the mornings.",
        "The master expressed a fondness for jazz music last Thursday evening.",
        "The master revealed a dislike for cold weather during a conversation on Wednesday.",
        "The master shared a memorable story about hiking in the mountains during our chat yesterday.",
        "The master stated that the science fiction genre is their favorite for movies.",
        "A new set of green ceramic pots appeared on the kitchen shelf this Monday.",
        "There's a fresh stain on the living room carpet, noticed on Tuesday afternoon.",
        "The master brought in a large, leafy plant for the office corner on the weekend.",
        "Noticed a pile of unread mail accumulating on the hallway table since last Friday.",
        "The wall in the dining area has been repainted to a light lavender shade as of yesterday.",
        "The master seemed particularly cheerful after receiving a phone call on Saturday morning.",
        "The master completed assembling a wooden bookshelf for the study room this Sunday.",
        "The master appeared frustrated with a malfunctioning kitchen appliance during breakfast today.",
        "Observed the master practicing guitar for an upcoming family gathering next weekend.",
        "The master spent the evening organizing old photographs into albums last night."
        ]

    query_texts=["Would master want oolong or latte?"]
    ```

- 结果：

  - 使用small：

  ```bash
  {'ids': [['1', '8', '2']], 'distances': [[0.8805083988283289, 1.2697696663283975, 1.285606081795958]], 'metadatas': [[None, None, None]], 'embeddings': None, 'documents': [['The master mentioned preferring coffee over tea in the mornings.', 'The master brought in a large, leafy plant for the office corner on the weekend.', 'The master expressed a fondness for jazz music last Thursday evening.']], 'uris': None, 'data': None}
  ```

  -使用large：

  ```bash
  {'ids': [['1', '2', '11']], 'distances': [[0.7920336229174424, 1.3228994917417647, 1.3447695342995178]], 'metadatas': [[None, None, None]], 'embeddings': None, 'documents': [['The master mentioned preferring coffee over tea in the mornings.', 'The master expressed a fondness for jazz music last Thursday evening.', 'The master seemed particularly cheerful after receiving a phone call on Saturday morning.']], 'uris': None, 'data': None}```

- 中文数据：

    ```python
    documents=[
        "主人提到他早上更喜欢喝咖啡而不是茶。",
        "主人上周四晚上表达了对爵士音乐的喜爱。",
        "主人在周三的对话中透露他不喜欢寒冷的天气。",
        "主人在昨天的聊天中分享了一次难忘的登山故事。",
        "主人表示，科幻是他最喜欢的电影类型。",
        "这周一厨房的架子上出现了一套新的绿色陶瓷盆。",
        "周二下午注意到客厅的地毯上有一个新的污渍。",
        "周末主人为办公室角落带来了一盆大而叶茂的植物。",
        "自上周五以来，走廊桌上积累了一堆未读的邮件。",
        "昨天，餐厅区域的墙壁被重新粉刷成浅薰衣草色。",
        "主人在周六早上接到一个电话后显得特别开心。",
        "主人这个周日完成了书房里一个木质书架的组装。",
        "今天早餐时，主人对一件故障的厨房用具显得很沮丧。",
        "观察到主人为下周末的家庭聚会练习吉他。",
        "主人昨晚花时间整理旧照片进相册。"
        ]

    query_texts=["主人会想要乌龙还是拿铁？"]
    ```

- 结果：

  - 使用small：

  ```bash
  {'ids': [['3', '2', '14']], 'distances': [[1.3531276181916707, 1.3847153910688852, 1.4065658840586726]], 'metadatas': [[None, None, None]], 'embeddings': None, 'documents': [['主人在周三的对话中透露他不喜欢寒冷的天气。', '主人上周四晚上表达了对爵士音乐的喜爱。', '观察到主人为下周末的家庭聚会练习吉他。']], 'uris': None, 'data': None}
  ```

  - 使用large：
  
  ```bash
  {'ids': [['1', '2', '11']], 'distances': [[1.1334754383728265, 1.3607543985868984, 1.3654447596177433]], 'metadatas': [[None, None, None]], 'embeddings': None, 'documents': [['主人提到他早上更喜欢喝咖啡而不是茶。', '主人上周四晚上表达了对爵士音乐的喜爱。', '主人在周六早上接到一个电话后显得特别开心。']], 'uris': None, 'data': None}
  ```

- 分析：“主人提到他早上更喜欢喝咖啡而不是茶”这条是明确相关的信息，其他信息则与检索内容无明显关联。中文检索需要使用large模型才能找到这条信息。此外，相比small模型，large模型中正确信息和无关信息之间的数据区别更加显著。

  事实上，GPT4的completion模型本身也能够正确给出相关信息的回复：

  ```python
  message = """
  基于这些信息:
  "主人提到他早上更喜欢喝咖啡而不是茶。",
  "主人上周四晚上表达了对爵士音乐的喜爱。",
  "主人在周三的对话中透露他不喜欢寒冷的天气。",
  "主人在昨天的聊天中分享了一次难忘的登山故事。",
  "主人表示，科幻是他最喜欢的电影类型。",
  "这周一厨房的架子上出现了一套新的绿色陶瓷盆。",
  "周二下午注意到客厅的地毯上有一个新的污渍。",
  "周末主人为办公室角落带来了一盆大而叶茂的植物。",
  "自上周五以来，走廊桌上积累了一堆未读的邮件。",
  "昨天，餐厅区域的墙壁被重新粉刷成浅薰衣草色。",
  "主人在周六早上接到一个电话后显得特别开心。",
  "主人这个周日完成了书房里一个木质书架的组装。",
  "今天早餐时，主人对一件故障的厨房用具显得很沮丧。",
  "观察到主人为下周末的家庭聚会练习吉他。",
  "主人昨晚花时间整理旧照片进相册。"

  请问其中哪一条是与下面这条询问最相关的？
  “主人会想要乌龙还是拿铁？”
  """
  ```

  ```bash
  ChatCompletion(id='chatcmpl-8lVwGZ79R6rQtTExRV5RbQ9AahTR9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='最相关的信息是："主人提到他早上更喜欢喝咖啡而不是茶。" 这条信息直接涉及到主人对早上饮料的偏好，因此与选择乌龙茶还是拿铁咖啡最为相关。', role='assistant', function_call=None, tool_calls=None))], created=1706334880, model='gpt-4-0125-preview', object='chat.completion', system_fingerprint='fp_376b7f78b9', usage=CompletionUsage(completion_tokens=83, prompt_tokens=470, total_tokens=553))
  ```

  但embedding成本更低，效率更高。可用于跨对话的，大量且长期的记忆存储和检索，而completion则只能用于单次对话的短期记忆。
