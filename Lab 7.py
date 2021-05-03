import numpy as np
import matplotlib.pyplot as plt

M1 = np.array([[1, 2, 3], [7, 5, 6], [3, 2, 1]])
M2 = np.array([[5, 3, 4], [3, 2, 5], [3, 4, 2]])
M3 = np.array([[5, 2, 5], [2, 3, 1], [3, 2, 2]])
M4 = np.identity(3)
M5 = np.zeros(3)

print("Shape of M1: ", M1.shape, "Shape of M2: ", M2.shape,"Shape of M3: ",
      M3.shape,"Shape of M4: ", M4.shape,"Shape of M5: ", M5.shape,)

def Commutative(MatrixA,MatrixB):
  Comm_AB = np.dot(M1, M2)
  Comm_BA = np.dot(M2, M1)
  print("Commutative Property")
  print(Comm_AB, " ≠ ", Comm_BA)
Commutative(M1, M2)

def Associative(MatrixA,MatrixB,MatrixC):
  Asso_AB = np.dot(M1, M2)
  Asso_ABC = np.dot(Asso_AB, M3)
  Asso_BC = np.dot(M2, M3)
  Asso_BCA = np.dot(M1, Asso_BC)
  print("Associative Property")
  print(Asso_ABC, " = ", Asso_BCA)
Associative(M1, M2, M3)


def Distributive(MatrixA,MatrixB,MatrixC):
  Distri_BC = np.add(M2, M3)
  Distri_ABC = np.dot(M1, Distri_BC)
  Distri_AB = np.dot(M1, M2)
  Distri_AC = np.dot(M1, M3)
  print("Distribute Property # 1")
  print(Distri_ABC, " = ", Distri_AB + Distri_AC)

  Distri_BCA = np.dot(Distri_BC, M1)
  Distri_BA = np.dot(M2, M1)
  Distri_CA = np.dot(M3, M1)
  print("Distribute Property # 2")
  print(Distri_BCA, " = ", Distri_BA + Distri_CA)
Distributive(M1, M2, M3)

def Identity(MatrixA,MatrixD):
  IdentA1 = np.dot(MatrixA, MatrixD)
  Ident1A = np.dot(MatrixD, MatrixA)
  print("Identity Property")
  print(IdentA1, " = ", Ident1A)
Identity(M1, M4)

def Zero(MatrixB,MatrixE):
  ZeroB0 = np.dot(MatrixB, MatrixE)
  Zero0B = np.dot(MatrixE, MatrixB)
  print("Zero Property")
  print(ZeroB0, " = ", Zero0B)
Zero(M2, M5)

def Dimension(MatrixA,MatrixB):
  MatrixA.shape[0]
  MatrixB.shape[1]
  print("Dimension Property")
  print(MatrixA[0], MatrixB[1])

Dimension(M1, M2)
