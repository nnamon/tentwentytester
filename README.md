# tentwentytester

Automated Test Case Testing for CS1020

# Installation

```
$ git clone git@github.com:nnamon/tentwentytester.git
$ cd tentwentytester
$ chmod +x tentwentytester
$ sudo ln -s tentwentytester /bin/tentwentytester
```

# Usage

```
$ tentwentytester -h
usage: Runs a java class for all test cases [-h] [--diff]
                                            classf inputd outputd

positional arguments:
  classf      java class to run
  inputd      input cases directory
  outputd     output cases directory

optional arguments:
  -h, --help  show this help message and exit
  --diff      run diff on invalid cases
```

# Examples

We simply specify the class we want to run, the input directory, and the output
directory. In this example, the cases were found to be invalid.

```
$ javac Main.java && tentwentytester Main.class ../input/ ../output/
Results:
------------------------------
lecturer1 - False
lecturer2 - True
lecturer3 - False
lecturer4 - False
lecturer5 - False
lecturer6 - False
lecturer7 - False
lecturer8 - False
------------------------------
```

This example shows when every test case passes.

```
$ javac Main.java && tentwentytester --diff  Main.class ../input/ ../output/
Results:
------------------------------
lecturer1 - True
lecturer2 - True
lecturer3 - True
lecturer4 - True
lecturer5 - True
lecturer6 - True
lecturer7 - True
lecturer8 - True
------------------------------
```

If the --diff option is passed, one gets more information on the differences
between their solution and the output test case.

```
Results:
------------------------------
lecturer1 - False
lecturer2 - True
lecturer3 - False
lecturer4 - False
lecturer5 - False
lecturer6 - False
lecturer7 - False
lecturer8 - False
------------------------------

------------------------------
lecturer1 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 0 ****
--- 1,10 ----
+ N+ O+ N+ E+
+ N+ O+ N+ E+

------------------------------
lecturer3 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 1,3 ****
--- 1,8 ----
+ N+ O+ N+ E+
  g  m  a
------------------------------
lecturer4 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 82,87 ****
--- 82,92 ----
  a  h  n+
+ N+ O+ N+ E
  f  o
------------------------------
lecturer5 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 8,13 ****
--- 8,44 ----
  l  f  w+
+ N+ O+ N+ E+
+ N+ O+ N+ E+
+ N+ O+ N+ E+
+ f+ s+ v+ z+ l+ o+ t+ l+ f+ w+
+ N+ O+ N+ E
  f  s***************
*** 42,47 ****
--- 73,103 ----
  f  w
+ N+ O+ N+ E+
+ N+ O+ N+ E+
+ N+ O+ N+ E+
+ N+ O+ N+ E+
+ N+ O+ N+ E+
  f  s  v***************
*** 52,57 ****
--- 108,118 ----
  l  f  w+
+ N+ O+ N+ E
  f  s***************
*** 86,101 ****
  f  w
! f! s! v! z! l! o! t! l! f! w
  f  s--- 147,156 ----
  f  w
! N! O! N! E
  f  s
------------------------------
lecturer6 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 26,569 ****
  h  j
! b! f! g! r! u! f! x! d! s! q! c! h! j!
! b! f! g! r! u! f! x! d! s! q! c! h! j!
! n! c! r! b! w!
! n! c! r! b! w!
! n! c! r! b! w!
! z! l!
! z! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! u! x! p! x! n! g! e! b! x! r! m! q! d! g! q! j! s! o! s!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! z! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l
  n  c--- 26,619 ----
  h  j
! N! O! N! E!
! N! O! N! E!
! N! O! N! E!
! b! f! g! r! u! f! x! d! s! q! c! h! j!
! b! f! g! r! u! f! x! d! s! q! c! h! j!
! N! O! N! E!
! N! O! N! E!
! n! c! r! b! w!
! n! c! r! b! w!
! N! O! N! E!
! n! c! r! b! w!
! z! l!
! z! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! N! O! N! E!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! N! O! N! E!
! u! x! p! x! n! g! e! b! x! r! m! q! d! g! q! j! s! o! s!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! z! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! N! O! N! E!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! s! y! y! v! o! p! e! p! m! v! d! o! s! i! b! r! v! q! o!
! n! c! r! b! w!
! t! v! w! g! u! k! j! w! s! e! k! f! c! g! l! l!
! N! O! N! E
  n  c
------------------------------
lecturer7 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 66,357 ****
  s  x
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! w! j! y! q! n! n! o! u! s! x!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
--- 66,367 ----
  s  x
! N! O! N! E!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! N! O! N! E!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! w! j! y! q! n! n! o! u! s! x!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! w! j! y! q! n! n! o! u! s! x!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!
! s! d! m! k! l! m! n! d! n! t! f! u! k! m! s! k! h! n!

------------------------------
lecturer8 Analysis
------------------------------
*** Your Output
--- Test Case
***************
*** 1,58 ****
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k
  z  p--- 1,78 ----
! N! O! N! E!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! N! O! N! E
  z  p***************
*** 315,320 ****
--- 335,345 ----
  m  f
+ N+ O+ N+ E+
  o  t  o***************
*** 351,356 ****
--- 376,391 ----
  m  f
+ N+ O+ N+ E+
+ N+ O+ N+ E+
  z  p  o***************
*** 563,1001 ****
  w  a
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! z! p! o! n! r! t! k!
! g! t! c! w! h! l! s! r! w! a!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! z! p! o! n! r! t! k!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! g! t! c! w! h! l! s! r! w! a!
! z! p! o! n! r! t! k!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k
  n  x--- 598,1091 ----
  w  a
! N! O! N! E!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! g! t! c! w! h! l! s! r! w! a!
! z! p! o! n! r! t! k!
! N! O! N! E!
! g! t! c! w! h! l! s! r! w! a!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! z! p! o! n! r! t! k!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! N! O! N! E!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! g! t! c! w! h! l! s! r! w! a!
! z! p! o! n! r! t! k!
! j! j! z! j! u! j! u! a! y! j! i! i! c! c! e! r! v! h! a! v!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! N! O! N! E!
! b! k! p! w! q! b! w! w! c!
! N! O! N! E!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! N! O! N! E!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! z! p! o! n! r! t! k!
! b! k! p! w! q! b! w! w! c!
! z! p! o! n! r! t! k!
! N! O! N! E!
! z! p! o! n! r! t! k!
! N! O! N! E
  n  x***************
*** 1229,1234 ****
--- 1319,1329 ----
  w  c
+ N+ O+ N+ E+
  z  p  o***************
*** 1397,1402 ****
--- 1492,1502 ----
  s  i
+ N+ O+ N+ E+
  n  x  e***************
*** 1926,1931 ****
--- 2026,2036 ----
  n  p
+ N+ O+ N+ E+
  j  j  z***************
*** 2030,2035 ****
--- 2135,2145 ----
  r  w  a+
+ N+ O+ N+ E
  g  t***************
*** 2337,2342 ****
--- 2447,2457 ----
  e  t
+ N+ O+ N+ E+
  g  t  c
```
