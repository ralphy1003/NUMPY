print("Problem No. 2")
import numpy as np
A=np.square(np.arange(1,101,1))
A.resize(10,10)
ANS=A[A%3==0]
ANS.resize(11,3)
print("Numbers divisible by 3:")
print(ANS)
   