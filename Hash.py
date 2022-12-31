from hashlib import sha256
text = "Secret message"
print(sha256(text.encode('ascii')).hexdigest())