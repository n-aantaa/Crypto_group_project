def inverse(r0,r1):
  s0=1
  s1=0
  t0=0
  t1=1

  rs = r1
  while r1 != 0:
    r=r0%r1
    q = r0//r1
    s = s0-q *s1
    t=t0-q*t1
    s0=s1
    s1=s
    t0=t1
    t1=t
    r0=r1
    r1=r
  return (s0+rs)%rs


def fast_raise_power_book(x,n,p):
  nb=bin(n)[2:]
  result=1
  for i in range(len(nb)):
    result= (result* result)%p
    if nb[i] == '1':
      result = (result * x) % p
  return result


def my_eea(r0,r1):
  #Initialize data
  s0=1
  s1=0
  t0=0
  t1=1

  while(r1!=0):
    r= r0 % r1
    q = r0//r1
    s = s0 - q*s1
    t= t0 - q*t1

    #Update r, s, t
    r0=r1
    r1=r
    s0=s1
    s1=s
    t0=t1
    t1=t

  return r0

