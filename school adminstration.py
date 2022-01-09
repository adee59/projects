# ___________________SCHOOL ADMINSTRATION_______________________

#1  :  taking Std. info.

import csv

def wic(info_list):
    with open('std_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(['NAME','AGE','CONTACT NO.','E-MAIL ID'])

        writer.writerow(info_list)

if __name__=='__main__':
    cndtn=True
    std_num=1
    while(cndtn):
        std_info=input('Enter the info. for student #{} in the given format (Name Age Contact_No. Email_ID): '.format(std_num))
       

        l1=std_info.split(' ')
        

        print("\nThe entered info. is: \nName: {}\nAge: {}\nContact_No.: {}\nE_mail_ID: {}".format(l1[0], l1[1], l1[2], l1[3]))

        choice_check=input('Is the entered info. corect? (yes/no) ').lower()
        
        if choice_check=='yes':
           wic(l1)

           cndtn_check=input('enter (yes/no) whether you wish to enter the info of another student: ').lower()
           if cndtn_check=='yes':
                cndtn=True
                std_num=std_num+1
           else:
                cndtn=False
        
        else:
            print('ALERT:Please re-enter the details!')
