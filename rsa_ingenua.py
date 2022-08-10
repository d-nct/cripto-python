from euclides import euclides_estendido, euclides
from miller_rabin import teste_de_miller_rabin
from alfabeto import alfabeto_int, alfabeto_char
import random

def gerador_de_primos(digitos:int, num_iter:int = 10):
    """Retorna um número primo de aproximadamente  d  dígitos.

    Notas
    -----
      Teorema de Rabin: Teste de Miller acerta em 3/4 das bases entre 2 e p-2.
      Então, 10 iterações é suficiente para a resposta ser precisa.
    """
    def gera_int():
        return random.randint(10**(digitos-1), 10**digitos)

    while True:
        candidato = gera_int() # Geramos um numero que esperamos que seja primo
        if teste_de_miller_rabin(candidato, num_iter) == False:
            return candidato

class RSA():
    def __init__(self, p: int, q: int):
        """Recebe p & q primos, em que nossa RSA estará baseada.
        """
        totiente = (p - 1) * (q - 1)
        self.n = p * q
        self.e = 65537
        mdc, _, self.d = euclides_estendido(totiente, self.e)
        if self.d < 0: self.d += totiente
        if mdc != 1:
            raise NotImplementedError

    @staticmethod
    def texto_para_num(texto:str):
        """Recebe uma string com a mensagem clara e codifica pra os números com
        a nossa codificação.
        Retorna uma string em que todos os caracteres são números.
        """
        return "".join((alfabeto_char[carac] for carac in texto))

    def quebra_em_blocos(self, msg:str):
        """Recebe a string mensagem codificada em números.
        Retorna uma lista com os blocos de números inteiros.
        """
        blocos = []
        len_n = len(str(self.n))
        while (len(msg) > len_n):
            candidato = int(msg[:len_n])
            if candidato >= self.n: # não pode
                candidato = int(msg[:len_n-1])

            blocos.append(candidato)
            msg = msg[len_n:] # Tiramos fora o bloco

        # Bloco restante, se houver
        if msg != "":
            blocos.append(int(msg)) # TODO: esse bloco pode ser pequeno demais
        
        return blocos

    def encriptar(self, texto:str, verbose=False):
        """Encripta uma mensagem usando a chave pública!

        Recebe
        ------
        texto : str
          Mensagem a ser encriptada.
        verbose : bool, opcional
          Se True, imprime o passo a passo da encriptação. O padrão é False.

        Retorna
        -------
        list(int)
          Lista de inteiros, em que cada elemento é um bloco criptografado da mensagem.
        """
        texto_numerico = self.texto_para_num(texto)
        blocos = self.quebra_em_blocos(texto_numerico)
        blocos_encriptados = [pow(bloco, self.e, self.n) for bloco in blocos]
        if verbose:
            print("ENCRIPTANDO")
            print("-----------")
            print("Mensagem Clara")
            print("--------------")
            print("Texto Original: ", texto)
            print("Texto Numérico: ", texto_numerico)
            print("Blocos: ", blocos)
            print("Mensagem Encriptada em blocos")
            print("-----------------------------")
            for num, bloco in enumerate(blocos_encriptados):
                print(f"  Bloco #{num}: {bloco}")
        return blocos_encriptados 

    @staticmethod
    def concatenar(blocos):
        return "".join( [str(bloco) for bloco in blocos] )

    @staticmethod
    def num_para_texto(texto_numerico:str):
        msg = ""
        for i in range(0, len(texto_numerico), 2): # 2 algarismos -> 1 letra
            msg += alfabeto_int[texto_numerico[i:i+2]] # intervalo semiaberto
        return msg
            

    def desencriptar(self, lista_de_blocos, verbose=False):
        """Desencripta uma mensagem dada numa lista de blocos criptografados 
        usando nossa chave privada!

        Recebe
        ------
        lista_de_blocos : list(int)
          Cada elemento é uma parcela da mensagem. Precisa estar na ordem correta.
        verbose : bool, opcional
          Se True, imprime o passo a passo da encriptação. O padrão é False.

        Retorna
        -------
        str
          Mensagem descriptografada.
        """
        blocos_desencriptados = [pow(bloco, self.d, self.n) for bloco in lista_de_blocos]
        texto_numerico = self.concatenar(blocos_desencriptados)
        try:
            texto = self.num_para_texto(texto_numerico)
        except KeyError:
            print("Houve um erro ao descriptografar a mensagem. Verifique se as chaves estão corretas!")
            return 

        if verbose:
            print("DESCRIPTANDO")
            print("------------")
            print("Mensagem Encriptada em blocos")
            print("-----------------------------")
            for num, bloco in enumerate(lista_de_blocos):
                print(f"  Bloco #{num}: {bloco}")
            print("Blocos Desencriptados: ", blocos_desencriptados)
            print("Texto Numérico: ", texto_numerico)
            print("Mensagem Clara")
            print("--------------")
            print("Texto Original: ", texto)
        return texto

if __name__ == "__main__":
    p = gerador_de_primos(100)
    q = gerador_de_primos(100)
    rsa = RSA(p, q)

    print("Chave Privada")
    print("-------------")
    print(rsa.d, end='\n\n')

    print("Chave Pública")
    print("-------------")
    print( (rsa.e, rsa.n) , end='\n\n')

    print("TESTE DE USO")
    print("------------")

    msg = "Oh meu Deus isso realmente ta encriptado"
    msg_encriptada = rsa.encriptar(msg, verbose=True)

    print()

    msg_descriptada = rsa.desencriptar(msg_encriptada, verbose=True)
