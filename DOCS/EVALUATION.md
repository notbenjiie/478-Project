Project Status: Alpha–Beta Integrated Release- What works and What's Next & Draft Results
What Works
The system currently demonstrates a fully operational end-to-end security pipeline within a hardened Docker environment. The decoy effectively identifies and classifies unauthorized reconnaissance, specifically flagging high risk probes directed at the sensitive /admin endpoint. When a suspicious entry is detected, the system triggers a response: the web decoy logs the event to a tamper-evident volume, and writes it to a .json file. A significant achievement in this release is the automated analysis pipeline, which programmatically ingests unstructured plain-text logs and exports them as a structured metrics.json artifact. This ensures that all security evidence is machine readable and ready for further evaluation, fulfilling the core observability requirements of the Beta milestone.

What’s Next
Looking forward, we're at a very good foundational spot so I think we should dive deeper and just refine this system to make it more streamlined. Something we could implement would be maybe pushing the suspicious json file to an administrative network and then doing something there, maybe banning the computer we tried it on or sending a message to the user that they can longer attempt to login until the end of the week or never again such and such. Anyways it would be easy to expand on our idea and create more security features. 

________________________________________________________________________________________________________________________________________________
Draft Results
-we did a run and we received, NORMAL, SUSPICIOUS, NORMAL, which were expected for each attempt in corresponding order. The screenshot below explains better than I can. 
<img width="1077" height="409" alt="Screenshot 2026-04-26 at 12 06 24 PM" src="https://github.com/user-attachments/assets/f923ebbe-638a-429f-8362-3820126cfacd" />
-You can also see that the security metrics were successfully exported and converted from a regular .log file into a .json file. 
-Observing this we can see that everything we've wanted has worked, only pushing us to refine this system further. 
