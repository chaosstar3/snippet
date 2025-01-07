-   ASN.1: protocols
    -   BER
    -   CER
    -   DER
    -   XER
    -   PER
    -   GSER
-   Encodings
    -   DER
    -   PEM: armor with base64(der)
        -   https://tls.mbed.org/kb/cryptography/asn1-key-structures-in-der-and-pem
-   Extension
    -   CRT: *nix, binary DER or ASCII PEM
    -   CER: ms
    -   KEY
-   Type
    -   PKey(RSA): .pem .der
    -   PKCS12: .p12 .pfx
    -   X509(cert): .cer
# openssl
- show
	- openssl x509 -in cert.pem -text -noout
	- openssl x509 -in cert.cer -text -noout
	- openssl x509 -in cert.crt -text -noout
	- if error inform der format
	- openssl x509 -in cert.crt -inform der -text -noout
-   convert
	- PEM to DER
		- openssl x509 -in cert.crt -outform der -out cert.der
	- DER to PEM
		- openssl x509 -in cert.crt -inform der -outform pem -out cert.pem

# JKS
#java #jks #keytool #openssl
### example
```sh
openssl s_client -showcerts -connect $HOST:443 </dev/null 2>/dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > cert.pem
keytool -import -keystore $JAVA_HOME/jre/lib/security/cacerts -alias $ALIAS -file cert.pem -storepass changeit
keytool -delete -keystore $JAVA_HOME/jre/lib/security/cacerts -alias $ALIAS -storepass changeit
```

- defaultopt: -keystore {storefile} -storepass {changeit}
- opt: -trustcacerts
- commands
	- -import -srckeystore {storefile} -srcstoretype {type} -alias {alias}
	- -export
	- -importcert -file {crt} -alias {alias}
	- -exportcert -file {crt} -alias {alias}
	- -delete -alias {alias}
	- -list
	- -changealias -alias {alias} -destalias {alias}
	- -genkeypair -storetype jks|ojcs12

keystore type
- JKS
- JCEKS
- PKCS12
- PKCS12S2
- JCERACFKS
