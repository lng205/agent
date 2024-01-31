from openai import OpenAI
client = OpenAI()

def chat(user_message):
    completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[{"role": "user", "content": user_message}])

    print(completion)

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

chat(message)