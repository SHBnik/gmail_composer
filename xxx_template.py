class template:
    def __init__(self):
        raise NameError('edit xxx_template.py file')   # delete or comment this line after you edited this file
        self._cv_file_name = 'address to your pdf cv file'
        self._my_template_subject = []
        self._my_template_body = []



        ####                       for first sheet                      ####
        self._my_template_subject.append('first subject')
        self._my_template_body.append(
            '''
Dear Professor {pn},

<I found your paper “ {rp} ” intresting>

# this is my email for second sheet.

            ''')
        ####                               end                           ####


        ###                        for second sheet                      ####
#        self._my_template_subject.append('second subject')
#         self._my_template_body.append(
#             '''
# Dear Professor {pn},
        
# this is my email for second sheet.
#             ''')
        ####                               end                           ####


        ###                         for more sheets                      ####
        '''
            .   maybe
            .       some
            .           more
        '''
        ####                               end                           ####
    
    
    def my_template_body(self,prof_name,paper_name,index):
        if len(self._my_template_body) > 1:
            temp = self._my_template_body[index].replace('{pn}',prof_name)
            if paper_name != '': temp = temp.replace('{rp}',paper_name)
            else : 
                firstDelPos=temp.find("<") 
                secondDelPos=temp.find(">") 
                temp = temp.replace(temp[firstDelPos:secondDelPos+1], '')  
        else:
            temp = self._my_template_body[0].replace('{pn}',prof_name)
            if paper_name != '':
                temp = temp.replace('<','')
                temp = temp.replace('>','') 
                temp = temp.replace('{rp}',paper_name)  
            else : 
                firstDelPos=temp.find("<") 
                secondDelPos=temp.find(">") 
                temp = temp.replace(temp[firstDelPos:secondDelPos+1], '')
        return temp


    
    def my_template_subject(self,index):
        if len(self._my_template_subject) > 1:
            return self._my_template_subject[index]
        else : 
            return self._my_template_subject[0]

    
    
    
    def cv_file_name(self):
        return self._cv_file_name


