Thisset = {"Vishal", "Rohan", "Prajyot", "Aakash", "Faroof"}
Thatset = {"Rohan", 17, 34, "Maruf", "Yondu", "Aakash"}

"""Set is the various collection of elements. other than being a collection, the elements inside it varies in position.
 simply they do not have a fixed index and position. pop function could be a risky one as you won't come to know which 
 element will be removed"""

Thisset.add()  # adds element to sets
Thisset.pop()  # removes last item from set.
Thisset.copy()  # copies whole set.
Thisset.clear()  # clears whole set.
Thisset.remove()  # removes specified elements.
Thisset.discard()  # discards element
Thisset.update()  # Thisset will be updated by the set mentioned in the brackets

Thisset.union()  # It will add the elements of specified set. It will ignore the same elements and will print only
# once. You will require a separate variable for it.Ex:- Thisset1 = Thisset.union(Thatset).
# You can union three sets together.


Thisset.intersection()  # It will pick common elements from both sets and add them into one set.
# You will require a separate variable for it.Ex:- Thisset1 = Thisset.intersection(Thatset).
# You can use intersection of three sets.

Thisset.difference()  # It returns the un-common values between two sets.# Ex:- T1=Thisset.difference(Thatset)
Thisset.difference_update()  # It excludes the common elements and displays a set of un-common elements between two set.
Thisset.intersection_update()  # It works similar as intersection.
Thisset.isdisjoint()  # tells whether two sets are intersecting or not.
Thisset.issubset()  # returns boolean values. Tells whether Thisset is a subset of thatset. If Thaset contains same
                    # elements as Thisset then it is true otherwise returns false.
Thisset.issuperset()  # Tells whether Thisset is a superset of Thatset. If Thisset contains same elements like
                      # Thatset then it will return True otherwise false.
Thisset.symmetric_difference()  # returns a set of un-common elements from the two sets. Requires only Sets of two.
Thisset.symmetric_difference_update()  # removes a common elements from the two sets.
