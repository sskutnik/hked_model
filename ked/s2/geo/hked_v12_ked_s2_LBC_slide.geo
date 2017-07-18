c HKED Model Geometry, v.12, MCook
c --- CELL CARDS ---
c --- CORE COMPONENTS ---
c Sample solution, force photon collisions in this cell
10    1  -10.97   -100                                       IMP:P=1 IMP:E=1 
c Sample vial
11    13   -6.52        100 -101                              IMP:P=1 IMP:E=1
c Air gap within the sample vial
c 12  3   -0.001293                                         IMP:P=1 IMP:E=1
c X-ray tube
13    8   -8.96       -103  104  105  106                       IMP:P=1 IMP:E=1
c X-ray tube interior
14    0               -104  106                                 IMP:P=1 IMP:E=1
c Beryllium window in x-ray tube
15    9   -1.85       -106                                      IMP:P=1 IMP:E=1
c X-ray tube shielding
16    5  -19.25        103 -107  105 -108  109  110  604  -999  IMP:P=1 IMP:E=1
c Beam line adjacent to x-ray tube
17    3   -0.001293  (-109:-105)                                IMP:P=1 IMP:E=1
c Aluminum beam filter
18    4   -2.70       -110                                      IMP:P=1 IMP:E=1
c Air gap filling notch in SS sample tube
19    3   -0.001293   -111                                      IMP:P=1 IMP:E=1
c Sample holder tube
20    6   -8.03        101 -112  113  111 -999                  IMP:P=1 IMP:E=1
c Sample holder tube interior
21    3   -0.001293   -113  101                                 IMP:P=1 IMP:E=1
c --- END CORE COMPONENTS ---
c
c --- KED BEAM LINE ---
c Inner KED shield
30    5  -19.25       -300  301  309  304  305  307  308  314  315
                      -999                                      IMP:P=1 IMP:E=1
c Outer KED shield
31    5  -19.25       -302  303  318 -999                       IMP:P=1 IMP:E=1
c KED collimator
32    5  -19.25      (-304:-305:-306:-307)  309  310  311 800   IMP:P=1 IMP:E=1
c KED collimator beam line tip, sample side
33    3   -0.001293  (-309) #34                                 IMP:P=1 IMP:E=1
c KED iron beam filter
34   11   -7.874   (-312:-313)                                IMP:P=1 IMP:E=1
c KED collimator beam line
35    3   -0.001293   (-310:-311) #34   #91                     IMP:P=1 IMP:E=1
c Air gap around collimator
36    3   -0.001293    306 -308 315 #32                         IMP:P=1 IMP:E=1
c KED collimator retainer pin recession
37    3   -0.001293   -314  316                                 IMP:P=1 IMP:E=1
c KED collimator retainer pin, assume 304SS for now
38    6   -8.03      (-315:-316)                                IMP:P=1 IMP:E=1
c Air gap around collimator tip, renumber later
39    3   -0.001293   -317  307                                 IMP:P=1 IMP:E=1
c Poly detector cup, renumber later
40    2   -0.98        300  303  317 -318 -999                  IMP:P=1 IMP:E=1
c Beryllium window for KED detector
41    9   -1.85       -319                                      IMP:P=1 IMP:E=1
c Aluminum detector casing
42    4   -2.70       -303  319  320  321                       IMP:P=1 IMP:E=1
c KED detector interior
43    0              (-320:-321) 319  322                       IMP:P=1 IMP:E=1
c KED detector crystal
44   10   -5.323      -322 (320:321)  319                       IMP:P=1 IMP:E=1
c --- END KED BEAM LINE ---
c
c --- ked BEAM LINE ---
c ked collimator cap (assume tungsten for now)
60    5  -19.25       600 -108 -604 608  609                    IMP:P=1 IMP:E=1
c ked collimator body
61    5  -19.25     (-604:-605:-606:-607) 608 -600 #92          IMP:P=1 IMP:E=1
c ked beam line tip
62    3   -0.001293  -108  609 -608  #64    #92                 IMP:P=1 IMP:E=1
c ked gadolinium filter (confirm thickness & material)
63   12   -7.90      -609                                       IMP:P=1 IMP:E=1
c ked beam line
64    3   -0.001293  -608 -600       #92                        IMP:P=1 IMP:E=1
c ked inner shield
65    5  -19.25      -610  611 605 606 607                      IMP:P=1 IMP:E=1
c ked collimator air gap
66    3   -0.001293  -611  606  605  #61                        IMP:P=1 IMP:E=1
c ked retainer pin recession
c 67
c ked retainer pin
c 68
c ked outer shield
69    5  -19.25      -615  616                                  IMP:P=1 IMP:E=1
c ked detector cup
70    2   -0.98      -616 617 618 607                           IMP:P=1 IMP:E=1
c ked collimator air gap, detector side
71    3   -0.001293  -618  607           #92                    IMP:P=1 IMP:E=1
c ked beryllium window
72    9   -1.85      -619                                       IMP:P=1 IMP:E=1
c ked detector casing
73    4   -2.70      -617  619  620  621                        IMP:P=1 IMP:E=1
c ked detector interior
74    0             (-620:-621) 622 619                         IMP:P=1 IMP:E=1
c ked detector crystal
75   10   -5.323     -622 (620:621) 619                         IMP:P=1 IMP:E=1
c --- END ked BEAM LINE ---
c
c --- AUX COMPONENTS ---
c Equipment table
c 90    6   -8.03       -900 -999                               IMP:P=1 IMP:E=1
c Microcell at end of KED beam line
91    3   -0.001293    -800        VOL=2.513E-6                 IMP:P=1 IMP:E=1
c Microcell at end of ked beam line
92    3   -0.001293    -801        VOL=3.524E-5                 IMP:P=1 IMP:E=1
c Interior model space, fill with air
98    3   -0.001293    #10 #11     #13 #14 #15 #16 #17 #18 #19
                       #20 #21
                       #30 #31 #32 #33 #34 #35 #36 #37 #38 #39
                       #40 #41 #42 #43 #44
                       #60 #61 #62 #63 #64 #65 #66         #69 
                       #70 #71 #72 #73 #74 #75   
                       #91 #92 -999                             IMP:P=1 IMP:E=1
