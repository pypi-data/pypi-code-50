class Corona:
  def __init__(self):
    self.name = "Covid-19"         #seif คือ แทนที่ตัวแปร
    self.how = "ผีน้อยต้องกักตัว"

  def What(self):
    """this is my code """
    print("virus name "+self.name)

  def __str__(self):                             # __str__ จะทำงานเมื่อสั่งแสดงผล class
    return "this is a Corona Class"

  def thainame(self):
    print("โคโรน่า")
    return "โคโรน่า"

#---------------------------------------------

if __name__ == "__main__":
  me = Corona()
  print(help(me.What))
  print(me)
  print(me.name)
  print(me.how)
  me.What()
  print(me.thainame())
  