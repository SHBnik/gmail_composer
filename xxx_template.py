class template:
    def __init__(self):
        raise NameError('edit xxx_template.py file')   # delete or comment this line after you edited this file
        self._cv_file_name = 'my cv name.pdf'
        self._my_template_subject = []
        self._my_template_body = []



        ####                       for first sheet                      ####
        self._my_template_subject.append('my email subject for first sheet')
        self._my_template_body.append(
            '''
Dear Professor {pn},
        
this is my email for first sheet.
            ''')
        ####                               end                           ####


        ###                        for second sheet                      ####
#         self._my_template_subject.append('my email subject for second sheet')
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
    
    
    def my_template_body(self,prof_name,index):
        if len(self._my_template_body) > 1:
            return self._my_template_body[index].replace('{pn}',prof_name)
        else:
            return self._my_template_body[0].replace('{pn}',prof_name)


    
    def my_template_subject(self,index):
        if len(self._my_template_subject) > 1:
            return self._my_template_subject[index]
        else : 
            return self._my_template_subject[0]

    
    
    
    def cv_file_name(self):
        return self._cv_file_name


