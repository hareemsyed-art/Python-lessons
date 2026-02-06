def tokenize(sentence):
    return sentence.lower().split()
def bleu_score(reference, predicted):
    reference_sentence = tokenize(reference)
    predicted_sentence = tokenize(predicted)
    count = 0
    for i in predicted_sentence:
        if i in reference_sentence:
            count = count + 1
    a = len(predicted_sentence)
    b = count / a
    print(b)
# bleu_score("The bottle is purple", "The bottle is")

def rouge_score(reference, predicted):
    reference_sentence = tokenize(reference)
    predicted_sentence = tokenize(predicted)
    count = 0
    for i in predicted_sentence:
        if i in reference_sentence:
            count = count + 1
    a = len(reference_sentence)
    b = count / a
    print(b)
#rouge_score("The bottle is purple", "The bottle is")

c = "My name is hareem"
h = input("Enter a sentence: ")
bleu_score(c, h)
rouge_score(c, h)