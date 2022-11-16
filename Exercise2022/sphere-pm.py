#! /usr/bin/env python2
# Generate a set of lens/source parameters

from random import randint

fn = "sphere-pm.csv"
n = 10000


def getline(idx,chi=50,nterms=16):
    x = randint(-85,85)
    y = randint(-85,85)
    einsteinR = randint(1,50)
    sigma = randint(1,50)
    sigma2 = 0
    theta = 0
    srcmode = "s"
    lensmode = "p"
    return f'"{idx:05}",image-{idx:05}.png,{srcmode},{lensmode},{chi},{x},{y},{einsteinR},{sigma},{sigma2},{theta},{nterms}'

header = "index,filename,source,lens,chi,x,y,einsteinR,sigma,sigma2,theta,nterms\n"

def main():
    with open(fn, 'w') as f:
      f.write(header)
      for i in range(n):
        l = getline(i+1)
        f.write(l)
        f.write("\n")

if __name__ == "__main__":
   main()
