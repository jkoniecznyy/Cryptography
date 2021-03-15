Ćwiczenie 3: Zapisywanie haseł, funkcje skrótu ciąg dalszy

1. Zaprojektuj i zaimplementuj prosty własny sposób przechowywania haseł w bazie sqlite: użytkownik podaje hasło dwa razy, losujesz sól, hashujesz wszystko i zapisujesz hash oraz sól do bazy. Dodaj funkcję weryfikującą hasło.

2. Przerób pkt 1. aby używał pbkdf2_hmac. Zrób z tego porządny projekt (testy, docstringi, itp.)