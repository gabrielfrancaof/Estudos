# Estudos de HTML - Guanabara

Aqui insiro todos os conhecimentos adquiridos ao longo do [Curso em vídeo](hhttps://www.youtube.com/@cursoemvideo)

## Anteriores ao capítulo 6
- Para colocar ```< ou >```, usar &lt; ou &gt;
- Para adicionar comentários usar 
``` html
<!-- assim você cria um comentário-->
```




## Capitulo 6
### **Aula 5 - favicon**
- Os favicon são os icones de imagem que fica ao lado de cada site
- O melhor formato de arquivo é .ico
- Site para criar um favicon via png - favicon.io
- Para adicionar o favicon basta usar o atalho escrevendo link :favicon

**Exemplo prático**
colocar o código na head
```html
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon >
```

## Capítulo 7
### **Aula 01 - Hierarquia de Títulos**
- Os títulos são organizados por níveis
- Em muitos lugares falam que é o tamanho da letra apenas, mas é mentira, sendo cada um deles um nível 
- Para gerar um texto aleatório usar "lorem"
- Os níveis vão até o ```<h6>```

## Capítulo 8
### **Aula 01 - Semântica**
- Existem tags obsoletas, como por exemplo "bgcolor", "marquee", "font"
- html5 não foca mais em formas, e sim em sêmantica, em significado
- html4 focava na forma das coisas, exemplo, o texto está na FORMA negrito. html5 fala que o texto esta forte, na semantica de o negrito estar mais forte, sendo um destaque

### **Aula 02 - Formatação de textos**
- ctrl+shift+p para envelopar texto selecionado com uma tag
```html
<b>termo em negrito</b> Usando a tag B (não sêmantica)
<strong> termo em destaque</strong> usando STRONG

<i>termo em itálico</i> usando a tag I (não sêmantica).
<em>termo em ênfase</em> usadno a tag EM (sêmantica)
```

### **Aula 3 - Formatações adicionais**
- Marcar textos usando MARK
- Texto grande usando BIG (porém, está obsoleta) e texto pequeno usando SMALL
```html
<del>texto como excluido</del> para indicar que ele deve ser lido, mas não considerado
<ins>texto como inserido</ins> para dar uma enfase e indicar que ele foi adicionado depois
<u>sublinhado</u> com a tag U (não semântica) 
<sup>Texto sobrescrito</sup>, para inserir coisas do tipo x<sup>20</sup>+3
<sub>Texto subscrito </sub> para inserir coisas do tipo H<sub>2</sub>0
```