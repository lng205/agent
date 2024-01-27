import chromadb, os
chroma_client = chromadb.PersistentClient(path="database_ZH_lg")
# chroma_client = chromadb.PersistentClient(path="database_ZH")

# Embedding function
openai_ef = chromadb.utils.embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.environ["OPENAI_API_KEY"],
                model_name="text-embedding-3-large"
            )

def create_collection():
    collection = chroma_client.create_collection(name="memory", embedding_function=openai_ef)
    collection.add(
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
            ],
        ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15"]
    )

# create_collection()
collection = chroma_client.get_collection(name="memory", embedding_function=openai_ef)
results = collection.query(
    query_texts=["主人会想要乌龙还是拿铁？"],
    n_results=3
)

print(results)
