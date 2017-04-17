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
s_lily=""

with open("testtab2.txt","r") as o_file:
    while True:
        s_line = o_file.readline()
        if not s_line: break
        i += 1
        print 'Parsing line ',i

        m = re.match('^e--.*$',s_line)
        if m:
            print "e found - read all strings"
            s_lily = "\n"
#todo: leerzeichen rausschmeissen
            s_e = m.string
            s_b = o_file.readline()
            s_g = o_file.readline()
            s_d = o_file.readline()
            s_A = o_file.readline()
            s_E = o_file.readline()

            j=0
            c=0
            zwei=0;
            # Eine Spalte durchgehen
            # beachte, dass es auch 2-Stellige Tabs geben kann
            # ja, es ist bekannt, der code ist quick and DIRTY
            while(j<len(s_e)):
                if(re.match('\d',s_e[j])):
                    if(re.match('\d',s_e[j+1])):
                        s_tmp = s_tmp + " " + a_eis[int(s_e[j]+s_e[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_eis[int(s_e[j])]
                        c=c+1
                if(re.match('\d',s_b[j])):
                    if(re.match('\d',s_b[j+1])):
                        s_tmp = s_tmp + " " + a_bis[int(s_b[j]+s_b[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_bis[int(s_b[j])]
                if(re.match('\d',s_g[j])):
                    if(re.match('\d',s_g[j+1])):
                        s_tmp = s_tmp + " " + a_gis[int(s_g[j]+s_g[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_gis[int(s_g[j])]
                if(re.match('\d',s_d[j])):
                    if(re.match('\d',s_d[j+1])):
                        s_tmp = s_tmp + " " + a_dis[int(s_d[j]+s_d[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_dis[int(s_d[j])]
                if(re.match('\d',s_A[j])):
                    if(re.match('\d',s_A[j+1])):
                        s_tmp = s_tmp + " " + " " + a_Ais[int(s_A[j]+s_A[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_Ais[int(s_A[j])]
                if(re.match('\d',s_E[j])):
                    if(re.match('\d',s_E[j+1])):
                        s_tmp = s_tmp + " " + a_Eis[int(s_E[j]+s_E[j+1])]
                        zwei=1
                        c=c+1
                    else:
                        s_tmp = s_tmp + " " + a_Eis[int(s_E[j])]

                # Mehr als eine Note in der Spalte -> "< note note .. >"
                if(c>1):
                    s_tmp = '<' + s_tmp + '>'
                s_lily = s_lily + " " + s_tmp
                s_tmp=""
                if zwei==1: # es wurde eine zweistellige zahl eingelesen
                    j=j+2 
                else: 
                    j=j+1
                zwei = 0
                c = 0
            print s_lily

o_file.close()



