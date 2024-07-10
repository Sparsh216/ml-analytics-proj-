
def matching_word(sentence1,sentence2):
    words1=sentence1.split(" ")
    words2=sentence2.split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2} ")
            if word1.lower()==word2.lower():
                score=score+1
    return score

n=int(input("How many list of sentences are you want to enter: "))
lis=[str(input("Elements of list: ")) for i in range(n)]

word=input("Enter the word you want to search: ")

scores=[matching_word(word,sent) for sent in lis]
sortedscoreSent=[sentScore for sentScore in sorted(zip(scores,lis),reverse=True)]
# print(sortedscoreSent)
for score,item in sortedscoreSent:
    print(f"\"{item}\"with a score of {score}")





