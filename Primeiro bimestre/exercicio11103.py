ano = int (input ("Em que ano você está?"))
if ano % 4 == 0:
 if ano % 100 ==0:
  if ano % 400 ==0:
   print ("O ano é bissexto.")

   
  else:
   print ("O ano não é um ano bissexto.")
   
 else:
  print ("O ano é um ano bissexto.")
  
else:
 print ("O ano não é um ano bissexto.")