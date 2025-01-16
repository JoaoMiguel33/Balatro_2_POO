from skimage import io
import matplotlib.pyplot as plt

# reading the sample image from a url
baralho = io.imread('https://github.com/alexse13dev/Balatro-Texture-Packs/blob/main/standard-texture-packs/Standard%20Balatro%20Deck/assets/1x/StandardBalatro.png?raw=true')

cartas = {
    "2":0,
    "3":1,
    "4":2,
    "5":3,
    "6":4,
    "7":5,
    "8":6,
    "9":7,
    "10":8,
    "J":9,
    "Q":10,
    "K":11,
    "A":12
}

naipes = {
    "copas":0,
    "espadas":1,
    "ouros":2,
    "paus":3
}


carta = cartas[input("Qual carta?(2 a 10, J, Q, K, A)\n")]
naipe = naipes[input("Qual naipe?(copas, espadas, ouros, paus)\n")]
naipe*=95
carta*=71
crop = baralho[naipe:naipe+95, carta:carta+71]

plt.figure(figsize=(5,2.5))
plt.axis('off')
plt.imshow(crop)
plt.show()
