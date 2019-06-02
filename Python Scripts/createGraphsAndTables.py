import re
import sys
import os
all_files = os.listdir("stats/")
import matplotlib.pyplot as plt
from tabulate import tabulate
'''
system.cpu.dcache.overall_miss_rate::total
system.cpu.icache.overall_miss_rate::total
system.l2.overall_miss_rate::total
system.cpu.dcache.overall_misses::total
system.cpu.icache.overall_misses::total
system.cpu.dcache.overall_hits::total
system.cpu.icache.overall_hits::total
system.l2.overall_hits::total 
system.l2.overall_misses::total  
'''
import csv
def tables(vary,a,b,c,d,e,f,g,title = '',postfix = '',bench = '',csvname = 'default'):
    print('\n')
    print('                                   Varying ' + str(title)+ ' for '+ str(bench))
    row_form = [[0 for _ in range(8)] for _ in range(6)]
    headers = ['','L1D HitRate','L1D MissRate','L1I HitRate','L1I MissRate','L2 HitRate','L2 MissRate','CPI']
    for i in range(len(headers)):
        row_form[0][i] = headers[i]
    for i in range(5):
        row_form[i+1][0] = str(vary[i]) + postfix
        row_form[i+1][1] = a[i]
        row_form[i+1][2] = b[i]
        row_form[i+1][3] = c[i]
        row_form[i+1][4] = d[i]
        row_form[i+1][5] = e[i]
        row_form[i+1][6] = f[i]
        row_form[i+1][7] = g[i]
    with open("charts/"+str(csvname)+".csv","w+",newline = '') as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')        
        csvWriter.writerows(row_form)
    print(tabulate(row_form[1:],headers = ['Size','L1D HitRate','L1D MissRate','L1I HitRate','L1I MissRate','L2 HitRate','L2 MissRate','CPI'], tablefmt='fancy_grid'))

ins_num = 100000000
l1d = [8,16,64,128,256]
l1i = [4, 8, 16, 64, 128]
l2 = [256, 512, 1, 2, 4]
l2_graph = [256,512,1024,2048,4096]
l1d_assoc = [1,2,4,8,16]
l1i_assoc = [1,2,4,8,16]
l2_assoc = [1,2,4,8,16]
block_size = [8,16,32,64,128]
benchmarks = ["401.bzip2", "429.mcf", "456.hmmer", "458.sjeng", "470.lbm"]
stat_files = ["stats_l1_d_cache_", "stats_l1_i_cache_", "stats_l2_cache_", "stats_l1_d_assoc_", "stats_l1_i_assoc_", "stats_l2_assoc_", "stats_block_size_"]

hits_l1d = []
misses_l1d = []
hits_l1i = []
misses_l1i = []
hits_l2 = []
misses_l2 = []
cpi_a = []

