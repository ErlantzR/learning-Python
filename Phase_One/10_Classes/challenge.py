class Reminder:
  def __init__(self, name):
    self.name = name
  
  def remind_me_to(self, task):
    self.task = task

  def remind(self):
    return f"{self.name}! {self.task}!"

  
reminder = Reminder("Kay")

reminder.remind_me_to("Walk the dog")

print(reminder.remind())
# Should print: "Kay! Walk the dog!"