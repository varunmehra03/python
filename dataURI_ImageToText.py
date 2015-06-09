from binascii import a2b_base64
from PIL import Image
import commands

data = 'iVBORw0KGgoAAAANSUhEUgAAADQAAAAWCAYAAACPHL/WAAAC/0lEQVRYw+2XW0gUYRSAP501L2lkeUnNrqQlpSZaFBRBdqEQ2UQtCaGiiwildrGbZmFoFymxsILCwhQjRCgpqTDCLLWtrbxsvVhqmpZGuu26u632EAwOFhvtPETseZr/P9/5h4+ZOYexC18UOcx/FPb8Z2ETsgn9S0KCYE/Stk08eXSXPanJktz80HlcuZRPTXUltytKSN6xGUGQHhcSPJfiokJqqispLiokJHjuqHvIxVgUmj5tClcvnydh/ToUCmFUruBMLgMDWnanZ3K99CYbE+JI3ZkkMl6eHpzNy6arq5u0fRn09HzmbF42Eye4y85YFBIEey6cO83goIENidtH5VcsX4aj4xiysk9RV6+itKycRzW1rFkdKTIxyigUgkDmsVzqG56TkZWDg8KBGGWU7IxFIbN5iJQ9h9malEpHR+dvH6/ZbBavjQYjBqNRXEeEh9LYrEGvHwTgm05Hi+YNCyLCZGf+6JVr0bxlePjXM/feg4cYDEYO7U/F3X08U6f6s3TJYq4Vl4mM/2Q/Pn7skdR1dnXjP9lXdmZkKP6mk7S+a2N3eiZ5J45RWVGCyfSdGzcrKC0rFxlXV1f0er2kTqfT4+bmKjtjtZC3txdpu5K4U3WfqnvVrIteS+LGeBQODuQXXBQ5OzvLU0EuxiqhjANpABzPPQPAM5UapUrNwfQUVM/V1DyuQ6vV4uTkKKlzcXFmYEArruVirB6sYfODefW6SbJ3q7LqZy40GID2jg/4+kySML4+3rSPaDJyMVYL9fb24eXpIdnz8/MB4NPnXgAanqkJmhOAs7MTAGNdXJgzO5AG1QuxRi5GMnJ8/WdkWRLYtiWRpmYNtU8bABgaGiI+Vsk4NzdMJhNBQYEc3LsLk8lEzsl8DAYjbW0dxMZEEzBrJl/7+9mZvBUvbw+OZp9Gp/v5kcvFWC3U1Kyhu/sTKyOXER+rZGFEGOqXjRw6kkNf3xdxXrx81cjqVctZH6fku9lMRlYura3vxXPlYiQNxPaDZxOyCdmERsYPSprGlGLU0DsAAAAASUVORK5CYII='
data1 = 'iVBORw0KGgoAAAANSUhEUgAAADIAAAAWCAYAAACCAs+RAAADUUlEQVRYw+2XaUxUVxiGH5hhmw4Bl4qiKMYIyCbqgPqjxq1VY3DDrUs0taO4QAS0CCrEBbcGqlGIGqOCoHWKBNQSqyRiLLUpUzdAwP6oy0zZhpEGhhlQhP5yzHWmOpeSNDXzJl9y7/e+J+e8J+d+57sOiskze3gP4Mh7ArsRu5H/wohE4si6NV/yy80f2Ry/QcCNDQ0mL/soZaXF5GUfZWxosMX4d2nUt0osIma90swvXjSPC+dPU1ZaTM7JTKtzvNPISN/h5JzM4rPli5BKJQJu0IcDOZSRRn19IwmJKTQ1NXMoI40B/fuJ0gBcv/ETX0VvNMd35wsA+Hx5FLHrleQXXCQhMYW2NgOHv92Ll9cg241IJI4cy0yno6OTT1dEW/BRCyORSiSk7tpPufoOKTv24SR1ImphpCgNgE6np6Ky2hz6Zy0AFF26Qmx8Eqr8IsrVd9iz/yAymRuzZk613cjLl93Ebd7O6nXxaLV1Fny4Ioyq6lpMpg4A2o1GamofEhE+XpTmbWg3GqmorH5tuFkPgKenh7ijVVP7Oz091u9Kn2FDaWhoEuTq6hvxGeYtSiMGviN8ANBY2dheVy25XI7JZBLkjEYT7u5yURqASRMVXLmsoqy0mLSdW3FxcbE6Z+TcWXR2PufGzZ+t8tLeljsHB8d/rck9+z26Zj2VVTUEBfoTF7uW1tZWvsnItCg8S6LmkXs2n5aWv/rOiMFgwNVVuHMymRttbQZRmsNZJ8zPVQ9qCFeMY9rUjwRGnJ2d2Lt7O388esKJU7n/uKZeGdFo/8R7yGBBznuIl+D82qJ5EzqdHne58OhtS0pg4ID+rFi1ga6urr692dW/3SNwjB9ubq4AfCCTMSbAH/Xtu6I0r7hXCPAfzVON1vy+bMkCZkybwqYtqdQ3NPZ9i1JQeJnu7h52pSYRET6e3TuSedH1goLCH2zWLF08n3NnjjN3zscoJoSRnLiR4KAAcvJU5q4gLnYthReLAQgNCSQ0JBC/0aOsf4+2/I+ob5Wgyi8i/WCWOTcuLISvE2LwHeHD4ycaDqQf4X5FlWDc2zTOzk6sUa5k9ifT8fTw4KlGS06eiqvXrgOgXPUF0cqVFmv5tfw2MXFJvTNi737tRuxG/v/4G4mcfv/p4V7QAAAAAElFTkSuQmCC'
data2 = 'iVBORw0KGgoAAAANSUhEUgAAADUAAAAWCAYAAABg3tToAAADM0lEQVRYw+2Xa0hTYRjHf5tBs4Yyu1h5qSwdXZcmUdDCtIuVzVp2ISqIgi50g4gKKaTS6F4ERR+6p1iUpmZGGtGFSiqiNE2tWCvTbVqZyzPUbX2oRsetVDgQxP7f3ud53ufH/305zzlHpo2d4eQ/k5z/UF5TXlP/UF08BX0VCpYsXsDkuBj8/f0wGIycPHOBR8VPPDYJDQnG+P6Dx9yI4UPZsHYFoaEhGI3vOXz0BCWlZZJz2r2p+XNnMyY6kuMnTpG8PZXGxkbSdm5jUNgAt1rNyGGcO3WM3r17ueV69ezB3rQUamrNbEnegdlSz960FAJUKkk5Hbqp8+kXyci8THNLCwCVVa/JvZLOxBgtb94aRLX6WTN5UVKG2Wxx65Oom46Pj5zU3QcQbDbKX1WQcyWdRN00Tp/NkIzToZuyOxwuEIDdbgegublZVBegUqEdP47snGsem4+O1FD+qhLBZgOgqUmgoqKK6KhRknI6PSj8/fzYsHYlJpOZ/IJCUU6XEE9DQwN37z3wuDcoqC+mNidbU2siOKifpJxOmVqzajl52RlEakaQuucQ9fWfXDkfuRxdQjz5BYXYHQ7Wr1nB3Vvik1QqlQiCIIoJgg2lsruknE6ZupyVy+p1m8gvKOTgvl1MmTTRldOOH0dAgIrcazf+CpDJ2n9rSMFpd1D8Uq3JTK3JTOnLciLCB7Fs6SJuFt12PbgPi59gsdQhk8mQy2U/TchwOn98TlqtVhSKruLXha8Cq/WbpJxOmfpdlro6oqI0rvUozXAA7hTlieruFOUxIS4BgOrqGvoEBoryffsE8qH6o6ScDpkKCe6HyWQRTSZ1RDgGg9G1Xr5yvWjPwgVJxMZoRfGnz54zb04ivgoFgs1Gt26+qNXhZF7MkpTTIVMp2zbjcDjJvJTFl4avxE+JRR0xmOTtu1w1lVVvRHs+f/7iFs/JvU6SXkfy1o1k5+STpNfR2tLK1bzrknLayqf/wIiUtsGHjx4TFjaAJL2OaVMn4XQ6OXDkGPcfFP+x0dgx0Qwdoub0uQxXrKlJoKS0jMlxMczV62httbMzbT+Gd0ZJOW7DyfuT6DXlNeU11Z6+A6k20hFyYDd7AAAAAElFTkSuQmCC'

binary_data = a2b_base64(data2)

with open('image.png', 'wb') as fd:
    fd.write(binary_data)
    fd.close()

img = Image.open('image.png')
img = img.convert("RGBA")
pixdata = img.load()

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
  if pixdata[x, y][0] < 90:
   pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
  if pixdata[x, y][1] < 136:
   pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
  if pixdata[x, y][2] > 0:
   pixdata[x, y] = (255, 255, 255, 255)


img.save("temp.png")


commands.getoutput('tesseract temp.png output')

with open('output.txt','r') as text:
    for line in text:
        print line.strip().upper().replace("A","4").replace("O","0")
        break


