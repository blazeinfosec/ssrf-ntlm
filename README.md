# ssrf-ntlm
Proof of concept written in Python to show that in some situations a SSRF vulnerability can be used to steal NTLMv1/v2 hashes.

Using Windows's WinHTTP.WinHTTPRequest native methods to demonstrate how Windows will give out hashes when asked to authenticate using NTLM.

written by Julio Cesar Fort, Wildfire Labs /// Blaze Information Security

Copyright 2016-2017, Blaze Information Security
https://www.blazeinfosec.com
