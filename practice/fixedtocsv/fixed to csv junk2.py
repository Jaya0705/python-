import csv
li=[]
ff= open('rawdata.prn', 'r') 
cf= open('output.csv', 'w')
writer = csv.writer(cf)
line = ff.readlines()
while line:
    x = line
    chunks, chunk_size = len(x), int(len(x) / 1)
    if line!= 0:
            i = [x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
            s = str(i)
            li.append(i)
            print i
            print s
            print li
            '''
            Employeeid, EmpName, Gender, Empmobileno, OnBoadDate,= s[2:13], s[13:38], s[38:45],s[45:58],s[58:71]
            Rollindate, Rolloffdate, Employeeaddress, Employeeemail=s[71:84],s[84:97],s[97:117],s[117:147]
            Employeedob,Deptid, DeptName, Deptdesc, Projectid=s[147:160],s[160:170],s[170:190],s[190:210],s[210:220]
            ProjectName,ProjectDescription, Projectlocation, Projeffdate=s[220:231],s[231:251],s[251:271],s[271:284]
            Projenddate, salaryid, salarydate, salaryamt,Bonus=s[284:297],s[297:307],s[307:320],s[320:330],s[330:338]
            Designationid,DesignationName,Designationdescription=s[338:353],s[353:373],s[373:395]
            ei, en, g,eno = Employeeid.strip(), EmpName.strip(),Gender.strip(),Empmobileno.strip()
            obd,rid , rod, ea = OnBoadDate.strip(), Rollindate.strip(),Rolloffdate.strip(),Employeeaddress.strip()
            ee ,ed , di,dn = Employeeemail.strip(),Employeedob.strip(),Deptid.strip(), DeptName.strip()
            dd, pi,pn, pd,pl = Deptdesc.strip(),Projectid.strip(),ProjectName.strip(),ProjectDescription.strip(),Projectlocation.strip()
            pefd,ped,si,sd,sa,b = Projeffdate.strip(),Projenddate.strip(),salaryid.strip(), salarydate.strip(), salaryamt.strip(),Bonus.strip()
            di,dn,dd=Designationid.strip(), DesignationName.strip(), Designationdescription.strip()
            writer.writerow(ei)
            writer.writerow(en)
            writer.writerow(g)
            writer.writerow(eno)
            writer.writerow(obd)
            writer.writerow(rid)
            writer.writerow(rod)
            writer.writerow(ea)
            writer.writerow(ee)
            writer.writerow(ed)
            writer.writerow(di)
            writer.writerow(dn)
            writer.writerow(dd)
            writer.writerow(pi)
            writer.writerow(pn)
            writer.writerow(pd)
            writer.writerow(pl)
            writer.writerow(pefd)
            writer.writerow(ped)
            writer.writerow(si)
            writer.writerow(sd)
            writer.writerow(sa)
            writer.writerow(b)
            writer.writerow(di)
            writer.writerow(dn)
            writer.writerow(dd)'''
ff.close()
cf.close()
