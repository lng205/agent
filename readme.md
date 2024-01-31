# Embeddings

[embeddings 性能测试记录](./chroma_test/log.md)

请在程序内将API_KEY改为自己的API_KEY（也可以使用环境变量）。

- idea：每次回复前都对输入调用一次API会明显增加延迟，降低使用体验，可能要考虑长短期记忆结合的方式短期记忆存储完整文本，长期记忆通过functioncall选择性调用。类比人类在睡觉时将短期记忆整理转化成长期记忆的机制，让Agent也必须睡觉并在此过程中整理记忆。

## Reference

- [OpenAI Embeddings guide](https://platform.openai.com/docs/guides/embeddings)
- [OpenAI Embeddings model](https://platform.openai.com/docs/models/embeddings)
- [Chorma vector database](https://www.trychroma.com/)
- [Using Chroma for Embeddings Search](https://cookbook.openai.com/examples/vector_databases/chroma/using_chroma_for_embeddings_search)
- [paper note](https://lng205.github.io/posts/agent/)
