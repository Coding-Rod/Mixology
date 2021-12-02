f = open('.pass.bin', 'rb')
text = input("Ingresa contraseña anterior\n")

s = ''

for line in f:
    s = line.decode()
f.close()

if s == text:
    f = open('.pass.bin', 'wb')
    print("Contraseña correcta\n")
    br = input("Ingrese nueva contraseña\n")
    f.write(br.encode())
    f.close()
    

