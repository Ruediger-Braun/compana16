︠cb0a4da2-82c6-4996-bac2-91a7a57edec4s︠
%latex \Large Matrixexponential
︡4fb462c5-304c-4f26-bb4d-0b90e19f8f20︡
︠fad25688-ab2d-45db-9dce-c7303fe5231es︠
A = matrix(4,4,[0,1,0,0,-1,0,1,0,0,0,0,1,1,0,-3, 0])
︡b788b97b-1bf1-4ca3-aeea-b5787f0a103b︡
︠b569b816-1a5e-428b-b71d-4f2f7f7f6953︠
show(A)
︡f9402c31-6b79-43c9-8a66-c70390017f07︡
︠dbeec8f2-b488-4b49-a154-2f2175161e75︠
show(x)
︡8ca64923-2ad3-403a-85e0-44c1070da8ad︡
︠91768247-617d-4361-b270-cd38558b25d8︠
exa = (A*x).exp()
︡6935193b-ebf6-40ab-b5de-01787c5a9c73︡
︠537c7086-71ab-4155-8511-1c7fc41ee7c7︠
show(exa[0,0].expand())
︡a0f2f452-5d11-4a20-a49e-0bf6e68b79ac︡
︠b54ff832-0899-4b85-bb04-f172fc173ba1︠
D, T = A.eigenmatrix_right()
︡74c4930b-f09e-4d2d-8481-656fa8ac699f︡
︠bceb6fc5-90a1-405d-99e8-264d18e398a0︠
A.eigenvectors_right()
︡d9da3050-6aff-4ac4-aed2-07e7e04d2d17︡
︠9a6c0942-9e21-4511-923b-0f5ba2e3db39︠
MS = MatrixSpace(QQbar, 4, 4)
A = MS([0,1,0,0,-1,0,1,0,0,0,0,1,1,0,-3, 0])
︡74e46e38-0ebc-4356-9452-d03888100c12︡
︠c9e25466-fce3-4b9e-b721-f0d4d86db379︠
show(A)
︡bab62257-9555-4bb3-b587-04aff1135fb7︡
︠097ecd9d-508d-4619-b892-5d4c58a0272c︠
A.eigenvectors_right(extend=True)
︡e3e1be28-0252-44b5-bc72-94ef1eaf7994︡
︠168c2a95-7387-433a-809f-831dc8aadc1b︠
4+4
︡e8f1f672-bf38-4e0e-87ae-6950ee24209a︡
︠dcb0a11c-e9aa-4e74-837f-8f829122e2fbs︠
%latex \Large Algebraische Zahlen
︡440993f3-1ebf-4731-b0d6-1638ea9b1ba8︡
︠98a64d12-486f-4f02-9028-224d7b4949aes︠
p = x^5 + x + 7
show(p)
︡7dc4e56a-8df6-4d24-a4d5-e19671d24ee9︡
︠b62809a8-a061-4dba-a85d-d9a1190b530ds︠
K.<y> = NumberField(p)
︡1d94487f-856b-46fb-a9c0-307faa9cb82c︡
︠f8ba79e9-da7b-496a-bf1e-bcb329d96060s︠
%latex Das bedeutet, dass $y$ eine Nullstelle von $p$ ist.
︡bd7cfc4e-4cdd-41f6-9cb1-e75428a39533︡
︠61a1a95c-1a43-413f-a852-fb1b74e7edf0s︠
y^5 + y
︡90580383-f0c8-42a9-8f94-15a9cf12edb0︡
︠8e9cd20b-1282-4ca1-9fc1-dc0ae51da11cs︠
y^10
︡4ac0ac80-8d16-4847-8ec5-b17e10a9a9a3︡
︠c4ab168a-9100-46b6-b7d2-310b334cba01s︠
K
︡228ba8ef-d04b-4c6c-91b3-b2324eaf6f1a︡
︠8d597ba8-b9a4-4af1-b346-a11c53bac801s︠
G = K.galois_group(type='pari')
G
︡7623efb3-e542-4287-b9dc-0d5f9ace3abf︡
︠d28c32c6-2330-4ac9-ba4f-e945a1103cbds︠
%latex Die Galoisgruppe ist die $S_5$.  In der Algebra wird gezeigt, dass die Nullstellen nicht durch iterierte Wurzeln ausgedrückt werden können.
︡edbc1c12-02f4-4985-b0c6-8ccda633e8d4︡
︠b3dcf678-de6d-46c9-90b9-561bd9a01318s︠
%latex \Large Integral
︡735f728f-82fa-41f2-a12d-bf2834a5cc99︡
︠dad07078-c268-45d2-8573-a120a6e527d7s︠
f = 1/(1-x^2)^(3/2)
show(f)
︡64d32162-ddb3-448f-908e-9b68ea52226f︡
︠9c362167-aca7-40ba-8958-a0dadad354a7s︠
F = f.integral(x)
show(F)
︡5669b1d2-4683-4a5f-8e3f-372f90fe59da︡
︠2a77d4bd-2aba-4fe8-8fb5-9a5a0c4c3417s︠
(F.diff(x) - f).canonicalize_radical()
︡8ede7f17-f411-4dc3-bf29-bb0d4d4b83e2︡
︠66a36da7-f305-4eeb-8706-74b19c73868cs︠
%latex sympy hatte diese Stammfunktion falsch bestimmt (in Lektion 7)
︡1588a812-4b81-4f10-a98b-98321ea1ca2f︡
︠8a71fbd8-2a31-4bce-a289-0ad6464473ca︠









