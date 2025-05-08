'''1.student_marks.csv contains the marks and other details for some students. Write a python program to:

Open the file in read mode
Create a dictionary from the given data
Add a new field to the dictionary total\_marks and store the total marks of the students.
Add a new field to the dictionary Average and store the average marks of the students.
Create a new file and write this information to the new file
'''



d = {}
with open("D:/CODE_BASICS/1.python/b.File_handling/student_marks.csv","r") as f:
    for line in f:
        name,Gender,dob,maths,physics,chemistry,english,biology,economics,history,civics = line.split(",")
        for i in name.split():
            clean = i.strip()  # Remove spaces from each word (though split already removes extra spaces)
            

             
         
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     maths = int(maths)
    #     print(type(maths))
        
    # #     if name in d:
    # #         pass
    # #     else:
    # #         d[name] = [maths,physics,chemistry,english,biology,economics,history,civics]
    # # print(d)
            
 
        
        