from ecosite.models import Produto, Imagem

img = []
for i in Produto.objects.all():
    try:
        if Imagem.objects.get(pk=i.id):
            img.append(i.id)
    except:
        pass


for i  in Produto.objects.all():
    if i.id in img:
        print(Imagem.objects.get(id=i.id))