# nummer auf Tab --> lily
# achtung: absoulte oktavbezeichnung
# tabs muessen wie folgt aufgebaut sein:

# e--
# b--
# g--
# d--
# A--
# E--
# d.h. Saite und -- am Begin der Zeile

import re

a_eis = ['e\'',  'f\'','fis\'',  'g\'','gis\'',  'a\'','ais\'',  'b\'',  'c\'\'','cis\'\'',  'd\'\'','dis\'\'',  'e\'\'',  'f\'\'','fis\'\'',  'g\'\'','gis\'\'',  'a\'\'','ais\'\'',  'b\'\'']
a_ees = ['e\'',  'f\'','ges\'',  'g\'', 'as\'',  'a\'','bes\'',  'b\'',  'c\'\'','des\'\'',  'd\'\'', 'es\'\'',  'e\'\'',  'f\'\'','ges\'\'',  'g\'\'', 'as\'\'',  'a\'\'','bes\'\'',  'b\'\'']
a_bis = ['b',  'c\'','cis\'',  'd\'','dis\'',  'e\'',  'f\'','fis\'',  'g\'','gis\'',  'a\'','ais\'',  'b\'',  'c\'\'','cis\'\'',  'd\'\'','dis\'\'',  'e\'\'',  'f\'\'','fis\'\'']
a_bes = ['b',  'c\'','des\'',  'd\'',' es\'',  'e\'',  'f\'','ges\'',  'g\'',' as\'',  'a\'','bes\'',  'b\'',  'c\'\'','des\'\'',  'd\'\'', 'es\'\'',  'e\'\'',  'f\'\'','ges\'\'']
a_gis = ['g','gis',  'a','ais',  'b',  'c\'','cis\'',  'd\'','dis\'',  'e\'',  'f\'','fis\'',  'g\'','gis\'',  'a\'','ais\'',  'b\'',  'c\'\'','cis\'\'',  'd\'\'']
a_ges = ['g',' as',  'a','bes',  'b',  'c\'','des\'',  'd\'', 'es\'',  'e\'',  'f\'','ges\'',  'g\'',' as\'',  'a\'','bes\'',  'b\'',  'c\'\'','des\'\'',  'd\'\'']
a_dis = ['d','dis',  'e',  'f','fis',  'g','gis',  'a','ais',  'b',  'c\'','cis\'',  'd\'','dis\'',  'e\'',  'f\'','fis\'',  'g\'','gis\'',  'a\'']
a_des = ['d',' es',  'e',  'f','ges',  'g',' as',  'a','bes',  'b',  'c\'','des\'',  'd\'', 'es\'',  'e\'',  'f\'','ges\'',  'g\'',' as\'',  'a\'']
a_Ais = ['a,','ais,',  'b,',  'c','cis',  'd','dis',  'e',  'f','fis',  'g','gis',  'a','ais',  'b',  'c\'','cis\'',  'd\'','dis\'',  'e\'']
a_Aes = ['a,','bes,',  'b,',  'c','des',  'd', 'es',  'e',  'f','ges',  'g',' as',  'a','bes',  'b',  'c\'','des\'',  'd\'', 'es\'',  'e\'']
a_Eis = ['e,',  'f,','fis,',  'g,','gis,',  'a,','ais,',  'b,',  'c','cis',  'd','dis',  'e',  'f','fis',  'g','gis',  'a','ais',  'b']
a_Ees = ['e,',  'f,','ges,',  'g,', 'as,',  'a,','bes,',  'b,',  'c','des',  'd', 'es',  'e',  'f','ges',  'g', 'as',  'a','bes',  'b']


o_file = open("testtab.txt","r")
i=0
for s_line in o_file:
    i += 1
    print 'Parsing line ',i,':',s_line

    if(re.match('^e--',s_line)):
        print "e found - read all strings"


o_file.close()


