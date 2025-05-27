#!/usr/bin/env python3
from Bio import Entrez as E, SeqIO
import csv, io, matplotlib.pyplot as p
f='taxid_'
n="nucleotide"
E.email=input("Email:")
E.api_key=input("API key:")
ml=int(input("Min seq len:"))
mxl=int(input("Max seq len:"))
tid=input("Taxid:")
h=E.esearch(db=n,term=f"txid{tid}[Organism] AND {ml}:{mxl}[SLEN]",usehistory="y")
sr=E.read(h)
h=E.efetch(db=n,rettype="gb",retmode="text",retstart=0,retmax=500,webenv=sr["WebEnv"],query_key=sr["QueryKey"])
t=h.read()
if(isinstance(t, bytes)):
    print('Query has no results')
    quit()
open(f"{f}{tid}.gb","w").write(t)
r=list(SeqIO.parse(io.StringIO(t),"genbank"))
w=csv.writer(open(f"{f}{tid}.csv","w"))
w.writerow(["ID","Len","Desc"])
[w.writerow([e.id,len(e.seq),e.description])for e in r]
r.sort(key=lambda e:-len(e.seq))
a=[e.id for e in r]
l=[len(x.seq)for x in r]
p.plot(a,l,"o-")
p.xticks(rotation=90)
p.tight_layout()
p.savefig(f"{f}{tid}.png")