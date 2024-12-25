SSL Chain
```java
import java.io.FileInputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.net.ssl.TrustManagerFactory;
import javax.net.ssl.X509TrustManager;

import org.bouncycastle.asn1.x509.AccessDescription;
import org.bouncycastle.asn1.x509.AuthorityInformationAccess;
import org.bouncycastle.asn1.x509.Extension;
import org.bouncycastle.cert.jcajce.JcaX509ExtensionUtils;

import lombok.extern.slf4j.Slf4j;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

@Slf4j
public class SslUtil {
    final static int MAX_CERT_CHAIN = 3;
    public static X509TrustManager defaultTrustManager;
    public static OkHttpClient httpClient;

    static {
        try {
            // Load java default keystore
            final String cacertsPath = System.getProperty("java.home") + "/lib/security/cacerts";
            KeyStore ks	= KeyStore.getInstance("JKS");
            ks.load(new FileInputStream(cacertsPath), "changeit".toCharArray());
            TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            tmf.init(ks);

            for(var tm: tmf.getTrustManagers()) {
                if(tm instanceof X509TrustManager x509tm) {
                    defaultTrustManager = x509tm;
                    break;
                }
            }
        } catch (KeyStoreException|NoSuchAlgorithmException|CertificateException|IOException e) {
            log.warn(e.getMessage());
        }

        if(defaultTrustManager == null) {
            log.warn("Unable to load default keystore");
        }
    }

    private static X509Certificate getCert(String uri) {
        if(httpClient == null) {
            httpClient = new OkHttpClient();
        }

        Request request = new Request.Builder().url(uri).build();
        try {
            Response response = httpClient.newCall(request).execute();
            return (X509Certificate) CertificateFactory.getInstance("X.509")
                                            .generateCertificate(response.body().byteStream());
        } catch (IOException|CertificateException e) {
            return null;
        }
    }

    public static X509TrustManager chain() {
        if(defaultTrustManager == null) {
            return null;
        }

        return new X509TrustManager() {
            @Override
            public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {}

            @Override
            public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
                List<X509Certificate> certChain = new ArrayList<>(Arrays.asList(chain));
                CertificateException lastCertException = null;

                for(int i = 0; i < MAX_CERT_CHAIN; i++) {
                    try {
                        defaultTrustManager.checkClientTrusted(certChain.toArray(new X509Certificate[0]), authType);
                        // trusted
                        return;
                    } catch (CertificateException untrusted) {
                        // untrusted, extend chain if available
                        lastCertException = untrusted;
                        var lastChain = certChain.getLast();
                        var aiaByte = lastChain.getExtensionValue(Extension.authorityInfoAccess.getId());
                        try {
                            boolean hasNextChain = false;
                            var aia = AuthorityInformationAccess.getInstance(JcaX509ExtensionUtils.parseExtensionValue(aiaByte));
                            for(var accessDescription: aia.getAccessDescriptions()) {
                                var method = accessDescription.getAccessMethod();
                                if(method.equals(AccessDescription.id_ad_caIssuers)) {
                                    String caIssuersUri = accessDescription.getAccessLocation().getName().toString();
                                    X509Certificate issuerCert = getCert(caIssuersUri);
                                    if(issuerCert != null) {
                                        // go to validate chain
                                        certChain.add(issuerCert);
                                        hasNextChain = true;
                                        break;
                                    }
                                } /*else if(method.equals(AccessDescription.id_ad_ocsp)) {
                                    // Need to check revocation?
                                }*/
                            }
                            if(!hasNextChain) {
                                // go to end of method
                                break;
                            }
                        } catch (IOException e) {
                            throw new CertificateException("Unable to read cert chain");
                        }
                    }
                }

                throw lastCertException;
            }

            @Override
            public X509Certificate[] getAcceptedIssuers() {
                return (defaultTrustManager != null) ? defaultTrustManager.getAcceptedIssuers() : new X509Certificate[]{};
            }
        };
    }

    public static X509TrustManager trustAll() {
        return new X509TrustManager() {
            @Override
            public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {}

            @Override
            public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {}

            @Override
            public X509Certificate[] getAcceptedIssuers() {
                return new X509Certificate[]{};
            }
        };
    }
}
```