c Exterior of model space
99    0              999                                        IMP:P=0 IMP:E=0
c --- END AUX COMPONENTS ---
c --- END CELL CARDS ---

c --- SURFACE CARDS ---
c --- CORE COMPONENTS ---
c Sample vial and solution
c 100   RCC   6.5     0 -0.98    0      0  3.214  0.7
c 101   RCC   6.5     0 -1.26    0      0  5.85   0.954
100   RPP    6.0   6.27     -1.0   1.0    -0.98   3.214
101   RPP    5.9   6.37     -1.2   1.2    -1.28   5.85
c Air gap inside sample vial above sample, renumber later
c    RCC   6.5     0  2.234   0      0  2.136  0.7
c X-ray tube
103   RCC   0  0 -2   0 0 6       2.5415
c X-ray tube shell
104   RCC   0  0 -1.8    0  0  5.6       2.3415
c Cone cutting off x-ray tube
105   TRC   2.415  0  0    0.13  0  0      0.2  0.21
c Beryllium window
106   RCC   2.335  0  0  0.08  0  0  0.2
c X-ray tube body shielding
107   RCC   0 0 -2   0 0 7.002   7.979
108   PX    3.6955
c Beam line within tungsten x-ray shield
109   RPP   2.5415  3.5815    -0.091  0.091   -0.065   0.065
c Aluminum x-ray filter within tungsten x-ray shield
c 110   RCC   3.5815  0  0       0.114  0  0      1.2835
110   RCC   3.5815  0  0       0.114  0  0      0.80
c Air gap in SS sample tube opposite from aluminum x-ray filter
111   RPP   3.6955  3.8255    -5.5    1.5     -0.5035  0.5035
c Sample holder tube
112   RPP   3.6955  9.2925  -13.197  15.197  -2      6
113   RPP   3.894   9.094   -11.197  15.197  -1.8015 5.8015
c --- END CORE COMPONENTS ---
c
c --- KED BEAM LINE ---
c Inner KED shield
300   RPP   9.2925  19.4055  -5.005   5.005  -5.005   5.005
301   RPP   9.2925  11.527   -5.005   5.005  -5.005  -3.501
c Outer KED shield
302   RPP  19.4055  29.0145  -5.005   5.005  -5.005  5.005
303   RCC  20.4055  0  0       9.0145 0  0      3.425
c KED collimator
304   RCC   9.2925  0  0       5.883  0  0      0.94
305   RCC  15.1755  0  0       2.6    0  0      1.037
306   RCC  17.7755  0  0       0.552  0  0      0.7295
307   RCC  18.3275  0  0       1.527  0  0      1.073
c Air gap around KED collimator
308   RCC  17.7755  0  0       0.552  0  0      1.037
c KED beam line w/ iron beam filter hole
309   RCC   9.2925  0  0       0.512  0  0      0.2685
310   RCC   9.8045  0  0       1.903  0  0      0.2215
c 311   RCC  11.6955  0  0       8.159  0  0      0.04
311   RCC  11.6955  0  0       8.1585  0  0      0.04
c KED iron beam filter
c old
c 312   RCC   9.3925  0  0       0.402  0  0      0.2585
c 313   RCC   9.7945  0  0       1.803  0  0      0.2115
312   RCC   9.3925  0  0       0.412  0  0      0.2685
313   RCC   9.7945  0  0       1.803  0  0      0.2215
c KED collimator retainer pin and hole
314   RCC  18.0515  0  4.414   0      0  0.591  0.985
315   RCC  18.0515  0  4.414   0      0 -3.594  0.276
316   RCC  18.0515  0  4.414   0      0  0.575  0.4435
c Air gap around KED collimator tip
317   RCC  19.4055  0  0       1.0    0  0    1.1465
c KED detector cup, polyethylene
318   RCC  19.4055  0  0       9.609  0  0    3.845
c KED detector window, Canberra model GL0510 LE-HPGe
319   RCC  20.4055  0  0       0.015   0  0   2.789
c KED detector housing, assume 2mm casing thickness
320   RCC  20.4205  0  0       0.1985   0  0    2.589
321   RCC  20.619   0  0       8.601    0  0    3.225
c KED detector crystal, Canberra model GL0510 LE-HPGe
322   RCC  20.9055  0  0       1.0      0  0    1.2616
c --- END KED BEAM LINE---
c
c --- ked BEAM LINE ---
c ked collimator cap
600       PX    3.4955
601       PX    3.6955
c 602   1   RCC   3.6955  -4.767  0    0.2  0  0    0.9855
c ked collimator body
604   1   RCC   3.4955  -4.767  0  -11.7835  0  0   0.9855
605   1   RCC  -8.288   -4.767  0   -1.813   0  0   1.4675
606   1   RCC -10.101   -4.767  0   -0.746   0  0   1.053
607   1   RCC -10.847   -4.767  0   -2.487   0  0   1.4675
c ked beam line
c 608   1   RCC   3.4955  -4.767  0  -16.8295   0  0   0.15
608   1   RCC   3.4955  -4.767  0  -16.829   0  0   0.15
c ked gadolinium foil, assume 0.1 mm thickness (Contact Bob & Tyler to verify)
609       RCC   3.4955  -2.17   0    0.01    0  0   0.98
c 609       RCC   3.4955  -3.32   0    0.01    0  0   0.98
c ked inner shield
610   1   RPP -12.496 -8.288   -9.9665  0.4325   -5.005  5.005
c ked retainer pin air gap
611   1   RCC -10.101   -4.767  0   -0.746   0  0   1.4675
c ked retainer pin recession
c 612
c ked collimator retainer pin
c 613
c 614
c ked outer shield
615   1   RPP  -22.105 -12.496   -9.9665  0.4325   -5.005  5.005
c ked detector cup
616   1   RCC  -12.496  -4.767  0   -9.609  0  0  3.845
617   1   RCC  -14.001  -4.767  0   -9.038  0  0  3.425
c ked detector side air gap
618   1   RCC  -12.496  -4.767  0    -1.505  0  0  1.676
c ked detector window, Canberra model GL0510 LE-HPGe
619   1   RCC  -14.001  -4.767  0     -0.015  0  0  2.789
c ked detector housing, assume 2mm casing thickness
620   1   RCC  -14.021  -4.767  0       -0.1985   0  0    2.589
621   1   RCC  -14.2145 -4.767  0       -8.601    0  0    3.225
c ked detector crystal, Canberra model GL0510 LE-HPGe
622   1   RCC  -14.501  -4.767      0   -1.0      0  0    1.2616
c --- END ked BEAM LINE ---
c
c Surfaces for DXTRAN spheres (KED & ked)
c 800       PX  19.854   
c 801   1   PX -13.3335
c KED & ked microcells
800       RCC   19.854   0      0         0.0005  0  0    0.04
801   1   RCC  -13.3335 -4.767  0         -0.0005  0  0    0.15
c --- AUX COMPONENTS ---
c Equipment table
c 900   RPP -20       9.2925  -20      20      -4     -2
c Model exterior boundary
c 999   SO   50
c 999   SX    4  28
999   RCC  4  0   -6   0  0  14    28
c --- END AUX COMPONENTS ---
c --- END SURFACE CARDS ---