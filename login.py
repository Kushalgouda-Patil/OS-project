def main():
    try:
        with open(file='login.txt',mode='w') as fp:
            usn=input('Enter USN')
            dob=input('Enter Date of birth in format "dd/mm/yyyy"')
            dict1={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
                '07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
            dob=dob.split('/')
            dob[1]=dict1[str(dob[1])]
            fp.write(usn+'\n')
            fp.write(dob[0]+'\n')
            fp.write(dob[1]+'\n')
            fp.write(dob[2])
        print("Successfully initialized login credentials")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You do not have permission to write to this file.")
    except IOError:
        print("An error occurred while writing to the file.")

if __name__=='__main__':
    main()



