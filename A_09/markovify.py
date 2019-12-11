import markovify


with open("beowulf.txt", errors ="ignore") as f:
    text_a = f.read()

with open("metamorphosis.txt", errors="ignore") as g:
    text_b = g.read()


model_a = markovify.Text(text_a)
model_b = markovify.Text(text_b)

model_combo = markovify.combine([ model_a, model_b ], [ .5, .5 ])


for i in range(5):
    print(model_combo.make_sentence())

print ("\n")


for i in range(3):
    print(model_combo.make_short_sentence(280))


