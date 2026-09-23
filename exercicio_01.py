imagem = [0, 50, 100, 150, 200, 255]

print("Quantidade de pixels:", len(imagem))
print("Menor intensidade:", min(imagem))
print("Maior intensidade:", max(imagem))

if imagem[0] == 255:
    print("O primeiro pixel é branco.")
else:
    print("O primeiro pixel não é branco.")

print("Imagem representada:", imagem)
