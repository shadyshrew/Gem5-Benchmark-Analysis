import subprocess
import os

stat_files = ["stats_l1_d_cache_", "stats_l1_i_cache_", "stats_l2_cache_", "stats_l1_d_assoc_", "stats_l1_i_assoc_", "stats_l2_assoc_", "stats_block_size_"]
l1d_sizes = ["8kB", "16kB" ,"64kB", "128kB", "256kB"]
l1i_sizes = ["4kB", "8kB", "16kB", "64kB", "128kB"]
l2_sizes = ["256kB", "512kB", "1MB", "2MB", "4MB"]
l1d_assoc = ["1","2","4","8","16"]
l1i_assoc = ["1","2","4","8","16"]
l2_assoc = ["1","2","4","8","16"]
block_size = ["8","16","32","64","128"]
benchmarks = ["401.bzip2", "429.mcf", "456.hmmer", "458.sjeng", "470.lbm"]
final_out_dir = "/home/csgrad/hgarg/ca_lab2_out/final/"
gem5_script_file = "/util/gem5/configs/example/se.py"
out_dir = "/home/csgrad/hgarg/ca_lab2_out/instance/"
ex_com = "/util/gem5/build/X86/gem5.opt"
gem5benchdir = "/util/gem5/benchmark/"
max_instr = "100000000"

dict = {
	"401.bzip2" : ["input.program"],
	"429.mcf" : ["inp.in", "mcf.out"],
	"456.hmmer" : ["bombesin.hmm", "bombesin.hmm.new"],
	"458.sjeng" : ["test.txt"],
	"470.lbm" : ["100_100_130_cf_a.of","lbm.in"]
}

base_l1d = "128kB"
base_l1i = "64kB"
base_l2 = "1MB"
base_l1dassoc = "2"
base_l1iassoc = "2"
base_l2assoc = "1"
base_block = "64"

'''******************* RUNNING FOR L1-D CACHE FOR ALL BENCHMARKS ***********************'''

