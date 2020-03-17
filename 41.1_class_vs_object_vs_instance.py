'''
1. Class vs Object vs Instance.

Explaining with example:

  Suppose you are god and you are given the task to make a new species called males. so you start designing your species. All the males will have hands, legs, eyes,
  nose, etc. These features/state can be called as attributes/properties. All males can run, walk, talk, etc. These are the behaviors/ functions of males and can be
  called as Methods.
  Once you have designed the properties and behaviors of your new species, your class is ready. So class is a design or a blueprint that how the males will look and behave.

  Now, Males doesn't exist in reality they are just a concept.
  Now God started making Males in reality, so he looked at a blueprint and created a male. When he created a male that male needs a space to live, so  a space is reserved for
  that male to live.
  Here the act of making a male is creating objects from the class. The act of giving the space to male is creating a memory fot he object.
  Now, there is a problem with a god, he can create n number of males all identical and give them space on earth to live but how can you identify and differentiate them.
  What if the God wants one of the male to do something. How will he command?
  Here comes the concept of instances. He took one of the males and gave him a name let y1, so now the object(male) has a reference called y1. the location given to him
  to live can be said as y1's location.

  Objects is a generic(common) term, it is physically present but remains undifferentiated. Instance is something that gives them a separate identity.
  For example: you are asking for a soap(this is a object) but you are asking for lux soap(this is the instance of the object). One object can have many instances.

  In coding:
  We have class Males:
  we create objects like
  y1 = Males(...)

  Here, when you write Males(...), an object is created.
  Males(...) #here another object is created.
  Males(...)# another object is created.
  Here both the above males object have different location in the memory, like if you print id of both them you will get different id's.

  Now, when you give name to the object like y2 = Male(...), the name(y1) which refers to the object is called an instance to that object.

  Definition:
  1. Class: This a blueprint for creating objects which consists of attributes(variables) and behavior(methods) the objects should have.
  2. Object : Objects are created by class which have behavior and attributes, it is a generic term which is physically present but is undifferentiated.
  3. Instance: An instance is a specific representation of any object, it is a single object that has been created in memory. An object may be varied in number of ways and
               each realized variation of that object is an instance.
               The process of creating instance is an instantiation.
   A class can have multiple objects and then multiple instances of each of those objects.

   Example: class Car: # here Car is a class
            Car() # This is an object
            y = Car() # Here y is called instance of the class which represents one of the object of the class.

'''

'''
2. Why Object are called Instance of the class?
'''
'''
Objects are created by the class that is going to represent the class in the real world, so object is an example of class.
That's why objects are called instance of the class.
'''
