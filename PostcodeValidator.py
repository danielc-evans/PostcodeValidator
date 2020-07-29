import re

regex = '''([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})$'''
      
def check(Postcode):
  
    if(re.search(regex, Postcode)):  
        print("Valid")  
          
    else:  
        print("Invalid")  
      
   
if __name__ == '__main__' :  
      
    # Enter the Postcode 
    Postcode = input("Enter postcode:")
      
    check(Postcode) 
