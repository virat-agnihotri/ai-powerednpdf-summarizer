import sys
print(sys.executable)
from sentence_transformers import SentenceTransformer,util
model=SentenceTransformer('all-MiniLM-L6-v2')

# # sentences=['this is framework generaes embeddings for each input sentence','Senetences are passed as a list of string.']
# # embeddings=model.encode(sentences)
# # for sentence,embedding in zip(sentences,embeddings):
# #     print("sentence:",sentence)
# #     print("embedding:",embedding)
# #     print("")

emb1=model.encode("i am eating apple")
emb2=model.encode("i am eating apples")
emb2=model.encode("i am eating appless")
cos_sim=util.cos_sim(emb1,emb2)
print("cosine similarity:",cos_sim)

                  
# import time

# start = time.time()

# from sentence_transformers import SentenceTransformer
# print("Import:", time.time() - start)

# start = time.time()

# model = SentenceTransformer("all-MiniLM-L6-v2")
# print("Model Load:", time.time() - start)

# start = time.time()

# print(model.max_seq_length)
# print("Print:", time.time() - start)