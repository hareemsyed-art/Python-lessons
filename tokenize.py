def tokenize(sentence):
    return sentence.lower().split()
tokenize("My name is Hareem.")
def bleu(predicted, actual):
    predicted_sentence = tokenize(predicted)
    actual_sentence = tokenize(actual)
    count = 0
    for i in predicted_sentence:
        if i in actual_sentence:
            count = count + 1
    a = len(predicted_sentence)
    bleu_score = count / a
    return bleu_score
print(bleu("My Hareem.", "My name is Hareem Syed."))
def rouge(actual, predicted):
    predicted_sentence = tokenize(predicted)
    actual_sentence = tokenize(actual)
    count = 0
    for i in actual_sentence:
        if i in predicted_sentence:
            count = count + 1
    a = len(actual_sentence)
    rouge_score = count / a
    return rouge_score
print(rouge("My cat Hareem.", "My name is Hareem Syed."))