#creating stats files for benchmark 401.bzip2 for L1-D cache
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[0]+l1d_sizes[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+l1d_sizes[i], "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L1-D cache
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[0]+l1d_sizes[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+l1d_sizes[i], "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer for L1-D cache
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[0]+l1d_sizes[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+l1d_sizes[i], "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng for L1-D cache
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[0]+l1d_sizes[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+l1d_sizes[i], "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L1-D cache
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[0]+l1d_sizes[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+l1d_sizes[i], "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])

'''******************* RUNNING FOR L1-I CACHE FOR EACH BENCHMARK ***********************'''

#creating stats files for benchmark 401.bzip2 for L1-I cache
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[1]+l1i_sizes[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+l1i_sizes[i], "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L1-I cache
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[1]+l1i_sizes[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+l1i_sizes[i], "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer for L1-I cache
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[1]+l1i_sizes[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+l1i_sizes[i], "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng for L1-I cache
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[1]+l1i_sizes[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+l1i_sizes[i], "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L1-I cache
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[1]+l1i_sizes[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+l1i_sizes[i], "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])


'''******************* RUNNING FOR L2 CACHE FOR EACH BENCHMARK ***********************'''

#creating stats files for benchmark 401.bzip2 for L1-I cache
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[2]+l2_sizes[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+l2_sizes[i], "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L1-I cache
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[2]+l2_sizes[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+l2_sizes[i], "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer for L1-I cache
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[2]+l2_sizes[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+l2_sizes[i], "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng for L1-I cache
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[2]+l2_sizes[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+l2_sizes[i], "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L1-I cache
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[2]+l2_sizes[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+l2_sizes[i], "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])

'''******************* RUNNING FOR L1-D ASSOCIATIVITY FOR EACH BENCHMARK ***********************'''

#creating stats files for benchmark 401.bzip2 for L1-D ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[3]+l1d_assoc[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+l1d_assoc[i], "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L1-D ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[3]+l1d_assoc[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+l1d_assoc[i], "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer L1-D ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[3]+l1d_assoc[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+l1d_assoc[i], "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng L1-D ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[3]+l1d_assoc[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+l1d_assoc[i], "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L1-D ASSOCIATIVITY
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[3]+l1d_assoc[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+l1d_assoc[i], "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])


'''******************* RUNNING FOR L1-I ASSOCIATIVITY FOR EACH BENCHMARK ***********************'''

#creating stats files for benchmark 401.bzip2 for L1-I ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[4]+l1i_assoc[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+l1i_assoc[i], "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L1-I ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[4]+l1i_assoc[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+l1i_assoc[i], "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer L1-I ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[4]+l1i_assoc[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+l1i_assoc[i], "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng L1-I ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[4]+l1i_assoc[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+l1i_assoc[i], "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L1-I ASSOCIATIVITY
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[4]+l1i_assoc[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+l1i_assoc[i], "--l2_assoc="+base_l2assoc, "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])


'''******************* RUNNING FOR L2 ASSOCIATIVITY FOR EACH BENCHMARK ***********************'''

#creating stats files for benchmark 401.bzip2 for L2 ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[5]+l2_assoc[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+l2_assoc[i], "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for L2 ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[5]+l2_assoc[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+l2_assoc[i], "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer L2 ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[5]+l2_assoc[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+l2_assoc[i], "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng L2 ASSOCIATIVITY
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[5]+l2_assoc[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+l2_assoc[i], "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for L2 ASSOCIATIVITY
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[5]+l2_assoc[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+l2_assoc[i], "--cacheline_size="+base_block])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])

'''******************* RUNNING FOR BLOCK SIZE FOR EACH BENCHMARK ***********************'''
#creating stats files for benchmark 401.bzip2 for BLOCK SIZE
arg_file = gem5benchdir+benchmarks[0]+"/data/"+dict[benchmarks[0]][0]
src_file = gem5benchdir+benchmarks[0]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[6]+block_size[i]+"_"+benchmarks[0]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+block_size[i]])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 429.mcf for BLOCK SIZE
arg_file = gem5benchdir+benchmarks[1]+"/data/"+dict[benchmarks[1]][0]
src_file = gem5benchdir+benchmarks[1]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[6]+block_size[i]+"_"+benchmarks[1]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+block_size[i]])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 456.hmmer BLOCK SIZE
arg_file = gem5benchdir+benchmarks[2]+"/data/"+dict[benchmarks[2]][1]
src_file = gem5benchdir+benchmarks[2]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[6]+block_size[i]+"_"+benchmarks[2]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+block_size[i]])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 458.sjeng BLOCK SIZE
arg_file = gem5benchdir+benchmarks[3]+"/data/"+dict[benchmarks[3]][0]
src_file = gem5benchdir+benchmarks[3]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[6]+block_size[i]+"_"+benchmarks[3]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+block_size[i]])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
#creating stats files for benchmark 470.lbm for BLOCK SIZE
arg_file = " 20 reference.dat 0 1 "+gem5benchdir+benchmarks[4]+"/data/"+dict[benchmarks[4]][0]
src_file = gem5benchdir+benchmarks[4]+"/src/benchmark"
for i in range(5):
	final_file = final_out_dir+stat_files[6]+block_size[i]+"_"+benchmarks[4]+".txt"
	subprocess.call(["time", ex_com, "-d",out_dir,gem5_script_file,"-c",src_file,"-o",arg_file,"-I", max_instr, "--l1d_size="+base_l1d, "--l1i_size="+base_l1i, "--l2_size="+base_l2, "--caches", "--l2cache","--l1d_assoc="+base_l1dassoc, "--l1i_assoc="+base_l1iassoc, "--l2_assoc="+base_l2assoc, "--cacheline_size="+block_size[i]])
	subprocess.call(["mv", out_dir+"stats.txt", final_file])
