def generate(upto):
  final_sentence = '1, '
  if upto == 1:
    return "1"
  else:
    for number in range(2, upto + 1):
      if number % 15 == 0:
        final_sentence = f"{final_sentence}FizzBuzz, "
      elif number % 3 == 0:
        final_sentence = f"{final_sentence}Fizz, "
      elif number % 5 == 0:
        final_sentence = f"{final_sentence}Buzz, "
      else:
        final_sentence = f"{final_sentence}{number}, "
  
  return final_sentence[:-2]