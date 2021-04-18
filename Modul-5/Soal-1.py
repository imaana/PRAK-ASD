from mhs import *

#nomor 1####################################################################

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def urutNim(daftar):
    for i in range(len(daftar)):
        for j in range(len(daftar)-1):
            if daftar[j].nim > daftar[j+1].nim :
                        swap(daftar,j,j+1)
                        
def daftarNim(daftar):
    mhs =[]
    for i in daftar:
        mhs.append([i.nama,i.nim])
    return mhs

##print('Daftar Mahasiswa sebelum di urutkan : \n' , daftarNim(daftar))
##urutNim(daftar)
##print('Daftar Mahasiswa setelah di urutkan : \n', daftarNim(daftar))

#nomor 2####################################################################

A = [2,1,3,7,8,5]
B = [13,10,9,14,15,12]

def urutkanC(A,B):
    C = A + B
    for i in range(len(C)):
        for j in range(len(C)-1):
            if C[j] > C[j+1]:
                swap(C,j,j+1)
    return(C)

##print('Array C setelah diurutkan : \n', urutkanC(A,B))

#nomor 3####################################################################

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print('bubble    : %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print('selection : %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print('insertion : %g detik' %(ak-aw));        























