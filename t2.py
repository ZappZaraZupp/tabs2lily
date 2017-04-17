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
# es muss immer ein zeichen zwischen den tabs(=nummer) sein ueber alle Zeilen

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


i=0
s_tmp=""

with open("testtab.txt","r") as o_file:
    while True:
        s_line = o_file.readline()
        if not s_line: break
        i += 1
        print 'Parsing line ',i,':\n',s_line

        m = re.match(r'^e--.*$',s_line)
        if m:
            print "e-- found"
#todo: leerzeichen rausschmeissen
            s_e = m.string
            s_b = o_file.readline()
            s_g = o_file.readline()
            s_d = o_file.readline()
            s_A = o_file.readline()
            s_E = o_file.readline()

            # vorbereiten fuer split
            s_e = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_e) # einstellig -> zweistellig
            s_b = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_b) # einstellig -> zweistellig
            s_g = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_g) # einstellig -> zweistellig
            s_d = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_d) # einstellig -> zweistellig
            s_A = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_A) # einstellig -> zweistellig
            s_E = re.sub(r'([^0-9])([0-9])[^0-9]',r'.\1\2',s_E) # einstellig -> zweistellig
            print s_e
            print s_b
            print s_g
            print s_d
            print s_A
            print s_E
            a_e = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_e)).split()
            a_b = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_b)).split()
            a_g = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_g)).split()
            a_d = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_d)).split()
            a_A = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_A)).split()
            a_E = re.sub(r'([0-9]{2})',r'\1 ',re.sub(r'([^0-9])',r'\1 ',s_E)).split()
            
            print len(a_e),' ',len(a_b),' ',len(a_g),' ',len(a_d),' ',len(a_A),' ',len(a_E),' '

o_file.close()


