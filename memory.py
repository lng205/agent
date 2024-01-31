import openai, chromadb

API_KEY = "YOUR_API_KEY"

# Text colors
MAGENTA = "\033[35m" # Magenta color
RESET = "\033[0m"  # Reset to default color

client = openai.OpenAI(api_key=API_KEY)
chroma_client = chromadb.PersistentClient(path="memory")
openai_ef = chromadb.utils.embedding_functions.OpenAIEmbeddingFunction(api_key=API_KEY, model_name="text-embedding-3-large")


def main():
    agent = Agent()
    agent.chat()

    # print(agent.collection.peek())# get first 5 items from a collection


class Agent():
    def __init__(self, name="HAL") -> None:
        self.name = name
        self.collection = chroma_client.get_or_create_collection(name=f"{name}_memory", embedding_function=openai_ef)
        self.memory_num = 0


    def memorize(self, messages) -> None:
        """Ask model to summarize messages and add the response to vector database"""
        completion = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[{"role": "user", "content": f"请用简短的语句总结这段对话的要点: {messages}"}])
        self.collection.add(documents=[completion.choices[0].message.content], ids=[str(self.memory_num)])
        self.memory_num += 1


    def recall(self, query) -> dict:
        """Query the vector database"""
        results = self.collection.query(query_texts=[query], n_results=3)
        return results


    def chat(self) -> None:
        """Start a chat with the agent"""
        messages = [{"role": "system", 
                     "content": f"你是一个小型AI桌面机器人，名字是{self.name}。你有一个记忆数据库，消息的末尾会用“记忆：”的格式附上检索到的相关记忆列表"}]
        print(MAGENTA + "开始" + RESET)
        while(True):
            # get user message
            user_message = input()

            # end the chat
            if user_message == "结束":
                break

            # add query
            user_message = user_message + "记忆：" + str(self.recall(user_message)["documents"])
            messages.append({"role": "user", "content": user_message})

            # get response
            completion = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=messages)
            messages.append({"role": "assistant", "content": completion.choices[0].message.content})

            # print response
            print(MAGENTA + messages[-1]["content"] + RESET)

        self.memorize(messages)


    def forget(self, ids) -> None:
        """Delete a document from the vector database"""
        self.collection.delete(ids=ids)


if __name__ == "__main__":
    main()