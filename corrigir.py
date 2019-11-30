import cv2

# fotos = ["teste1.jpeg", "teste2.jpeg", "teste3.jpeg", "teste4.jpeg", "teste5.jpeg"]

prova_em_branco = "prova/teste.png"
prova_marcada = "prova/teste_marcado.png"

# for i,photo in enumerate(fotos):
#     im_gray = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)
    # im_lim = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #muitos ruidos
    # im_lim = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 1) # muitos ruidos perto das letras
    # im_lim_81x20 = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor
    # im_lim_teste = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 60) # bordas mais finas    
    # cv2.imwrite( "teste" + str(i+1) + "_gray.jpeg", im_gray)


prova_em_branco_G = cv2.imread(prova_em_branco, cv2.IMREAD_GRAYSCALE)
prova_marcada_G = cv2.imread(prova_marcada, cv2.IMREAD_GRAYSCALE)


prova_em_branco_L = cv2.adaptiveThreshold(prova_em_branco_G, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor
prova_marcada_L = cv2.adaptiveThreshold(prova_marcada_G, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor

cv2.imwrite("prova/prova_em_branco_L.jpeg",prova_em_branco_L)
cv2.imwrite("prova/prova_marcada_L.jpeg",prova_marcada_L)

subtract = cv2.subtract(prova_em_branco_L, prova_marcada_L)
cv2.imwrite("prova/subtract.jpeg", subtract)

# cv2.imshow('prova_em_branco',prova_em_branco_M)
# cv2.imshow('prova_marcada',prova_marcada_M)
# cv2.imshow('original_81x60',subtract)

cv2.waitKey(0)
cv2.destroyAllWindows()
