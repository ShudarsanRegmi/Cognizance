# Writeup

The provide morse code
```
... ...-- -.-. .-. ...-- - -.- ...-- -.-- .--.-. .---- ..--- ...-- ....- ..... -....

```
was decoded to obtain the secret code for the cipher
```
S3CR3TK3Y@123456
```

Alogorithm of first guess was Aes-128 as the keysize was 16 char long.
So, AES in ECB mode was used to decipher the provided cipher to obtain the secret key

**cipher**
```
hoZyGgMHU4dM+8zgZAPXhA==
```

**obtained plain**
```
algorithmissafe
```

The obtained password was used to open the PDF to obtain the below secret:
```
CogML24@2024
```
