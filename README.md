This was all in my efforts to determine the security of modern encryption (specifically RSA) as computers become more powerful. 
I simulated an RSA brute force factoring attack with my (classical, not quantum) computer for small RSA keys. I then extrapolated the time to estimate the computational power required to succeed in a brute force attack with RSA keys that are actually currently used, which are 2048 bits minimum, at the time of writing. 

Read the full paper > 'Math IA - Cole Westerveld.pdf'

In summary, I found that with modern factoring methods and classical (non-quantum) computers, it is completely unfeasible to crack modern RSA even with a supercomputer. However, with Shor's algorithm and a functioning quantum computer, RSA becomes pretty easy to crack. 
However, with better computers to crack encryption, we will have those same better computers to create more secure encryption, and we will likely have to move away from RSA to another encryption method. The problem arises when people store currently encrypted vulnerable data, until a future date when they are able to decrypt it with a quantum computer, which is a real security concern, especially with highly sensitive data.

Note: this was uploaded only after I had graduated, until then the paper was private to avoid plagarism.
