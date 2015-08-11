def my_sum(list1):
    new=''
    for item in list1:
        new+=item
    return new
          




def main():
    print my_sum(['hello','world'])
    print  my_sum(["aa", "bb", "cc"])
    



if __name__=='__main__':
    main()
