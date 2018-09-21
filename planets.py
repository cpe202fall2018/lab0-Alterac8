def weight_on_planets():
   earthWeight = float(input("What do you weigh on earth? "))

   print("\nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds." % (earthWeight*0.38, earthWeight*2.34))
   
if __name__ == '__main__':
   weight_on_planets()