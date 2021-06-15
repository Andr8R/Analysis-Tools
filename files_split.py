import os

fitqunfiles = open("../fitqun_files_all.txt", "r").read().split('\n')
softfiles = open("../softmax_files_all.txt", "r").read().split('\n')

if len(fitqunfiles)==len(softfiles):
  Length = len(fitqunfiles)
else: print('error length')

lsingle = Length//100

for k in range (1,101):
  filefit = open('fitqun_files_'+str(k)+'.txt', 'w')
  for onefile in fitqunfiles[(k-1)*lsingle : k*lsingle]:
    filefit.write(str(onefile + os.linesep))    
  filefit.close()
  
  filesoft = open('softmax_files_'+str(k)+'.txt', 'w')
  for twofile in softfiles[(k-1)*lsingle : k*lsingle]:
    filesoft.write(str(twofile + os.linesep))
  filesoft.close()
  
    