#Change this
bench = benchmarks[4]
varier = stat_files[6]
iterator = block_size
iterator_graph = block_size
iterator_label = 'block'
chart_labelsss = 'Cache Block Size'
inter = "_"
vary_postfix = ''
for indexf,filename in enumerate(iterator):
    #inter = "kB_"
    #if indexf > 1:
    #    inter = "MB_"
    file_to_open = 'stats/'+varier+ str(filename) + inter + str(bench) +'.txt'
    print(file_to_open)
    #if file_to_open not in all_files:
    #file_to_open = 'stats/'+varier+ str(filename) + 'MB_' + str(bench) +'.txt'
    
    with open(file_to_open ,'r') as textfile:        
        all_lines = textfile.readlines()
        for i in range(len(all_lines)): 
            all_lines[i] = all_lines[i].split()
            if len(all_lines[i]):
                if all_lines[i][0] == "system.cpu.dcache.overall_miss_rate::total":
                    l1d_miss = float(all_lines[i][1])
                    l1d_hit = 1 - l1d_miss
                    #print('Miss Rate L1 D' +' : '+ str(l1d_miss))
                    #print('\nHit Rate L1 D' +' : '+ str(l1d_hit))
                    hits_l1d.append(l1d_hit)
                    misses_l1d.append(l1d_miss)
                elif all_lines[i][0].rstrip() == "system.cpu.icache.overall_miss_rate::total":                    
                    l1i_miss = float(all_lines[i][1])
                    l1i_hit = 1 - l1i_miss
                    #print('Miss Rate L1 I' +' : '+ str(l1i_miss))
                    #print('\nHit Rate L1 I' +' : '+ str(l1i_hit))
                    hits_l1i.append(l1i_hit)
                    misses_l1i.append(l1i_miss)
                elif all_lines[i][0] == "system.l2.overall_miss_rate::total":
                    l2_miss = float(all_lines[i][1])
                    l2_hit = 1 - l2_miss
                    #print('Miss Rate L2' +' : '+ str(l2_miss))
                    #print('\nHit Rate L2' +' : '+ str(l2_hit))
                    hits_l2.append(l2_hit)
                    misses_l2.append(l2_miss)
                elif all_lines[i][0] == "system.cpu.dcache.overall_misses::total":
                    l1d_m = float(all_lines[i][1])
                elif all_lines[i][0] == "system.cpu.icache.overall_misses::total":
                    l1i_m = float(all_lines[i][1])
                elif all_lines[i][0] == "system.l2.overall_misses::total":
                    l2_m = float(all_lines[i][1])
                
                    
        cpi = 1 + ((((l1i_m + l1d_m)*6) + (l2_m*50))/ ins_num)
        #print('CPI : ' + str(cpi))
        cpi_a.append(cpi)
        #print("\n\n\n###################################################")

#print(l1d)
#print(hits_l1d)  
#print(misses_l1d)
#print(hits_l1i)
#print(misses_l1i)
#print(hits_l2)
#print(misses_l2)
#print(cpi_a)         



chrtdir = "chrtimages/"
#Change this
x_axis = iterator


x_labels = {"l1d":"L1 D Cache Size (kB)", 'l1i':'L1 I Cache Size (kB)', 'l2':'L2 Cache Size (kB)', 'l1d_a':'L1 D Associativity', 'l1i_a':'L1 I Associativity','l2_a':'L2 Associativity','block':'Block Size'}

#Change this, possible values l1d, l1i,l2,l1d_a,l1i_a,l2_a,block
cur = iterator_label

#benchmarks = ["401.bzip2", "429.mcf", "456.hmmer", "458.sjeng", "470.lbm"]

#Change this
cur_bench = bench

#plt.subplot(2,2,1)
plt.plot(x_axis,hits_l1d,color = 'red', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('HitRate L1 D')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"HitRate L1 D")
plt.show()


#plt.subplot(2,2,1)
plt.plot(x_axis,misses_l1d, color = 'green', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('MissRate L1 D')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"HitRateL1D.png")
plt.show()

#plt.subplot(2,2,1)
plt.plot(x_axis,hits_l1i, color = 'blue', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('HitRate L1 I')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"HitRateL1I.png")
plt.show()

#plt.subplot(2,2,1)
plt.plot(x_axis,misses_l1i, color = 'yellow', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('MissRate L1 I')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"MissRateL1I.png")
plt.show()

plt.plot(x_axis,hits_l2, color = 'black', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('HitRate L2')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"HitRateL2.png")
plt.show()

plt.plot(x_axis,misses_l2, color = 'orange', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('MissRate L2')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"MissRateL2.png")
plt.show()

plt.plot(x_axis,cpi_a, color = 'brown', linewidth = 2.0)
plt.xlabel(x_labels[cur])
plt.ylabel('CPI')
plt.title('Varying '+str(x_labels[cur])+'for '+str(cur_bench))
plt.savefig(chrtdir+"CPI.png")
plt.show()

tables(iterator_graph, hits_l1d, misses_l1d,hits_l1i,misses_l1i,hits_l2,misses_l2,cpi_a,chart_labelsss,vary_postfix,bench=bench,csvname = iterator_label+bench)

      
            
        
