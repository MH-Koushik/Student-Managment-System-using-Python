import sys
import os


Student_Name=[]
Student_ID=[]
Student_Batch=[]
Student_Dep=[]
Student_sem=[]
student_info=[]
student_exist=[]

class std_info:
    def admin_panel():
        admin_name= str(input("Enter Admin User Name:"))
        admin_pass= input("Enter Admin Password:")
        
        with open('admin.txt','r') as file:
            for line in file.readlines():
                user_Name,user_pass=line.split('|')
                if admin_name.lower().strip() == user_Name.lower().strip() and admin_pass.strip() == user_pass.strip():
                    print("\n\t\t' ********** WELCOME TO Admin panel ********** ' \n")
                    print("\t\t' Press 1 - Add new Student' \n")
                    print("\t\t' Press 2 - View All Student Information' \n")
                    print("\t\t' Press 3 - Update Student Information' \n")
                    print("\t\t' Press 4 - Remove Student Information' \n")
                    print("\t\t' Press 5 - Home Menu' \n")
                    admin_Input= int(input("Enter a Number to chose an Option: "))
                    if admin_Input==1:
                        std_name=input("Enter Student Name: ")
                        std_id=input("Enter Student ID: ")
                        std_batch=input("Enter Student Batch: ")
                        std_dep=input("Enter Student Department: ")
                        std_sem=input("Enter Student Semester: ")
                        student_add=std_name.strip().upper()+"|"+str(std_id.strip())+"|"+std_batch.strip().upper()+"|"+std_dep.strip().upper()+"|"+str(std_sem.strip())
                        with open('std_info.txt','a') as file2:
                            file2.write(student_add + "\n")
                            
                        print("\t\t\t\t!!!-----Student Info Added!----!!!\n\n")
                        break
                    
                    elif admin_Input==2:
                        print()
                        with open('std_info.txt','r') as file3:
                            for line in file3.readlines():
                                if len(line)>1:
                                    s_name,s_id,s_batch,s_dep,s_sem=line.split('|')
                                    print("Name: "+s_name+ " ID: "+s_id+ " Batch: "+s_batch+ " Department: "+s_dep+ " Semester: "+s_sem)
                        u_input=input("Back to Home Menu? (y/n)")
                        if u_input.strip().lower()=='y':
                            break
                        else:
                            exit()
                            
                    
                    elif admin_Input==3:
                        Student_Name.clear()
                        Student_ID.clear()
                        Student_Batch.clear()
                        Student_Dep.clear()
                        Student_sem.clear()
                        with open('std_info.txt','r') as file4:
                          for line in file4.readlines():
                              if len(line)>1:
                                s_name,s_id,s_batch,s_dep,s_sem=line.split('|')
                                Student_Name.append(s_name)
                                Student_ID.append(s_id)
                                Student_Batch.append(s_batch)
                                Student_Dep.append(s_dep)
                                Student_sem.append(s_sem)
                                
                        print("\n\t\t----Update Information----")
                        print("\t\tPress 1- Update Name ")
                        print("\t\tPress 2- Update ID ")
                        print("\t\tPress 3- Update Batch ")
                        print("\t\tPress 4- Update Departmen ")
                        print("\t\tPress 5- Update Semester\n")
                        ad_input=int(input("Enter a Numeber to select Option: "))
                        
                        if ad_input==1:
                            stdID=input("Enter Student ID: ")
                            try:
                                id_index=Student_ID.index(str(stdID.strip()))
                            except ValueError:
                                    print("\t\t\t!!!---Student is not on the List.---!!!\n")
                                    break
                            new_Name=str(input("Enter New Name: "))
                            Student_Name[id_index]=new_Name.strip().upper()
                            with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+ "\n")
                                    print("\t\t\t!!!---NAME Updated Succesfully.---!!!\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                            
                            
                        elif ad_input==2:
                            old_id=input("Enter Previous ID: ")
                            try:
                                id_index=Student_ID.index(str(old_id.strip()))
                            except ValueError:
                                    print("\t\t\t!!!---Student ID does not Match---!!!\n")
                                    break
                            new_id=input("Enter New ID: ")
                            Student_ID[id_index]=str(new_id.strip())
                            with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+"\n")
                                    print("\t\t\t!!!---ID Updated Successfully.---!!!\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                                    
                            
                        elif ad_input==3:
                            stdID=input("Enter Student ID: ")
                            try:
                                id_index=Student_ID.index(str(stdID.strip()))
                            except ValueError:
                                    print("\t\t\t!!!---Student is not on the List.---!!!\n")
                                    break
                            new_batch=input("Enter New Batch: ")
                            Student_Batch[id_index]=str(new_batch.strip())
                            with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+"\n")
                                    print("\t\t\t!!!---Batch Updated Successfully.---!!!\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                                    
                            
                        elif ad_input==4:
                            stdID=input("Enter Student ID: ")
                            try:
                                id_index=Student_ID.index(str(stdID.strip()))
                            except ValueError:
                                    print("\t\t\t!!!---Student is not on the List.---!!!\n")
                                    break
                            new_dep=str(input("Enter New Department: "))
                            Student_Dep[id_index]=new_dep.strip().upper()
                            with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+ "\n")
                                    print("\t\t\t!!!---Department Updated Successfully.---!!!\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                                    
                            
                        elif ad_input==5:
                            stdID=input("Enter Student ID: ")
                            try:
                                id_index=Student_ID.index(str(stdID.strip()))
                            except ValueError:
                                    print("\t\t\t!!!---Student is not on the List.---!!!\n")
                                    break
                            new_sem=str(input("Enter New Semester: "))
                            Student_sem[id_index]=new_sem.strip().upper()
                            with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+ "\n")
                                    print("\t\t\t!!!---Semester Updated Successfully.---!!!\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                                    break
                    
                    elif admin_Input==4:
                        stdID=input("Enter Student ID: ")
                        id_index=int()
                        
                        Student_Name.clear()
                        Student_ID.clear()
                        Student_Batch.clear()
                        Student_Dep.clear()
                        Student_sem.clear()
                        with open('std_info.txt','r') as file4:
                          for line in file4.readlines():
                              if len(line)>1:
                                s_name,s_id,s_batch,s_dep,s_sem=line.split('|')
                                Student_Name.append(s_name)
                                Student_ID.append(s_id)
                                Student_Batch.append(s_batch)
                                Student_Dep.append(s_dep)
                                Student_sem.append(s_sem)
                        
                        try:
                            id_index=Student_ID.index(str(stdID.strip()))
                        except ValueError:
                            print("\t\t\t!!!---Student is not on the List.---!!!\n")
                            break
                        Student_Name.remove(Student_Name[id_index])
                        Student_ID.remove(Student_ID[id_index])
                        Student_Batch.remove(Student_Batch[id_index])
                        Student_Dep.remove(Student_Dep[id_index])
                        Student_sem.remove(Student_sem[id_index])
                        with open('std_info.txt','w+') as file5:
                                if len(Student_Name)==len(Student_ID):
                                    for i in range(0,len(Student_ID)):
                                       file5.write(Student_Name[i]+"|"+Student_ID[i]+"|"+str(Student_Batch[i])+"|"+Student_Dep[i]+"|"+ str(Student_sem[i])+ "\n")
                                else:
                                    print("\t\t\tArray value Missing!")
                                    
                        print("\t\t\t!!!---Student Removed Successfully---!!!\n")     
                                
                    elif admin_Input==5:
                        break
                    
                else:
                    print("\t\t\tUsername or Password did not match.")
                    try_again=input("Try again? (y/n): ")
                    if try_again.strip().lower()=='y':
                        std_info.admin_panel()
                    else:
                        break
                    
                    
    def student_panel():
        id_index=int()
        Student_Name.clear()
        Student_ID.clear()
        Student_Batch.clear()
        Student_Dep.clear()
        Student_sem.clear()
        
        std_ID=input("Enter your ID: ")
        std_ID=str(std_ID.strip())
        
        with open('std_info.txt','r') as file8:
            for line in file8.readlines():
                if len(line)>1:
                    s_name,s_id,s_batch,s_dep,s_sem=line.split('|')
                    Student_Name.append(s_name)
                    Student_ID.append(s_id)
                    Student_Batch.append(s_batch)
                    Student_Dep.append(s_dep)
                    Student_sem.append(s_sem)
        try:
            id_index=Student_ID.index(std_ID)
            print("\t\t\t' ********** STUDENT INFORMATION********** ' \n")
            print("\n\t\t"+"Name: "+Student_Name[id_index]+ " ID: "+Student_ID[id_index]+ " Batch: "+str(Student_Batch[id_index])+ " Department: "+Student_Dep[id_index]+ " Semester: "+ str(Student_sem[id_index])+"\n")  
        except ValueError:
             print("\t\t\t!!!---Student Does not Exist!---!!!\n")
                        

while True:
    print("\t\t' ********** WELCOME TO STUDENT MANAGEMENT SYSTEM ********** ' \n")
    print("\t\t\t\t' Press 1 - Admin' \n")
    print("\t\t\t\t' Press 2 - Student' \n")
    print("\t\t\t\t' Press 3 - Exit the Program' \n")
    user_input=int()
    try:
        user_input=int(input("Enter a Number to Select above option: "))
    except ValueError:
        print("\n\t\t\t!!!!---Please Enter a valid Number to Select Options.---!!!\n")
    if user_input==1:
        std_info.admin_panel()
    elif user_input==2:
        std_info.student_panel()
    elif user_input==3:
        sys.exit()
        
    
        
    