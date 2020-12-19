1 - 
    I call client.py and server.py functions as stated in the pdf. I call server first and then client. After client sends
    the file to the server, I check if the file sent is correct or not by using "diff -q file1.txt file2.txt" command.

2 - 
    Q1-)
        I have gone over the slides before starting homework. I have tried to understand TCP and UDP structures, their
        multiplexing/demultiplexing mechanisms. After that, I have implemented TCP and I have implemented UDP without
        an RDT.
    Q2-)
        I have started with TCP implementaion. I used the simple example in the slides.
    Q3-)
        I thought that I can implement first TCP since it is reliable and no need extra work compared to UDP. 
        After that, UDP without and RDT and add each RDT features one by one. (checksum, ack, seq, ...)
    Q4-)
        Sending time/ack/sequence/checksum informations and extracting them was so hard until I understand them truely.
        Debugging was very hard or the concept was confusing because when I thought I did the same thing, while one 
        version was working the other one was not and understanding what is the reason for that was hard as well.
        Learning or knowing what to encode and what to decode was very frustrating. For checksum, I tried to use hashlib.md5(),
        and struct.pack() functison to include these informations into the message. I learned that struct.pack() converts bytes, but
        while concatenating them with my message even if I call encode() function for strings, I got errors.
        RDT was hard and I couldn't implement it. I know the idea, but understanding, getting the general idea is much more easy
        than implementing/coding it for me. I got stuck for some parts, finite state machines, states, going the next state.  
    Q5-)
        TCP is reliable and contains its own rdt implementaion but udp is not reliable so if we want to use udp we need to
        implement an rdt. TCP has congestion and flow control mechanisms while udp does not. That measn when possible, UDP sends
        as fast as possible. 
        I have learned how to implement basic network application over TCP and UDP, how to use sockets, how to send, recieve 
        messages amon application without caring lower levels. 
    Q6-)
        4 days without an RDT

3 - 
    I did not implement and RDT over UDP. I just hoped for the best. :')