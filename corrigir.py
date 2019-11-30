import cv2

# fotos = ["teste1.jpeg", "teste2.jpeg", "teste3.jpeg", "teste4.jpeg", "teste5.jpeg"]

provaGabarito = "prova/originais/provaImpressa/gabarito.jpeg"
provaAluno = "prova/originais/provaImpressa/aluno.jpeg"

# for i,photo in enumerate(fotos):
#     im_gray = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)
    # im_lim = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #muitos ruidos
    # im_lim = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 1) # muitos ruidos perto das letras
    # im_lim_81x20 = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor
    # im_lim_teste = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 60) # bordas mais finas    
    # cv2.imwrite( "teste" + str(i+1) + "_gray.jpeg", im_gray)


# provaGabaritoGreyScale = cv2.imread(provaGabarito, cv2.IMREAD_GRAYSCALE)
# provaAlunoGreyScale = cv2.imread(provaAluno, cv2.IMREAD_GRAYSCALE)

provaGabaritoGreyScale = cv2.imread(provaGabarito)
provaAlunoGreyScale = cv2.imread(provaAluno)
# provaGabaritoThreshold = cv2.adaptiveThreshold(provaGabaritoGreyScale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor
# provaAlunoThreshold = cv2.adaptiveThreshold(provaAlunoGreyScale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20) # melhor

# cv2.imwrite("prova/limiarizados/gabarito.jpeg", provaGabaritoThreshold)
# cv2.imwrite("prova/limiarizados/aluno.jpeg", provaAlunoThreshold)

subtract = provaGabaritoGreyScale - provaAlunoGreyScale
# cv2.subtract(provaGabaritoThreshold, prova_marcada_L)
cv2.imwrite("prova/resultados/subtract.jpeg", subtract)
# cv2.imshow("Output", subtract)
# cv2.waitKey(0)

average = cv2.blur(subtract,(9,9))
# cv2.imshow("Average Filter", subtract)
# cv2.waitKey(0)
cv2.imwrite("prova/resultados/average.jpeg", average)

ret, result = cv2.threshold(average,127,255,cv2.THRESH_BINARY)
cv2.imwrite("prova/resultados/result.jpeg", result)
# cv2.imshow("Result", result)
# cv2.waitKey(0)

#reading the image 
edged = cv2.Canny(result, 10, 250)
# cv2.imshow("Edges", edged)
# cv2.waitKey(0)
 
#applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Closed", closed)
# cv2.waitKey(0)
 
#finding_contours 
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(cnts)) 

# for c in cnts:
# 	peri = cv2.arcLength(c, True)
# 	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
# 	cv2.drawContours(subtract, [approx], -1, (0, 255, 0), 2)
# cv2.imshow("Output", subtract)
# cv2.waitKey(0)


# cv2.waitKey(0)
# cv2.destroyAllWindows()
