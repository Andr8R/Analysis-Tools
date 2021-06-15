import numpy as np
import os
import uproot3 as uproot

def convert(numpyfile, outfile):
    softmax = np.load(numpyfile)
    g_array = softmax[:, 0]
    e_array = softmax[:, 1]
    mu_array = softmax[:, 2]

    with uproot.recreate(outfile) as output:
        output['softmax_output'] = uproot.newtree({'prob_gamma': "float32", 'prob_e': "float32", 'prob_mu': "float32"})
        output['softmax_output'].extend({'prob_gamma': g_array, 'prob_e': e_array, 'prob_mu': mu_array})

softfiles = open("softmax_files_5.txt", "w")

count = 0
for file in open('fitqun_files_5.txt', 'r').read().split('\n'):
    fitqunnameloc = file #/home/andriio/scratch/datadir/fhc/1/fitqun/fitqun_nuprism_mpmt_1km_nd9_oaa1.24_1e17POT_b3_3670.root
    idname = file[49:-5]  #_nuprism_mpmt_1km_nd9_oaa1.24_1e17POT_b3_3670
    check_softmax = 'wcsim'+idname+'_softmax.npy'
    check_softmax_loc = './softmax/'+check_softmax
    outloc = './softmax_root/softmax'+idname+'.root'
    #outloc_cedar = '/home/andriio/scratch/datadir/fhc/1/softmax/softmax_root/softmax'+idname+'.root'
    outloc_cedar = '/home/andriio/scratch/datadir/fhc/5/new_softmax/softmax_root/softmax'+idname+'.root'
    if check_softmax in os.listdir('./softmax/'):
        convert(check_softmax_loc, outloc)
        count += 1
        softfiles.write(str(outloc_cedar) + os.linesep)
    else: print(check_softmax)
#    print(count)

    #if count >= 2:
       #break
