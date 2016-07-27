#Implicit Inheritance
'''class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
  #pass allows code to run by adding an empty block. without pass here code result in an error
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
'''
#Inheritance override Explicitly
'''
class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

'''
#Inheritance Alter Before or After
'''
class Parent(object):

    def altered(self):
      print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
'''
#three versions of Inheritance
#creates parent
class Parent(object):
#function to print override
  def override(self):
    print "PARENT override()"

  def implicit(self):
    print "PARENT implicit()"

  def altered(self):
    print "PARENT altered()"
#Overrides Parent
class Child(Parent):
#overides the overide function form Parent Class
  def override(self):
    print "CHILD override()"


  def altered(self):
    print "CHILD, BEFORE PARENT altered()"
    super(Child, self).altered()
    print "CHILD, AFTER PARENT altered()"

#sets variables
dad = Parent()
son = Child()
#function calls
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
