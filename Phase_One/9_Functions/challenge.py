# function to add 'super' at the beginning of any word
def superify(word):
  return f"super{word}"

print(superify(superify(superify(superify("cat")))))

# should print "supersupersupersupercat"