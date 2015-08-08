def istrcmp(str1,str2):
    return str1.lower()==str2.lower()




def main():
    print istrcmp("python",'PYTHON')
    print  istrcmp('LaTeX', 'Latex')
    print istrcmp('a', 'b')


if __name__=='__main__':
    main()
