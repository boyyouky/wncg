import rsa
import base64
data_private ='''-----BEGIN RSA PRIVATE KEY-----
MIICYAIBAAKBgQCuNOnV8mNVLKWbKKrD3NDlmaw4r467PThYU+in55Cp7QTczk+C
Cu+19BV9lK/MALlMjp3j/YtOMTnN5RvfFx+6eCHhbgl9GIdD7BSxp5Yi3wVySJnK
xZKRKeQ/rSG8MBzi/LiliS7ObHs4jX99Jx8bZdCW3uw3q4ks1iP8wJxOYQIDAQAB
AoGADbtiC1lV9yrTyw1DmLjZRp/8cWN1TtEelefXWRTp1Fs4nOcuYUPXbXJWF1YX
HW+ZK626SHR9/KXotpAutfx6v8Wmkf87voZR7DzNNXY68CH3htV7xPnz7kwGvIF9
eSYGq50aR3P7Bv4By+HdIoFEEbhxs3INUJiFEyqPL26JjZkCRQDnwMNYh3o0ZC4c
IPPIPly9dOLV30CLshVJMz4VgfZ+U92UkQWmDrphGTvZ+QcVrkvXOgMaQgkZvFWk
6KojFKwvqgMmMwI9AMBu1tkHyJrNeVh/mWflcpwrqEmRj7Hd4Yr8iJoUmnL9qQMp
IEL7vY2fEVrj4IM1MZ16ljBsMI1oTr6dGwJFAKnuz45/sJzwBFt90iO3jpshNR8r
15FXYIJPP6vXox3YcvZ4LFMqI4IFVbyr/ITqTBQiJpo/Z5rmXUpRjEey5dsBZ9O/
AjwCxlZgwMT6vnW+efCLV/qkF9kQXoH07Z8f8u5BUoS7nb6/JeuqK5kbHq0QY3LM
UYsKm0bpIdY9Y8Cm7PsCRAEK7cufAMuovE+kNoSYuwIfAnLPtoDQ1bLO/RWOWmyb
rNCkKLM3uNVetLwn11a+diqqETI3dBcbRCfBwZDbNZgatT0M
-----END RSA PRIVATE KEY-----
'''
data_public ='''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAK406dXyY1UspZsoqsPc0OWZrDivjrs9OFhT6KfnkKntBNzOT4IK77X0
FX2Ur8wAuUyOneP9i04xOc3lG98XH7p4IeFuCX0Yh0PsFLGnliLfBXJImcrFkpEp
5D+tIbwwHOL8uKWJLs5seziNf30nHxtl0Jbe7DeriSzWI/zAnE5hAgMBAAE=
-----END RSA PUBLIC KEY-----
'''
pubkey = rsa.PublicKey.load_pkcs1(data_public.encode())
prikey = rsa.PrivateKey.load_pkcs1(data_private.encode())

def encrypt(message):
    crypto = rsa.encrypt(message.encode(), pubkey)
    return base64.b64encode(crypto).decode()
def decrypt(crypto):
    message = rsa.decrypt(base64.b64decode(crypto), prikey).decode()
    return message

