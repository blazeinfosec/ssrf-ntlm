# ssrf-ntlm
Proof of concept written in Python to show that in some situations a SSRF vulnerability can be used to steal NTLMv1/v2 hashes.

Using Windows's WinHTTP.WinHTTPRequest native methods to demonstrate how Windows will give out hashes when asked to authenticate using NTLM.

We published a blog post with details of how to exploit web application vulnerabilities to steal NTLM hashes:
https://blog.blazeinfosec.com/leveraging-web-application-vulnerabilities-to-steal-ntlm-hashes-2/


## Author

* **Julio Cesar Fort** - julio at blazeinfosec dot com

## License 

This proof of concept is licensed under the Apache License.

Copyright 2016-2017, Blaze Information Security
https://www.blazeinfosec.com


## Kudos

Thanks to the talented folks of [Hackerstrip](https://hackerstrip.exposure.co/) for the art used in our blog post.

![We need a bigger boat](fisherman-for-blog.jpg)

