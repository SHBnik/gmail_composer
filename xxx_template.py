class template:
    def __init__(self):
        # raise NameError('edit xxx_template.py file')   # delete or comment this line after you edited this file
        self._cv_file_name = 'ShahabNikkhoo_CV.pdf'
        self._my_template_subject = []
        self._my_template_body = []



        ####                       for first sheet                      ####
        self._my_template_subject.append('Looking for Ph.D. position in Robotics')
        self._my_template_body.append(
            '''
Dear Professor {pn},
 
I am Shahab Nikkhoo, a senior undergraduate student of Electrical Engineering at the University of Tehran.
I'm interested in robotics,  Autonomous Systems, Embedded Systems, and human-robot interaction.
I started working in the Advanced Robotics Laboratory at the University of Tehran in 2018. I worked in a team to make robots and toys for teaching skills to children with Autism Spectrum Disorder and analyze their behavior with different learning algorithms.
 
<I found your paper “ {rp} ” pretty exciting and close to my interests.>
 
Currently, I am working on the "Humanoid robot for children education and entertainment ” as my B.Sc. project under the supervision of Dr. Hadi Moradi. I am also writing a research paper on the comprehensive autism screening system. 
 
The similarity between your works and my research interests encouraged me to contact you to receive the chance of being your student.
 
Please find my CV attached to this email.
 
I believe I have the necessary skills to warrant my success and productivity as an M.Sc or Ph.D. student in your lab. I hope to receive your email with good news and join your research team.
 
Sincerely yours,
Shahab Nikkhoo
 
Research Assistant at Advanced Robotics and Artificial Intelligence Lab, Electrical and Computer Engineering Department, University of Tehran, Tehran, Iran.
            ''')
        ####                               end                           ####


        ###                        for second sheet                      ####
        self._my_template_subject.append('Looking for M.Sc position in Robotics')
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


